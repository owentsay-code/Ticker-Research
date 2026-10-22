"""Lab 14 interface. All portfolio and estimation math stays in portfolio.py."""
import copy
import hashlib
import io
import importlib
from pathlib import Path
import pandas as pd
import streamlit as st
import portfolio as engine

# A browser refresh must pick up saved engine edits, even without Watchdog.
importlib.reload(engine)
ENGINE_REVISION = hashlib.sha256(Path(engine.__file__).read_bytes()).hexdigest()
from portfolio import (SLEEVES, CORRELATIONS, OBJECTIVE_RETURN, RESERVE_ELIGIBLE,
                       search_portfolio, estimate_from_csv)

st.set_page_config(page_title="Lab 14 portfolio", layout="wide")
st.title("Find the lowest-risk mix")
st.caption("Built with AI help, a learning demonstration, not investment advice.")

@st.cache_data(max_entries=64, show_spinner=False)
def search(sleeves, correlations, objective, eligible, minimum, engine_revision):
    return search_portfolio(sleeves, correlations, objective, eligible, minimum)

@st.cache_data(max_entries=16, show_spinner=False)
def estimate(raw, recent, engine_revision):
    return estimate_from_csv(io.BytesIO(raw), last_36=recent)

with st.sidebar:
    st.header("Mandate controls")
    objective = st.number_input("Objective (%)", value=OBJECTIVE_RETURN * 100, step=.1, key="objective") / 100
    reserve_min = st.number_input("Reserve minimum (%)", min_value=0., max_value=100., value=3., step=1., key="minimum") / 100
    uploaded = st.file_uploader("Upload prices.csv", type="csv", key="prices")
    recent = st.checkbox("Last 36 months", key="recent", help="Use the last 36 monthly returns (37 prices). Applies only to uploaded prices.")

try:
    if uploaded is None:
        loaded = copy.deepcopy(SLEEVES)
        current = copy.deepcopy(SLEEVES)
        loaded_corr = current_corr = CORRELATIONS
        default_eligible = RESERVE_ELIGIBLE
        dataset = "Meridian"
        token = "meridian"
        st.caption("Meridian · course training inputs · fully invested, long-only allocations in 5-percentage-point steps.")
        if recent:
            st.info("The 36-month switch applies to a CSV; Meridian's supplied estimates are unchanged.")
    else:
        raw = uploaded.getvalue()
        baseline_est = estimate(raw, False, ENGINE_REVISION)
        current_est = estimate(raw, recent, ENGINE_REVISION)
        loaded, loaded_corr = baseline_est["sleeves"], baseline_est["correlations"]
        current, current_corr = copy.deepcopy(current_est["sleeves"]), current_est["correlations"]
        default_eligible = tuple(name for name in loaded if name.upper() == "SGOV")
        token = hashlib.sha256(raw).hexdigest()[:16]
        dataset = uploaded.name
        st.caption(f"{dataset} · all-month baseline: {baseline_est['months']} returns · current window: {current_est['months']} returns, {current_est['first_return_month']} to {current_est['last_return_month']}.")
        st.info("SGOV is preselected as the assignment's Treasury-bill reserve proxy when present. Other CSV assets start unticked. VGIT is an intermediate-term Treasury fund, not Cedar Grove's short-term payout reserve. Confirm fund eligibility against the mandate; the saved reserve wording specifies cash or direct bills.")
except (ValueError, UnicodeError, TypeError) as exc:
    st.error(f"Cannot load prices: {exc}")
    st.stop()

st.subheader("Edit expected returns and reserve eligibility")
st.caption("Expected returns are annual percentages: change 8.00 to 7.00 for a one-percentage-point reduction. Volatility and correlations stay at the selected estimation window's values.")
eligible = []
for name, inputs in current.items():
    left, right = st.columns([3, 2], vertical_alignment="bottom")
    inputs["expected_return"] = left.number_input(f"{name} expected return (%)", value=float(inputs["expected_return"] * 100), step=.1, format="%.2f", key=f"return_{token}_{recent}_{name}") / 100
    if right.checkbox(f"{name}: reserve-eligible", value=name in default_eligible, key=f"eligible_{token}_{name}"):
        eligible.append(name)

st.caption("Both answers use the current objective and reserve minimum. The loaded answer keeps original expected returns, original reserve flags, and all available months. CSV reserve flags select SGOV only, as the assignment's reserve proxy; files without SGOV start with none.")
try:
    baseline = search(loaded, loaded_corr, objective, default_eligible, reserve_min, ENGINE_REVISION)
    answer = search(current, current_corr, objective, eligible, reserve_min, ENGINE_REVISION)
except (ValueError, TypeError) as exc:
    st.error(f"Cannot search: {exc}")
    st.stop()

for col, heading, result in zip(st.columns(2), ["Current inputs", "Inputs as loaded"], [answer, baseline]):
    with col.container(border=True):
        st.subheader(heading)
        if result is None:
            st.warning("no mix meets the objective")
            st.caption("No 5-point mix passes both the expected-return floor and the reserve minimum.")
        else:
            st.dataframe(pd.DataFrame({"Asset":list(loaded), "Weight (%)":[100*w for w in result["weights"]]}),
                         hide_index=True, column_config={"Weight (%)":st.column_config.NumberColumn(format="%.2f%%")},
                         alt=f"Lowest-risk grid allocation for {heading.lower()}")
            st.metric("Expected return", f"{result['expected_return']:.2%}")
            st.metric("Volatility", f"{result['volatility']:.2%}")
            st.metric("Reserve-eligible weight", f"{result['reserve_weight']:.2%}")

if answer is not None and baseline is not None:
    changes = [abs(a-b)*100 for a,b in zip(answer["weights"],baseline["weights"])]
    largest = max(changes)
    assets = ", ".join(name for name,change in zip(loaded,changes) if abs(change-largest)<1e-9)
    st.metric("Largest weight change", f"{largest:.2f} percentage points")
    if largest > 1e-9:
        st.caption(f"Asset(s): {assets}")
else:
    st.info("Largest weight change: unavailable because one or both searches found no feasible mix.")

with st.expander("Estimates and model scope"):
    st.dataframe(pd.DataFrame([{"Asset":name,"Loaded return (%)":loaded[name]["expected_return"]*100,
        "Current return (%)":v["expected_return"]*100,"Current volatility (%)":v["volatility"]*100} for name,v in current.items()]),
        hide_index=True, alt="Loaded and current annual investment estimates")
    st.dataframe(pd.DataFrame(current_corr,index=list(current),columns=list(current)),alt="Current correlation matrix")
    st.markdown("Monthly returns are price ratios minus one. Annual expected return is the arithmetic monthly mean × 12; annual volatility is sample standard deviation × √12. Correlations use the same return months. These estimates are calculated in portfolio.py.")
    st.markdown("This search checks full investment, long-only weights, expected return and the selected reserve minimum. It does not certify the full mandate, including fund concentration, turnover, or a calendar-year loss limit. The result is the lowest volatility on the 5-point grid, not a continuous optimizer.")
