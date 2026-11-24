import unittest
from pathlib import Path
from dataclasses import replace
import numpy as np
from engine import Inputs,load_prices,estimates,run,evaluate,grid

class ModelTests(unittest.TestCase):
    def test_returns_known_answer(self):
        p=load_prices(); mu,cov,m,cap,r=estimates(p,Inputs())
        self.assertEqual(len(r),59)
        self.assertAlmostEqual(r.iloc[0,0],p.iloc[1,0]/p.iloc[0,0]-1)
        self.assertAlmostEqual(m,p.ACWI.iloc[-1]/p.ACWI.iloc[-13]-1)
        w=np.array([.4,.2,0,.4]); monthly=r.to_numpy()@w
        self.assertAlmostEqual(float(np.sqrt(w@cov@w)),float(np.std(monthly,ddof=1)*np.sqrt(12)))
        self.assertAlmostEqual(float(w@mu),float(monthly.mean()*12))
    def test_baselines_and_strict_mandate(self):
        r=run(); p=r['candidate']; self.assertIsNotNone(p)
        self.assertEqual(p['weights'],dict(SGOV=.4,VGIT=.2,VCIT=0.,ACWI=.4))
        self.assertTrue(p['modeled_pass']); self.assertEqual(p['mandate_verdict'],'FAIL')
        self.assertFalse(r['baselines']['Equal weight']['checks']['Research net return floor'])
        self.assertFalse(r['baselines']['60/40 reference (proposed benchmark)']['checks']['Diversified fund cap'])
        self.assertIsNone(run(Inputs(reserve_proxy=False))['candidate'])
    def test_grid_and_optimum_independently(self):
        x=Inputs(); mu,cov,_,cap,_=estimates(load_prices(),x)
        feasible=[]
        for w in grid():
            if all(evaluate(w,mu,cov,x,cap)['checks'].values()):feasible.append(float(w@cov@w))
        self.assertEqual(len(grid()),1771)
        self.assertAlmostEqual(run()['candidate']['volatility']**2,min(feasible))
    def test_cost_units(self):
        x=Inputs(); mu,cov,_,cap,_=estimates(load_prices(),x)
        a=evaluate([.25]*4,mu,cov,x,cap)
        b=evaluate([.25]*4,mu,cov,replace(x,cost_bps=50),cap)
        self.assertAlmostEqual(a['net_return']-b['net_return'],.0025)
        self.assertEqual(a['volatility'],b['volatility'])
    def test_lag_excludes_latest_observation(self):
        p=load_prices(); q=p.copy(); q.iloc[-1,3]*=2
        a=estimates(p,Inputs(lag_months=1)); b=estimates(q,Inputs(lag_months=1))
        np.testing.assert_allclose(a[0],b[0]); self.assertEqual(a[2],b[2])
    def test_negative_signal(self):
        p=load_prices(); p.iloc[-1,3]=p.ACWI.iloc[-13]*.9
        _,_,m,cap,_=estimates(p,Inputs()); self.assertAlmostEqual(m,-.1); self.assertEqual(cap,.2)
    def test_invalid_inputs(self):
        for x in [Inputs(cost_bps=-1),Inputs(fund_cap=.5),Inputs(cpi=float('nan'))]:
            with self.assertRaises(ValueError):run(x)
    def test_no_feasible_under_too_small_caps(self):
        self.assertIsNone(run(Inputs(fund_cap=.2))['candidate'])

class AppTests(unittest.TestCase):
    def test_control_changes_result(self):
        from streamlit.testing.v1 import AppTest
        app=AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
        self.assertFalse(app.exception)
        base=app.dataframe[0].value
        app.slider(key='cost').set_value(50).run()
        self.assertFalse(app.exception)
        self.assertNotEqual(base.iloc[0]['Net return (%)'],app.dataframe[0].value.iloc[0]['Net return (%)'])
        app.checkbox(key='proxy').uncheck().run()
        self.assertFalse(app.exception)
        self.assertTrue(any('No portfolio' in x.value for x in app.warning))

if __name__=='__main__':unittest.main()
