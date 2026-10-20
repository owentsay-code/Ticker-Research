# Meridian portfolio lab — results and verification

These are course-authored training values, not market estimates. The calculations are implemented in `portfolio.py`; the static mandate checks are implemented in `mandate.py`. This report records their results.

## Inputs

| Sleeve | Expected return | Volatility |
| --- | ---: | ---: |
| Treasury bills | 3.5% | 0.5% |
| Treasury 10-year note | 4.3% | 7.0% |
| Investment-grade bond fund | 5.0% | 6.0% |
| Global equity index fund | 8.0% | 16.0% |

| Correlation | Bills | 10-year | IG bonds | Equity |
| --- | ---: | ---: | ---: | ---: |
| Bills | 1.00 | 0.10 | 0.05 | 0.00 |
| 10-year | 0.10 | 1.00 | 0.80 | -0.10 |
| IG bonds | 0.05 | 0.80 | 1.00 | 0.25 |
| Equity | 0.00 | -0.10 | 0.25 | 1.00 |

The expected-return objective is 6.5%: the labelled CPI estimate of 2.5% plus 4%. Bills and the 10-year Treasury note are reserve eligible for this exercise. Meridian requires at least 3% in reserve-eligible holdings.

## Calculation method

- Covariance between sleeves i and j = correlation(i, j) × volatility(i) × volatility(j).
- Expected portfolio return = sum of weight(i) × expected return(i).
- Portfolio variance = sum over all i and j of weight(i) × weight(j) × covariance(i, j).
- Portfolio volatility = square root of portfolio variance.
- Inverse-volatility weight(i) = (1 / volatility(i)) divided by the sum of inverse volatilities.
- Reserve-eligible weight = bills weight + 10-year Treasury weight.

Calculations use unrounded decimal inputs. Rounding is applied only to displayed results.

## Baseline results

Weights below are percentages in the order bills / 10-year Treasury / IG bonds / equity.

| Portfolio | Weights (%) | Expected return | Volatility | Reserve eligible | Meets 6.5%? |
| --- | --- | ---: | ---: | ---: | --- |
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77% | 1.05% | 90.3% | No |

Every displayed value matches the course's known-answer table. The displayed inverse-volatility weights total 99.9% because of rounding; the underlying weights sum to 100%.

## Executed verification

### Correlation sensitivity

Both IG–equity correlation cells were changed from 0.25 to 0.50 in `portfolio.py`, and the script was rerun.

- Expected benchmark volatility: 11.00%.
- Observed benchmark volatility: 11.00%.
- Both cells were restored to 0.25, and a rerun confirmed benchmark volatility returned to 10.46%.

This confirms that the calculation responds to the correlation input. Omitting the cross-covariance contribution would incorrectly give benchmark volatility of about 9.90% at the baseline.

### Invalid correlation

Both IG–equity correlation cells were temporarily set to 1.3. The script refused to run, exited with status 1, and printed:

```text
Input error: Correlation [2, 3] must be between -1 and 1.
```

Both cells were restored to 0.25 afterward. A separate asymmetric-table test also raised a clear error. Weight-total and single-sleeve volatility checks passed.

### Benchmark through the mandate checker

Candidate E was added to `mandate.py` with 60% global equities, 40% investment-grade bonds, and zero in all other holdings. The file's holding order differs from the four-sleeve results table; its saved weight list is:

```python
"E": [0, 0, 0, 60, 40, 0, 0, 0]
```

Running the checker produced:

| Check | Candidate E result | Outcome |
| --- | ---: | --- |
| Weights sum to 100% | 100.0% | Pass |
| Long-only: lowest weight | 0.0% | Pass |
| Reserve at least 3% | 0.0% | FAIL |
| Redeemable within five business days at least 90% | 100.0% | Pass |
| Largest nonexempt single company at most 8% | 0.0% | Pass |
| Calendar-year loss requirement | Requires CIO clarification | Unresolved |

Candidate E fails one numerical rule: the reserve requirement.

## What earns, what risks, and what meets the mandate?

The benchmark has the highest modeled expected return and volatility of the three baselines. Equal weight has lower expected return and volatility. Inverse volatility assigns most of its weight to Treasury bills and has the lowest expected return and volatility.

None of the three baselines satisfies both the 6.5% expected-return target and the 3% reserve requirement. The benchmark meets the return target but fails the reserve rule. Equal weight and inverse volatility satisfy the reserve minimum but miss the modeled return target.

The client's benchmark therefore breaks the client's reserve rule when held as the actual portfolio. It can still serve as a performance comparison: S4 does not require the client to hold the benchmark allocation.

Volatility is not a maximum loss, and expected returns are not guarantees. These calculations do not establish compliance with the unresolved 10% calendar-year loss requirement, turnover cap, or annual rebalancing policy. No separate cost assumption was supplied, so the modeled return comparison does not independently establish achievement of the net-of-costs objective.

## Run the files

On this machine, use `python3`; the command `python` is unavailable.

```bash
python3 portfolio.py
python3 mandate.py
```

This Markdown report is a static record. Rerun the Python files and update the report if the inputs change.
