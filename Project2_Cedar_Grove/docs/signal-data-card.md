# Point-in-time signal data card

- **Signal:** ACWI trailing 12-month adjusted-price momentum, P(last complete month) / P(12 months earlier) − 1. Uses 13 monthly prices; no annualization.
- **Decision timestamp:** October 22, 2026, after the supplied snapshot was downloaded. Latest represented month ends September 30, 2026. Earliest possible implementation is after the snapshot became available; no return earned earlier is attributed to the signal.
- **Source:** frozen Yahoo monthly chart JSON in `data/source/ACWI_yahoo_monthly.json`, adjusted close field; processed values in `data/prices.csv`. Original download notes are retained. Build output records SHA-256 of the CSV.
- **Availability:** this snapshot was saved October 22, 2026 according to the inherited download record. The archive has no intraday download timestamp, so use the next trading day or later for implementation. No claim is made that today's adjusted history was available at earlier historic decision dates.
- **Revision risk:** adjusted histories may change following distributions or corrections. Frozen files prevent later revisions from silently changing this submission; they do not reconstruct vintages before the download.
- **Transformation and use:** negative momentum limits research ACWI weight to 20%; nonnegative momentum permits up to 40%, also bounded by the selected fund cap. This is an unvalidated research rule, not an approved mandate condition or established alpha.
- **Lag:** baseline uses the last fully completed month in the snapshot. An optional one-month additional lag excludes the latest monthly observation from both estimates and the signal. It does not merely relabel a timestamp.
- **Missing values:** reject missing, nonpositive, nonfinite, duplicate, out-of-order or nonconsecutive monthly data; never backfill or interpolate.
- **Universe selection risk:** four funds were selected for assignment roles after their history existed; no unbiased historical universe-selection backtest is asserted.
- **Tests:** hand-compute the 13-price ratio, test the negative-momentum branch, and change excluded future information to verify the lag boundary.
- **Stop condition:** insufficient or invalid prices stop calculation; a failed constraint stops a proposed research allocation; unresolved governance stops live adoption regardless of signal sign.
