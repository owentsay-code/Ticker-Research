"""Lab 14: client-facing controls over the existing portfolio engine."""
import copy
import json
import numpy as np
import pandas as pd
import streamlit as st
from lab14_engine import CLASSES, default_assets, model, optimize, evaluate, checks, portfolio

st.set_page_config(page_title="Meridian | Portfolio lab", page_icon=":material/account_balance:", layout="wide")

@st.cache_data(max_entries=64, show_spinner=False)
def solve(assets, corr, target, reserve, client, cost):
    m = model(assets, corr, target, reserve, client, cost)
    return m, optimize(m)


def numeric_table(df, alt):
    st.dataframe(df, hide_index=True, alt=alt, column_config={
        col: st.column_config.NumberColumn(format="%.3f")
        for col in df.select_dtypes(include="number").columns})


with st.sidebar:
    st.title("Portfolio lab")
    client = st.selectbox("Client", ["Meridian", "Cedar Grove"], key="client")
    st.caption("Lab 14 · minimum risk under a mandate")
    st.caption("Powered by your portfolio.py calculations.")

st.title("Which mix takes the least risk?")
st.markdown("Find the lowest modeled annual volatility that meets the return target and allocation rules. Then change one estimate and test the decision.")
if client == "Cedar Grove":
    st.info("Project 2 workspace: the Cedar Grove mandate is loaded. The starting investments and estimates below are Meridian course examples, not your approved Project 2 universe. Replace them before drawing a Project 2 conclusion.")
else:
    st.caption("Meridian Foundation Reserve · course-authored training estimates from your saved portfolio.py")

with st.expander("Mandate and investment estimates", expanded=False):
    cols = st.columns(4)
    cpi = cols[0].number_input("Expected CPI (%)", value=2.5, step=.1, key=f"cpi_{client}")
    spread = 4. if client == "Meridian" else 3.
    target = (cpi + spread) / 100
    cost = cols[1].number_input("Annual investment cost (%)", min_value=0., max_value=10., value=0., step=.05, key=f"cost_{client}") / 100
    value = cols[2].number_input("Portfolio value ($)", min_value=1., value=100_000_000. if client == "Meridian" else 2_000_000., key=f"value_{client}")
    payout = cols[3].number_input("Quarterly payout ($)", min_value=0., value=750_000. if client == "Meridian" else 15_000., key=f"payout_{client}")
    reserve = 4 * payout / value
    st.caption(f"Expected net return floor = CPI + {spread:g}% = {target:.2%}. Reserve = four payouts ÷ current value = {reserve:.2%}. Costs default to 0% because none were supplied in the course inputs.")
    st.caption("All investments must be unleveraged and eligible. Treasury bills must have remaining maturity of one year or less. Reserve eligibility and holding caps follow the selected investment class. Liquidity uses the stated days to available proceeds.")
    base = pd.DataFrame(default_assets()).rename(columns={"name":"Investment", "kind":"Class", "expected_return":"Return (%)", "volatility":"Volatility (%)", "days":"Redemption days"})
    base[["Return (%)", "Volatility (%)"]] *= 100
    data = st.data_editor(base, key=f"assets_{client}", num_rows="dynamic" if client == "Cedar Grove" else "fixed", hide_index=True,
        disabled=["Investment", "Class", "Redemption days"] if client == "Meridian" else [],
        column_config={"Class":st.column_config.SelectboxColumn(options=CLASSES, required=True),
            "Return (%)":st.column_config.NumberColumn(required=True, step=.1),
            "Volatility (%)":st.column_config.NumberColumn(required=True, min_value=.001, step=.1),
            "Redemption days":st.column_config.NumberColumn(required=True, min_value=0)},
        alt="Editable investment return, volatility and liquidity assumptions")
    st.caption("Returns and volatilities are annual percentages. Enter 8 for 8%. Project 2 supports two to six distinct investments.")
    n = len(data)
    if not 2 <= n <= 6:
        st.error("Use two to six investments.")
        st.stop()
    # Pair editor makes symmetry automatic; diagonal is always one.
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    pairdata = pd.DataFrame([{"Pair": f"{i+1} ↔ {j+1}", "Correlation": float(portfolio.CORRELATIONS[i][j]) if i < 4 and j < 4 else 0.} for i,j in pairs])
    st.caption("Correlation pairs refer to investment row numbers above. Editing a pair updates both matrix cells.")
    pairdata = st.data_editor(pairdata, key=f"corr_{client}_{n}", disabled=["Pair"], hide_index=True,
        column_config={"Correlation":st.column_config.NumberColumn(min_value=-1., max_value=1., step=.01, required=True)}, alt="Editable pairwise correlations")

try:
    assets = [dict(name=row["Investment"], kind=row["Class"], expected_return=float(row["Return (%)"])/100,
                   volatility=float(row["Volatility (%)"])/100, days=float(row["Redemption days"])) for _,row in data.iterrows()]
    corr = np.eye(n)
    for (i,j), val in zip(pairs, pairdata["Correlation"]):
        corr[i,j] = corr[j,i] = float(val)
    m, w = solve(assets, corr.tolist(), target, reserve, client, cost)
except (ValueError, TypeError, KeyError) as exc:
    st.error(f"Check your inputs: {exc}")
    st.stop()

st.caption(f"{client} · expected net return ≥ {target:.2%} · reserve ≥ {reserve:.2%} · five-day liquidity ≥ {m['liquid_min']:.0%}" + (" · each fund ≤ 40%" if client == "Cedar Grove" else ""))
if w is None:
    st.error("No feasible mix meets these modeled requirements. Review the target, reserve, investment estimates and caps; the app will not silently relax the mandate.")
    st.stop()
result = evaluate(w, m)
for col, (label, val) in zip(st.columns(3), [("Expected net return",result["Expected net return (%)"]), ("Annual volatility",result["Volatility (%)"]), ("Reserve allocation",result["Reserve (%)"])]):
    col.metric(label, f"{val:.2f}%", border=True)
st.success("Least-risk mix found. It passes the modeled return and static allocation checks.")
allocation = pd.DataFrame({"Investment":[a["name"] for a in assets], "Weight (%)":w*100, "Amount ($)":w*value})
left, right = st.columns([3,2])
with left:
    st.subheader("Your modeled allocation")
    numeric_table(allocation, "Minimum-volatility allocation and dollar amounts")
with right:
    st.bar_chart(allocation.set_index("Investment")[["Weight (%)"]], horizontal=True, alt="Allocation weights by investment")

st.subheader("Does it survive a one-point change?")
st.caption("One percentage point is an absolute change: an 8% expected return becomes 7% or 9%. A correlation point here means 0.01. Only the selected estimate changes; the mandate stays fixed.")
c1,c2,c3 = st.columns(3)
field = c1.selectbox("Estimate to change", ["Expected return", "Volatility", "Correlation"], key="shock_field")
if field == "Correlation":
    idx = c2.selectbox("Investment pair", list(range(len(pairs))), format_func=lambda k:f"{assets[pairs[k][0]]['name']} / {assets[pairs[k][1]]['name']}", key=f"pair_{client}_{n}")
else:
    idx = c2.selectbox("Investment", list(range(n)), index=n-1, format_func=lambda k:assets[k]["name"], key=f"shock_asset_{client}_{n}")
direction = c3.selectbox("Change", ["−1 point", "+1 point"], key="direction")
change = -.01 if direction == "−1 point" else .01
changed_assets, changed_corr = copy.deepcopy(assets), corr.copy()
if field == "Correlation":
    i,j = pairs[idx]
    before = corr[i,j]
    changed_corr[i,j] += change
    changed_corr[j,i] += change
    description = f"{assets[i]['name']} / {assets[j]['name']} correlation: {before:.2f} → {before+change:.2f}"
else:
    key = "expected_return" if field == "Expected return" else "volatility"
    before = assets[idx][key]
    changed_assets[idx][key] += change
    description = f"{assets[idx]['name']} {field.lower()}: {before:.2%} → {before+change:.2%}"
st.markdown(f"**{description}**")
try:
    sm, sw = solve(changed_assets, changed_corr.tolist(), target, reserve, client, cost)
except (ValueError, TypeError) as exc:
    st.error(f"This change produces invalid assumptions: {exc}")
    st.stop()
old_after = evaluate(w, sm)
comparison = [{"Scenario":"Original mix · original estimates", **result}, {"Scenario":"Original mix · changed estimate", **old_after}]
if sw is not None:
    new_after = evaluate(sw, sm)
    comparison.append({"Scenario":"Reoptimized mix · changed estimate", **new_after})
numeric_table(pd.DataFrame(comparison), "Original and reoptimized portfolios evaluated before and after the selected estimate change")
if old_after["Passes modeled rules"]:
    st.info("The original mix still passes the modeled rules after this change.")
else:
    st.warning("The original mix fails the modeled rules after this change. Passing before the change did not make the allocation robust.")
if sw is None:
    conclusion = "No feasible reoptimized mix exists under the changed estimate."
    st.error(conclusion)
    turnover = None
else:
    turnover = float(np.abs(sw-w).sum()/2)
    same = np.max(np.abs(sw-w)) < 1e-6
    conclusion = ("The same mix remains optimal to numerical tolerance." if same else
        f"The least-risk mix changes: {turnover:.2%} of the portfolio would need to be reallocated.")
    st.markdown(conclusion)
    weights_compare = pd.DataFrame({"Investment":[a["name"] for a in assets], "Original (%)":w*100, "Reoptimized (%)":sw*100, "Change (pp)":(sw-w)*100})
    numeric_table(weights_compare, "Change in each investment weight after reoptimization")
    st.caption("Reallocation is half the sum of absolute weight changes. It is a hypothetical trade size, not certification of the calendar-year turnover rule.")

with st.expander("Mandate checks and comparison portfolios"):
    numeric_table(pd.DataFrame([{"Rule":label,"Actual (%)":actual*100,"Boundary (%)":bound*100,"Pass":passed} for label,actual,bound,passed in checks(w,m)]), "Numerical mandate checks for the optimized baseline")
    if client == "Meridian":
        baselines = {"60/40 benchmark":portfolio.benchmark_weights(m["sleeves"],portfolio.BENCHMARK_WEIGHTS), "Equal weight":portfolio.equal_weights(m["sleeves"]), "Inverse volatility":portfolio.inverse_volatility_weights(m["sleeves"]), "Minimum volatility":w}
        numeric_table(pd.DataFrame([{"Portfolio":name,**evaluate(weights,m)} for name,weights in baselines.items()]), "Benchmark, equal-weight, inverse-volatility and optimized portfolio comparison")
    st.markdown("Risk means annual return volatility in this pilot. Expected return is treated as a modeled floor using CPI plus the mandate's spread and the entered costs. Volatility does not enforce Meridian's unresolved 10% calendar-year loss statement. Future realized returns, annual rebalancing and calendar-year turnover are not certified by these static checks.")
    st.markdown("The permitted universe contains cash, direct Treasuries and diversified unleveraged equity or investment-grade bond funds. Meridian's company issuer cap is therefore nonbinding. Cedar Grove additionally caps each fund at 40% and excludes Treasury notes from its payout reserve.")

text = (f"{client}: minimizing annual volatility under the displayed modeled constraints gives "
        + "; ".join(f"{a['name']} {weight:.3%}" for a,weight in zip(assets,w))
        + f". Expected net return is {result['Expected net return (%)']:.3f}%, volatility {result['Volatility (%)']:.3f}%, and reserve {result['Reserve (%)']:.3f}%. "
        + f"Sensitivity: {description}. The unchanged mix {'passes' if old_after['Passes modeled rules'] else 'fails'} after the change, with expected net return {old_after['Expected net return (%)']:.3f}%. {conclusion} "
        + (f"Reoptimized volatility is {new_after['Volatility (%)']:.3f}%. " if sw is not None else "")
        + "These are model results, not a guaranteed loss bound or full operational mandate certification. "
        + ("Project 2 inputs require confirmation; starting estimates are Meridian course examples." if client == "Cedar Grove" else "Source: portfolio.py course training inputs, with any edits recorded in the downloaded scenario."))
with st.expander("Lab 14 answer and downloads"):
    st.text_area("Copy into your Lab 14 chat", text, height=210)
    st.download_button("Download answer", text, file_name="lab14_answer.txt")
    st.download_button("Download allocation", allocation.to_csv(index=False), file_name="lab14_allocation.csv", mime="text/csv")
    payload = dict(client=client,assets=assets,correlations=corr.tolist(),target=target,cost=cost,reserve=reserve,portfolio_value=value,quarterly_payout=payout,weights=w.tolist(),sensitivity=description,changed_assets=changed_assets,changed_correlations=changed_corr.tolist(),reoptimized_weights=None if sw is None else sw.tolist())
    st.download_button("Download scenario inputs and results", json.dumps(payload,indent=2), file_name="lab14_scenario.json", mime="application/json")
