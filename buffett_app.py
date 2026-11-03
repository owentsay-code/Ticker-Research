from pathlib import Path
import json
import sys
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'skill/buffett-business/scripts'))
from edgar import run, ticker_name, value_table, report_text, audit_memo

@st.cache_data(ttl=3600, max_entries=20)
def load_facts(ticker, source_mtime):
    return run(ticker, ROOT)

st.set_page_config(page_title='The Business Owner’s Notebook', page_icon='📖', layout='wide')
st.title('The Business Owner’s Notebook')
st.caption('data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.')
st.write('A Buffett-inspired look at earning power, using annual filings and reproducible calculations.')
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
chart = pd.DataFrame([{'Fiscal-year end': pd.to_datetime(r['fiscal_year_end']),
    'Owner earnings': None if r['owner_earnings'] is None else r['owner_earnings']/1e6,
    'Net income': None if r['cells']['net_income']['value'] is None else r['cells']['net_income']['value']/1e6}
    for r in result['rows']])
st.subheader('Earning power over time')
st.line_chart(chart, x='Fiscal-year end', y=['Owner earnings', 'Net income'],
              y_label='USD millions', color=['#14856B', '#5279B8'], alt='Owner earnings and net income by fiscal-year end')
st.caption('Owner earnings = operating cash flow − capital spending. Missing observations are not estimated.')
st.subheader('Annual financials')
st.caption('Amounts in USD millions; ROE in percent. Rows use fiscal-year-end dates.')
st.dataframe(pd.DataFrame(value_table(result)), hide_index=True, width='stretch', alt='Annual SEC financial figures')
with st.expander('XBRL tags and filing provenance'):
    st.markdown(report_text(result).split('## XBRL provenance')[1])
    st.link_button('SEC source JSON', result['source_url'])
st.download_button('Download calculated report', report_text(result), f'{ticker}_facts.md')
st.subheader('Buffett-inspired memo')
st.caption('AI-authored judgment about the business. No stock-price analysis.')
memo_path = ROOT / 'reports' / f'{ticker}_memo.md'
meta_path = ROOT / 'reports' / f'{ticker}_memo_meta.json'
memo = memo_path.read_text() if memo_path.exists() else ''
if memo and meta_path.exists():
    if json.loads(meta_path.read_text()).get('fingerprint') != result['fingerprint']:
        st.warning('The source figures have changed since this memo was written. Ask your AI to update it.')
if not memo:
    st.info(f'Ask Codex: “Use $buffett-business on {ticker} and save the memo in {ROOT / "reports"}.” Then reload this app. You can also paste the AI-written memo below.')
with st.expander('Edit or paste the AI memo', expanded=not bool(memo)):
    edited = st.text_area('Memo text', value=memo, height=240, key=f'memo_{ticker}_{result["fingerprint"]}')
if edited:
    flags = audit_memo(edited, result)
    if flags:
        st.error(f'Found {len(flags)} unsupported numeric occurrence(s).')
        st.dataframe(pd.DataFrame(flags), hide_index=True, width='stretch', alt='Unsupported memo numbers with line numbers')
    else:
        st.success('All recognized memo numbers appear in the calculated financial output.')
    st.caption('This checks numeric support, not whether a number is attached to the right claim. Use the report’s USD-million units and exact date/percentage formats; review the meaning too.')
    st.markdown(edited)
    st.download_button('Download memo', edited, f'{ticker}_memo.md')
    if st.button('Save memo locally'):
        memo_path.write_text(edited)
        meta_path.write_text(json.dumps({'fingerprint': result['fingerprint']}))
        st.success(f'Saved {memo_path.name}')
