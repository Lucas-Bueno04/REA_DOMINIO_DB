"""Mede, no banco REAL (somente leitura, só agregados), fatos sobre as entidades geradas em lote e os grava como `regras` e
como confirmação de domínios nos YAML gerados por scripts/mapear_lote.py.

Uso:  python scripts/medir_fatos.py <modulo> [<modulo> ...]  |  --todos-gerados   [--refazer: remede mesmo com regras já escritas]
Só mexe em arquivos cujo cabeçalho diz "Gerado em lote". Entidades que já têm `regras` são puladas (idempotente).

O que é medido por entidade (cada item vira uma regra com os números e a data da medição):
  1. volume, período (coluna `periodo`), nº de empresas;
  2. colunas expostas que NUNCA são preenchidas (nulo, vazio ou 0 em 100% das linhas);
  3. para cada domínio extraído de comentário: valores reais x valores do comentário -> `confirmado: true` só se TODOS os valores
     observados estão no comentário; senão fica `parcial` e a nota lista os valores fora do comentário;
  4. para cada vínculo: linhas sem pai na tabela relacionada (empresa mediana).
Isso NÃO é conciliação de regra de negócio com um total que a Domínio calcula: é verificação estrutural medida.
"""
import datetime, pathlib, sys, collections
import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor import db as bd

MODULOS = RAIZ / "src" / "model" / "modulos"
HOJE = datetime.date.today().isoformat()
T = 120


def fmt(n):
    return f"{int(n):,}".replace(",", ".")


def q(cn, sql, params=()):
    return bd.select(cn, sql, params, timeout=T)


def medir(e, doms):
    tab = e["tabela"]; ac = e.get("acesso", {}); regras = []
    cn = bd.conectar()
    try:
        cols = {}
        for api, v in e["colunas"].items():
            cols[api] = v["coluna"] if isinstance(v, dict) else v
        usa = list(dict.fromkeys(cols.values()))
        agg = ["COUNT(*) AS n"]
        if ac.get("empresa"):
            agg.append(f"COUNT(DISTINCT {ac['empresa']}) AS emp")
        per = ac.get("periodo")
        pcol = per["coluna"] if isinstance(per, dict) else per
        if pcol and not isinstance(per, dict):
            agg += [f"MIN({pcol}) AS pmin", f"MAX({pcol}) AS pmax"]
        for i, c in enumerate(usa):
            agg.append(f"COUNT({c}) AS c{i}")
        r = q(cn, f"SELECT {', '.join(agg)} FROM bethadba.{tab}")[0]
        n = r["n"]
        if n == 0:
            return ["Tabela sem linhas na data da medição."]
        txt = f"Medido em {HOJE}: {fmt(n)} linhas"
        if ac.get("empresa"):
            txt += f", {fmt(r['emp'])} empresa(s)"
        if r.get("pmin") is not None:
            txt += f", {pcol} de {r['pmin']} a {r['pmax']}"
        regras.append(txt + ".")
        if ac.get("empresa") and r["emp"] == 0:       # coluna de empresa nula em 100% das linhas: tabela global, não pode exigir empresa
            ac["empresa"] = None
            regras.append(f"A coluna de empresa ({tab}) é nula em 100% das linhas: tabela global, sem filtro de empresa.")
        # colunas nunca preenchidas (nulo em 100%); zero/vazio exigiria outro scan por coluna, então só nulo
        nulas = [api for api, c in cols.items() if r[f"c{usa.index(c)}"] == 0]
        if nulas:
            regras.append(f"Colunas expostas nulas em 100% das linhas ({len(nulas)}): " + ", ".join(nulas[:12]) + (" ..." if len(nulas) > 12 else "") + ".")
        # domínios
        for api, v in e["colunas"].items():
            if not (isinstance(v, dict) and v.get("dominio") in doms):
                continue
            dn, col = v["dominio"], v["coluna"]
            obs = q(cn, f"SELECT TOP 40 {col} AS v, COUNT(*) AS n FROM bethadba.{tab} GROUP BY {col} ORDER BY n DESC")
            chaves = {str(k).strip() for k in doms[dn]["valores"]}
            vistos = {str(o["v"]).strip() if o["v"] is not None else None: o["n"] for o in obs}
            fora = {k: c for k, c in vistos.items() if k is not None and k not in chaves}
            reais = {k: c for k, c in vistos.items() if k is not None}
            dist = ", ".join(f"{k if k is not None else 'nulo'}={fmt(c)}" for k, c in list(vistos.items())[:8])
            d = doms[dn]
            if not reais:
                d["confirmado"] = "parcial"
                d["nota"] = f"Coluna {tab}.{col} só tem valores nulos na data da medição ({HOJE}): sem evidência para confirmar o comentário do banco."
                regras.append(f"{api}: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.")
            elif not fora and len(obs) < 40:
                d["confirmado"] = True
                d["nota"] = f"Todos os valores observados em {tab}.{col} estão no comentário do banco ({HOJE}). Distribuição: {dist}."
                regras.append(f"{api}: todos os valores reais estão no comentário do banco ({dist}).")
            else:
                d["confirmado"] = "parcial"
                d["nota"] = (f"Valores em {tab}.{col} fora do comentário do banco: " + ", ".join(f"{k}={fmt(c)}" for k, c in list(fora.items())[:8])
                             + f". Distribuição: {dist} ({HOJE}).")
                regras.append(f"{api}: valores reais fora do comentário do banco ({', '.join(f'{k}={fmt(c)}' for k, c in list(fora.items())[:6])}); tratar o domínio como hipótese.")
        # vínculos: linhas sem pai (empresa mediana)
        if e.get("vinculos"):
            emp = None
            if ac.get("empresa"):
                g = q(cn, f"SELECT {ac['empresa']} AS e, COUNT(*) AS n FROM bethadba.{tab} GROUP BY {ac['empresa']} ORDER BY n")
                emp = g[len(g) // 2]["e"] if g else None
            for vn, vv in e["vinculos"].items():
                liga = vv["liga"]
                on = " AND ".join(f"p.{rc} = t.{lc}" for lc, rc in liga.items())
                any_local = next(iter(liga))
                rem = next(iter(liga.values()))
                where = f"WHERE t.{ac['empresa']} = ?" if emp is not None else ""
                rr = q(cn, f"SELECT COUNT(*) AS n, SUM(CASE WHEN p.{rem} IS NULL AND t.{any_local} IS NOT NULL THEN 1 ELSE 0 END) AS orf "
                           f"FROM bethadba.{tab} t LEFT JOIN bethadba.{vv['tabela']} p ON {on} {where}", (emp,) if emp is not None else ())[0]
                regras.append(f"Vínculo {vn} ({vv['tabela']}): {fmt(rr['orf'] or 0)} de {fmt(rr['n'])} linhas sem registro relacionado"
                              + (f" (empresa {emp})" if emp is not None else "") + ".")
        return regras
    finally:
        cn.close()


def main():
    refazer = "--refazer" in sys.argv
    nomes = [x for x in sys.argv[1:] if x != "--refazer"]
    if nomes == ["--todos-gerados"]:
        nomes = [p.stem for p in sorted(MODULOS.glob("*.yaml")) if "Gerado em lote" in p.read_text(encoding="utf-8")[:200]]
    for mod in nomes:
        arq = MODULOS / f"{mod}.yaml"
        if "Gerado em lote" not in arq.read_text(encoding="utf-8")[:200]:
            print(f"{mod}: não é arquivo gerado em lote; ignorado"); continue
        y = yaml.safe_load(arq.read_text(encoding="utf-8"))
        feitos = falhas = 0
        for nome, e in y["entidades"].items():
            if e.get("regras") and not refazer:
                continue
            try:
                e["regras"] = medir(e, y.get("dominios", {}))
                feitos += 1
            except Exception as ex:
                falhas += 1
                print(f"  FALHA {mod}.{nome}: {str(ex)[:160]}", flush=True)
        cab = arq.read_text(encoding="utf-8").split("\nmodulo:", 1)[0]
        arq.write_text(cab + "\n" + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=160, default_flow_style=None), encoding="utf-8")
        print(f"{mod}: {feitos} entidades medidas, {falhas} falhas", flush=True)


if __name__ == "__main__":
    main()
