---
name: buffett-business
description: Analyze a ticker's last five fiscal years from SEC EDGAR 10-K facts, calculate Buffett business-quality checks, and write an evidence-bound business memo. Use for the FIN43900 Buffett assignment or a request for this SEC business-quality workflow.
---

# Buffett business analysis

Use the bundled `scripts/edgar.py`. Read Buffett's framework as a reference, never install FAskills or use its paid data sources:
https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md

Run the script for the requested ticker with `--output-dir` pointing to the user's app folder. For Owen's assignment this is `/Users/owentsay/Documents/Codex/week11_buffett`. The script uses Owen Tsay's supplied SEC User-Agent. For a different user, request their name and email before changing the header.

```bash
python scripts/edgar.py COST --output-dir /Users/owentsay/Documents/Codex/week11_buffett --refresh
```

Use the app's `.venv/bin/python` when available. The script downloads keyless SEC ticker mapping and company facts, saves raw JSON and reports, and prints calculations and tags. Cached responses are reused without `--refresh`; disclose their download timestamp.

## Calculation contract

- Only 10-K filings; last five fiscal years labelled by fiscal-year-end dates, not the API's filing-year `fy` label.
- Flows require annual periods (350–380 days accommodates 52/53-week years).
- For the same period within a tag, use the latest filing. Prefer RevenueFromContractWithCustomerExcludingAssessedTax then Revenues; prefer PaymentsToAcquirePropertyPlantAndEquipment then PaymentsToAcquireProductiveAssets.
- Net income: NetIncomeLoss. Cash flow: NetCashProvidedByUsedInOperatingActivities. Equity: StockholdersEquity.
- ROE = net income / year-end equity. Owner earnings = operating cash flow − total capital spending, the course's simplified definition; never estimate maintenance capex.
- Missing values stay `not found`. Zero or negative equity gives `not known` ROE (and liabilities/equity if later requested). Checks with missing inputs are `not known`.
- Code checks ROE at least 15% every year, owner earnings positive every year, and owner earnings greater in the last year than the first. Never compute these in prose.

## Model-written memo

Read the printed output, then write `reports/TICKER_memo.md` with a short first-person, Buffett-inspired business assessment. Label it as an AI simulation, not Buffett's actual opinion. Choose **own the business**, **watch it**, or **pass**. The choice is model judgment, never a hard-coded mapping from checks.

Use only numeric values printed in the financial table or checks. Keep USD-million units, fiscal-end dates, and displayed ROE precision. Avoid numbered lists or additional numerical claims. Discuss earning power, capital intensity, and what the limited evidence does or does not establish about durable advantages and management. Do not invent operating facts or infer a moat merely from high ROE. No prices, price targets, valuation conclusions, or paid data.

Audit the completed memo with `--audit-memo PATH` and fix every unsupported number. The audit checks numeric presence, not factual entailment; personally verify every number's units, year, and meaning. Save `reports/TICKER_memo_meta.json` containing the `fingerprint` from `reports/TICKER_facts.json` so the app can detect stale memos.

The Streamlit app loads saved memos and can accept pasted AI prose for other tickers. It does not silently substitute a template for model judgment or require a paid model API.
