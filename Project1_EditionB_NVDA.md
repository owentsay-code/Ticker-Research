# Project 1 — Edition B: NVIDIA

Prepared October 19, 2026 with AI assistance; student review and agreement subsequently confirmed (see ../07_Validation_AI_Record/Student_Review_Confirmation.md). This is separate from the unchanged Edition A. The historical valuation date is September 8, 2026, replacing Edition A's September 1 date to align with the saved price/peer analysis. No October market inputs are silently substituted. Decision horizon: next 12 months; five rolling annual forecast periods approximately September 2026–September 2031. The July 26 opening balance sheet and TTM sales are lagged proxies; no stub-period forecast or roll-forward is added.

## Mandate and scope

Buy-side portfolio manager deciding whether to initiate a position in NASDAQ NVDA common stock, with no existing holding. Action: WATCH/DEFER pending conservative-value support. USD billions for financial statements, billions of diluted shares, dollars per share. Eligible nonfinancial operating company. Exclude nonmarketable investments from the bridge, investment gains from operating forecast, unqualified transactions, and screening scores from valuation evidence. Operating leases stay in operating costs; a separate lease-debt deduction would require a consistent operating recast.

## Edition A to B

| Edition A position or gap | Evidence and modeling change | Decision effect |
| --- | --- | --- |
| Provisional INITIATE was linked to screen quality | Distinguish target admission from valuation; build FCFF, bridge and sensitivity | WATCH/DEFER; quality alone is insufficient |
| Approximate FY2026 revenue mixed fiscal-year references | Reconcile FY26 and H1 periods to a $302.970bn TTM starting point | Correct units/periods before forecasting |
| FCFF not yet rebuilt; FCF definitions unclear | Linked operating forecast; economic SBC convention; explicit reinvestment and financing | Value comes from operating FCFF, not cash after distributions |
| Customer and peer assumptions unresolved | Preserve concentration challenge; compare two qualified peers with explicit definitions | Do not transfer their P/E mechanically |
| No defended valuation range | Causal cases, WACC/g grid and reverse DCF | Conditional range and reversal triggers replace point confidence |
| Statements calculated once | Add bounded driver panel, reset and failing checks | Teammate can test and audit the assumptions |

### What did not materially change

| Topic | Continuity from Edition A | Evidence in Edition B |
| --- | --- | --- |
| Company under study | NVIDIA remains the selected company and subject of the analysis. | Mandate and scope; the analysis still covers NASDAQ NVDA common stock. |
| Operating quality | The view that NVIDIA has a strong operating record remains; quality alone no longer determines whether to buy. | Linked forecast, peer diagnostics and WATCH/DEFER decision. |
| Customer concentration | The literal single-customer threshold remains distinct from broader concentration risk. | Customer concentration is retained as a challenge and a reason to monitor demand. |
| Decision framework | Initiate, defer/watch and do-not-initiate remain possible actions; evidence can change the action. | Conditional valuation range, margin-of-safety condition and reversal triggers. |

Edition A's original wording and errors are retained. Checkpoint acceptance is resolved through the Lab 03 record and student-reported TA confirmation. These records do not independently establish the original AI-use boundary. The October peer policy and workbench cannot be backdated to demonstrate work completed in earlier labs.

## Model architecture

Opening sourced balances → bounded assumptions → linked income statement, balance sheet and cash flow → economic FCFF → WACC/terminal DCF → opening enterprise-to-equity bridge → per-share range. Historical facts, normalization choices, forecasts and calculated outputs are separated in Evidence_Ledger.md and Assumption_Challenge_Record.md. The original model and research remain in archive; the active Python engine reproduces the saved $209.28 base. The active workbench wraps that engine rather than replacing its economics.

Year t sales = prior sales × (1 + growth). EBIT = sales × margin. NOPAT = EBIT × (1 - operating tax). FCFF = NOPAT + D&A - capex - change in operating working capital. A condensed working-capital allocation uses opening account proportions. Cash follows cash flow; equity follows earnings, SBC and distributions. R&D is residual to gross profit, SG&A and chosen EBIT, so negative R&D is a real infeasibility signal. This is a NVIDIA demand/margin/reinvestment architecture; it does not claim a bottom-up GPU units/ASP or segment model.

D&A and SBC already sit in GAAP operating expenses. D&A is added back in FCFF; SBC is not. Cash-flow statements add SBC and assume offsetting repurchases, preserving a fixed diluted-share proxy. Terminal revenue grows at g; terminal working-capital investment is recomputed at g rather than repeating the high-growth year-five charge. Terminal ratios remain at year five. No accumulated forecast cash is added again to the equity bridge.

## WACC convention

The inherited 10% WACC is a required-return judgment. Using historical quote × 24.285bn diluted proxy shares and $33.366bn debt gives approximately 99.4% equity weight and 0.6% debt. With 4% assumed debt cost and 17% tax, a 10% WACC implies roughly 10.04% cost of equity. This algebra makes the hurdle internally interpretable; it is not evidence for beta, the risk-free rate or the equity risk premium. Test 9–11%; independently estimate dated market components before treating the hurdle as an observed cost of capital.

## Causal valuation cases

| Scenario | Causal assumptions | Year 5 EBIT ($bn) | Year 5 FCFF ($bn) | Value/share |
| --- | --- | --- | --- | --- |
| Low | Growth -5pp; EBIT margin -5pp; WACC 11%; g 2.5% | 373.24 | 290.41 | $125.30 |
| Base | Saved growth/margins; WACC 10%; g 3.5% | 502.82 | 385.97 | $209.28 |
| High | Growth +5pp; EBIT margin +5pp; WACC 9%; g 4.5% | 666.74 | 506.73 | $386.04 |

Detailed committee action, conditions and triggers are in the committee memo. The high/low cases change several mutually consistent assumptions; they are not the same as one-at-a-time sensitivities and have no assigned probabilities. These ranges do not bound a catastrophic spending collapse.

## Own-pro-forma sensitivity and fresh eyes

Over ±5pp paths, growth has larger Year 5 EBIT, FCFF and value spans than operating margin. The new range experiment narrows growth to ±1pp while retaining margin ±5pp: margin then ranks first for all three measures. That is an executed robustness check, not merely a warning that ranges could matter. All seven exposed drivers are also varied separately; discount rates affect value but leave explicit EBIT/FCFF unchanged.

The existing human-partner account reports the challenge “What if the AI bubble pops?” and approval of a growth mechanism example. The student has now identified the challenger as Kristyn and supplied a retrospective discussion summary; see ../07_Validation_AI_Record/Partner_Exchange_Kristyn.md. The answer is revised to distinguish useful AI technology from sustainable customer spending, preserve the watch decision and acknowledge that the modest ±5pp demand range is not a collapse case. The original locked record separately says the assistant acted as Partner for its initial prediction review. These are different events; do not conflate them.

## Comparable policy and disagreement

Read Peer_Policy.txt and Peer_Comparison.md. The October policy was written before new EV calculations, then the existing AMD/AVGO candidates were re-qualified. It is not evidence that a policy preceded September selection; the archive explicitly says no peer policy was assigned. Both annual EV/revenue and total-GAAP annual P/E are calculated consistently, with qualified timing and share proxies. No transaction comparison is forced and no arithmetic average of methods determines the recommendation.

## Validation and limits

Read the validation/AI record and machine-readable results. Numerical checks include opening-source mapping, historical cash rollforward, statement articulation, independent FCFF, equity bridge, known-answer Decimal calculation, WACC/g monotonicity, reverse re-pricing, range ranking, invalid controls and highest-risk failure. A clean temporary virtual environment run is separately logged. A recorded cold run, course published benchmark and qualifying human AI-off record remain student/course evidence tasks. No fabricated receipt, precommit, transcript, partner name or prior AI-off claim has been created.
