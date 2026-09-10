# Training case

Training inputs: starting FCFF 100; annual growth rates 8%, 6%, 5%, 4%, 3%; WACC 10%; terminal growth 3%; non-operating cash 50; debt 300; diluted shares 50. Dollar amounts and shares are in millions.

Reverse DCF target: **$30.00 per share**. Search bounds: **−5 to +10 percentage points** added uniformly to all five annual growth rates.

The solved shift is **+1.77795 percentage points**, matching the expected **+1.78**. All nine sensitivity cells were independently checked using Decimal arithmetic. The reference table was not provided, so a direct comparison to that table was not performed.

## Sensitivity: value per diluted share (USD)

| WACC / terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | 28.5989 | 32.9426 | 39.0238 |
| 10% | 24.3564 | 27.4974 | 31.6853 |
| 11% | 21.0579 | 23.4140 | 26.4433 |

## Interpretation and conditional call — TRAINING ONLY

NVIDIA's starting FCFF and the corresponding five-year FCFF growth inputs for `dcf.py` remain unresolved. The training result and $30.00 target are retained; this is not a company valuation against today's NVIDIA price.

**Reverse DCF shift: +1.77795 percentage points** added to every annual FCFF growth rate. The resulting path is approximately **9.77795%, 7.77795%, 6.77795%, 5.77795%, 4.77795%**, which values the training case at **$30.00 per diluted share**.

**Held fixed:** starting FCFF of 100 million; WACC of 10%; terminal growth of 3%; non-operating cash of 50 million; debt of 300 million; diluted shares of 50 million; five annual forecast periods, year-end discounting, and the terminal-value formula. The baseline growth path remains 8%, 6%, 5%, 4%, 3%; only its uniform additive shift is solved for.

This is one set of assumptions consistent with the target price, not proof of mispricing.

**Conditional call (training):** Watch-defer. Initiate if the price falls below the unshifted model value of approximately $27.50, with the forecast assumptions still supported; otherwise watch-defer. This threshold belongs only to the training case and is not an NVIDIA entry price.

**Monitor:** NVIDIA's operating margin next quarter, as evidence for the profitability assumptions when resolving the company forecast.

## Complete output

Run `python3 dcf.py` from this folder with the training inputs above to reproduce:

```text
Year 1 FCFF (USD millions): 108.0000
Year 2 FCFF (USD millions): 114.4800
Year 3 FCFF (USD millions): 120.2040
Year 4 FCFF (USD millions): 125.0122
Year 5 FCFF (USD millions): 128.7625
PV of five explicit FCFF (USD millions): 448.4408
Terminal value at Year 5 (USD millions): 1894.6486
PV of terminal value (USD millions): 1176.4277
Enterprise value (USD millions): 1624.8685
Equity value (USD millions): 1374.8685
Value per diluted share (USD): 27.4974
PV of terminal value / enterprise value (fraction): 0.7240

Training case — sensitivity: value per diluted share (USD)
WACC / terminal growth |   2.00% |   3.00% |   4.00%
-----------------------+---------+---------+--------
                 9.00% | 28.5989 | 32.9426 | 39.0238
                10.00% | 24.3564 | 27.4974 | 31.6853
                11.00% | 21.0579 | 23.4140 | 26.4433

Training case — reverse DCF: uniform shift added to all five explicit growth rates
Target share price (USD): 30.0000
Shift bracket (percentage points): -5.000000 to +10.000000
Held fixed: STARTING_FCFF=100; baseline YEARLY_GROWTH_RATES=[0.08, 0.06, 0.05, 0.04, 0.03] (only uniform shift varies); WACC=0.1; TERMINAL_GROWTH=0.03; NON_OPERATING_CASH=50; DEBT=300; DILUTED_SHARES=50
Solved shift (percentage points): +1.77794768
Value per diluted share at solved shift (USD): 29.99999999
```
