I used OpenAI Codex (GPT-6) to develop code, check calculations, and draft this analysis. The analysis and decision are mine.

Education, not investment advice.

# Validation and AI use — Project 2

Prepared November 22, 2026. Recommendation: **reject live allocation, 0%–0%**. This record distinguishes a conditional research-model pass from a full mandate failure.

## Sources and information boundary

The original [Lab 13 mandate](lab13-mandate.md) defines a fictional $2 million scholarship fund with four $15,000 quarterly payments. [Source notes](original-data-notes.md) identify the archived Yahoo adjusted-price responses; [the signal card](signal-data-card.md) explains availability, revisions, missing values and lag. The research information set is October 22, 2026, with monthly prices through September 2026. Sixty prices produce 59 monthly returns. This November 22 verification does not update the investment information set.

CSV SHA-256: `26e2b2552b4ff99d55815895e5d18aeef07115cc74b3373f3745fd6815d09066`.

The 2.50% CPI assumption, 25-basis-point incremental annual cost, 60/40 proposed benchmark, minimum-variance objective and momentum exposure rule are research choices. No board-approved benchmark or numeric risk ceiling is claimed. The original mandate's unresolved risk criterion is an adoption blocker. Adjusted histories may be revised; the frozen snapshot is not a historical vintage backtest. See [methods](methods.md). The inherited source notes mention two Lab 14 screenshots that are not included in this self-contained package; those historical screenshots are not used as evidence for today’s checks.

## Verification and cold-run record

Environment: Python 3.14.7, Streamlit 1.67.0, NumPy 2.5.5, pandas 3.1.1; packages installed from the existing pinned requirements in a fresh temporary environment on November 22. Initial sandbox installation failed to resolve PyPI; installation succeeded with approved network access. No dependency versions were changed.

The inherited [November 17 checkout](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20-checkout.md) reports the earlier GitHub package lacked launch documentation and had missing/mismatched imports. That is historical evidence, not a claim of a new independent human cold run. The existing self-contained Cedar Grove folder supplies its own README, dependencies, engine and data.

Today's first test run passed all eight model tests but failed the app test: Streamlit resolved `app.py` relative to `tests/test_model.py`, looking for `tests/app.py`. The test now resolves the project entry point from its own absolute path. No portfolio logic changed. Final rerun: **all 9 tests passed in 1.266 seconds**, including the app startup and cost/reserve interactions. The only logged warning was Streamlit’s expected bare-mode ScriptRunContext warning; no app exception remained.

| Check | Evidence and result |
| --- | --- |
| Return and signal arithmetic | First monthly return equals current/prior price minus one; signal equals the 13-price trailing ratio minus one. |
| Annualization | Weighted monthly returns independently reproduce annual mean and sample volatility. |
| Grid optimum | Enumerates 1,771 weights and independently compares feasible variances. |
| Baselines and mandate | Equal weight fails the 5.50% research floor; 60/40 fails cap/reserve/signal rules; constrained mix passes modeled rules but all fail the full mandate. |
| Cost units | 25 to 50 bp lowers a fixed mix's net return by 0.25 percentage point without changing volatility. |
| Timing boundary | Changing the excluded latest price does not change one-month-lag estimates or signal. |
| Negative momentum | Negative signal reduces the research equity cap to 20%. |
| Invalid/infeasible settings | Invalid assumptions raise errors; a 20% four-fund cap returns no feasible portfolio. |
| App interaction | Startup, cost control, and strict-reserve control are exercised by the existing AppTest. |
| Saved results | Newly executed baseline and all seven ordinary stress results equal the saved JSON outputs. |

Reproduce from the project folder after following README installation:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python build_report.py
```

AppTest is headless interaction verification, not a claim that a stranger performed a browser walkthrough. Final uploaded-repository access and video checks remain submission steps.

## Locked Changed-Input Record

**Authorship:** AI-assisted. The student confirmed permission to use AI on November 22. The existing November 17 prediction records the student's report of an instructor accommodation waiving AI-off work. Instructor correspondence was not independently inspected. This is not described as a human-authored AI-off prediction; acceptance under the accommodation remains for the instructor.

**Immutable pre-run evidence:** [published prediction](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20-prediction.md), [baseline](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20-before.json), [engine](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20_engine.py), [prices](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/prices.csv). GitHub records commit `ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c` at **2026-11-17 22:01:00 UTC**. The record was recovered from the existing Lab 20 repository and carried forward into Project 2; no new pre-run authorship is claimed.

**Change:** annual incremental costs **25 → 125 basis points/year**, or **0.25% → 1.25%**. Fixed: 59-return window, October 22 information set, 2.50% CPI, 40% fund cap, 3% reserve requirement, SGOV research-proxy interpretation, zero extra lag, zero equity-estimate shift and 5-percentage-point grid.

**Prediction, written before the run:** each fixed portfolio's annual net return falls by exactly 1.00 percentage point; its weights and volatility stay unchanged. The feasible set can only shrink. If a reoptimized feasible portfolio remains, its minimum volatility cannot decrease; infeasibility is also possible. Reject/0%–0% remains because costs cannot repair reserve eligibility or governance.

**Verification before calculation:** the four published files above were downloaded at the immutable SHA and byte-compared with the existing local Lab 20 files; all matched. Cedar Grove's engine differs only in the price-file path and the combined-stress label. Its newly computed full baseline object exactly equaled the published baseline before executing the changed scenario. The prediction was not edited.

**Actual execution:** `2026-11-22T20:38:47.020113+00:00`. The following are executed results, not predictions:

| Fixed portfolio | Before net return | After net return | Change | Volatility before and after |
| --- | --- | --- | --- | --- |
| Equal weight | 3.6510% | 2.6510% | −1.0000 pp | 6.5134% |
| 60% ACWI / 40% VCIT reference | 6.7913% | 5.7913% | −1.0000 pp | 11.5367% |
| Original 40% SGOV / 20% VGIT / 0% VCIT / 40% ACWI | 5.7309% | 4.7309% | −1.0000 pp | 6.7143% |

Reoptimization: **14 feasible grid portfolios before; 0 after**. The changed scenario has no constrained weights, return or volatility to report. Infeasible is not zero volatility. Fixed-weight outcomes and shrinking feasibility agree with the prediction; no directional divergence needs diagnosis. The original constrained weights miss the 5.50% floor at the new cost. Decision remains **reject live allocation, 0%–0%**.

To reproduce the now-completed scenario in the app, retain defaults and set annual costs to 125 bp. Or run:

```bash
.venv/bin/python -c 'from engine import Inputs,run; import json; print(json.dumps(run(Inputs(cost_bps=125)),indent=2))'
```

The immutable GitHub Lab 20 prediction above is the verified pre-run receipt for this record. An earlier local draft was excluded from this submission package to avoid confusing it with that published evidence. This completed record is published after that pre-run commit.

## Ordinary stress results and stop rule

The memo and [saved stress output](../outputs/stress.json) cover estimates (ACWI −2 pp), window (36 returns), costs (50 bp), constraints (30% fund cap and strict reserve eligibility), and combined changes. The equity-estimate, 30% cap and strict-reserve cases are infeasible. The 36-return case has 324 feasible mixes; the 50-bp case has 5; the combined case has 34. The existing label “Combined adverse” does not mean every component worsens estimates: the shorter window can improve them. All mandate verdicts remain FAIL.

Stop on invalid data or no feasible grid solution. Withhold live adoption while reserve implementation, benchmark/risk approval, or operational evidence is missing. Monitor quarterly reserve dollars, 95% five-day liquidity and 40% fund caps; review targets annually; obtain advance approval for one-way turnover above 30%; report breaches within five business days. Reconsider only after those blockers are resolved and approved stress criteria pass.

## Material AI uses and disposition

| Interaction date | Tool/model disclosed | Use | Check and disposition |
| --- | --- | --- | --- |
| November 17, 2026 (inherited records) | OpenAI Codex (GPT-6), as recorded locally | Code, methodology, memo and AI-assisted partner prediction | Retained with explicit research assumptions and unresolved governance. Historical dates/attribution are inherited, not a reconstructed chat log. |
| November 22, 2026 | OpenAI Codex, GPT-6 family as exposed by this session; exact build not exposed | Reviewed files and checklist, located pre-run GitHub evidence, executed validation and cost experiment, corrected test path, drafted submission records and video narration | Compared published bytes and full baseline, checked saved stress output, ran tests. Retained verified numbers; rejected the implication that a modeled PASS authorizes adoption. |
| November 23, 2026 | Anthropic Claude (Opus 5.5) | Extracted YouTube auto-captions of the three recorded videos into transcript files, corrected misheard names/tickers/terms, and filled video URLs, durations and timestamps in the manifest | Transcript wording kept as spoken apart from filler words and caption errors; one unclear phrase in Video 2 marked [unclear]. Numbers in transcripts match the memo and validation record. |

AI-assisted drafting is disclosed in the README, memo and each video opening. Student review and responsibility are required before reading first-person narration. No independent human partner, approval, transcript, recording, or GitHub upload is invented.

## Submission package

All three videos are published on YouTube with captions; transcripts taken from those captions are in `docs/`, and the manifest lists the YouTube URLs, measured durations and timestamp indices. The same decision-memo.md, validation-and-ai-use.md and manifest.md are attached to Brightspace. Edition A/B, PDFs and video files are not part of this submission.
