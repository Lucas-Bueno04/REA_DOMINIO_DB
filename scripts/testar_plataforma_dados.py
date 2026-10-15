"""Teste rápido do núcleo da plataforma (sem servidor web): resumo, fila, detalhe, rascunho, validação e teste no banco."""
import json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from plataforma import dados as d

t0 = time.time()
r = d.resumo()
print(f"resumo ({(time.time()-t0)*1000:.0f} ms): {r['tabelas']} tabelas | por status {r['por_status']}")
print(f"  modeladas {r['tabelas_modeladas']} ({r['linhas_modeladas']:,} linhas) | relevantes {r['relevantes']} (modeladas {r['relevantes_modeladas']}) | colunas expostas {r['colunas_expostas']}/{r['colunas_uteis_total']}".replace(",", "."))
f = d.fila(8)
print("fila (top 8):")
for x in f:
    print(f"  {x['score']:>6}  {x['nome']:<44}{x['status']:<13}{x['motivo']}")
fa = d.familias()[:5]
print("famílias por linhas:", [(x['familia'], x['n'], x['mod']) for x in fa])
for tab in sys.argv[1:] or ["efsdopro"]:
    det = d.detalhe(tab)
    print(f"\n[{tab}] status={det['status']} colunas={len(det['colunas'])} pendentes={sum(1 for c in det['colunas'] if c['auto']=='pendente')} sem_uso={sum(1 for c in det['colunas'] if c['auto']=='sem_uso')} relações={len(det['relacoes'])}")
    g = d.gerar_rascunho(tab)
    print(f"  rascunho: entidade={g['entidade']} módulo={g['modulo']} colunas={g['colunas_escolhidas']}/{g['colunas_total']} domínios={len(g['dominios'])} vínculos={g['vinculos']} filtros={g['filtros']}")
    print("\n".join("    | " + l for l in g["yaml"].splitlines()[:26]))
    d.salvar_rascunho(tab, g["yaml"])
    v = d.validar_rascunho(tab)
    print("  validação:", "OK" if v["ok"] else v["erros"][:4], "| avisos:", v["avisos"][:2])
    if v["ok"]:
        te = d.testar_rascunho(tab)
        print("  teste no banco:", {k: (v if k != 'preenchimento_pct' else f'{len(v)} colunas') for k, v in te.items()})
