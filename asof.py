"""Compare point-in-time and naive signals using only the standard library."""

# Editable inputs: Row, Ticker, Month measured, Published on, Index.
TABLE = """Row,Ticker,Month measured,Published on,Index
1,AAA,2026-01,2026-02-10,101.0
2,AAA,2026-02,2026-03-10,104.0
3,AAA,2026-03,2026-04-10,109.0
4,AAA,2026-02,2026-03-25,103.0
5,BBB,2026-01,2026-02-10,98.0
6,BBB,2026-02,2026-03-10,97.0
7,BBB,2026-02,2026-03-10,97.0
8,BBB,2026-03,2026-04-10,92.0
9,CCC,2026-01,2026-02-10,110.0
10,CCC,2026-02,2026-04-05,112.0
11,,2026-02,2026-03-10,99.0
12,CCC,2026-02,2026-03-10,111.0
"""
DECISION_DATE = "2026-03-31"

import csv
from datetime import date
from decimal import Decimal
from io import StringIO


def read_rows():
    return [
        {
            "row": int(r["Row"]),
            "ticker": r["Ticker"].strip(),
            "month": date.fromisoformat(r["Month measured"] + "-01"),
            "published": date.fromisoformat(r["Published on"]),
            "index": Decimal(r["Index"]),
        }
        for r in csv.DictReader(StringIO(TABLE.strip()))
    ]


def report(label, before, after):
    kept = {r["row"] for r in after}
    removed = [r["row"] for r in before if r["row"] not in kept]
    print(f"{label}: removed {len(removed)}; rows {removed}; remaining {len(after)}")


def deduplicate(rows):
    # Row numbers identify provenance and are excluded from the duplicate key.
    seen = set()
    kept = []
    for r in rows:
        key = (r["ticker"], r["month"], r["published"], r["index"])
        if key not in seen:
            seen.add(key)
            kept.append(r)
    return kept


def latest_publications(rows):
    latest = {}
    for r in rows:
        key = (r["ticker"], r["month"])
        prior = latest.get(key)
        if prior is None or r["published"] > prior["published"]:
            latest[key] = r
        elif r["published"] == prior["published"] and r["index"] != prior["index"]:
            raise ValueError(f"Conflicting same-date publications: rows {prior['row']} and {r['row']}")
    return sorted(latest.values(), key=lambda r: (r["ticker"], r["month"]))


def signal(rows, ticker):
    observations = sorted(
        (r for r in rows if r["ticker"] == ticker), key=lambda r: r["month"]
    )
    if not observations:
        return None, "N/A (no available observations)"
    latest = observations[-1]
    month = latest["month"]
    previous_month = date(month.year - 1, 12, 1) if month.month == 1 else date(month.year, month.month - 1, 1)
    previous = next((r for r in observations if r["month"] == previous_month), None)
    if previous is None or previous["index"] == 0:
        return None, f"{month:%Y-%m}: N/A (previous month missing or zero)"
    change = (latest["index"] / previous["index"] - 1) * 100
    return change, f"{month:%Y-%m}: {change:+.2f}% (from {previous_month:%Y-%m})"


def main():
    cutoff = date.fromisoformat(DECISION_DATE)
    original = read_rows()
    if len({r["row"] for r in original}) != len(original):
        raise ValueError("Row identifiers must be unique.")
    print(f"Decision date: {cutoff}\nRow funnel: starting with {len(original)} rows")
    identified = [r for r in original if r["ticker"]]
    report("1. Quarantine missing ticker", original, identified)
    unique = deduplicate(identified)
    report("2. Remove exact duplicates", identified, unique)
    knowable = [r for r in unique if r["published"] <= cutoff]
    report("3. Remove late publications", unique, knowable)
    panel = latest_publications(knowable)
    report("4. Remove superseded revisions", knowable, panel)

    print("\nAs-of panel")
    print(f"{'Row':>3}  {'Ticker':6}  {'Month':7}  {'Published':10}  {'Index':>8}")
    for r in panel:
        print(f"{r['row']:>3}  {r['ticker']:6}  {r['month']:%Y-%m}  {r['published']}  {r['index']:>8}")

    # Same validity and duplicate rules; only the publication cutoff is ignored.
    naive = latest_publications(unique)
    print("\nSignals (naive uses latest publications regardless of decision date)")
    for ticker in sorted({r["ticker"] for r in unique}):
        asof_value, asof_text = signal(panel, ticker)
        naive_value, naive_text = signal(naive, ticker)
        print(f"{ticker}: as-of {asof_text}; naive {naive_text}")
        if asof_value is not None and naive_value is not None:
            print(f"     Naive minus as-of: {naive_value - asof_value:+.2f} percentage points")


if __name__ == "__main__":
    main()
