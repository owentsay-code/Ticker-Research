from pathlib import Path
import json
import pandas as pd
import streamlit as st
from engine import Inputs, run, table, DECISION, DISCLOSURE, EDUCATION

st.set_page_config(page_title='Cedar Grove | Committee review',page_icon=':material/account_balance:',layout='wide')
st.caption(DISCLOSURE)
st.caption(EDUCATION)
st.title('Cedar Grove scholarship reserve')
st.caption('Committee research review · frozen information set available October 22, 2026 · $2,000,000 fictional fund')
with st.sidebar:
    st.header('Test the decision')
    st.caption('Change one assumption. All figures and rule checks update together.')
    cost=st.slider('Annual incremental costs (basis points)',0,200,25,5,key='cost')
    shift=st.slider('ACWI annual return estimate shift (percentage points)',-5.,5.,0.,.5,key='shift')
    window=st.selectbox('Estimation window (monthly returns)',[59,36],key='window')
    cap=st.selectbox('Maximum weight per fund (%)',[40,35,30,25,20],key='cap')
    lag=st.selectbox('Additional information lag (months)',[0,1],key='lag')
    proxy=st.checkbox('Research only: count SGOV as reserve proxy',value=True,key='proxy')
    st.caption('This checkbox is a hypothetical interpretation, not board approval. Strict mandate verdict remains FAIL.')

@st.cache_data(max_entries=128)
def calculate(x, fingerprint):
    return run(x)

x=Inputs(cost_bps=cost,equity_shift_pp=shift,window=window,fund_cap=cap/100,lag_months=lag,reserve_proxy=proxy)
fingerprint=(Path(__file__).parent/'data/prices.csv').read_bytes()
r=calculate(x,fingerprint)
st.error(DECISION)
with st.container(horizontal=True):
    st.metric('Live allocation range','0%–0%',border=True)
    st.metric('Next four scholarships','$60,000',border=True)
    st.metric('Research return floor','5.50%',border=True)
    st.metric('Feasible grid portfolios',str(r['feasible_count']),border=True)
st.subheader('Two baselines and the constrained portfolio')
st.dataframe(pd.DataFrame(table(r)),hide_index=True,alt='Portfolio weights, net expected returns, volatility and pass fail verdicts')
if r['candidate'] is None:
    st.warning('STOP: No portfolio on the 5-point grid meets the selected model rules. Do not relax the mandate to force an answer.')
else:
    st.bar_chart(pd.Series(r['candidate']['weights'],name='Weight (%)')*100,alt='Constrained research allocation by fund')
    st.caption('Grid minimum variance subject to a modeled return floor. A modeled PASS does not authorize investing.')
selection=st.selectbox('Inspect rules for',list(r['baselines'])+['Constrained research portfolio'],key='inspect')
p=r['candidate'] if selection=='Constrained research portfolio' else r['baselines'][selection]
if p:
    st.dataframe(pd.DataFrame([{'Rule':k,'Verdict':'PASS' if v else 'FAIL'} for k,v in p['checks'].items()]),hide_index=True,alt='Individual modeled rule checks')
    st.error('Full mandate FAIL: '+'; '.join(p['mandate_failures']))
st.subheader('Signal and information boundary')
st.write(f"ACWI trailing 12-month return: {r['signal']['value']:.2%}. Research equity cap: {r['signal']['equity_cap']:.0%}. Information through {r['information_through']}; {r['returns_count']} returns used.")
st.caption('If trailing momentum is negative, research equity exposure is capped at 20%; otherwise 40%. Snapshot available October 22, 2026; this is not a historical point-in-time backtest. Historical adjusted values can be revised.')
st.subheader('Committee conditions')
st.write('Approve reserve implementation, a benchmark and a risk policy before live use. Quarterly: verify $60,000 reserve, 95% five-day liquidity and 40% fund caps. Review annually for rebalance; obtain prior approval for calendar-year turnover above 30%. Report breaches within five business days.')
st.download_button('Download this scenario',json.dumps(r,indent=2),file_name='cedar-grove-scenario.json',mime='application/json')
with st.expander('Read the mandate, signal data card and methods'):
    for name in ['lab13-mandate.md','signal-data-card.md','methods.md']:
        path=Path(__file__).parent/'docs'/name
        if path.exists(): st.markdown(path.read_text())
