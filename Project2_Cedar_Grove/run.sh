#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON_BIN="${PROJECT2_PYTHON:-python3}"
if [ ! -x .venv/bin/python ]; then "$PYTHON_BIN" -m venv .venv; fi
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build_report.py
exec .venv/bin/python -m streamlit run app.py --server.address=127.0.0.1
