# UNRATE data card

**Series:** UNRATE — Unemployment Rate  
**Download and verification date:** October 29, 2026

## Source, measure, and units

The source is the U.S. Bureau of Labor Statistics (BLS), Current Population Survey (household survey), distributed through the Federal Reserve Bank of St. Louis's [FRED series page](https://fred.stlouisfed.org/series/UNRATE). Historical snapshots come from ALFRED.

UNRATE measures unemployed people as a percentage of the civilian labor force, age 16 and older. It is the U-3 unemployment rate. Units are **percent**, the frequency is **monthly**, and the series is **seasonally adjusted**. These definitions are documented on the [FRED page](https://fred.stlouisfed.org/series/UNRATE).

## Publication lag

The observation month precedes publication. In this check, September 2026 was unavailable on September 30; FRED records its update on October 2, 2026. That is a lag of **two calendar days after the end of the measured month** for this release, not a guaranteed lag for every month. The CSV labels September as `2026-09-01`; that label is an observation period, not a publication date. [FRED series and update information](https://fred.stlouisfed.org/series/UNRATE)

## Last month versus today

Entered `UNRATE` in the app's additional-series field and tested both dates using freshly downloaded CSVs. The app's date inputs and comparison table were checked with Streamlit's testing interface.

| As known on | Last observation available | Value then | Additional observations in today's data | Revised shared observations |
|---|---|---:|---:|---:|
| September 30, 2026 | August 2026 | 4.1% | 1 | 0 |
| October 29, 2026 | September 2026 | 4.2% | 0 | 0 |

September 2026 is the one observation that disappears from the historical snapshot: its 4.2% value had not yet been published on September 30. The app's charts always show today's data; the historical cutoff appears in the caption and table.

## Revisions

There were **zero changed values on shared, nonmissing observation dates** between the September 30 snapshot and today's download, comparing all available history. This describes this comparison interval only.

UNRATE **is subject to revision**. BLS reestimates seasonal factors annually and revises seasonally adjusted household-survey data for the preceding five years. Therefore, a zero count over this short interval does not establish that the series is unrevised. UNRATE is a monthly labor-market statistic, not a daily market interest rate. [BLS seasonal adjustment methodology](https://www.bls.gov/cps/seasonal-adjustment-methodology.htm)

## Three values checked directly against FRED

Read the following observations on the [FRED UNRATE page](https://fred.stlouisfed.org/series/UNRATE) and compared them with the current CSV on October 29, 2026:

| Observation month | FRED page | Downloaded CSV | Result |
|---|---:|---:|---|
| July 2026 | 4.1% | 4.1% | Match |
| August 2026 | 4.1% | 4.1% | Match |
| September 2026 | 4.2% | 4.2% | Match |

## Response to partner: Trusting revisions

Revisions are a normal part of improving economic estimates, and BLS documents how it updates UNRATE's seasonal adjustments. We are good to go once we use the ALFRED vintage available at each decision date, because that keeps later revisions from entering earlier decisions.

## Project 2 decision: Quarantine

**Quarantine:** UNRATE is published after the month it measures and is subject to annual seasonal-adjustment revisions. On September 30, 2026, the latest available observation was August at 4.1%; September's 4.2% was not available until October 2. Although the comparison with October 29 showed zero revisions on shared dates, that does not make the series revision-free. Using today's historical values in past investment decisions could introduce information that was unavailable at the time.

**What would change the decision:** Admit UNRATE as a Project 2 input only when each decision uses the ALFRED vintage available at that decision's cutoff, with release timing checked and unavailable observations left unavailable. For intraday decisions, verify that the release preceded the decision time; a date-only snapshot is insufficient to establish that. Retain the vintage date and source with each observation. Do not use today's revised history with a fixed lag as a substitute for historical vintages. If the required vintage or release timing cannot be verified, keep the affected observations quarantined.

Here, quarantine means holding the series out of the historical decision model until those availability checks are satisfied; it is not a judgment that the BLS data are unreliable. The publication and revision evidence is documented above.

## Downloads used

- [Current UNRATE CSV](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE)
- [ALFRED snapshot: September 30, 2026](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=UNRATE&vintage_date=2026-09-30)
- [ALFRED snapshot: October 29, 2026](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=UNRATE&vintage_date=2026-10-29)

Prepared and verified with AI assistance. The current-download link changes as new data arrive; the results above record the October 29, 2026 check.
