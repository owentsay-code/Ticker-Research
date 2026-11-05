"""Lab 19 — Four-Investor Panel + Cathie Wood (single-file version).

Everything the app needs is in this one file: the keyless SEC EDGAR loader,
Buffett / Graham / Burry / Cathie Wood checks, the memo number audit, the
saved COST and NVDA memos, and the Streamlit interface.

Run locally:   streamlit run lab19_app.py
Needs only:    streamlit and pandas (certifi is installed with streamlit)

Data from SEC EDGAR; built with AI help; a learning demonstration, not investment advice.
"""
from datetime import date, datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import ssl
import tempfile
import time
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Settings (formerly skill/graham-business/settings.json and edgar.py constants)
# ---------------------------------------------------------------------------
GRAHAM_CURRENT_RATIO_MINIMUM = 2.0   # assigned defensive liquidity cushion
WOOD_CAGR_THRESHOLD = 20             # illustrative classroom proxy, not an ARK rule
USER_AGENT = 'Owen Tsay octsay43@gmail.com'   # SEC requires a contact in the User-Agent
TICKERS_URL = 'https://www.sec.gov/files/company_tickers.json'

TAGS = {
    'revenue': ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues'],
    'net_income': ['NetIncomeLoss'],
    'operating_cash_flow': ['NetCashProvidedByUsedInOperatingActivities'],
    'capital_spending': ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets'],
    'equity': ['StockholdersEquity'],
    'liabilities': ['Liabilities'],
    'current_assets': ['AssetsCurrent'],
    'current_liabilities': ['LiabilitiesCurrent'],
}
INSTANTS = {'equity', 'liabilities', 'current_assets', 'current_liabilities'}
LABELS = {'revenue': 'Revenue', 'net_income': 'Net income', 'operating_cash_flow': 'Operating cash flow',
          'capital_spending': 'Capital spending', 'equity': 'Equity', 'roe': 'ROE', 'owner_earnings': 'Owner earnings',
          'liabilities': 'Liabilities', 'current_assets': 'Current assets', 'current_liabilities': 'Current liabilities'}

ROOT = Path(__file__).resolve().parent


def writable_dir(name):
    """Use a folder next to this file; fall back to a temp folder on read-only hosts."""
    for base in (ROOT, Path(tempfile.gettempdir()) / 'lab19_panel'):
        folder = base / name
        try:
            folder.mkdir(parents=True, exist_ok=True)
            probe = folder / '.write_test'
            probe.write_text('ok')
            probe.unlink()
            return folder
        except OSError:
            continue
    raise OSError(f'No writable location found for {name}.')


DATA_DIR = writable_dir('data')
REPORTS_DIR = writable_dir('reports')


# ---------------------------------------------------------------------------
# SEC EDGAR loading and annual selection (formerly skill/buffett-business/scripts/edgar.py)
# ---------------------------------------------------------------------------
def ticker_name(value):
    value = value.strip().upper()
    if not re.fullmatch(r'[A-Z][A-Z0-9.-]{0,14}', value):
        raise ValueError('Enter a valid US ticker, such as COST or BRK-B.')
    return value


def ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def download(url, path, refresh=False):
    if path.exists() and path.stat().st_size > 0 and not refresh:
        try:
            return json.loads(path.read_text())
        except ValueError:
            pass  # damaged cache: download again
    time.sleep(0.2)
    request = Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    with urlopen(request, timeout=45, context=ssl_context()) as response:
        data = json.load(response)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return data


def annual(fact):
    if fact.get('form') != '10-K' or fact.get('fp') != 'FY' or 'start' not in fact:
        return False
    # Accept normal calendar years and 52/53-week fiscal years, not quarters or YTD.
    days = (date.fromisoformat(fact['end']) - date.fromisoformat(fact['start'])).days + 1
    return 350 <= days <= 380


def select(facts, tags, end, flow):
    for tag in tags:
        entries = facts.get(tag, {}).get('units', {}).get('USD', [])
        matches = [f for f in entries if f.get('form') == '10-K' and f.get('end') == end
                   and (annual(f) if flow else 'start' not in f)]
        if matches:
            winner = max(matches, key=lambda f: (f['filed'], f['accn']))
            tied = [f for f in matches if (f['filed'], f['accn']) == (winner['filed'], winner['accn'])]
            if len({f['val'] for f in tied}) > 1:
                raise ValueError(f'Ambiguous SEC facts for {tag} ending {end}; inspect the filing.')
            return {'value': winner['val'], 'tag': 'us-gaap:' + tag,
                    'filed': winner['filed'], 'accession': winner['accn'],
                    'start': winner.get('start'), 'end': end}
    return {'value': None, 'tag': 'not found', 'searched_tags': tags, 'end': end}


# ---------------------------------------------------------------------------
# Investor checks (formerly skill/<investor>-business/scripts/*_checks.py)
# ---------------------------------------------------------------------------
def graham_checks(rows, threshold=GRAHAM_CURRENT_RATIO_MINIMUM):
    latest = rows[-1] if rows else None
    ratio = latest['current_ratio'] if latest else None
    income = [r['cells']['net_income']['value'] for r in rows]
    complete = len(income) == 5 and all(v is not None for v in income)
    endpoints = len(income) == 5 and income[0] is not None and income[-1] is not None
    return {
        f'Current ratio ≥ {threshold:g}, latest year': 'not known' if ratio is None else ('pass' if ratio >= threshold else 'fail'),
        'Net income positive every year': 'not known' if not complete else ('pass' if all(v > 0 for v in income) else 'fail'),
        'Net income grew from first year to last': 'not known' if not endpoints else ('pass' if income[-1] > income[0] else 'fail'),
    }


def burry_checks(rows):
    pairs = [(r['cells']['operating_cash_flow']['value'], r['cells']['net_income']['value']) for r in rows]
    complete = len(pairs) == 5 and all(a is not None and b is not None for a, b in pairs)
    ratio = rows[-1]['liabilities_equity'] if rows else None
    return {
        'Operating cash flow ≥ net income every year': 'not known' if not complete else ('pass' if all(a >= b for a, b in pairs) else 'fail'),
        'Liabilities ≤ 2 × equity, latest year': 'not known' if ratio is None else ('pass' if ratio <= 2 else 'fail'),
    }


def wood_checks(rows):
    """Illustrative classroom growth proxies, not official Wood/ARK criteria."""
    values = [r['cells']['revenue']['value'] for r in rows]
    complete = len(values) == 5 and all(v is not None and v > 0 for v in values)
    cagr = None if not complete else ((values[-1] / values[0]) ** (1 / 4) - 1) * 100
    return cagr, {
        f'Revenue CAGR ≥ {WOOD_CAGR_THRESHOLD}% (classroom proxy)': 'not known' if cagr is None else ('pass' if cagr >= WOOD_CAGR_THRESHOLD else 'fail'),
        'Revenue increased every year (classroom proxy)': 'not known' if not complete else ('pass' if all(b > a for a, b in zip(values, values[1:])) else 'fail'),
        'Disruptive innovation supported by supplied facts': 'not known',
    }


def compute(company, ticker):
    facts = company['facts'].get('us-gaap', {})
    # Each filing's latest annual period is its reporting year; comparative fy labels
    # identify the filing year, so never group facts using the SEC's `fy` property.
    latest_by_filing = {}
    for concept in facts.values():
        for f in concept.get('units', {}).get('USD', []):
            if annual(f):
                latest_by_filing[f['accn']] = max(f['end'], latest_by_filing.get(f['accn'], ''))
    ends = sorted(set(latest_by_filing.values()))[-5:]
    if not ends:
        raise ValueError('No annual US-GAAP USD facts from 10-K filings were found.')
    rows = []
    for end in ends:
        cells = {name: select(facts, tags, end, name not in INSTANTS) for name, tags in TAGS.items()}
        ni, eq, ocf, cap = [cells[k]['value'] for k in ('net_income', 'equity', 'operating_cash_flow', 'capital_spending')]
        ca, cl, liabilities = [cells[k]['value'] for k in ('current_assets', 'current_liabilities', 'liabilities')]
        rows.append({'fiscal_year_end': end, 'cells': cells,
                     'current_ratio': None if ca is None or cl is None or cl <= 0 else ca / cl,
                     'liabilities_equity': None if liabilities is None or eq is None or eq <= 0 else liabilities / eq,
                     'roe': None if ni is None or eq is None or eq <= 0 else ni / eq * 100,
                     'owner_earnings': None if ocf is None or cap is None else ocf - cap})

    def every(key, predicate):
        if len(rows) != 5 or any(r[key] is None for r in rows):
            return 'not known'
        return 'pass' if all(predicate(r[key]) for r in rows) else 'fail'

    first, last = rows[0]['owner_earnings'], rows[-1]['owner_earnings']
    growth = 'not known' if len(rows) != 5 or first is None or last is None else ('pass' if last > first else 'fail')
    result = {'ticker': ticker, 'company': company.get('entityName', ticker), 'cik': company['cik'],
              'rows': rows, 'checks': {'ROE ≥ 15% every year': every('roe', lambda n: n >= 15),
                                       'Owner earnings positive every year': every('owner_earnings', lambda n: n > 0),
                                       'Owner earnings grew from first year to last': growth}}
    # All investors consume exactly these same selected rows.
    result['panel_checks'] = {'Buffett': result['checks'], 'Graham': graham_checks(rows), 'Burry': burry_checks(rows)}
    result['wood_cagr'], result['panel_checks']['Cathie Wood'] = wood_checks(rows)
    return result


# ---------------------------------------------------------------------------
# Tables and report text
# ---------------------------------------------------------------------------
def money(value):
    return 'not found' if value is None else f'{value / 1_000_000:,.3f}'.rstrip('0').rstrip('.')


def value_table(result):
    return [{'Fiscal-year end': r['fiscal_year_end'],
             **{LABELS[k]: money(v['value']) for k, v in r['cells'].items()},
             'ROE (%)': 'not known' if r['roe'] is None else f"{r['roe']:.1f}",
             'Owner earnings': money(r['owner_earnings']),
             'Current ratio': 'not known' if r['current_ratio'] is None else f"{r['current_ratio']:.2f}",
             'Liabilities / equity': 'not known' if r['liabilities_equity'] is None else f"{r['liabilities_equity']:.2f}"}
            for r in result['rows']]


def panel_table(result):
    return [{'Investor': investor, 'Check': check, 'Status': status}
            for investor, checks in result['panel_checks'].items() for check, status in checks.items()]


def report_text(result):
    lines = [f"# {result['ticker']} — {result['company']}", '',
             'Amounts in USD millions; ROE in percent. Fiscal years are labelled by end date.', '']
    table = value_table(result)
    columns = list(table[0])
    lines += ['| ' + ' | '.join(columns) + ' |', '| ' + ' | '.join(['---'] * len(columns)) + ' |']
    lines += ['| ' + ' | '.join(row.values()) + ' |' for row in table]
    lines += ['', '## Checks'] + [f'- {k}: {v}' for k, v in result['checks'].items()]
    lines += ['', '## Investor panel', '', '| Investor | Check | Status |', '| --- | --- | --- |']
    lines += ['| ' + ' | '.join(row.values()) + ' |' for row in panel_table(result)]
    lines += ['', 'Cathie Wood classroom proxy revenue CAGR: ' + ('not known' if result['wood_cagr'] is None else f"{result['wood_cagr']:.1f}%"),
              'The 20% threshold is a classroom choice, not an official Wood/ARK rule. Innovation evidence is not supplied.']
    lines += ['', '## XBRL provenance', '', '| Fiscal-year end | Metric | XBRL tag | Filed | Accession |', '| --- | --- | --- | --- | --- |']
    for r in result['rows']:
        for k, cell in r['cells'].items():
            lines.append(f"| {r['fiscal_year_end']} | {LABELS[k]} | {cell['tag']} | {cell.get('filed', 'not found')} | {cell.get('accession', 'not found')} |")
        lines.append(f"| {r['fiscal_year_end']} | ROE | derived: NetIncomeLoss / StockholdersEquity × 100 | — | — |")
        lines.append(f"| {r['fiscal_year_end']} | Current ratio | derived: AssetsCurrent / LiabilitiesCurrent | — | — |")
        lines.append(f"| {r['fiscal_year_end']} | Liabilities / equity | derived: Liabilities / StockholdersEquity | — | — |")
        lines.append(f"| {r['fiscal_year_end']} | Owner earnings | derived: {r['cells']['operating_cash_flow']['tag']} − {r['cells']['capital_spending']['tag']} | — | — |")
    lines += ['', 'ROE, owner earnings, current ratio and liabilities / equity are derived, not standalone XBRL tags.',
              'Current ratio uses current assets / current liabilities; nonpositive current liabilities make it not known.',
              'Liabilities / equity uses total liabilities, not just debt; nonpositive equity makes it not known.',
              'Missing source values: not found. Checks with missing inputs: not known.',
              'Nonpositive equity makes ROE not known. Latest filing wins within each preferred tag.',
              'Annual flow periods must span 350–380 days, allowing 52/53-week years.',
              'Owner earnings uses operating cash flow minus total capital spending, per the assignment.']
    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Memo number audit
# ---------------------------------------------------------------------------
# Audit numeric literals, retaining entire dates, signs, and percent units. Also
# recognize common written numbers so spelling a new amount does not bypass checks.
NUMBER = re.compile(r'\d{4}-\d{2}-\d{2}|(?<![\w])[-+−]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?%?')
WORDS = dict(zip('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen '
                 'sixteen seventeen eighteen nineteen twenty'.split(), range(21)))


def canonical(token):
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', token):
        return token
    percent = token.endswith('%')
    value = Decimal(token.rstrip('%').replace(',', '').replace('−', '-'))
    return str(value.normalize()) + ('%' if percent else '')


def numeric_tokens(text):
    matches = [(m.start(), m.group(), canonical(m.group())) for m in NUMBER.finditer(text)]
    for m in re.finditer(r'\b(' + '|'.join(WORDS) + r')\b', text, flags=re.I):
        matches.append((m.start(), m.group(), canonical(str(WORDS[m.group().lower()]))))
    return sorted(matches)


def audit_memo(memo, result):
    # Only numbers in the printed financial table/checks are evidence; accession
    # numbers, tag names, and explanatory prose must not authorize numeric claims.
    evidence = '\n'.join(' '.join(row.values()) for row in value_table(result))
    evidence += '\n' + '\n'.join(check for checks in result['panel_checks'].values() for check in checks)
    if result['wood_cagr'] is not None:
        evidence += f" {result['wood_cagr']:.1f}%"
    allowed = {c for _, _, c in numeric_tokens(evidence)}
    allowed |= {canonical(f"{r['roe']:.1f}%") for r in result['rows'] if r['roe'] is not None}
    return [{'number': raw, 'line': memo.count('\n', 0, pos) + 1,
             'context': memo[max(0, pos - 40):pos + len(raw) + 50].replace('\n', ' ')}
            for pos, raw, c in numeric_tokens(memo) if c not in allowed]


def fingerprint(result):
    return hashlib.sha256(json.dumps({'rows': result['rows'], 'checks': result['panel_checks']},
                                     sort_keys=True).encode()).hexdigest()


def run(ticker, refresh=False):
    ticker = ticker_name(ticker)
    mapping = download(TICKERS_URL, DATA_DIR / 'company_tickers.json', refresh)
    match = next((v for v in mapping.values() if v['ticker'].upper() == ticker), None)
    if match is None:
        raise ValueError(f'{ticker} was not found in SEC ticker data.')
    cik = int(match['cik_str'])
    url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'
    path = DATA_DIR / f'{ticker}_companyfacts.json'
    company = download(url, path, refresh)
    result = compute(company, ticker)
    result.update(source_url=url, downloaded_at=datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat())
    result['fingerprint'] = fingerprint(result)
    (REPORTS_DIR / f'{ticker}_facts.json').write_text(json.dumps(result, indent=2))
    (REPORTS_DIR / f'{ticker}_facts.md').write_text(report_text(result))
    return result


# ---------------------------------------------------------------------------
# Saved AI memos (formerly reports/*_memo.md and *_memo_meta.json).
# The fingerprint records which SEC figures each memo was written from.
# A memo saved from the app into reports/ takes priority over these.
# ---------------------------------------------------------------------------
BUILT_IN_MEMOS = {
    'COST': {
        'fingerprint': '21fd4b7c42e1d7d51ca9cd5fbba79cfacc115746c16a5482a19cfe41c6d5f1a1',
        'text': '''# Costco: own the business

*AI-written, Buffett-inspired classroom assessment; not Warren Buffett's actual opinion. All dollar amounts below are USD millions.*

I would own this business on the earning-power evidence presented, while reserving judgment about any purchase price. From the fiscal year ended 2022-08-28 to the fiscal year ended 2026-08-30, revenue rose from $226,954 to $303,154 and net income rose from $5,844 to $9,226. These are encouraging signs of a business increasing its economic output.

The cash record matters most to me. Owner earnings, defined here as operating cash flow less total capital spending, increased from $3,501 to $9,382 and remained positive throughout the period. The path was not uninterrupted: owner earnings slipped from $6,745 at 2023-09-03 to $6,629 at 2024-09-01 before recovering. At 2026-08-30, operating cash flow of $15,817 covered capital spending of $6,435 and left substantial cash after reinvestment.

ROE exceeded the 15% threshold in every reported year and ended at 25.8%. All the prescribed checks pass. That supports my favorable judgment, but high ROE alone does not establish a durable moat or prove excellent management. I would still investigate competitive advantages, customer loyalty, and capital-allocation discipline before treating that durability as established.

My conclusion concerns business quality. These figures do not establish a sensible stock price or a margin of safety. I would reconsider if cash generation persistently weakened relative to earnings, reinvestment consumed the cash available to owners, or evidence showed competitive advantages eroding.
''',
    },
    'COST_graham': {
        'fingerprint': '21fd4b7c42e1d7d51ca9cd5fbba79cfacc115746c16a5482a19cfe41c6d5f1a1',
        'text': '''# Costco: watch it

*AI-written, Graham-inspired classroom assessment; not Benjamin Graham's actual opinion. Dollar amounts are USD millions.*

I would watch this business. Net income is positive throughout the reported period and rises from $5,844 at 2022-08-28 to $9,226 at 2026-08-30. The earnings-stability and first-to-last growth checks pass, giving me evidence of a profitable business.

The liquidity screen prevents an unqualified defensive assessment. At 2026-08-30, current assets are $46,582 and current liabilities are $43,952. The printed current ratio is 1.06, below the required 2, so this check fails. Growing profits do not remove that balance-sheet concern. The ratio alone does not establish financial distress, but I would want evidence about asset liquidity and the timing of obligations before accepting the available cushion.

My verdict is watch it because the favorable earnings record is accompanied by a failed defensive liquidity screen. I would reconsider after reviewing the composition of current assets and near-term obligations. These facts do not establish a purchase price, liquidation value, or margin of safety.

**Threshold kept: 2.0, to preserve the assigned defensive liquidity cushion rather than relax the screen to make Costco pass.**
''',
    },
    'COST_burry': {
        'fingerprint': '21fd4b7c42e1d7d51ca9cd5fbba79cfacc115746c16a5482a19cfe41c6d5f1a1',
        'text': '''# Costco: watch it

*AI-written, Burry-inspired classroom assessment; not Michael Burry's actual opinion. Dollar amounts are USD millions.*

I would watch this business while investigating the risks these summary figures cannot resolve. Operating cash flow is at least net income in every reported year, so the cash-backing check passes. At 2026-08-30, operating cash flow of $15,817 exceeds net income of $9,226. This provides a useful initial check on reported earnings, but it does not establish that the cash generation will persist.

The liabilities check also passes. At 2026-08-30, total liabilities are $53,242 against equity of $35,803, with a printed liabilities-to-equity ratio of 1.49, below the limit of 2. Total liabilities are not synonymous with borrowing, and this ratio does not reveal the timing or terms of obligations. The current ratio of 1.06 also warrants a closer look at liquidity.

Passing the prescribed checks gives me no numerical basis here to allege accounting manipulation. I would still examine working-capital movements, the quality of current assets, and obligations disclosed in the notes before moving from watch it to ownership. Those are unanswered questions, not problems established by this table. No stock valuation or contrarian trading opportunity can be established from these figures alone.
''',
    },
    'COST_wood': {
        'fingerprint': '21fd4b7c42e1d7d51ca9cd5fbba79cfacc115746c16a5482a19cfe41c6d5f1a1',
        'text': '''# Costco: watch it

*AI-written, Cathie Wood-inspired classroom assessment; not her actual opinion. Dollar amounts are USD millions. Growth checks are classroom proxies.*

I would watch this business. Revenue rises from $226,954 at 2022-08-28 to $303,154 at 2026-08-30, and increases in every reported year. Revenue CAGR is 7.5%, below the illustrative 20% growth threshold. This is evidence of expansion, but it does not meet this deliberately demanding classroom growth screen.

The supplied financial table does not establish disruptive technology, expanding addressable markets, cost declines or platform convergence. That innovation check remains not known. I would seek evidence of an innovation-driven growth opportunity before reaching an ownership conclusion through this perspective. Failing the chosen growth threshold does not make this a poor business; it limits the fit with this particular screen.
''',
    },
    'NVDA': {
        'fingerprint': 'fdd83a545f8a833c2d8ad41ae6e5b4396d23fdb779191ec7830768bc441d2763',
        'text': '''# NVIDIA: own the business

*AI-written, Buffett-inspired classroom assessment; not Warren Buffett's actual opinion. Dollar amounts are USD millions.*

I would own this business on the reported earning-power evidence, while reserving judgment on any purchase price. Net income rises from $9,752 at 2022-01-30 to $120,067 at 2026-01-25. Owner earnings, defined here as operating cash flow less total capital spending, rise from $8,132 to $96,676 and remain positive throughout the period. ROE stays above the prescribed 15% threshold and ends at 76.3%. The Buffett checks pass.

The path is uneven: owner earnings fall to $3,808 at 2023-01-29 before recovering. At 2026-01-25, operating cash flow of $102,718 covers capital spending of $6,042, leaving substantial cash after reinvestment. These figures support a favorable business-quality judgment, but they do not prove a durable moat or exceptional management.

I would investigate the durability of earnings and why operating cash flow is below net income in the latest year. Strong historical growth does not establish its future persistence. I would reconsider if reinvestment began consuming the cash available to owners or earning power deteriorated. No purchase price or margin of safety follows from this table.
''',
    },
    'NVDA_graham': {
        'fingerprint': 'fdd83a545f8a833c2d8ad41ae6e5b4396d23fdb779191ec7830768bc441d2763',
        'text': '''# NVIDIA: own the business

*AI-written, Graham-inspired classroom assessment; not Benjamin Graham's actual opinion. Dollar amounts are USD millions.*

I would own this business on the limited defensive evidence supplied. At 2026-01-25, current assets of $125,605 exceed current liabilities of $32,163, producing a printed current ratio of 3.91. This clears the required 2 and provides a favorable initial liquidity screen.

Net income is positive throughout the reported period and rises from $9,752 at 2022-01-30 to $120,067 at 2026-01-25. The profitability and first-to-last growth checks therefore pass. Earnings are not uniformly rising: net income falls to $4,368 at 2023-01-29. Passing the endpoint test should not be confused with uninterrupted stability.

This is a favorable assessment of the business under the assigned screens. It is not a conclusion that the stock is cheap or satisfies a complete defensive-investment framework. I would examine the realizable value of current assets and the persistence of earnings before committing capital. The table does not establish a conservative stock valuation or margin of safety.

**Threshold kept: 2.0, to preserve the assigned defensive liquidity cushion rather than relax the screen to make a company pass.**
''',
    },
    'NVDA_burry': {
        'fingerprint': 'fdd83a545f8a833c2d8ad41ae6e5b4396d23fdb779191ec7830768bc441d2763',
        'text': '''# NVIDIA: watch it

*AI-written, Burry-inspired classroom assessment; not Michael Burry's actual opinion. Dollar amounts are USD millions.*

I would watch this business. The cash-backing check fails because operating cash flow is not at least net income in every reported year. At 2026-01-25, operating cash flow is $102,718 while net income is $120,067. The same direction of divergence appears at 2025-01-26, when operating cash flow is $64,089 against net income of $72,880. Growing earnings alone do not resolve that question.

The balance-sheet screen is more reassuring. At 2026-01-25, total liabilities of $49,510 compare with equity of $157,293; the printed liabilities-to-equity ratio is 0.31, below the ceiling of 2. The current ratio is 3.91. These figures support the assigned leverage check, although total liabilities are broader than borrowing and the ratios do not expose every obligation or asset-quality concern.

I would investigate working-capital movements and the reconciliation between earnings and operating cash flow before moving to ownership. The observed divergence warrants investigation; it is not proof of manipulation. I cannot infer hidden liabilities, a short-selling case, or a mispriced stock from these summary figures.
''',
    },
    'NVDA_wood': {
        'fingerprint': 'fdd83a545f8a833c2d8ad41ae6e5b4396d23fdb779191ec7830768bc441d2763',
        'text': '''# NVIDIA: watch it

*AI-written, Cathie Wood-inspired classroom assessment; not her actual opinion. Dollar amounts are USD millions. Growth checks are classroom proxies.*

I would watch this business with interest. Revenue rises from $26,914 at 2022-01-30 to $215,938 at 2026-01-25 and increases in every reported year. Revenue CAGR is 68.3%, clearing the illustrative 20% growth threshold. These figures support a strong historical growth signal.

Historical growth does not establish its cause or persistence. The supplied table does not prove technological disruption, an expanding addressable market, cost-curve advantages or platform convergence, so the innovation check remains not known. I would investigate those questions and the gap between latest operating cash flow of $102,718 and net income of $120,067 before moving to ownership. The missing evidence prevents a confident innovation thesis or a stock-price conclusion.
''',
    },
}


def memo_suffix(investor):
    return {'Buffett': '', 'Cathie Wood': '_wood'}.get(investor, '_' + investor.lower())


def load_memo(ticker, investor):
    """Return (memo text, saved fingerprint) from reports/ first, then the built-in copy."""
    suffix = memo_suffix(investor)
    memo_path = REPORTS_DIR / f'{ticker}{suffix}_memo.md'
    meta_path = REPORTS_DIR / f'{ticker}{suffix}_memo_meta.json'
    if memo_path.exists():
        try:
            meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        except (ValueError, OSError):
            meta = {}
        return memo_path.read_text(), meta.get('fingerprint')
    saved = BUILT_IN_MEMOS.get(f'{ticker}{suffix}')
    if saved:
        return saved['text'], saved['fingerprint']
    return '', None


# ---------------------------------------------------------------------------
# Streamlit interface
# ---------------------------------------------------------------------------
@st.cache_data(ttl=3600, max_entries=20)
def load_facts(ticker, source_mtime):
    return run(ticker)


st.set_page_config(page_title='Lab 19 — Four-Investor Panel + Cathie Wood', page_icon='📖', layout='wide')
st.title('Lab 19 — Four-Investor Panel + Cathie Wood')
st.caption('data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.')
st.caption('Separate Lab 19 project · original Week 11 Buffett app preserved.')
st.write('Buffett, Graham, Burry and Cathie Wood examine the same annual SEC facts through different business-quality checks.')

with st.sidebar:
    st.header('Choose a business')
    entered = st.text_input('Ticker', 'COST')
    refresh = st.button('Refresh from SEC EDGAR')
    st.caption('Saved SEC responses are reused until you refresh. No API key is needed.')
    st.caption('Built-in memos: COST and NVDA.')

try:
    ticker = ticker_name(entered)
    with st.spinner('Reading annual SEC facts…'):
        if refresh:
            run(ticker, refresh=True)
            load_facts.clear()
        source = DATA_DIR / f'{ticker}_companyfacts.json'
        result = load_facts(ticker, source.stat().st_mtime if source.exists() else 0)
except Exception as exc:
    st.error(f'Unable to load company facts: {exc}')
    st.info('Check the ticker and your connection. SEC may temporarily limit requests; try again later.')
    st.stop()

st.subheader(result['company'])
st.caption(f"SEC data downloaded: {result['downloaded_at']} · {len(result['rows'])} fiscal years available")
if len(result['rows']) < 5:
    st.warning('Fewer than five fiscal years are available. Five-year checks are not known.')
for col, (check, status) in zip(st.columns(3), result['checks'].items()):
    with col:
        st.metric(check, status.upper())

st.subheader('Investor panel')
st.dataframe(pd.DataFrame(panel_table(result)), hide_index=True, width='stretch',
             alt='Investor, check and pass, fail or not known result')
st.caption('Checks use unrounded figures. Verdicts are AI-written judgments, not automatic votes or stock recommendations.')
st.caption(f'Cathie Wood uses illustrative growth proxies, including a {WOOD_CAGR_THRESHOLD}% CAGR threshold; '
           'these are not official ARK rules. Innovation evidence remains not known.')
st.write('Revenue CAGR: ' + ('not known' if result['wood_cagr'] is None else f"{result['wood_cagr']:.1f}%"))

st.subheader('Four perspectives on the same business')
st.caption('AI simulations inspired by the investors; these are not their actual opinions.')
all_flags = []
missing_memos = []
for col, investor in zip(st.columns(4), ('Buffett', 'Graham', 'Burry', 'Cathie Wood')):
    with col:
        st.subheader(investor)
        suffix = memo_suffix(investor)
        memo_path = REPORTS_DIR / f'{ticker}{suffix}_memo.md'
        meta_path = REPORTS_DIR / f'{ticker}{suffix}_memo_meta.json'
        memo, memo_fingerprint = load_memo(ticker, investor)
        if memo and memo_fingerprint != result['fingerprint']:
            st.warning('Source figures or checks have changed, or memo provenance is missing. Review and update this memo.')
        with st.expander('Edit or paste the AI memo', expanded=not bool(memo)):
            edited = st.text_area(f'{investor} memo text', value=memo, height=240,
                                  key=f'memo_{investor}_{ticker}_{result["fingerprint"]}')
        if edited:
            heading = next((line for line in edited.splitlines() if line.startswith('# ')), '')
            verdict = re.search(r':\s*(own the business|watch it|pass)\s*$', heading, re.I)
            st.markdown('**Verdict: ' + (verdict.group(1).lower() if verdict else 'not stated') + '**')
            if not verdict:
                st.warning('Use a title ending in : own the business, : watch it, or : pass.')
            flags = audit_memo(edited, result)
            all_flags.extend({'Investor': investor, **flag} for flag in flags)
            if flags:
                st.error(f'{len(flags)} unprinted numeric occurrence(s) in this memo.')
            st.markdown(edited.replace('$', r'\$'))  # show $ as dollars, not math
            st.download_button('Download memo', edited, memo_path.name, key=f'download_{investor}')
            if st.button('Save memo locally', key=f'save_{investor}'):
                memo_path.write_text(edited)
                meta_path.write_text(json.dumps({'fingerprint': result['fingerprint']}))
                st.success(f'Saved {memo_path.name}')
        else:
            missing_memos.append(investor)
            st.info(f'Ask your AI to write a {investor}-style {ticker} memo from the printed report '
                    'and paste it above. Title it "# Company: own the business", ": watch it" or ": pass".')

st.subheader('Number audit across all memos')
if all_flags:
    st.error(f'Found {len(all_flags)} unsupported numeric occurrence(s) across the panel.')
    st.dataframe(pd.DataFrame(all_flags), hide_index=True, width='stretch', alt='Unprinted numbers by investor and memo line')
elif missing_memos:
    st.warning('Panel audit incomplete. Missing memos: ' + ', '.join(missing_memos))
else:
    st.success('All recognized numbers in all four memos appear in the calculated financial output or checks.')
st.caption('Numeric presence does not prove a claim, its units, or its interpretation. Review meaning and source provenance too.')

chart = pd.DataFrame([{'Fiscal-year end': pd.to_datetime(r['fiscal_year_end']),
                       'Owner earnings': None if r['owner_earnings'] is None else r['owner_earnings'] / 1e6,
                       'Net income': None if r['cells']['net_income']['value'] is None else r['cells']['net_income']['value'] / 1e6}
                      for r in result['rows']])
st.subheader('Earning power over time')
st.line_chart(chart, x='Fiscal-year end', y=['Owner earnings', 'Net income'],
              y_label='USD millions', color=['#14856B', '#5279B8'], alt='Owner earnings and net income by fiscal-year end')
st.caption('Owner earnings = operating cash flow − capital spending. Missing observations are not estimated.')

st.subheader('Annual financials')
st.caption('Amounts in USD millions; ROE in percent; ratios in times. Rows use fiscal-year-end dates.')
st.dataframe(pd.DataFrame(value_table(result)), hide_index=True, width='stretch', alt='Annual SEC financial figures')
with st.expander('XBRL tags and filing provenance'):
    st.markdown(report_text(result).split('## XBRL provenance')[1])
st.link_button('SEC source JSON', result['source_url'])
st.download_button('Download calculated report', report_text(result), f'{ticker}_facts.md')
