# NVIDIA — From Company Selection to Valuation Conclusion

Based on saved project evidence. The market comparison is dated September 8, 2026; the pro forma was prepared September 24 and the locked sensitivity test completed September 29. These are not updated market estimates.

## Present your analysis

Walk your partner through the full route in your own words, using the files already open. Explain the economic reason for an assumption as well as its value.

At the sensitivity stop, show a base-versus-changed result already computed in Lab 11. Trace **input → statement line → cash flow → value**, stopping at cash flow if valuation is unavailable. Explain why the driver matters over the stated range.

End with your supported conclusion and the assumption you would research next.

**Expect:** Your partner can follow the path from target selection to valuation and identify which evidence and assumptions carry the conclusion. Presentation polish is not the task.

## 1. Target selection

I selected NVIDIA because its profitability, cash generation, operating history, and public disclosures made it a promising company for an FCFF valuation. My screen required positive EBIT in all five historical years and positive FCFF in at least four, followed by a ranking weighted 60% toward ROIC and 40% toward FCFF stability. A single customer exceeding 30% of revenue would disqualify it.

My initial view was **INITIATE—provisionally**. However, the complete five-year FCFF reconstruction and comparative ranking were unfinished, so I had not fully demonstrated that NVIDIA passed every selection requirement.

**Show:** [Original Edition A—initial thesis, screening rules, and unknowns](</Users/owentsay/Downloads/Project1_EditionA_NVDA (1).md>) and [nine-line screening policy](<01-nine-line-policy.md>).

## 2. Company and evidence

NVIDIA earns revenue from accelerated-computing products and platforms, including GPUs, networking, and systems used in data centers, gaming, professional visualization, and automotive applications. CUDA supports its platform differentiation. The central forecast driver is sustained AI infrastructure spending.

My saved history uses FY2024, FY2025, and FY2026 10-Ks, covering years ended January 28, 2024; January 26, 2025; and January 25, 2026. Recorded revenue rises from **USD 60,922 million to 130,497 million to 215,938 million**. The forecast starts with **USD 302.970 billion TTM revenue through July 26, 2026**, calculated as annual revenue plus current first-half revenue minus the prior first half: 215.938 + 177.837 − 90.805.

Historical tables use **USD millions**; forecasts use **USD billions**. Annual reports establish history, while quarterly results and guidance provide near-term reference points—not five-year forecasts.

**Show:** [Pro-forma report—source-linked history, reporting dates, and TTM bridge](<DCF Models and Research/NVIDIA - Five Year Pro Forma - Sep 24.md>).

## 3. Your pro forma

I translated strong historical growth into a slowing forecast: **45%, 30%, 20%, 15%, and 10% revenue growth**. EBIT margins decline from **64% to 58%**, allowing for competition and pricing pressure while retaining strong platform profitability. These are analyst judgments.

Historical ratios and quarterly guidance informed assumptions including 17% tax, capex at 3% of revenue, D&A at 1.2%, and incremental working capital at 20% of additional revenue. R&D is a residual expense consistent with the selected EBIT margin, rather than an independently forecast driver. Years 1–5 are rolling annual periods from the September 24 modeling date, not NVIDIA fiscal years; July balances are opening proxies without a separate reporting-lag roll-forward.

The income statement feeds net income into equity and cash flow; investment updates operating assets; financing and distributions update cash and equity. Saved verification reports **671 accounting and feasibility checks passed** across sensitivity and locked-scenario runs. These checks establish internal consistency, not forecast accuracy. Cash-flow deductions retain their signs—for example, base Year 5 investing cash flow is **−USD 26.008 billion**.

**Show:** The [linked statements](<DCF Models and Research/NVIDIA - Five Year Pro Forma - Sep 24.md>) and [saved reconciliation checks](<../../NVIDIA - Locked Changed-Input Record.md>).

## 4. Valuation

My DCF discounts five years of:

**FCFF = EBIT × (1 − tax rate) + D&A − capex − incremental working capital.**

I assume **10% WACC** and **3.5% perpetual growth**, retaining the 58% Year 5 operating margin in the terminal period. Terminal working-capital investment is recalculated at the slower perpetual growth rate. WACC is an assumption, not a documented current cost-of-capital estimate. Terminal value supplies approximately **78% of enterprise value**.

The September 8 bridge is **USD 5,016.250bn enterprise value + USD 66.003bn net non-operating assets = USD 5,082.253bn equity value**. The net addition comprises USD 22.443bn cash, USD 34.143bn marketable debt securities, and USD 42.783bn marketable equity securities, less USD 33.366bn debt. Included assets are assumed available at carrying value without realization taxes; nonmarketable investments are excluded pending assessment. Accumulated forecast cash is not added again.

| Saved result | Value, date, and share basis |
| --- | --- |
| DCF base | **USD 209.28/share; September 8, 2026; 24.285bn quarterly diluted weighted-average shares used as a current-share proxy** |
| Market close | **USD 225.73/common share; September 8, 2026** |
| Peer P/E output | **USD 378.60–935.14/share; September 8, 2026 prices; NVIDIA FY2026 annual GAAP diluted EPS of USD 4.90** |

AMD provides AI-GPU overlap; Broadcom provides custom-accelerator and networking overlap. Their business mixes and earnings periods differ from NVIDIA’s. P/E is calculable, but transferring those multiples remains insufficiently justified. DCF values future operating cash flows; P/E applies market multiples to historical annual earnings. **I do not average the methods.**

The peer earnings periods end January 25, 2026 for NVIDIA, December 27, 2025 for AMD, and November 2, 2025 for Broadcom. Their annual diluted EPS conventions also differ from the DCF’s latest quarterly diluted-share proxy. The business, timing, and earnings-quality differences are limitations; they do not establish a corrected transferable multiple.

Reverse DCF requires **26.258% constant annual revenue growth for five years** to match the saved market price, holding margins, taxes, reinvestment, WACC, terminal growth, equity bridge, and shares fixed. It is conditional on that growth-path shape, not a uniquely observable market forecast.

**Show:** [DCF, bridge, and reverse DCF](<DCF Models and Research/NVIDIA - Full Valuation Report - Sep 08.md>) and [peer comparison](<Canidates.md>).

## 5. Sensitivity and drivers

Lab 11 shifted each annual growth or margin assumption **±5 percentage points**, one path at a time. All other independent inputs stayed at base while linked statement quantities recalculated.

*Values below: USD/share, September 24 rolling-model basis, fixed 24.285bn diluted-share proxy; tested in the saved September sensitivity work. Paths list Years 1–5.*

| Driver | Lower path | Base path | Higher path | Lower / base / higher value |
| --- | --- | --- | --- | --- |
| Revenue growth | 40/25/15/10/5% | 45/30/20/15/10% | 50/35/25/20/15% | **174.41 / 209.28 / 249.97** |
| EBIT margin | 59/57/55/54/53% | 64/62/60/59/58% | 69/67/65/64/63% | **190.42 / 209.28 / 228.13** |

The separately locked **+2-point growth** test changed the growth path to **47%, 32%, 22%, 17%, and 12%**, holding every other independent input fixed.

| Output | Base | Changed | Signed change |
| --- | ---: | ---: | ---: |
| Year 5 EBIT, USD billions | 502.818 | 545.108 | +42.290 |
| Year 5 FCFF, USD billions | 385.972 | 415.383 | +29.411 |
| Value, USD/share; September 24 model basis; 24.285bn diluted-share proxy | 209.28 | 224.81 | +15.54 |

Growth compounds revenue and raises EBIT; taxes and reinvestment absorb part of the increase before it becomes FCFF. Higher revenue also increases working-capital investment even though the 20% input remains fixed, because it applies to a larger revenue increase. Higher FCFF and the larger terminal revenue base raise value per share.

**Walkthrough to explain aloud:** “The economic reason for testing higher growth is stronger or more sustained AI infrastructure spending. I added two percentage points to each annual growth assumption while keeping margins and other independent inputs fixed. By Year 5, revenue rises from USD 866.927bn to USD 939.841bn. At the unchanged 58% EBIT margin, operating profit rises by USD 42.290bn. Taxes, capital spending, and working-capital investment absorb part of that gain, so FCFF rises by USD 29.411bn. Discounting the higher cash flows and larger terminal cash flow raises value from USD 209.28 to USD 224.81 per share, on the September 24 model basis using 24.285bn diluted-share equivalents. This explains the mechanism; it does not establish that the higher-growth scenario will happen.”

Revenue growth produces the larger valuation span **over these ranges**: USD 75.56/share versus USD 37.71/share for margin. This establishes neither probabilities nor a universal driver ranking, and it does not test simultaneous downturns. Equal percentage-point ranges do not imply equal economic uncertainty. The +2-point scenario supplies no new evidence that faster growth is more likely. Restoring the base inputs reproduced the original results exactly.

**Show:** [Lab 11 sensitivity results](<../../NVIDIA - Individual Sensitivity Submission.md>) and [locked prediction and actual results](<../../NVIDIA - Locked Changed-Input Record.md>).

## 6. Interpretation

My supported conclusion is **WATCH-DEFER**. The September 8 DCF base is 7.3% below the saved market price, while its conditional discount-rate/terminal-growth envelope includes that price. The evidence does not establish a sufficient margin of safety.

The saved **USD 164–294/share envelope, dated September 8, 2026 and using the 24.285bn diluted-share proxy**, varies WACC from 9% to 11% and terminal growth from 2.5% to 4.5%, holding the operating forecast fixed. It is not a confidence interval or an unconditional fair-value range.

My view changed from provisional enthusiasm about company quality to requiring evidence for the purchase valuation. I would reconsider initiating if conservative, source-supported forecasts and a documented discount rate establish sufficient upside. A lower purchase price could also change the decision after rechecking fundamentals; the existing evidence sets no numerical entry threshold. Persistent spending weakness, lower sustainable margins, or greater reinvestment would weaken the case; a customer exceeding 30% would trigger the original exclusion rule.

Next, I would investigate customer spending and financing durability, sustainable margins, and cost of capital; complete the original historical screen; and test a combined AI-spending downturn. A quantified comparison of peer growth, recurring earnings, risk, and fiscal timing could strengthen or weaken reliance on P/E. Continued AI usefulness alone does not rule out an investment bubble or spending contraction.

**Show:** [Final recommendation and unresolved evidence](<Canidates.md>) and [the saved AI-bubble discussion](<../../NVIDIA - Individual Sensitivity Submission.md>).

**Closing statement:** “My supported conclusion is WATCH-DEFER because the saved valuation does not establish a sufficient margin of safety. The assumption I would research next is the durability of the five-year revenue-growth path. My biggest concern is that AI remains useful but customers cut or delay data-center spending because their investments do not generate enough revenue. I would examine customer spending plans, order delays, inventory, and cash collection to assess whether growth can hold up. The sensitivity results show why this matters over the tested ranges, but a combined growth-and-margin downturn remains untested.”
