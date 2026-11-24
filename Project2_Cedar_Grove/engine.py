"""Deterministic Cedar Grove research model. Fractions internally; no live trades."""
from dataclasses import dataclass, asdict, replace
from pathlib import Path
import hashlib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
TICKERS = ['SGOV', 'VGIT', 'VCIT', 'ACWI']
AS_OF = '2026-10-22'
DISCLOSURE = 'I used OpenAI Codex (GPT-6) to develop code, check calculations, and draft this analysis. The analysis and decision are mine.'
EDUCATION = 'Education, not investment advice.'
DECISION = ('Reject live allocation to this process (0%–0% of fund assets); reconsider only after reserve eligibility, benchmark and risk policy are approved, operational controls are evidenced, and the approved model passes its stress checks.')

@dataclass(frozen=True)
class Inputs:
    window: int = 59
    cost_bps: float = 25.0
    equity_shift_pp: float = 0.0
    fund_cap: float = .40
    reserve: float = .03
    cpi: float = .025
    lag_months: int = 0
    reserve_proxy: bool = True


def load_prices(path=None):
    p = pd.read_csv(path or ROOT / 'data/prices.csv', index_col='Date', parse_dates=True)
    if list(p.columns) != TICKERS or len(p) < 38:
        raise ValueError('Expected at least 38 monthly prices in SGOV, VGIT, VCIT, ACWI order.')
    if p.index.has_duplicates or not p.index.is_monotonic_increasing:
        raise ValueError('Dates must be unique and increasing.')
    expected = pd.date_range(p.index[0], periods=len(p), freq='MS')
    if not p.index.equals(expected):
        raise ValueError('Monthly labels must be consecutive month starts.')
    if not np.isfinite(p.to_numpy()).all() or (p <= 0).any().any():
        raise ValueError('Prices must be finite and strictly positive; no filling is permitted.')
    if (p.index + pd.offsets.MonthEnd(0) >= pd.Timestamp(AS_OF)).any():
        raise ValueError('Incomplete or future price month at decision date.')
    return p


def grid():
    # Exhaustive 5-percentage-point grid; minimum is on this grid, not continuous.
    return np.array([(a,b,c,20-a-b-c) for a in range(21)
                     for b in range(21-a) for c in range(21-a-b)], dtype=float)/20


def estimates(p, x):
    if x.window not in (36, 59) or x.lag_months not in (0, 1):
        raise ValueError('Window must be 36 or 59 returns; lag 0 or 1 month.')
    if not np.isfinite([x.cost_bps,x.equity_shift_pp,x.fund_cap,x.reserve,x.cpi]).all():
        raise ValueError('All assumptions must be finite.')
    if x.cost_bps < 0 or not 0 <= x.reserve <= 1 or not 0 < x.fund_cap <= .4:
        raise ValueError('Costs must be nonnegative, reserve 0–100%, cap >0 and <=40%.')
    q = p.iloc[:-x.lag_months] if x.lag_months else p
    r = q.pct_change(fill_method=None).dropna().tail(x.window)
    mu = r.mean().to_numpy()*12
    mu[3] += x.equity_shift_pp/100
    cov = r.cov().to_numpy()*12
    momentum = float(q.ACWI.iloc[-1]/q.ACWI.iloc[-13]-1)
    equity_cap = min(x.fund_cap, .2 if momentum < 0 else .4)
    return mu, cov, momentum, equity_cap, r


def evaluate(w, mu, cov, x, equity_cap):
    w = np.asarray(w, dtype=float)
    net = float(w@mu - x.cost_bps/10000)
    vol = float(np.sqrt(max(0, w@cov@w)))
    # SGOV is a fund, not direct bills. Proxy checks are explicitly conditional.
    modeled_reserve = float(w[0]) if x.reserve_proxy else 0.0
    checks = {
        'Fully invested': bool(abs(w.sum()-1)<1e-9),
        'Long-only': bool(w.min()>=-1e-9),
        'Diversified fund cap': bool(w.max()<=x.fund_cap+1e-9),
        'Reserve under selected interpretation': bool(modeled_reserve>=x.reserve-1e-9),
        'Normal-market five-day liquidity (assumed)': True,
        'Research net return floor': bool(net>=x.cpi+.03-1e-9),
        'Research signal equity cap': bool(w[3]<=equity_cap+1e-9),
    }
    return dict(weights=dict(zip(TICKERS, w.tolist())), net_return=net, volatility=vol,
                proxy_reserve=float(w[0]), strict_reserve=0.0, liquid_share=1.0,
                target=x.cpi+.03, checks=checks, modeled_pass=all(checks.values()),
                mandate_verdict='FAIL',
                mandate_failures=['Reserve: 0% in cash/direct bills versus required reserve',
                                  'Benchmark and risk policy not approved',
                                  'Turnover, actual liquidity and payout controls unverified'])


def run(x=Inputs(), prices=None):
    p = load_prices() if prices is None else prices
    mu,cov,momentum,equity_cap,r = estimates(p,x)
    weights = grid()
    net = weights@mu-x.cost_bps/10000
    reserve = weights[:,0] if x.reserve_proxy else np.zeros(len(weights))
    valid = ((weights.max(axis=1)<=x.fund_cap+1e-9) & (reserve>=x.reserve-1e-9)
             & (net>=x.cpi+.03-1e-9) & (weights[:,3]<=equity_cap+1e-9))
    eligible = weights[valid]
    candidate = None
    if len(eligible):
        variance = np.einsum('ij,jk,ik->i',eligible,cov,eligible)
        candidate = evaluate(eligible[int(np.argmin(variance))],mu,cov,x,equity_cap)
    baselines = {'Equal weight':evaluate([.25]*4,mu,cov,x,equity_cap),
                 '60/40 reference (proposed benchmark)':evaluate([0,0,.4,.6],mu,cov,x,equity_cap)}
    return dict(inputs=asdict(x),as_of=AS_OF, price_month_end=str(p.index[-1].date()),
                information_through=str((r.index[-1]+pd.offsets.MonthEnd(0)).date()),
                returns_count=len(r), estimated_returns=dict(zip(TICKERS,mu.tolist())),
                covariance=cov.tolist(), signal=dict(name='12-month ACWI momentum',value=momentum,
                equity_cap=equity_cap,available_on=AS_OF), candidate=candidate, baselines=baselines,
                feasible_count=int(valid.sum()), decision=DECISION,
                data_sha256=hashlib.sha256((ROOT/'data/prices.csv').read_bytes()).hexdigest())


def stresses():
    base=Inputs()
    return {'Base':run(base), 'Equity estimate -2 pp':run(replace(base,equity_shift_pp=-2)),
            '36-return window':run(replace(base,window=36)),
            'Cost 50 bps/year':run(replace(base,cost_bps=50)),
            'Fund cap 30%':run(replace(base,fund_cap=.30)),
            'Strict reserve eligibility':run(replace(base,reserve_proxy=False)),
            'Combined adverse':run(replace(base,equity_shift_pp=-2,window=36,cost_bps=50,fund_cap=.30))}


def table(result):
    rows=[]
    for name,p in {**result['baselines'],'Constrained research portfolio':result['candidate']}.items():
        if p is None:
            rows.append({'Portfolio':name,'Net return (%)':None,'Volatility (%)':None,
                         'Model verdict':'INFEASIBLE','Mandate verdict':'FAIL'})
        else:
            rows.append({'Portfolio':name,'Net return (%)':round(p['net_return']*100,4),
                         'Volatility (%)':round(p['volatility']*100,4),
                         **{k+' (%)':round(v*100,2) for k,v in p['weights'].items()},
                         'Model verdict':'PASS' if p['modeled_pass'] else 'FAIL: '+', '.join(k for k,v in p['checks'].items() if not v),
                         'Mandate verdict':p['mandate_verdict']})
    return rows
