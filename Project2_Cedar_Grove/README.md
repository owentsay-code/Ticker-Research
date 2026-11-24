I used OpenAI Codex (GPT-6) to develop code, check calculations, and draft this analysis. The analysis and decision are mine.

Education, not investment advice.

# Cedar Grove — Project 2

**Reject live allocation (0%–0%); reconsider after reserve implementation, benchmark and risk policy approval, operational evidence, and passing approved stress criteria.**

This is a fictional $2 million scholarship fund. Start with [executed numbers](outputs/visible-output.md), the [decision memo](docs/decision-memo.md), and [validation and AI use](docs/validation-and-ai-use.md). The base research portfolio is 40% SGOV, 20% VGIT, 0% VCIT and 40% ACWI: estimated net return 5.7309%, annual volatility 6.7143%. It passes conditional research rules but **fails the literal mandate**, because fund shares do not meet the cash/direct-bill reserve rule. The app explains every baseline's verdict.

## One-command start

Prerequisites: macOS/Linux, Python 3.14, and internet access for the first dependency installation. Download this repository as ZIP and unzip, or clone it. If downloaded within Ticker-Research, open its Project2_Cedar_Grove subfolder. Open Terminal in the folder containing this README, then run:

```bash
bash run.sh
```

This creates `.venv`, installs pinned dependencies, regenerates baseline and stress output, then starts the interactive app. Open the Local URL printed in Terminal, normally http://localhost:8501. Stop with Ctrl+C. No API keys, uploads or account login are required. The locked changed-input experiment is deliberately not rerun by this command.

Windows PowerShell equivalent:

```powershell
py -3.14 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python build_report.py
.venv\Scripts\python -m streamlit run app.py
```

## Operate without the author

Change annual incremental costs from 25 to 50 basis points. Read the updated comparison and inspect an individual portfolio's rules. Uncheck the SGOV research-proxy box to apply the literal reserve rule: no feasible portfolio remains. The full mandate verdict is FAIL in either case. Download the scenario JSON for an auditable record. The app never places trades.

To regenerate files without the app after installation: `.venv/bin/python build_report.py`. To run checks: `.venv/bin/python -m unittest discover -s tests -v`.

## Evidence map

- [Original Lab 13 mandate](docs/lab13-mandate.md), [methods and unapproved assumptions](docs/methods.md), [signal data card](docs/signal-data-card.md).
- [Baseline JSON](outputs/baseline.json), [stress JSON](outputs/stress.json), [visible output](outputs/visible-output.md).
- [Published locked pre-run prediction](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20-prediction.md), [validation and AI use](docs/validation-and-ai-use.md), [Lab 20 checkout](https://github.com/owentsay-code/Ticker-Research/blob/ecfe8bd691fa0e2e8e15829db37a67a17e2e2d6c/lab20-checkout.md).
- [Submission manifest](docs/manifest.md).

Information set: October 22, 2026; prices through September 2026; analysis prepared November 17, 2026. This is a frozen research snapshot, not a live recommendation. Prior Lab 14 work is not overwritten. No submitted Edition A/B is required.

## Troubleshooting

If `python3` is missing or older than 3.14, install Python 3.14 from python.org; alternatively set `PROJECT2_PYTHON` to your Python 3.14 executable before running the command. If pip cannot reach its index, check network access and rerun; no partial outputs are treated as verified. If port 8501 is occupied, use `.venv/bin/python -m streamlit run app.py --server.port=8502`. A package install cannot be completed offline on a fresh machine; all computations after installation use local frozen data.

## Submission preparation

The completed locked cost result and verification record are in [validation and AI use](docs/validation-and-ai-use.md). The student reports the three videos are recorded. Add the actual transcripts as docs/transcript-video-1.txt, docs/transcript-video-2.txt and docs/transcript-video-3.txt after checking them against the recordings. Recording scripts and draft transcripts are excluded from this submission package. The [manifest](docs/manifest.md) identifies intended GitHub locations and the remaining video/upload checks. This local package has not been published by the November 22 preparation session.
