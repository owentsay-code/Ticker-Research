# NVIDIA five-year FCFF DCF — September 8, 2026

Base value: **$209.28 per share**, versus a **$226.00** intraday quote (September 8, 2026, 12:15 p.m. EDT), or **7.4% downside**. Reverse DCF implies **26.3% constant annual revenue growth for five years**, with all other assumptions fixed. This is an analyst scenario, not a uniquely observable market forecast.

## Sources and starting point

- [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm): annual revenue $215.938 billion.
- [Q2 FY2027 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx): current/prior first-half revenue $177.837/$90.805 billion; latest balance sheet and diluted shares. TTM revenue is therefore $302.970 billion.
- [Quote source](https://stockanalysis.com/stocks/nvda/history/): $226.00 timestamped header quote; intraday figures vary. The model uses that snapshot, not the separate daily row or a closing price.

## Model conventions and judgments

Five future annual periods measured from the valuation date, with year-end discounting. Latest TTM revenue through July is a starting proxy; no fiscal-year stub is mixed with full future years. The reporting lag is not separately rolled forward.

FCFF = EBIT × (1 − cash operating tax rate) + depreciation/amortization − capital expenditure − change in operating working capital.

Revenue growth assumptions: 45%, 30%, 20%, 15%, 10%. These imply a 23.4% five-year CAGR. GAAP operating margins fade from 64% to 62%, 60%, 59%, and 58%, reflecting slower growth and competition while preserving substantial platform economics. These are analyst assumptions, not company guidance. The first-year revenue estimate is broadly consistent with the latest quarterly revenue outlook annualized but is not a fiscal-year forecast.

Tax: 17%, using the midpoint of company guidance as a normalized operating-tax proxy. D&A: 1.2% of revenue; capex: 3%. Incremental operating working capital: 20% of the revenue increase. These rounded reinvestment assumptions approximate recent operating intensity; they are not a detailed account-by-account forecast. Stock compensation remains an expense in GAAP EBIT and is not added back. No buyback-driven share reduction is assumed.

WACC: 10%, an assumed required return, not an estimated current CAPM result. Perpetual growth: 3.5%. Terminal-year margin, tax, capex and D&A ratios remain at year-five levels; working-capital investment is recalculated at terminal growth. Terminal FCFF is not simply year-five FCFF multiplied by 1.035 because working-capital growth slows.

## Forecast (USD billions)

| Future year | Revenue | EBIT | NOPAT | D&A | Capex | ΔNWC | FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 439.3 | 281.2 | 233.4 | 5.3 | 13.2 | 27.3 | 198.2 |
| 2 | 571.1 | 354.1 | 293.9 | 6.9 | 17.1 | 26.4 | 257.2 |
| 3 | 685.3 | 411.2 | 341.3 | 8.2 | 20.6 | 22.8 | 306.1 |
| 4 | 788.1 | 465.0 | 385.9 | 9.5 | 23.6 | 20.6 | 351.2 |
| 5 | 866.9 | 502.8 | 417.3 | 10.4 | 26.0 | 15.8 | 386.0 |

PV of explicit FCFF: $1,102.283 billion. PV of terminal value: $3,913.967 billion. Enterprise value: $5,016.250 billion.

Equity bridge adds $22.443 billion cash, $34.143 billion marketable debt securities and $42.783 billion marketable equity securities; subtracts $33.366 billion debt. Net addition: $66.003 billion. Equity value: $5,082.253 billion. Divide by 24.285 billion latest quarterly diluted weighted-average shares as a proxy for valuation-date diluted shares: **$209.28**.

All included cash and securities are assumed available to equity holders at carrying value, without realization taxes. Nonmarketable investments are excluded pending a realizable-value assessment; adding their $51.157 billion book value would add about $2.11 per share before taxes or discounts. Operating leases are treated as operating costs within EBIT, so lease debt is not separately deducted. Debt carrying value approximates fair value. Other non-operating claims and post-quarter balance-sheet changes are not separately valued. These simplifications should be refined for a transaction-grade valuation.

## Reverse DCF and sensitivity

Solve for one constant revenue growth rate over five years such that the same model equals $226.00. Result: **26.2912%**, reaching **$973.3 billion** year-five revenue (3.21 times TTM revenue). Margins, tax, reinvestment, terminal growth, WACC, equity bridge and shares are held fixed. This differs from the declining base-case growth path; implied CAGR is conditional on the chosen constant-growth shape.

| WACC / terminal growth | 2.5% | 3.5% | 4.5% |
|---|---:|---:|---:|
| 9% | $217 | $249 | $294 |
| 10% | $187 | $209 | $240 |
| 11% | $164 | $180 | $202 |

Terminal value represents 78.0% of enterprise value. Consequently, the point estimate is highly sensitive to long-run profitability and discount rates. At the base assumptions the quoted price provides no margin of safety; this supports retaining WATCH-DEFER in the existing research rather than establishing a precise trading target.

## Reproduce

Run `.venv/bin/python nvda_dcf.py` or pass a different quote, for example `.venv/bin/python nvda_dcf.py 230.36`. The standard-library-only script prints forecasts, the equity bridge result, sensitivities and implied growth. The reverse solver checks that its answer reprices the input quote within $0.00000001.
