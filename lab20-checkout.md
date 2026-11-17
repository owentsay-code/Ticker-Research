# Lab 20 — Cedar Grove checkout

OpenAI Codex (GPT-6) is the AI partner for this lab under an instructor accommodation reported by the student. AI-assisted; not an AI-off or independent human-partner exercise. Education, not investment advice. Prepared November 17, 2026.

## Decision line

**Reject live allocation to this process (0%–0%); reconsider only after reserve eligibility, benchmark and risk policy are approved, operational controls are evidenced, and the approved model passes stress checks.**

## First cold-run finding

Public GitHub revision `b9ca4d2c03d5f6884947f2ad58e6c23dc985f32f` was downloaded to a separate folder on November 17. No README or dependency file existed, so a stranger had no documented start command. Analyst-selected diagnostic runs with Streamlit AppTest then found:

- `app.py`: `ImportError: cannot import name 'search_portfolio' from 'portfolio'` (0.71 seconds).
- `streamlit_app.py`: `ModuleNotFoundError: No module named 'lab14_engine'` (0.06 seconds).

Times are execution only, not installation/download. The existing local `portfolio.py` was newer than GitHub (10,541 versus 5,541 bytes). Pairing the old app with that local file in a separate diagnostic folder restored startup with zero exceptions (0.71 seconds); its Meridian training result was 6.51% return, 9.44% volatility, 20% reserve. Those are not Cedar Grove results.

## Additive fix

All old files are preserved. A new self-contained `lab20_app.py` imports `lab20_engine.py`, reads the existing identical `prices.csv`, displays equal-weight and 60/40 baselines plus a constrained research portfolio, and exposes rule-by-rule verdicts. A new README and `lab20_run.sh` document the launch. Every fund, including SGOV, has the 40% research cap. Strict reserve eligibility and missing governance are visible adoption blockers.

Current research baseline: 40% SGOV / 20% VGIT / 0% VCIT / 40% ACWI; net annual estimate 5.7309%, volatility 6.7143%; conditional model PASS, full mandate FAIL. These numbers are generated, not manually entered in the engine. See [baseline](lab20-before.md) and [methods](lab20-methods.md).

## Locked changed-input sequence

The AI-assisted prediction is in [lab20-prediction.md](lab20-prediction.md). This first commit precedes the locked run. After it is published, `lab20_report.py --after --prediction-commit FULL_SHA` verifies the remote prediction, baseline, engine and data bytes before calculating the 25-to-125-bp cost scenario. The actual result and commit link will be added in [lab20-after.md](lab20-after.md).

## Explain the code

`estimates` computes 12 times monthly sample means and covariance; volatility uses square root of the weighted covariance quadratic form. `run` enumerates all 1,771 fully invested long-only 5-point-grid portfolios, filters caps, reserve interpretation, net target and signal cap, then selects minimum variance. `evaluate` gives the numerical checks and the separate full-mandate verdict. `table` supplies the app's comparable numbers. The app does not implement trades.

Partner question: Why can a portfolio pass the model but fail the mandate? Answer: the model may conditionally count SGOV as reserve; the actual mandate specifies cash or direct bills, and risk/benchmark approvals and operational evidence are still missing. An optimizer cannot grant those approvals.

This is an AI-assisted code explanation; it is not falsely certified as a six-minute human oral demonstration.

## Reflection

The cold run exposed a local-versus-GitHub version mismatch that was invisible when using the working local files. The new entry point makes its dependencies and its mandate limitations explicit. Freeze the tested new entry point, data snapshot, assumptions and locked experiment before the deadline; do not silently change the prediction after publication or relax constraints to force a pass.

## Unresolved full-project work

The lab does not certify Project 2 readiness. The final Project 2 `docs/decision-memo.md`, `docs/validation-and-ai-use.md`, manifest and three Project 2 videos/transcripts remain separate requirements. A benchmark and risk policy remain unapproved; reserve implementation and operational monitoring require resolution before live use. Today's checkout reports those limitations rather than claiming adoption readiness.

## Verification status before publication

Baseline and ordinary stress calculations have run. Post-fix clean-folder launch verification and the locked changed-input result are recorded in a follow-up commit after this pre-run prediction is public.
