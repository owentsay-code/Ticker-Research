"""One source of truth for the committee memo and GitHub-visible numbers."""
import json
from engine import ROOT, run, stresses, table, DISCLOSURE, EDUCATION, DECISION

def markdown(rows):
    keys=list(rows[0])
    def cell(v):
        if v is None:return '—'
        if isinstance(v,float):return f'{v:.4f}'
        return str(v).replace('|','/')
    return '| '+' | '.join(keys)+' |\n| '+' | '.join(['---']*len(keys))+' |\n'+'\n'.join('| '+' | '.join(cell(row.get(k)) for k in keys)+' |' for row in rows)+'\n'

def main():
    r=run(); s=stresses()
    (ROOT/'outputs/baseline.json').write_text(json.dumps(r,indent=2)+'\n')
    (ROOT/'outputs/stress.json').write_text(json.dumps(s,indent=2)+'\n')
    rows=[]
    for name,v in s.items():
        p=v['candidate']
        rows.append({'Scenario':name,'Net return (%)':p['net_return']*100 if p else None,
                     'Volatility (%)':p['volatility']*100 if p else None,
                     'Feasible portfolios':v['feasible_count'],'Decision':'REJECT'})
    summary=(f'**{DECISION}**\n\nInformation available: **{r["as_of"]}**; latest price month: **September 2026**; report prepared **November 17, 2026**. '
             f'60 prices produce {r["returns_count"]} monthly returns. Initial fund: **$2,000,000**; four quarterly payments: **$60,000 (3%)**. '
             'Assumed CPI: **2.50%**; modeled net target: **5.50%**; incremental annual cost: **25 bp**.\n\n'
             +markdown(table(r))+'\nNet return is an annual arithmetic estimate after incremental costs; volatility is annualized sample volatility. '
             'Weights are percentages; missing values mean infeasible, not zero risk. The research portfolio counts SGOV as a reserve proxy. '
             'Under the literal cash/direct-bill requirement, every fund portfolio has **0% eligible reserve** and fails.\n\n'
             f'ACWI 12-month momentum: **{r["signal"]["value"]:.4%}**; research equity cap: **{r["signal"]["equity_cap"]:.0%}**.\n\n'
             '### Stress evidence\n\n'+markdown(rows))
    rationale=('\n### Committee ask and monitoring\n\n'
        'Withhold live approval and allocate **0%–0%** to this process. Approve a compliant reserve implementation, evaluation benchmark and risk policy before reconsideration. '
        'The 60/40 reference and volatility objective are research proposals because the saved Cedar Grove mandate did not approve them. '
        'The research result is not sufficient evidence of rolling-five-year performance, real-principal preservation or payout sustainability.\n\n'
        'At each quarterly review verify the next four $15,000 payments, reserve dollars, 95% five-business-day liquidity, and each fund at or below 40%. '
        'Review targets annually; require prior board approval for calendar-year one-way turnover above 30%. Report breaches within five business days. '
        'Do not run live when data are invalid, the selected model is infeasible, or governance/operational evidence is missing. '
        'Reverse the reject recommendation only after these blockers are resolved and the approved process passes its stress criteria.\n\n'
        '### Evidence and limitations\n\n'
        'The data window and gross return estimates are historical, not forecasts guaranteed to recur. The snapshot has no historical vintage sequence. '
        'The 5-point-grid optimum is conditional on the assumptions, and 59 monthly returns cannot establish a five-year rolling outcome. '
        'See [methods](methods.md), [signal card](signal-data-card.md), [original mandate](lab13-mandate.md), '
        '[validation and AI use](validation-and-ai-use.md), and [full numerical output](../outputs/baseline.json).\n')
    (ROOT/'docs/decision-memo.md').write_text(DISCLOSURE+'\n\n'+EDUCATION+'\n\n# Cedar Grove — committee decision\n\n'+summary+rationale)
    (ROOT/'outputs/visible-output.md').write_text('# Executed decision output\n\n'+summary+'\nCSV SHA-256: `'+r['data_sha256']+'`\n\n[Methods](../docs/methods.md) · [Decision memo](../docs/decision-memo.md)\n')
    print(markdown(rows))
if __name__=='__main__':main()
