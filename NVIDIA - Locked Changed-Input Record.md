# NVIDIA — Locked Changed-Input Record

Locked timestamp: **2026-09-29 13:43:50 EDT (UTC−04:00)**.

Company: NVIDIA. Model: `nvidia_proforma.py`, September 24 five-year rolling forecast. Year 1–5 are rolling annual periods, not NVIDIA fiscal years.

Status: Prediction saved before running this specific scenario. Earlier sensitivity results were already available; this is a new, unrun +2-percentage-point growth scenario, not a retrospective prediction of those earlier runs.

## Ranges shown to Partner before the run

All entries are percentages, ordered Year 1 through Year 5. Lower and higher paths shift the base by minus or plus **5 percentage points in each year**, not a 5% relative change.

| Independent input | Lower | Base | Higher |
| --- | --- | --- | --- |
| Annual revenue growth | 40%, 25%, 15%, 10%, 5% | 45%, 30%, 20%, 15%, 10% | 50%, 35%, 25%, 20%, 15% |
| EBIT margin | 59%, 57%, 55%, 54%, 53% | 64%, 62%, 60%, 59%, 58% | 69%, 67%, 65%, 64%, 63% |

Range rationale — labeled judgment: Revenue growth tests weaker or stronger AI infrastructure demand and deployment while preserving deceleration. EBIT margin tests pricing pressure and operating costs versus stronger pricing and efficiency while preserving margin compression. These are NVIDIA scenario judgments, not guidance or statistical confidence intervals.

## Locked prediction shown to Partner

Change only the **revenue-growth path**, adding **2 percentage points to every forecast year**:

| Forecast period | Old annual revenue growth | New annual revenue growth |
| --- | --- | --- |
| Year 1 | 45% | 47% |
| Year 2 | 30% | 32% |
| Year 3 | 20% | 22% |
| Year 4 | 15% | 17% |
| Year 5 | 10% | 12% |

This is one independent assumption path changed across its five affected years. The new path lies within the displayed lower/higher range. Keep EBIT margins at 64%, 62%, 60%, 59%, 58%; retain all other base assumptions, including 17% tax, capital spending at 3% of revenue, D&A at 1.2% of revenue, incremental working capital at 20% of additional revenue, 10% WACC, 3.5% terminal growth, and 24.285 billion shares.

| Output | Base result | Expected direction and rough size |
| --- | --- | --- |
| Year 5 operating profit (EBIT), USD billions | 502.818 | Increase by about $40–45 billion, to roughly $543–548 billion |
| Year 5 economic FCFF, USD billions | 385.972 | Increase by about $28–32 billion, to roughly $414–418 billion |
| Value per share, USD/share | 209.28 | Increase by about $15–16, to roughly $224–225/share |

Why: Higher growth compounds the sales base through all five years. Unchanged positive EBIT margins turn additional sales into additional operating profit. Taxes, capital spending, and working-capital investment absorb part of that increase, so the dollar increase in FCFF should be smaller than the increase in EBIT. Higher Year 5 revenue also raises normalized terminal cash flow while terminal growth itself stays unchanged. Rough sizes are informed by the previously completed sensitivities; these are predictions, not calculated results for this new scenario.

## Partner review and swap-back

**Partner:** I reviewed the prediction and both ranges before running this scenario. Revenue growth and EBIT margin are independent input paths in the NVIDIA model. The proposed change is +2 percentage points each year: for example, 45% becomes 47%, not 45.9%. Only the revenue-growth path changes. EBIT margin and all other independent assumptions remain fixed. Revenue, EBIT, capital spending, working capital, and FCFF may change as calculated consequences; that does not constitute changing additional independent inputs.

**Partner:** Output units are consistent: Year 5 EBIT and economic FCFF are USD billions; value per share is USD per share. FCFF is used throughout, not FCFE. Each affected year and its old/new input are explicit, and the selected path falls within the declared range. No unclear unit or range remains.

Swap-back check: The Partner interpretation matches the locked proposal: change only annual revenue growth by +2 percentage points in Years 1–5. No second prediction or second run is introduced by the review. This written exchange records the assistant acting as Partner; it does not claim a separate human or independent reviewer participated.

**Run status at lock: Not run.** Preserve this prediction when recording actual results later. Retain signed cash flows if a later run produces negatives; do not discard negative years or invent a terminal value.

## V — Actual result and verification

Appended 2026-09-29T14:00:43.442174-04:00. Original prediction above is preserved. The locked +2 percentage point growth scenario has now been run.

| Output | Base | Changed | Changed minus base |
| --- | ---: | ---: | ---: |
| Year 5 EBIT ($bn) | 502.817919 | 545.108057 | +42.290138 |
| Year 5 economic FCFF ($bn) | 385.971862 | 415.383081 | +29.411219 |
| Value/share ($) | 209.275411 | 224.813894 | +15.538482 |

Verification: PASS. Base before and after agrees exactly for inputs, all five statement years, outputs, valuation and checks. Only GROWTH differs in the changed run; every other saved independent input equals base. Revenue growth is 47%, 32%, 22%, 17%, 12%; EBIT margins remain 64%, 62%, 60%, 59%, 58%.

Also checked all eight saved sensitivity runs: only the selected input differs in each lower/higher run, all signed changes recompute, and base restoration agrees exactly. Across those eight runs and the three locked-scenario runs, 671 recorded accounting/feasibility checks pass; largest absolute reconciliation gap is 4.547e-13 USD billions, below the 1e-8 tolerance. Independently recomputed revenue, EBIT, FCFF, balance-sheet balance, cash and equity rollforwards, and discounted value/share from saved inputs and statement rows. No failed run requires correction. Display rounding: statements generally 0.001 billion and value/share $0.01; verification uses unrounded values.

### Trace through the statements

All table amounts below are Year 5 USD billions.

| Line | Base | Changed | Difference |
| --- | ---: | ---: | ---: |
| revenue | 866.927447 | 939.841478 | +72.914031 |
| ebit | 502.817919 | 545.108057 | +42.290138 |
| rd | 85.825817 | 93.044306 | +7.218489 |
| tax | 85.252157 | 92.441481 | +7.189323 |
| ni | 416.231122 | 451.331936 | +35.100815 |
| da | 10.403129 | 11.278098 | +0.874968 |
| capex | 26.007823 | 28.195244 | +2.187421 |
| delta_nwc | 15.762317 | 20.139460 | +4.377143 |
| cfo | 429.944338 | 463.147086 | +33.202749 |
| cfi | -26.007823 | -28.195244 | -2.187421 |
| cff | -43.357404 | -44.961513 | -1.604109 |
| cash | 1394.188478 | 1464.220547 | +70.032069 |
| equity | 1773.834763 | 1861.665975 | +87.831212 |
| fcff | 385.971862 | 415.383081 | +29.411219 |

Revenue compounds from the same opening $302.970 billion through the five revised growth rates. EBIT equals revenue × the unchanged annual EBIT margin. Gross margin and SG&A rules remain fixed; R&D is the model’s residual expense, so its dollar amount recalculates. Interest stays fixed because debt and its interest rate stay fixed; incremental net income is incremental EBIT × 83%.

Higher revenue raises D&A (1.2% of revenue), capex (3%), and incremental operating working capital (20% of the annual revenue increase). FCFF = EBIT × 83% + D&A − capex − incremental working capital. CFO also adds SBC; matching SBC buybacks enter financing cash flow. Closing cash follows CFO + CFI + CFF, and equity follows net income + SBC − buybacks − dividends. These links reconcile in every forecast year.

Value/share discounts all five FCFFs and normalized terminal FCFF, then adds opening cash and securities, subtracts opening debt, and divides by unchanged shares. Accumulated forecast cash is not added again. Terminal growth stays at 3.5%, but a larger Year 5 revenue base raises terminal cash flow.

### Prediction error

- ebit: actual increase 42.290138; predicted increase 40–45; within the predicted range. Difference from the range midpoint: -0.209862.
- fcff: actual increase 29.411219; predicted increase 28–32; within the predicted range. Difference from the range midpoint: -0.588781.
- per_share: actual increase 15.538482; predicted increase 15–16; within the predicted range. Difference from the range midpoint: +0.038482.

The direction prediction was correct. Midpoint errors reflect the rough estimates: revenue compounds multiplicatively over five years, and FCFF also reflects taxes and additional reinvestment. The exact discounted calculation includes the higher terminal revenue base. A range forecast does not imply that its midpoint must equal the actual result.

### Partner exchange 2 — verification evidence

The numerical verification is recorded below. The user subsequently confirmed that the partner exchange was completed and everything looked good; no issues or corrections were reported.

Presenter evidence: base Year 5 FCFF 385.971861766; changed FCFF 415.383080804. Listener recomputation: 415.383080804 − 385.971861766 = +29.411219038 billion. Checked every saved independent input against base: only GROWTH changed. The statement trace above explains the result.

Review question: Why does working-capital investment rise when the 20% input stays fixed? Answer: 20% is applied to a larger annual revenue increment. The linked dollar amount changes without changing a second independent input. Clarification: this locked scenario is +2 percentage points; the earlier sensitivity endpoints are ±5 percentage points. No numerical correction was needed.

Partner exchange completion: The user reported, “we checked and everything looks good.” No corrections were reported, so the recorded results, prediction comparison, and valuation/research implications remain unchanged. The partner’s model, numerical example, and specific question/answer were not provided in this record.

### Valuation conclusion and research priority

The base valuation remains $209.28/share; the changed scenario gives $224.81/share, an increase of 7.42%. This sensitivity alone does not justify replacing the base assumptions or changing an investment recommendation: it supplies no new evidence that the higher growth path is more likely, and no current market-price comparison was performed. The research priority is to validate the five-year revenue-growth path and its demand, deployment and reinvestment assumptions. Under the saved ±5-point ranges, the growth value/share span is $75.56 versus $37.71 for EBIT margin; this comparison depends on the chosen ranges and does not measure probabilities. Base-case conclusion unchanged; growth-assumption validation is reinforced.

Full run evidence: `nvidia_locked_scenario_results.json`.

## Output-span comparison and Partner exchange 3 preparation

Span means maximum minus minimum across the valid lower/base/higher runs. Both input paths move ±5 percentage points in each of Years 1–5: revenue growth ranges from 40%, 25%, 15%, 10%, 5% to 50%, 35%, 25%, 20%, 15%; EBIT margin ranges from 59%, 57%, 55%, 54%, 53% to 69%, 67%, 65%, 64%, 63%. Other independent inputs remain at base.

| Output | Revenue-growth span | EBIT-margin span | Larger driver over these ranges |
| --- | ---: | ---: | --- |
| Year 5 operating profit / EBIT ($bn) | 205.365 | 86.693 | Revenue growth |
| Year 5 economic FCFF ($bn) | 143.178 | 71.955 | Revenue growth |
| Value/share ($) | 75.56 | 37.71 | Revenue growth |

Over these ranges, revenue growth produces the larger span for all three outputs. This is a scenario-specific ranking, not proof that growth is inherently more important. A bigger span can reflect a wider input range. Here both paths have the same 10-percentage-point lower-to-higher width in each year, but growth compounds the revenue base across years, while margin changes apply to revenue at the unchanged base growth path. Equal percentage-point widths do not imply equal economic uncertainty or equal relative changes. Different ranges could change the ranking.

Causal link using actual results: raising the revenue-growth path from its lower to higher endpoint raises Year 5 EBIT from $408.456 billion to $613.821 billion. Higher compounded revenue raises EBIT at unchanged margin assumptions, but taxes and increased reinvestment absorb part of the operating-profit increase: FCFF rises from $319.635 billion to $462.814 billion, a smaller $143.178 billion span. Higher forecast and terminal cash flows raise value/share from $174.41 to $249.97. These comparisons use unrounded results before display rounding.

Partner exchange 3 details were subsequently supplied below. The following range question remains a suggested discussion prompt, not a question reported as received:

Suggested listener question: “Could the ranking reflect the ranges you chose?”

Prepared answer: “Yes. Revenue growth is the larger driver over these ranges. Both tested paths span 10 percentage points per year, but they act differently: growth compounds revenue, and margin determines the profit earned on that revenue. Different ranges could produce a different ranking; these ranges are judgments, not probability estimates.”

Suggested listener summary to confirm in the exchange: “Your NVIDIA model is more sensitive to revenue growth over the tested ranges, because growth compounds sales and increases operating and terminal cash flows. That conclusion is conditional on the ranges and fixed assumptions.”

Company comparison: both partners analyzed NVIDIA. The partner identified data-center business buildout as the business driver; this maps conceptually to the revenue-growth input in this model. Our explanations therefore point to the same growth mechanism rather than different company drivers. The partner’s numerical results and input ranges were not supplied, so agreement on a quantitative sensitivity ranking cannot be verified. Data-center buildout is a business explanation, not a separately tested independent input in this sensitivity analysis. Do not rank companies by raw dollar changes; even comparisons of the same company require consistent units, horizons and ranges.

Recorded exchange, based on the user’s report:
- Partner’s company: NVIDIA.
- Partner’s stated business driver: building out data-center businesses.
- Actual question received: “What if the AI bubble pops?”
- Answer given: “The world is evolving, and AI will always now be needed in the future.”
- Interpretation: the answer expresses a long-term AI-demand thesis. It does not establish that spending, NVIDIA revenue growth, margins or valuation will remain at the modeled levels.

Analytical qualification for the conclusion: continued use of AI can coexist with a fall in investment, slower data-center construction, lower pricing or reduced margins. In this model, the lower growth path gives $174.41/share versus the $209.28 base, while the lower margin path gives $190.42/share. These are separate one-input scenarios, not a combined stress test or a modeled AI-bubble collapse. Even the lower growth path retains positive growth in every year, so these results do not establish a downside floor. The long-term demand thesis alone does not resolve the partner’s downside question.

Main-driver comparison and limitation: both partners’ explanations emphasize NVIDIA’s revenue growth through data-center demand. Our numerical conclusion remains that revenue growth is the larger driver for EBIT, FCFF and value/share over these ranges. That conclusion depends on the chosen ranges and fixed assumptions; it does not show that growth is inherently the dominant driver under every scenario.

Remaining exchange evidence not supplied: the partner’s actual numerical example and tested ranges, a question about whether the ranking reflects range choices, and each listener’s confirmed summary of the other’s conclusion and limitation. These are not recorded as completed. Research priority: validate the durability of data-center spending and consider a separately specified downside scenario before claiming resilience to an AI investment downturn. No new downside run was performed for this entry.

## Revised answer and prepared partner example

Revised answer to “What if the AI bubble pops?”:

“I believe AI will remain useful, but an investment bubble could still burst and reduce data-center spending and NVIDIA’s growth. Revenue growth was the larger driver over our tested ranges, so that risk matters. Our sensitivity analysis did not test a full bubble-collapse scenario.”

This is the revised written answer; the original answer given during the exchange remains recorded above.

Prepared numerical example for the partner to review (from this model, not independently supplied by the partner): increasing annual revenue growth from the base path of 45%, 30%, 20%, 15%, 10% to 50%, 35%, 25%, 20%, 15% raises Year 5 EBIT from $502.817919 billion to $613.821007 billion, an increase of $111.003088 billion. Year 5 FCFF rises from $385.971862 billion to $462.813677 billion, an increase of $76.841815 billion. Value/share rises from $209.275411 to $249.966552, an increase of $40.691141. Differences use unrounded outputs. Only the revenue-growth path changes; all other independent inputs remain at base.

Causal explanation to discuss: data-center buildout could support the higher sales-growth path. Compounding higher annual growth increases revenue and EBIT at unchanged margins. Taxes and additional capex and working-capital investment absorb part of the incremental profit, so FCFF increases by less than EBIT. This scenario illustrates the proposed business mechanism; it does not establish that data-center buildout will produce the assumed growth rates.

Range question to ask: “Could revenue growth rank first because of the ranges we chose?”

Prepared answer: “Yes. Revenue growth produces the larger output spans over these ranges. Both growth and margin paths were varied by ±5 percentage points per year, but equal percentage-point widths do not represent equal economic uncertainty. Growth compounds across years; margin changes affect the profit earned on revenue. Different ranges could change the ranking.”

Partner-approved confirmation (approval reported by the user):

“I checked the numerical example and understand that higher revenue growth compounds sales, raising EBIT and FCFF while requiring additional reinvestment. We both connect NVIDIA’s growth to data-center demand. Revenue growth is the larger driver over the tested ranges, but that ranking depends on the ranges and assumptions. Continued AI use does not rule out a spending downturn.”

Draft reciprocal summary for the user to verify with the partner:

“My partner identifies data-center buildout as a business driver of NVIDIA’s revenue growth. I understand the causal link, but we need their actual model inputs and outputs to claim that their own sensitivity results establish the same numerical ranking.”

Confirmation status: approved. The user reported that her partner approved the prepared numerical example and confirmation wording. The example comes from this NVIDIA model; approval does not establish a separate calculation in the partner’s own model.

Partner exchange 3 update: The user reported, “she approved it.” The prepared numerical example and the statement explaining the causal link and the limitation of the chosen ranges are now recorded as partner-approved. No correction was reported. Earlier references to missing partner confirmation describe the status before this update. No separate partner-model results have been supplied.
