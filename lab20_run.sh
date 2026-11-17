#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .lab20-venv/bin/python ]; then python3 -m venv .lab20-venv; fi
.lab20-venv/bin/python -m pip install -r lab20_requirements.txt
.lab20-venv/bin/python lab20_report.py
exec .lab20-venv/bin/python -m streamlit run lab20_app.py --server.address=127.0.0.1
