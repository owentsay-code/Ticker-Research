"""FRED current observations and ALFRED point-in-time comparisons."""

from datetime import date
from io import StringIO
import re
import ssl
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

import pandas as pd
import streamlit as st
import certifi


SERIES = {
    "BAA": "Moody's Baa corporate bond yield",
    "FEDFUNDS": "Federal funds rate",
    "DGS10": "10-year Treasury yield",
    "MORTGAGE30US": "30-year mortgage rate",
}
NAMES = {**SERIES, "UNRATE": "Unemployment rate"}


def read_csv(url: str) -> pd.Series:
    """Read either endpoint, including ALFRED's vintage-suffixed column."""
    try:
        with urlopen(url, timeout=30, context=ssl.create_default_context(cafile=certifi.where())) as response:
            raw = response.read().decode("utf-8-sig")
    except HTTPError as exc:
        raise ValueError(f"Download returned HTTP {exc.code}; check the series ID and vintage availability.") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise ValueError(f"Download failed: {exc}") from exc
    try:
        frame = pd.read_csv(StringIO(raw), na_values=["."])
        if len(frame.columns) != 2:
            raise ValueError("Expected one date column and one value column.")
        dates = pd.to_datetime(frame.iloc[:, 0], errors="raise")
        values = pd.to_numeric(frame.iloc[:, 1], errors="raise")
        result = pd.Series(values.to_numpy(), index=pd.DatetimeIndex(dates), name="Value")
        if result.index.hasnans or result.index.has_duplicates:
            raise ValueError("Invalid or duplicate observation dates.")
        return result.sort_index().rename_axis("Observation date")
    except (ValueError, TypeError, pd.errors.ParserError) as exc:
        raise ValueError("The service did not return a valid single-series CSV. Check the ID or try again later.") from exc


@st.cache_data(ttl=3600, show_spinner=False)
def download_today(series_id: str, downloaded_on: date) -> pd.Series:
    """One request per series per cache fill; date prevents overnight stale data."""
    return read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?" + urlencode({"id": series_id}))


@st.cache_data(ttl=3600, show_spinner=False)
def download_vintage(series_id: str, vintage_date: date, downloaded_on: date) -> pd.Series:
    """One request for the complete history available on the selected date."""
    return read_csv("https://alfred.stlouisfed.org/graph/alfredgraph.csv?" + urlencode({
        "id": series_id, "vintage_date": vintage_date.isoformat(),
    }))


def summarize(series_id, current, vintage):
    now = current.dropna() if current is not None else pd.Series(dtype=float)
    then = vintage.dropna() if vintage is not None else pd.Series(dtype=float)
    common = now.index.intersection(then.index)
    comparable = current is not None and vintage is not None
    return {
        "Series": f"https://fred.stlouisfed.org/series/{series_id}",
        "Last measured — as known then": then.index[-1].date() if not then.empty else None,
        "Value — as known then": float(then.iloc[-1]) if not then.empty else None,
        "Last measured — today": now.index[-1].date() if not now.empty else None,
        "Value — today": float(now.iloc[-1]) if not now.empty else None,
        "Values after last date known then": int((now.index > then.index[-1]).sum()) if comparable and not then.empty else None,
        "Revised values on shared dates": int((now.loc[common] != then.loc[common]).sum()) if comparable else None,
    }


def main():
    st.set_page_config(page_title="Rates, as known then", layout="wide")
    today = date.today()
    st.title("Rates, as known then")
    st.caption(f"Data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded today ({today:%Y-%m-%d}); built with AI help, a learning demonstration, not investment advice.")
    with st.sidebar:
        st.header("Explore data")
        selected = st.multiselect("Series", options=list(SERIES), default=list(SERIES),
                                  format_func=lambda key: f"{key} — {SERIES[key]}")
        extra = st.text_input("Add another FRED series ID", placeholder="UNRATE").strip().upper()
        start = st.date_input("Start date", value=date(2020, 1, 1),
                              min_value=date(1776, 1, 1), max_value=today)
        asof = st.date_input("As known on", value=today,
                             min_value=date(1776, 1, 1), max_value=today)
        st.caption("Start date controls charts. The comparison table uses all downloaded history. Downloads are cached for up to one hour.")
    if extra:
        if not re.fullmatch(r"[A-Z0-9_]+", extra):
            st.error("Additional series ID must contain only letters, numbers, or underscores.")
        elif extra not in selected:
            selected.append(extra)
    if not selected:
        st.info("Select a series or enter a FRED series ID to begin.")
        return

    rows = []
    for series_id in selected:
        st.subheader(f"{series_id} — {NAMES.get(series_id, 'Additional FRED series')}")
        current = vintage = None
        with st.spinner(f"Loading {series_id}…"):
            try:
                current = download_today(series_id, today)
            except ValueError as exc:
                st.error(f"{series_id} · FRED: {exc}")
            try:
                vintage = download_vintage(series_id, asof, today)
            except ValueError as exc:
                st.error(f"{series_id} · ALFRED: {exc}")
        if current is not None:
            visible = current.loc[pd.Timestamp(start):]
            if visible.dropna().empty:
                st.info("No current observations in the selected chart period.")
            else:
                st.line_chart(visible, y_label="Percent" if series_id in NAMES else "Value", height=250)
        available = vintage.dropna() if vintage is not None else pd.Series(dtype=float)
        if not available.empty:
            st.caption(f"As known on {asof:%Y-%m-%d}: last observation date {available.index[-1]:%Y-%m-%d}.")
        elif vintage is not None:
            st.caption(f"No nonmissing observations available as known on {asof:%Y-%m-%d}.")
        else:
            st.caption(f"Historical data unavailable for {asof:%Y-%m-%d}.")
        rows.append(summarize(series_id, current, vintage))

    st.subheader("Then and today")
    st.caption(f"Historical snapshot: {asof:%Y-%m-%d}. Dates are observation periods, not publication dates. Counts exclude missing values; revisions compare only dates with a value in both downloads. A dash means unavailable.")
    st.dataframe(pd.DataFrame(rows), hide_index=True, column_config={
        "Series": st.column_config.LinkColumn("Series", display_text=r"https://fred\.stlouisfed\.org/series/(.*)"),
        "Values after last date known then": st.column_config.NumberColumn(format="%d"),
        "Revised values on shared dates": st.column_config.NumberColumn(format="%d"),
    })


if __name__ == "__main__":
    main()
