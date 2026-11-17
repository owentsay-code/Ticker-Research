# Locked changed-input prediction — PRE-RUN

Prepared November 17, 2026. AI-assisted partner prediction, not AI-off.
The student reports that the instructor authorized AI to act as the partner and waived the AI-off portion for this lab. This records the student's report, not independently verified instructor correspondence.

One changed input: annual incremental investment cost, from **25 basis points per year (0.25%) to 125 basis points per year (1.25%)**. Hold the information set, CPI assumption, signal, estimation window, grid, reserve-proxy setting and fund cap fixed.

Prediction before executing the changed scenario: every fixed portfolio's expected net return falls by exactly **1.00 percentage point per year**; its weights and estimated volatility do not change. The constrained optimizer's feasible set can only shrink, never expand. If a feasible portfolio remains, its minimum achievable volatility cannot decrease; the mix may move toward higher estimated returns. It may instead become infeasible. I do not predict an exact reoptimized allocation before the run.

Decision effect: **reject live allocation, 0%–0%**, remains unchanged because increasing costs cannot resolve the strict reserve shortfall, missing risk approval, missing benchmark approval or missing operational evidence.

Pre-run publication rule: commit this file and the baseline output, push them to GitHub, verify the remote commit, then execute `python lab20_report.py --after --prediction-commit FULL_SHA`. Keep this file unchanged after that commit; append actual results in lab20-after.md. Do not call a local commit a GitHub push.
