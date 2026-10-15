"""Teste de fumaça das entidades contra o banco REAL (somente leitura).

Para cada entidade do modelo:
  1. escolhe uma empresa que tenha dados NAQUELA tabela (mediana das empresas com >=200 linhas; ou fixe com --empresa);
  2. executa o SELECT gerado (3 linhas) com os filtros obrigatórios;
  3. confere que os vínculos (LEFT JOIN) NÃO multiplicam linhas: COUNT(*) sem vínculos == COUNT(*) com vínculos;
  4. mede a taxa de preenchimento das colunas vindas dos vínculos (junção que casa = campo preenchido);
  5. mede o tempo.
Uso: python scripts/testar_entidades.py [--empresa N] [entidade ...]
"""
import datetime, pathlib, sys, time
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor.db import conectar, select
from server.sqlbuilder import carregar_modelo, montar, ErroConsulta

args = sys.argv[1:]
fixa = None
if "--empresa" in args:
    i = args.index("--empresa"); fixa = int(args[i + 1]); del args[i:i + 2]
ents, _ = carregar_modelo()
alvo = args or list(ents)
cn = conectar()
_cache = {}


def empresa_para(tabela):
    if fixa is not None:
        return fixa
    if tabela not in _cache:
        r = select(cn, f"SELECT codi_emp, COUNT(*) AS n FROM bethadba.{tabela} GROUP BY codi_emp HAVING COUNT(*) >= 200 ORDER BY n")
        if not r:
            r = select(cn, f"SELECT codi_emp, COUNT(*) AS n FROM bethadba.{tabela} GROUP BY codi_emp ORDER BY n")
        _cache[tabela] = r[len(r) // 2]["codi_emp"] if r else None
    return _cache[tabela]


def executar(sql, params):
    t0 = time.time()
    return select(cn, sql, tuple(params)), time.time() - t0


falhas = 0
for nome in alvo:
    e = ents[nome]
    ac = e.get("acesso", {})
    filtros, emp = {}, None
    try:
        if ac.get("empresa"):
            emp = empresa_para(e["tabela"])
            if emp is None:
                print(f"SEM DADOS {nome:<24}tabela vazia"); continue
            filtros["empresa"] = emp
        exige = ac.get("exige_algum")
        if exige and "codigo_nota" in exige:
            col = e["filtros"]["codigo_nota"]["coluna"]
            notas = select(cn, f"SELECT DISTINCT TOP 3 {col} AS c FROM bethadba.{e['tabela']} WHERE codi_emp = ? ORDER BY {col} DESC", (emp,))
            filtros["codigo_nota"] = ("in", [x["c"] for x in notas])
        elif exige and "periodo" in exige:            # exige período
            filtros["periodo"] = ("entre", (datetime.date(2000, 1, 1), datetime.date(2030, 12, 31)))
        elif exige:                                   # exige um filtro de chave: usa 3 valores reais dessa coluna na empresa
            fn = exige[0]
            col = e["filtros"][fn]["coluna"]
            col = col[0] if isinstance(col, list) else col
            vals = select(cn, f"SELECT DISTINCT TOP 3 {col} AS c FROM bethadba.{e['tabela']} WHERE codi_emp = ? ORDER BY {col} DESC", (emp,))
            filtros[fn] = ("in", [x["c"] for x in vals])
        elif isinstance(ac.get("periodo"), str) and ac.get("volume") == "grande":
            filtros["periodo"] = ("entre", (datetime.date(2000, 1, 1), datetime.date(2030, 12, 31)))
        sql, params = montar(e, filtros, limite=3)
        rows, dt = executar(sql, params)
        n_com = None; fan = "-"; pr = ""
        if e.get("vinculos"):
            vinc_where = ac["periodo"]["vinculo"] if isinstance(ac.get("periodo"), dict) and "periodo" in filtros else None
            n_com = select(cn, *[montar(e, filtros, contar=True)[0]], tuple(montar(e, filtros, contar=True)[1]))[0]["total"] if False else None
            sql_c, par_c = montar(e, filtros, contar=True)
            n_com = select(cn, sql_c, tuple(par_c))[0]["total"]
            ent_sem = dict(e); ent_sem["vinculos"] = {k: v for k, v in e["vinculos"].items() if k == vinc_where}
            sql_b, par_b = montar(ent_sem, filtros, contar=True)
            n_base = select(cn, sql_b, tuple(par_b))[0]["total"]
            fan = "OK" if n_com == n_base else f"FAN-OUT {n_base}->{n_com}"
            amostra, _ = executar(*montar(e, filtros, limite=500))
            preench = {api: sum(1 for r in amostra if r.get(api.lower()) not in (None, "")) / len(amostra)
                       for v in e["vinculos"].values() for api in v["colunas"] if amostra}
            for cn_ in e.get("coalescidas", {}):          # colunas coalescidas também precisam vir preenchidas
                if amostra:
                    preench[cn_] = sum(1 for r in amostra if r.get(cn_.lower()) not in (None, "")) / len(amostra)
            pr = ", ".join(f"{k}={100*p:.0f}%" for k, p in preench.items() if k.endswith(("_nome", "_descricao", "_aparece_recibo")))
        status = "OK   " if rows else "VAZIA"
        if fan.startswith("FAN"):
            status = "ERRO "; falhas += 1
        print(f"{status}{nome:<26}emp={emp!s:<5}{len(rows)} linhas {dt*1000:5.0f} ms  fan-out={fan:<6} {('nomes: ' + pr) if pr else ''}")
    except (ErroConsulta, Exception) as ex:
        falhas += 1
        print(f"ERRO {nome:<26}{type(ex).__name__}: {str(ex)[:230]}")
print(f"\n{len(alvo)} entidades, {falhas} falhas")
sys.exit(1 if falhas else 0)
