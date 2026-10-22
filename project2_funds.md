# Project 2 fund universe and price sources

Download date: **October 22, 2026** (America/Indiana/Indianapolis).

Selected tickers: **QQQ, SPY, VOO, FCNTX**. These are the four funds requested for the exercise. No money market funds are included.

## Fund names and roles

| Ticker | Fund name | Role in this universe |
| --- | --- | --- |
| QQQ | Invesco QQQ Trust, Series 1 | Equity: Nasdaq-100 exposure to large nonfinancial Nasdaq-listed companies; a growth-oriented equity allocation, not a cash or bond holding. |
| SPY | State Street SPDR S&P 500 ETF Trust | Equity: core U.S. large-company stock index exposure through the S&P 500. |
| VOO | Vanguard S&P 500 ETF | Equity: another implementation of the S&P 500 core allocation. It overlaps substantially with SPY rather than supplying a different asset-class role. |
| FCNTX | Fidelity Contrafund | Equity: actively managed stock exposure seeking capital appreciation; an active equity complement to the index funds. |

Fund identity and strategy sources: [Invesco QQQ](https://www.invesco.com/us/en/financial-products/etfs/invesco-qqq-trust-series-1.html), [State Street SPY](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy), [Vanguard VOO fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F0968.pdf), and [Fidelity FCNTX](https://fundresearch.fidelity.com/mutual-funds/view-all/316071109).

## Fit with the Cedar Grove mandate

This is an **equity-only research universe**, not a complete universe for the saved Cedar Grove Scholarship Fund mandate. None of these funds provides the required cash/Treasury-bill distribution reserve, government-bond role, or investment-grade fixed-income role. SPY and VOO serve the same core equity role.

Cedar Grove requires four quarterly payments in cash or direct U.S. Treasury bills with remaining maturity of one year or less. At the initial $2 million portfolio value, that is $60,000, or 3%. A portfolio invested exclusively in these four funds cannot satisfy that reserve requirement. Its 40% cap on each diversified fund also remains applicable. The assignment's separate-role requirement is therefore not fulfilled merely by having four tickers. These four requested tickers have been retained without relabeling them or changing the mandate. A Treasury-bill fund would require confirmation that the mandate permits a fund as a reserve proxy, because its saved wording specifies cash or direct Treasury bills.

## Historical price sources

| Ticker | Source: Yahoo Finance Historical Data, Monthly, Adj Close | Download date |
| --- | --- | --- |
| QQQ | [Monthly historical data](https://finance.yahoo.com/quote/QQQ/history/?period1=1633046400&period2=1790812800&interval=1mo) | 2026-10-22 |
| SPY | [Monthly historical data](https://finance.yahoo.com/quote/SPY/history/?period1=1633046400&period2=1790812800&interval=1mo) | 2026-10-22 |
| VOO | [Monthly historical data](https://finance.yahoo.com/quote/VOO/history/?period1=1633046400&period2=1790812800&interval=1mo) | 2026-10-22 |
| FCNTX | [Monthly historical data](https://finance.yahoo.com/quote/FCNTX/history/?period1=1633046400&period2=1790812800&interval=1mo) | 2026-10-22 |

The prices were retrieved programmatically from Yahoo Finance's chart endpoint, using `interval=1mo`, `period1=1633046400`, and `period2=1790812800`. The exact endpoint pattern is `https://query2.finance.yahoo.com/v8/finance/chart/TICKER?period1=1633046400&period2=1790812800&interval=1mo`. The selected field was `indicators.adjclose[0].adjclose`, not unadjusted Close. The original Yahoo JSON responses are preserved in the `source` folder.

## prices.csv conventions and checks

- Columns: `Date,QQQ,SPY,VOO,FCNTX`, with the oldest month first.
- Coverage: **October 2021 through September 2026**, the latest 60 completed calendar months as of download. October 2026 is excluded because it is incomplete.
- Dates retain Yahoo's monthly bar labels: the **first day of the represented month**, not the date of a trade at that price. For example, `2021-10-01` labels October's monthly observation. Timestamps were interpreted in `America/New_York`.
- Prices are Yahoo's monthly adjusted-close observations in USD, accounting for the provider's distribution and split adjustments. Original numeric precision is preserved; no prices are rounded to cents, interpolated, or forward-filled.
- Validation: all four series contain the same 60 consecutive months, with no missing, duplicate, nonfinite, or nonpositive prices. The output contains 60 data rows and five columns.
- Sixty monthly prices generate **59 consecutive monthly returns** using `P[t] / P[t-1] - 1`. A subsequent requirement for 60 monthly returns would need one additional starting price from September 2021.
- Adjusted histories can be revised by the provider after later distributions or corrections. This is the snapshot downloaded on the date recorded above.

The original `portfolio.py`, `mandate.py`, and Meridian inputs were not modified. This file and `prices.csv` prepare the separate Project 2 dataset; they do not replace the Meridian-first app workflow.
