"""Valida os modelos YAML (src/model/modulos/*.yaml) contra o catálogo. Não acessa o banco.

ERRO  = o modelo está errado (tabela/coluna inexistente, junção que multiplica linhas, domínio inexistente...)
AVISO = risco ou lacuna (sem índice, relação não encontrada no grafo, chave diferente da PK...)

Uso: python src/model/validar_modelo.py [fiscal ...]      (padrão: todos os módulos)
Código de saída 1 se houver erros.
"""
import pathlib
import re
import sqlite3
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
MODULOS = RAIZ / "src" / "model" / "modulos"
OPS = {"eq", "in", "entre", "gte", "lte", "contem", "prefixo"}


class Catalogo:
    def __init__(self):
        d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")
        self.tab = {r[0]: r[1:] for r in d.execute("select nome_lower, nome, tipo, linhas, legivel from tabelas")}
        self.cols, self.pk = {}, {}
        for t, c, pk in d.execute("select lower(tabela), lower(nome), pk from colunas"):
            self.cols.setdefault(t, set()).add(c)
            if pk:
                self.pk.setdefault(t, set()).add(c)
        self.idx = {}
        for t, cs, un in d.execute("select lower(tabela), lower(colunas), unico from indices"):
            self.idx.setdefault(t, []).append((cs.split(","), un))
        self.rel = {}
        for f, p, tp, o, cf in d.execute("select lower(filha), lower(pai), tipo, origens, confianca from relacoes"):
            for par in ((f, p), (p, f)):
                if par not in self.rel or cf > self.rel[par][2]:
                    self.rel[par] = (tp, o, cf)

    def indexada(self, t, col):
        return any(cs and cs[0] == col for cs, _ in self.idx.get(t, []))


def validar(arqs):
    cat = Catalogo()
    erros, avisos, infos = [], [], []
    docs = {a.stem: yaml.safe_load(a.read_text(encoding="utf-8")) for a in arqs}
    dominios = {}
    for d in docs.values():
        dominios.update(d.get("dominios", {}))
    entidades = {}
    for m, d in docs.items():
        for n, e in d.get("entidades", {}).items():
            if n in entidades:
                erros.append(f"{m}.{n}: entidade duplicada")
            entidades[n] = (m, e)
    nomes_api = {n: set() for n in entidades}

    for n, (m, e) in entidades.items():
        P = f"{m}.{n}"
        t = e["tabela"].lower()
        if t not in cat.tab:
            erros.append(f"{P}: tabela '{e['tabela']}' não existe"); continue
        if not cat.tab[t][3]:
            erros.append(f"{P}: tabela '{e['tabela']}' não é legível pelo usuário de leitura")
        cols = cat.cols[t]
        # chave
        ch = [c.lower() for c in e["chave"]]
        falta = [c for c in ch if c not in cols]
        if falta:
            erros.append(f"{P}: chave com coluna inexistente {falta}")
        elif set(ch) != cat.pk.get(t, set()):
            if any(set(cs) == set(ch) and un for cs, un in cat.idx.get(t, [])):
                infos.append(f"{P}: chave {ch} difere da PK mas é um índice único")
            else:
                avisos.append(f"{P}: chave {ch} difere da PK {sorted(cat.pk.get(t, []))} e não há índice único igual")
        # colunas
        api2real = {}
        for api, v in e["colunas"].items():
            col = (v["coluna"] if isinstance(v, dict) else v).lower()
            api2real[api] = col
            if col not in cols:
                erros.append(f"{P}: coluna '{col}' (api '{api}') não existe em {e['tabela']}")
            if isinstance(v, dict) and v.get("dominio") and v["dominio"] not in dominios:
                erros.append(f"{P}: domínio '{v['dominio']}' (coluna {api}) não definido")
        nomes_api[n] = set(api2real)
        e["_api2real"] = api2real
        # colunas calculadas: só aritmética sobre colunas da própria tabela (nada de funções nem subconsultas)
        for cn_, expr in e.get("calculadas", {}).items():
            if not re.fullmatch(r"[A-Za-z0-9_+\-*/(). ]+", expr) or re.search(r"[A-Za-z_]\w*\s*\(", expr):
                erros.append(f"{P}.calculadas.{cn_}: expressão inválida (apenas colunas, números e + - * / parênteses)")
                continue
            for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr):
                if tok.lower() not in cols:
                    erros.append(f"{P}.calculadas.{cn_}: coluna '{tok}' não existe em {e['tabela']}")
            if cn_ in nomes_api[n]:
                erros.append(f"{P}: nome '{cn_}' repetido (coluna calculada)")
            nomes_api[n].add(cn_)
        # colunas coalescidas: primeiro valor não nulo entre colunas de vínculos ("vinculo.coluna") e, opcionalmente, um literal
        for cn_, itens in e.get("coalescidas", {}).items():
            for item in itens:
                if item.startswith("'"):
                    if not re.fullmatch(r"'[A-Za-z0-9 ]*'", item):
                        erros.append(f"{P}.coalescidas.{cn_}: literal inválido {item!r}")
                    continue
                vn_, _, vc_ = item.partition(".")
                vv = e.get("vinculos", {}).get(vn_)
                if not vv:
                    erros.append(f"{P}.coalescidas.{cn_}: vínculo '{vn_}' não existe")
                elif vc_.lower() not in cat.cols.get(vv["tabela"].lower(), set()):
                    erros.append(f"{P}.coalescidas.{cn_}: coluna '{vc_}' não existe em {vv['tabela']}")
            if cn_ in nomes_api[n]:
                erros.append(f"{P}: nome '{cn_}' repetido (coluna coalescida)")
            nomes_api[n].add(cn_)
        # vínculos
        for vn, v in e.get("vinculos", {}).items():
            vt = v["tabela"].lower()
            if vt not in cat.tab:
                erros.append(f"{P}.vinculos.{vn}: tabela '{v['tabela']}' não existe"); continue
            vcols = cat.cols[vt]
            for loc, rem in v["liga"].items():
                if loc.lower() not in cols:
                    erros.append(f"{P}.vinculos.{vn}: coluna local '{loc}' não existe em {e['tabela']}")
                if rem.lower() not in vcols:
                    erros.append(f"{P}.vinculos.{vn}: coluna remota '{rem}' não existe em {v['tabela']}")
            remotas = {r.lower() for r in v["liga"].values()}
            pk_v = cat.pk.get(vt, set())
            unico = pk_v and pk_v <= remotas or any(set(cs) <= remotas and un for cs, un in cat.idx.get(vt, []))
            if not unico:
                erros.append(f"{P}.vinculos.{vn}: junção por {sorted(remotas)} não cobre a chave única de {v['tabela']} "
                             f"(PK {sorted(pk_v)}) — pode multiplicar linhas")
            for ca, cr in v["colunas"].items():
                if cr.lower() not in vcols:
                    erros.append(f"{P}.vinculos.{vn}: coluna '{cr}' não existe em {v['tabela']}")
                if ca in nomes_api[n]:
                    erros.append(f"{P}: nome '{ca}' repetido (coluna x vínculo)")
                nomes_api[n].add(ca)
            r = cat.rel.get((t, vt))
            if r is None and t != vt:
                avisos.append(f"{P}.vinculos.{vn}: nenhuma relação {e['tabela']}↔{v['tabela']} no grafo")
            elif r:
                infos.append(f"{P}.vinculos.{vn}: relação no grafo = {r[0]} / {r[1]} / conf {r[2]}")
        # acesso
        ac = e.get("acesso", {})
        emp = ac.get("empresa")
        if emp and emp.lower() not in cols:
            erros.append(f"{P}: acesso.empresa '{emp}' não existe")
        per = ac.get("periodo")
        per_col_local = None   # coluna de período na própria tabela (None se via vínculo)
        if isinstance(per, dict):
            vn = per["vinculo"]
            if vn not in e.get("vinculos", {}):
                erros.append(f"{P}: acesso.periodo usa vínculo '{vn}' inexistente")
            else:
                vt = e["vinculos"][vn]["tabela"].lower()
                if per["coluna"].lower() not in cat.cols.get(vt, set()):
                    erros.append(f"{P}: acesso.periodo coluna '{per['coluna']}' não existe em {vt}")
        elif per:
            per_col_local = per.lower()
            if per_col_local not in cols:
                erros.append(f"{P}: acesso.periodo '{per}' não existe")
        # filtros
        for fn, f in e.get("filtros", {}).items():
            fcs = f["coluna"] if isinstance(f["coluna"], list) else [f["coluna"]]
            for fc in (c.lower() for c in fcs):
                if fc not in cols:
                    erros.append(f"{P}.filtros.{fn}: coluna '{fc}' não existe")
            if len(fcs) > 1 and not set(f["ops"]) <= {"eq", "in"}:
                erros.append(f"{P}.filtros.{fn}: filtro de várias colunas (OR) só aceita eq/in")
            bad = set(f["ops"]) - OPS
            if bad:
                erros.append(f"{P}.filtros.{fn}: operadores inválidos {sorted(bad)}")
        for x in ac.get("exige_algum", []):
            if x != "periodo" and x not in e.get("filtros", {}):
                erros.append(f"{P}: exige_algum '{x}' não é um filtro")
        # caminho de acesso eficiente: algum índice precisa ter como 1ª coluna uma coluna que o chamador é obrigado a informar
        linhas = cat.tab[t][2] or 0
        if linhas >= 100_000:
            obrig = set()
            if emp:
                obrig.add(emp.lower())
            for x in ac.get("exige_algum", []):
                if x == "periodo":
                    if per_col_local:
                        obrig.add(per_col_local)
                elif x in e.get("filtros", {}) and not isinstance(e["filtros"][x]["coluna"], list):
                    obrig.add(e["filtros"][x]["coluna"].lower())
            lideres = [c for c in obrig if cat.indexada(t, c)]
            if not lideres:
                avisos.append(f"{P}: {linhas:,} linhas e nenhum índice começa por uma coluna obrigatória {sorted(obrig)} — consulta pode varrer a tabela")
            elif emp and emp.lower() not in lideres:
                infos.append(f"{P}: empresa ({emp}) não lidera índice; o acesso eficiente depende de {sorted(lideres)} (exige_algum)")
            if emp and emp.lower() in lideres and not ac.get("exige_algum"):
                pass  # empresa lidera índice: filtrar por empresa já estreita bastante
        if cat.tab[t][2] and cat.tab[t][2] >= 1_000_000 and ac.get("volume") != "grande":
            avisos.append(f"{P}: tabela com {cat.tab[t][2]:,} linhas declarada como volume '{ac.get('volume')}'")
        if cat.tab[t][2] and cat.tab[t][2] >= 100_000 and not (ac.get("exige_algum") or ac.get("periodo") or ac.get("empresa")):
            avisos.append(f"{P}: tabela grande sem nenhuma proteção de acesso")

    # filhos (precisa de todas as entidades carregadas)
    for n, (m, e) in entidades.items():
        P = f"{m}.{n}"
        if "_api2real" not in e:
            continue
        for fn, f in e.get("filhos", {}).items():
            if f["entidade"] not in entidades:
                erros.append(f"{P}.filhos.{fn}: entidade '{f['entidade']}' não existe"); continue
            ce = entidades[f["entidade"]][1]
            if "_api2real" not in ce:
                continue
            for pai_col, filho_api in f["liga"].items():
                if pai_col.lower() not in cat.cols[e["tabela"].lower()]:
                    erros.append(f"{P}.filhos.{fn}: coluna do pai '{pai_col}' não existe em {e['tabela']}")
                # o lado "filho" pode ser nome api (ex.: codigo_nota) ou coluna real (ex.: parc_saip)
                if filho_api not in ce["_api2real"] and filho_api.lower() not in cat.cols[ce["tabela"].lower()]:
                    erros.append(f"{P}.filhos.{fn}: '{filho_api}' não é coluna/nome de {f['entidade']}")
            r = cat.rel.get((e["tabela"].lower(), ce["tabela"].lower()))
            if r is None:
                avisos.append(f"{P}.filhos.{fn}: nenhuma relação {e['tabela']}↔{ce['tabela']} no grafo")
    return entidades, erros, avisos, infos


def main():
    nomes = sys.argv[1:] or [a.stem for a in sorted(MODULOS.glob("*.yaml"))]
    arqs = [MODULOS / f"{n}.yaml" for n in nomes]
    if "comum" not in nomes and (MODULOS / "comum.yaml").exists():
        arqs.append(MODULOS / "comum.yaml")
    ents, erros, avisos, infos = validar(arqs)
    for tag, lst in (("ERRO", erros), ("AVISO", avisos)):
        for x in lst:
            print(f"{tag}: {x}")
    if "-v" in sys.argv or True:
        print(f"\n{len(ents)} entidades | {len(erros)} erros | {len(avisos)} avisos | {len(infos)} informações")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
