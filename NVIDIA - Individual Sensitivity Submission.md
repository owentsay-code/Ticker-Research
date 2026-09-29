# NVIDIA — Individual Sensitivity Submission

All statement amounts are USD billions; value/share is USD per share. Outputs use the existing five-year rolling model and saved assumptions. These are scenario results, not updated market estimates.

## Two operating drivers: visible sensitivity results

Each driver is varied separately by ±5 percentage points in every forecast year. All other independent inputs stay at base; linked statement quantities recalculate.

| Driver | Lower path, Years 1–5 | Base path, Years 1–5 | Higher path, Years 1–5 |
| --- | --- | --- | --- |
| Revenue growth | 40%, 25%, 15%, 10%, 5% | 45%, 30%, 20%, 15%, 10% | 50%, 35%, 25%, 20%, 15% |
| EBIT margin | 59%, 57%, 55%, 54%, 53% | 64%, 62%, 60%, 59%, 58% | 69%, 67%, 65%, 64%, 63% |

| Run | Year 5 EBIT | Year 5 FCFF | Value/share | Status |
| --- | ---: | ---: | ---: | --- |
| Initial base | 502.818 | 385.972 | $209.28 | VALID |
| Revenue growth: lower | 408.456 | 319.635 | $174.41 | VALID |
| Revenue growth: base | 502.818 | 385.972 | $209.28 | VALID |
| Revenue growth: higher | 613.821 | 462.814 | $249.97 | VALID |
| EBIT margin: lower | 459.472 | 349.994 | $190.42 | VALID |
| EBIT margin: base | 502.818 | 385.972 | $209.28 | VALID |
| EBIT margin: higher | 546.164 | 421.949 | $228.13 | VALID |

| Output span: maximum − minimum | Revenue growth | EBIT margin |
| --- | ---: | ---: |
| Year 5 EBIT ($bn) | 205.365 | 86.693 |
| Year 5 FCFF ($bn) | 143.178 | 71.955 |
| Value/share ($) | 75.557 | 37.712 |

## Restored-base and accounting checks

| Check | Visible result |
| --- | --- |
| Initial base: EBIT / FCFF / value per share | 502.817919 / 385.971862 / $209.275411 |
| Restored base: EBIT / FCFF / value per share | 502.817919 / 385.971862 / $209.275411 |
| Restored inputs, all statement rows and valuation | PASS — exact agreement |
| Lower/higher runs | PASS — only the selected independent input changed |
| Signed changes | PASS — changed output minus base, using unrounded values |
| Accounting/feasibility checks across 8 sensitivity runs and 3 locked-scenario runs | PASS — 671 checks; no failures |
| Largest absolute reconciliation gap | 4.547e-13 billion, below the 1e-8 billion tolerance |

Statements display to $0.001 billion and value/share to $0.01; verification uses unrounded values. The locked-scenario base-before/base-after check also passed exactly.

## Reconciled locked prediction

The prediction was locked before running a separate +2-percentage-point growth scenario: 47%, 32%, 22%, 17%, 12%. EBIT margins and all other independent inputs stayed at base. The original locked prediction is preserved.

| Output | Predicted increase | Base | Actual changed result | Actual increase |
| --- | --- | ---: | ---: | ---: |
| Year 5 EBIT ($bn) | 40–45 | 502.817919 | 545.108057 | +42.290138 |
| Year 5 FCFF ($bn) | 28–32 | 385.971862 | 415.383081 | +29.411219 |
| Value/share ($) | 15–16 | 209.275411 | 224.813894 | +15.538482 |

All three increases were within the predicted ranges. Actual-minus-predicted-midpoint errors were −$0.210bn EBIT, −$0.589bn FCFF and +$0.038/share. The predictions were rough ranges: exact results reflect growth compounding, taxes, reinvestment and discounting, so their midpoints were not expected to match exactly.

Higher revenue increases EBIT at fixed margins. FCFF equals EBIT × (1 − tax rate) + D&A − capex − incremental working capital. With tax at 17%, capex at 3% of revenue and incremental working capital at 20% of additional revenue, some incremental profit is absorbed before becoming FCFF. CFO, investing and financing cash flows reconcile to closing cash; net income and distributions reconcile to equity. Higher forecast FCFF and a larger terminal revenue base raise value/share.

## Main driver and valuation implication

Revenue growth is the larger driver of Year 5 operating profit, FCFF and value/share **over these ranges**. Growth compounds the sales base over five years; margins then convert those sales into operating profit. The revenue-growth FCFF span is $143.178bn versus $71.955bn for EBIT margin.

A bigger span can reflect a wider input range, not an inherently more important driver. Here both paths span 10 percentage points per year, but equal percentage-point widths do not represent equal economic uncertainty. Different ranges could change the ranking.

The base value remains $209.28/share. The locked scenario raises it to $224.81, but sensitivity alone supplies no new evidence that the higher growth assumptions are more likely. My base conclusion therefore stays unchanged; validating the durability of data-center demand and spending remains the research priority. No current market-price comparison or full AI-downturn stress test was performed.

## Partner exchange and evidence checked

My partner also analyzed NVIDIA and identified data-center business buildout as a growth driver. This is consistent with the revenue-growth mechanism in my model, rather than a different company driver.

Question received: **“What if the AI bubble pops?”**

My revised response: **“I believe AI will remain useful, but an investment bubble could still burst and reduce data-center spending and NVIDIA’s growth. Revenue growth was the larger driver over our tested ranges, so that risk matters. Our sensitivity analysis did not test a full bubble-collapse scenario.”**

For exchange 2, we checked the analysis and reported no issues or corrections. The specific shared numerical example subsequently approved by my partner uses the higher revenue-growth path: Year 5 EBIT rises from $502.817919bn to $613.821007bn (+$111.003088bn); FCFF rises from $385.971862bn to $462.813677bn (+$76.841815bn); value/share rises from $209.275411 to $249.966552 (+$40.691141). The numerical verification recomputed these differences, checked that only growth changed, and traced the smaller FCFF increase to taxes and reinvestment.

My partner approved the example and the explanation that growth compounds revenue, increases profit and cash flow, and requires additional reinvestment. She also approved the limitation that the main-driver ranking depends on the chosen ranges. Continued AI use does not rule out a spending downturn.

Evidence scope: the shared numerical example is from my model and was approved by my partner; it is not a separately supplied output from her model. Her independently calculated endpoints and inputs were not provided for this record. Accordingly, I do not claim a separately documented numerical audit of her model. Both analyses concern NVIDIA, so our business-driver explanations align; there is no cross-company ranking by raw dollar changes.

## Sensitivity — Learn on your own

**1. What is one-at-a-time sensitivity?** It changes one independent assumption at a time while holding the other independent assumptions at base. The model recalculates linked quantities and compares the resulting output with base. Here an entire five-year growth or margin path counts as the selected assumption. This isolates that assumption’s modeled effect but does not test simultaneous shocks or interactions between changing inputs.

**2. How does the chosen input range affect the ranking?** The output span measures the response over the selected lower-to-higher interval. A wider interval can produce a larger output span and move a driver up the ranking. Ranking therefore depends on range widths, starting assumptions and the model’s response, including compounding or nonlinear effects. Always say “over these ranges.”

**3. Why is a sensitivity table not a forecast probability?** It answers “what would the model produce if these assumptions held?” It does not estimate how likely those assumptions are. Lower, base and higher cases have no assigned probabilities and are not confidence intervals. One-at-a-time scenarios also leave other assumptions fixed even when real-world drivers could move together. A probability forecast would require justified probabilities and a treatment of that joint uncertainty.

Supporting evidence: [locked record](NVIDIA%20-%20Locked%20Changed-Input%20Record.md), [full sensitivity results](NVIDIA%20-%20Sensitivity%20Results.md), and `nvidia_locked_scenario_results.json`.
