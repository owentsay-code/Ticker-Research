# Meridian Foundation Reserve: mandate review

This is the assigned fictional common case only. No portfolio has been optimized.

## R — classify S1–S10

| ID | CIO statement | Classification | One-line reason |
| --- | --- | --- | --- |
| S1 | Horizon seven years; annual rebalancing. | Hard constraint | The planning horizon and rebalancing schedule bind the process, but a weights snapshot cannot verify implementation. |
| S2 | Objective: CPI + 4% a year, net of costs, over rolling five-year periods. | Objective | This is a performance target, not an assured return or a selected optimization criterion. |
| S3 | Pays out $0.75 million every quarter; twelve months of payouts held in cash or daily-liquid government securities. | Hard constraint | Four distributions require $3 million, or 3% of the initial $100 million, in the table's reserve-eligible holdings. |
| S4 | Benchmark: 60% global equities, 40% U.S. investment-grade bonds. | Preference (evaluation reference) | In the supplied taxonomy this is an evaluative reference, not a required allocation or tracking-error limit. |
| S5 | Long-only: no borrowing, short sales or derivatives. | Hard constraint | Nonnegative fully funded weights in the supplied holdings implement the static portion of this prohibition. |
| S6 | No single issuer above 8%. | Hard constraint | Aggregate each company's securities; cash, Treasury and diversified funds are exempt. |
| S7 | Annual turnover at most 25% without committee approval. | Hard constraint | The conditional cap requires a turnover definition, trades and approval records, none supplied here. |
| S8 | At least 90% redeemable within five business days. | Hard constraint | Sum the weights of holdings whose stated redemption period is at most five business days. |
| S9 | “The reserve cannot have a calendar-year loss greater than 10%.” No measure, no breach rule. | Unverifiable promise | A future loss guarantee cannot be inferred from weights; the CIO must define the risk measure and response to a breach. |
| S10 | No sector, ESG, tax or home-bias preference; nobody has said what the pilot should optimize. | Missing | Preferences are explicitly absent, while the pilot's optimization criterion and trade-offs remain unspecified. |

S4 does not fit the five labels precisely: it is a benchmark designation rather than an allocation preference. Its classification above must not be used to impose 60/40 weights.

## What the CIO must answer before optimization

1. **S10/S2:** What should the pilot optimize: expected net real return, risk subject to a return target, shortfall probability, or benchmark-relative performance? Is CPI + 4% a target or a modeled constraint, and what trade-offs are authorized?
2. **S9:** Does loss mean nominal total return, real return, or change in assets after payouts? Define valuation, fees, cash-flow treatment and calendar-year measurement. Is 10% a realized monitoring threshold, a stress limit, or a probabilistic risk limit? For the latter, specify confidence level, model and scenarios; specify who monitors, reports and acts after a breach. Do not silently substitute volatility, VaR or maximum drawdown.
3. **S4:** Is 60/40 only a comparison benchmark, or must allocation bands or a tracking-error budget be imposed? Specify any limits explicitly.
4. **S1/S7:** Define turnover (one-way or two-way, treatment of cash flows), supply current holdings and trade history, and state approval and rebalancing procedures when annual rebalancing would exceed the cap.
5. **S2/S3:** Specify CPI series, annualization, cost assumptions and payout treatment; confirm reserve monitoring and replenishment. The table explicitly permits the 10-year Treasury note in the reserve, despite its price risk.
6. **Model governance:** Approve return, risk, correlation, inflation and cost assumptions, their estimation horizon, feasibility criteria and the authority to resolve conflicting requirements.

CFA Institute's *Elements of an Investment Policy Statement for Institutional Investors* separates objectives, constraints, governance, risk measures and rebalancing. Relevant sections are 2e–2f, 3b–3d and 4a–4c; they support documenting these choices before modeling. These Meridian classifications and questions are applications to the supplied fictional case, not quotations from CFA Institute. [Source PDF](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-institutional-investors.pdf).

## I — checker scope

Run `python mandate.py` from this directory (or `python3 mandate.py` if Python is installed under that name).

The checker implements the five requested numerical rules only. Its required verdict “passes every checkable rule” means those five checks; it does not certify turnover, annual rebalancing, future returns, or the loss promise. Borrowing and derivatives outside the supplied table cannot be audited from these weights.

## E — proposed adversarial portfolio

### Executed verification

`python mandate.py` was attempted, but this machine provides `python3` rather than `python`. All subsequent runs used `python3 mandate.py` successfully.

The baseline run matched every supplied expected value:

| Rule | A | B | C |
| --- | --- | --- | --- |
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass |
| Lowest weight | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve >= 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL |
| Redeemable within 5 days >= 90% | 100.0 pass | 85.0 FAIL | 100.0 pass |
| Largest company <= 8% | 0.0 pass | 9.0 FAIL | 8.0 pass |
| Calendar-year loss | requires CIO clarification | requires CIO clarification | requires CIO clarification |
| Verdict | passes every checkable rule | fails 3 rule(s) | fails 1 rule(s) |

Next, A was edited to Cash -2 and global equity 64 and rerun: lowest weight -2.0 failed, reserve 10.0 passed, and all other numerical checks passed. A was restored before adding D and rerunning. D returned total 100.0, minimum weight 0.0, reserve 100.0, liquid share 100.0 and largest company 0.0, all passing.

Only A among the original three is eligible under all five numerical checks. Full mandate permission remains unresolved because passing this checker does not establish compliance with the untested requirements.

Candidate D: 100% Cash, 0% in each other holding. This is a counterexample for inspection, not an optimized recommendation. It passes all static checks but provides no demonstrated basis for achieving S2's net CPI + 4% target; the CIO could reasonably reject it on that basis. Without cash-return and inflation assumptions, this is not proof of future underperformance. S4 alone does not prohibit D because no benchmark deviation constraint was stated.

### Two-sentence judgment (Codex acting as the assigned lab partner)

The objection holds as a reasonable basis for CIO rejection because a 100% cash portfolio passes the static checks without establishing a credible path to the required real return. S2 decides the objection: its CPI + 4% net return objective still matters, although the supplied information cannot prove that cash will miss it.

### Completed simulated partner swap

Per the revised classroom instructions, Codex supplies the partner role in this chat; this is an AI-assisted exchange, not an independent human judgment or a separate chat.

**Portfolio sent to the partner:** Original D, 100% Cash and zero in every other holding.

**Partner's response:** I cite **S2** against this portfolio: passing liquidity and concentration checks does not establish that it can meet the net real-return objective. This is a suitability objection, not a demonstrated numerical breach.

**Portfolio received from the partner:** Partner D, 3% Cash and 97% Global equity index fund, with zero in all other holdings. No optimization was used to select it.

The existing checker was run with partner D substituted in memory, leaving the saved original D unchanged:

| Check | Partner D result |
| --- | --- |
| Weights sum to 100 | 100.0 pass |
| Lowest weight | 0.0 pass |
| Reserve >= 3.0% | 3.0 pass |
| Redeemable within 5 days >= 90% | 100.0 pass |
| Largest single company <= 8% | 0.0 pass |
| Calendar-year loss | requires CIO clarification |
| Verdict | passes every checkable rule |

**Response to the partner's portfolio:** I cite **S9**: a 97% equity allocation exposes the gap between the CIO's loss statement and the rules the checker can enforce, so the CIO could reasonably withhold approval pending a defined risk assessment. This does not prove a future loss above 10%; S9 remains untestable as written, and S4's 60/40 benchmark by itself does not prohibit this allocation.

Both sides of the swap show that static eligibility is insufficient for approval: the original D exposes the return objective in S2, while partner D exposes the unresolved loss requirement in S9. Before optimization, the CIO must also select the pilot's objective under S10 and resolve the operational questions listed above.

## One CIO question before optimization

**Question:** What should the pilot optimize, and which takes priority if the CPI + 4% net return target and your 10% calendar-year loss requirement cannot both be satisfied?

**An answer that would change my portfolio:** “Prioritize limiting loss risk; minimize an explicitly defined downside-risk measure, and treat CPI + 4% as a secondary aspiration if it conflicts with that priority.” That answer would make me reconsider the partner portfolio's 97% equity allocation and evaluate a greater allocation to cash and Treasury bills. It would not justify selecting exact new weights yet: the CIO must define the loss measure, acceptable risk level and breach response, and approve the modeling assumptions. No allocation here is claimed to guarantee the 10% loss limit.

## Investment policy statement — learn on your own

**1. What is it?** An investment policy statement (IPS) is a written agreement about the purpose of a client's investments, the results sought, the limits on investing, and the responsibilities for managing and reviewing the portfolio. It provides a consistent basis for decisions and accountability.

**2. How does it work — objectives and constraints?** Objectives describe what success means; constraints restrict the choices and actions available to pursue it. A benchmark supplies a comparison, while governance specifies who approves decisions, monitors compliance and responds to problems. An optimizer needs a chosen criterion and measurable constraints; a return aspiration or an undefined loss promise cannot silently become a mathematical rule. The IPS guides the model, and the model does not replace client judgment.

**3. Map S1–S10 onto the IPS:** S1 supplies the horizon and rebalancing policy; S2 supplies the return objective; S3 supplies spending and reserve requirements; S4 supplies the performance benchmark; S5 supplies investment-method restrictions; S6 supplies issuer concentration limits; S7 supplies turnover limits and an approval exception; S8 supplies liquidity requirements; S9 expresses risk tolerance but lacks an operational definition; S10 states the absence of special preferences and exposes the missing optimization criterion. The R table above gives each statement's classification and reason.

These explanations apply the CFA Institute IPS framework cited above to this case.

## Reflect — Codex acting as the lab partner

**1. Why can a portfolio pass every checkable rule and still be wrong for this client?** The checker tests a small set of conditions using a single snapshot of holdings. It does not establish the portfolio's ability to earn CPI + 4% net, control calendar-year losses, follow annual rebalancing or satisfy the turnover cap over time. Our exchange demonstrates this: 100% cash passes while raising a return-objective concern under S2, and 97% equities with 3% cash passes while exposing the unresolved risk requirement under S9. Eligibility is necessary but does not establish suitability or full mandate compliance.

**2. Which S1–S10 type was least certain?** S4 was the least clear classification because a benchmark does not fit neatly into objective, hard constraint, preference, unverifiable promise or missing. I placed it under preference with an explicit qualification: it is an evaluation reference, and the CIO has not required the portfolio to hold exactly 60% equities and 40% bonds or stay within any stated deviation limit. Treating that benchmark as a hard allocation constraint would invent a rule.

## Floor — individual submission check

- Checker matches: all supplied A–C values matched the executed baseline.
- Probe fails long-only: A's -2% cash probe failed only long-only, with reserve still 10%; original A was restored.
- S1–S10 sorted: classifications, reasons and IPS mapping are included.
- D judged: original D and the simulated partner's D are evaluated, with the latter also run through the checker.
- One CIO question: the optimization priority question and a portfolio-changing hypothetical answer appear above.
- Partner work: Codex performed the partner role under the revised class instructions; this remains an individual submission.

## Project 2 mandate — Cedar Grove Scholarship Fund

**Fictional case:** This client and all following facts are invented for Project 2. They are separate from the Meridian common case and provide the starting mandate for Week 9; no portfolio has been optimized.

**Client and purpose:** Cedar Grove Scholarship Fund is a fictional community nonprofit with a $2 million investment portfolio. The portfolio supports local students through $60,000 in annual scholarships, paid in four equal quarterly installments. Its planning horizon is ten years, and it expects no new donations during that period. Awards remain fixed in nominal dollars unless the board revises the mandate.

### Objective

Fund the scheduled scholarships while seeking to preserve the portfolio's inflation-adjusted principal over ten years. Target an annualized return of CPI + 3% net of investment costs over rolling five-year periods, using U.S. CPI-U as the inflation reference. This is a performance aspiration, not a guaranteed return; the 3% initial spending rate motivates the target but does not prove that it will preserve purchasing power under every return path.

### Hard constraints

| Requirement | Operational rule |
| --- | --- |
| Spending | Pay $15,000 at each quarter-end, totaling $60,000 annually. |
| Distribution reserve | Hold at least the next four quarterly payments ($60,000) in cash or U.S. Treasury bills with remaining maturity of one year or less; this is 3% of the initial portfolio, and its percentage changes with portfolio value. |
| Liquidity | At least 95% of portfolio market value must be redeemable or saleable with proceeds available within five business days under normal market conditions. |
| Eligible investments | Cash, direct U.S. Treasury securities, and unleveraged diversified public equity or investment-grade bond funds; exclude private funds, individual corporate securities and cryptoassets. |
| Investment methods | Fully funded, long-only positions; no portfolio borrowing, short sales, direct derivatives, leveraged funds or inverse funds. |
| Concentration | No single diversified fund may exceed 40% of portfolio market value; cash and direct U.S. Treasury securities are exempt. |
| Rebalancing | Review compliance quarterly and rebalance to approved target weights annually, with additional trades allowed to meet payouts or restore compliance. |
| Turnover | Calendar-year one-way turnover, defined as the lesser of total security purchases and total security sales divided by average month-end portfolio value, must not exceed 30% without prior board approval; count Treasury and fund trades, including trades to fund payouts, but exclude movements between cash accounts. |

At each quarterly review, use current market values and updated liquidity information. Report any breach to the board within five business days and submit a correction plan; obtain approval before corrective trades that would exceed the turnover cap. No numeric loss ceiling has been agreed, so none is asserted as a hard constraint.

### Risk tolerance and preferences

The fictional board accepts that market values can fall and describes its risk tolerance as moderate, but that description is insufficient to set a mathematical risk limit. The board has no sector, ESG or home-bias preference and does not request after-tax optimization for this exercise. It prioritizes continuity of scholarship payments; its willingness to sacrifice expected long-term growth to protect principal still needs clarification.

### One question for the client

**If preserving the portfolio's real principal and achieving the CPI + 3% target require different levels of investment risk, should the pilot minimize downside risk subject to funding scholarships, or pursue the return target subject to a board-approved downside-risk limit?**

**An answer that would change the portfolio:** “Minimize downside risk and accept a lower expected return.” That answer would lead the pilot to evaluate more cash and short-maturity Treasuries and less equity exposure, while explicitly assessing the resulting risk of losing purchasing power after scholarship payments. Exact weights would depend on the agreed downside-risk measure and modeling assumptions; the answer would not establish a loss guarantee.

Before optimization in Week 9, translate the board's answer into a precise criterion and any approved risk limit, specify inflation and return calculations and investment-cost assumptions, and assess whether the objectives are feasible under these constraints.
