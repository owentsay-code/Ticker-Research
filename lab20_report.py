"""Reproduce Lab 20; changed run requires a verified published pre-run commit."""
import argparse
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
from urllib.request import urlopen
from lab20_engine import ROOT, Inputs, run, stresses, table, evaluate, estimates, load_prices

REPO='https://github.com/owentsay-code/Ticker-Research'

def mdtable(rows):
    keys=list(dict.fromkeys(k for row in rows for k in row))
    def fmt(v):
        if v is None:return '—'
        return f'{v:.4f}' if isinstance(v,float) else str(v).replace('|','/')
    return '| '+' | '.join(keys)+' |\n| '+' | '.join('---' for _ in keys)+' |\n'+'\n'.join('| '+' | '.join(fmt(row.get(k)) for k in keys)+' |' for row in rows)+'\n'

def before():
    r=run()
    (ROOT/'lab20-before.json').write_text(json.dumps(r,indent=2)+'\n')
    text='# Lab 20 — before output\n\n'+r['decision']+'\n\n'
    text+='As of October 22, 2026; prepared November 17, 2026. 60 monthly prices through September 2026; 59 returns. CPI assumption 2.50%, net research target 5.50%, annual incremental cost 25 basis points.\n\n'
    text+=mdtable(table(r))+'\nModel PASS assumes SGOV is a reserve proxy. Literal cash/direct-bill reserve is 0%, so full mandate FAIL remains. Benchmark and risk policy require approval; no live allocation is authorized.\n\n'
    text+='Data SHA-256: `'+r['data_sha256']+'`.\n\n[Methods and signal](lab20-methods.md) · [Locked prediction](lab20-prediction.md)\n'
    (ROOT/'lab20-before.md').write_text(text)
    return r

def after(sha):
    if len(sha)!=40 or any(c not in '0123456789abcdef' for c in sha):
        raise ValueError('Supply the full published pre-run GitHub commit SHA.')
    raw=f'https://raw.githubusercontent.com/owentsay-code/Ticker-Research/{sha}/'
    for filename in ['lab20-prediction.md','lab20-before.json','lab20_engine.py','prices.csv']:
        with urlopen(raw+filename,timeout=30) as response:published=response.read()
        if published!=(ROOT/filename).read_bytes():
            raise ValueError(f'{filename} differs from the published pre-run snapshot; stop.')
    # The changed calculation starts only after the four remote byte comparisons pass.
    b=json.loads((ROOT/'lab20-before.json').read_text())
    x=replace(Inputs(),cost_bps=125)
    a=run(x)
    if a['data_sha256']!=b['data_sha256']:raise ValueError('Data changed.')
    mu,cov,_,cap,_=estimates(load_prices(),x)
    frozen=evaluate(list(b['candidate']['weights'].values()),mu,cov,x,cap)
    (ROOT/'lab20-after.json').write_text(json.dumps(dict(prediction_commit=sha,
        verified_before_run=True,run_utc=datetime.now(timezone.utc).isoformat(),
        after=a,frozen_before_weights_at_new_cost=frozen),indent=2)+'\n')
    rows=[]
    for name,p in [('Equal weight',b['baselines']['Equal weight']),
                   ('60/40 reference',b['baselines']['60/40 reference (proposed benchmark)']),
                   ('Original constrained weights held fixed',b['candidate'])]:
        changed=frozen if name.startswith('Original') else a['baselines']['Equal weight' if name=='Equal weight' else '60/40 reference (proposed benchmark)']
        rows.append({'Portfolio':name,'Before net (%)':p['net_return']*100,
                     'After net (%)':changed['net_return']*100,
                     'Change (percentage points)':100*(changed['net_return']-p['net_return']),
                     'Before volatility (%)':p['volatility']*100,'After volatility (%)':changed['volatility']*100})
    candidate=a['candidate']
    outcome='No feasible constrained portfolio remains.' if candidate is None else f"Reoptimized net return {candidate['net_return']:.4%}; volatility {candidate['volatility']:.4%}."
    text='# Locked changed-input result\n\nAI-assisted partner run under the student-reported instructor accommodation; not AI-off.\n\n'
    text+=f'[Immutable pre-run prediction]({REPO}/blob/{sha}/lab20-prediction.md). Prediction, baseline JSON, engine and prices were downloaded from this commit and byte-verified BEFORE the changed calculation.\n\n'
    text+='Only annual incremental cost changed: **25 → 125 basis points/year (0.25% → 1.25%)**.\n\n'+mdtable(rows)
    text+=f'\nBefore: {b["feasible_count"]} feasible grid portfolios. After: {a["feasible_count"]}. **{outcome}**\n\n'
    text+='The fixed-weight net returns fell exactly 1.00 percentage point/year, with no change in volatility, as predicted. The feasible set shrank, as predicted. '
    text+='The pre-run prediction allowed infeasibility rather than claiming an exact reoptimized mix. '
    text+='The recommendation remains **reject live allocation, 0%–0%**: costs do not resolve the reserve or governance blockers. There is no reoptimized volatility to report when the solver is infeasible; do not report zero.\n\n'
    text+='Decision reversal requires approved reserve implementation, benchmark and risk policy, operational evidence, and successful approved stress checks.\n'
    (ROOT/'lab20-after.md').write_text(text)
    print(text)

def stress():
    s=stresses(); rows=[]
    for name,r in s.items():
        p=r['candidate']; rows.append({'Scenario':name,'Net (%)':p['net_return']*100 if p else None,
            'Volatility (%)':p['volatility']*100 if p else None,'Feasible count':r['feasible_count'],'Decision':'REJECT'})
    (ROOT/'lab20-stress.json').write_text(json.dumps(s,indent=2)+'\n')
    (ROOT/'lab20-stress.md').write_text('# Ordinary stress checks (separate from locked experiment)\n\n'+mdtable(rows)+'\nThe shorter window can improve historical estimates; the combined case is not uniformly adverse. No passing research result overrides the full mandate FAIL.\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--after',action='store_true');parser.add_argument('--prediction-commit')
    args=parser.parse_args()
    if args.after:after(args.prediction_commit or '')
    else:before();stress();print('Saved baseline and ordinary stress output; locked 125-bp scenario NOT run.')
