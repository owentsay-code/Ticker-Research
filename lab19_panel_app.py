from pathlib import Path
import json
import sys
import re
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'skill/buffett-business/scripts'))
from edgar import run, ticker_name, value_table, report_text, audit_memo, panel_table

@st.cache_data(ttl=3600, max_entries=20)
def load_facts(ticker, source_mtime, settings_mtime):
    return run(ticker, ROOT)

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
try:
    ticker = ticker_name(entered)
    with st.spinner('Reading annual SEC facts…'):
        if refresh:
            run(ticker, ROOT, refresh=True)
            load_facts.clear()
        source = ROOT / 'data' / f'{ticker}_companyfacts.json'
        settings = ROOT / 'skill/graham-business/settings.json'
        result = load_facts(ticker, source.stat().st_mtime if source.exists() else 0, settings.stat().st_mtime_ns)
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
st.caption('Cathie Wood uses illustrative growth proxies, including a 20% CAGR threshold; these are not official ARK rules. Innovation evidence remains not known.')
st.write('Revenue CAGR: ' + ('not known' if result['wood_cagr'] is None else f"{result['wood_cagr']:.1f}%"))
st.subheader('Four perspectives on the same business')
st.caption('AI simulations inspired by the investors; these are not their actual opinions.')
all_flags = []
missing_memos = []
for col, investor in zip(st.columns(4), ('Buffett', 'Graham', 'Burry', 'Cathie Wood')):
    with col:
        st.subheader(investor)
        suffix = '' if investor == 'Buffett' else ('_wood' if investor == 'Cathie Wood' else '_' + investor.lower())
        memo_path = ROOT / 'reports' / f'{ticker}{suffix}_memo.md'
        meta_path = ROOT / 'reports' / f'{ticker}{suffix}_memo_meta.json'
        memo = memo_path.read_text() if memo_path.exists() else ''
        if memo:
            try:
                meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
            except (ValueError, OSError):
                meta = {}
            if meta.get('fingerprint') != result['fingerprint']:
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
            st.markdown(edited)
            st.download_button('Download memo', edited, memo_path.name, key=f'download_{investor}')
            if st.button('Save memo locally', key=f'save_{investor}'):
                memo_path.write_text(edited)
                meta_path.write_text(json.dumps({'fingerprint': result['fingerprint']}))
                st.success(f'Saved {memo_path.name}')
        else:
            missing_memos.append(investor)
            st.info(f'Ask your AI to read skill/{'wood' if investor == 'Cathie Wood' else investor.lower()}-business/SKILL.md and write a {ticker} memo from the printed report. You can paste it above.')
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
    'Owner earnings': None if r['owner_earnings'] is None else r['owner_earnings']/1e6,
    'Net income': None if r['cells']['net_income']['value'] is None else r['cells']['net_income']['value']/1e6}
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
