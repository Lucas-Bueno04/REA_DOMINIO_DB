"""Gera exports/modelo_relacional.html — mapa visual e inventário do que foi mapeado (arquivo único, sem dependências externas).

Fontes (nada é digitado à mão): catálogo SQLite (tabelas, colunas, PK, FK, relações), modelos YAML (entidades) e o código-fonte
(funções e docstrings por análise sintática). Uso: python src/model/gerar_visual.py
"""
import ast
import collections
import datetime
import json
import pathlib
import sqlite3
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "src"))
from server import sqlbuilder as sb  # noqa: E402

DB = RAIZ / "data" / "catalog" / "dominio_catalog.db"
SAIDA = RAIZ / "exports" / "modelo_relacional.html"
HUB = "geempre"
CONF_MIN = 0.8

PASTAS = [
    ("src/extractor/", "Extração: catálogo do banco (tabelas, colunas, FKs, índices, perfil) e mineração dos JOINs nos programas da Domínio."),
    ("src/model/", "Modelo: relações entre tabelas, modelos YAML por módulo (src/model/modulos/), validador, gerador de documentação e deste mapa."),
    ("src/server/", "Servidor: gerador de SQL, motor de consulta e as 12 ferramentas do servidor MCP."),
    ("config/", "Configuração: .env (credenciais locais) e seguranca.yaml (credenciais bloqueadas, limites)."),
    ("data/catalog/", "Catálogo SQLite (dominio_catalog.db): estrutura do banco e relações. Sem dados de clientes."),
    ("data/raw/", "Material bruto da análise: inventário das fontes do gerador, strings dos .pbd, valores distintos de códigos."),
    ("docs/", "Documentação gerada: modelo-<módulo>.md, relacionamentos.md, colunas/<tabela>.md, uso-mcp.md, formato-modelo.md."),
    ("exports/", "Saídas: grafo.json (relações), tabelas_sem_relacao.txt e este mapa visual."),
    ("scripts/", "Sondas, conciliações e testes ponta a ponta (somente leitura; mostram só agregados)."),
    ("tests/", "Testes automatizados (pytest): segurança do SQL, consistência dos modelos, integração com o banco."),
    ("logs/", "Auditoria do servidor (auditoria.jsonl): ferramenta, argumentos, linhas, tempo e erro de cada chamada."),
    ("./", "PLANO.md (plano em fases), STATUS.md (andamento e descobertas), README.md, executar_servidor.cmd."),
]


def inventario_codigo() -> list[dict]:
    out = []
    for pasta in ("src/extractor", "src/model", "src/server", "scripts", "tests"):
        for arq in sorted((RAIZ / pasta).glob("*.py")):
            if arq.name == "__init__.py":
                continue
            try:
                tree = ast.parse(arq.read_text(encoding="utf-8"))
            except SyntaxError:
                continue
            doc = (ast.get_docstring(tree) or "").strip().splitlines()
            fns = []
            for no in tree.body:
                if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    fns.append({"nome": no.name + "()", "tipo": "função", "doc": (ast.get_docstring(no) or "").strip().split("\n")[0][:170]})
                elif isinstance(no, ast.ClassDef):
                    fns.append({"nome": no.name, "tipo": "classe", "doc": (ast.get_docstring(no) or "").strip().split("\n")[0][:170]})
                    for m in no.body:
                        if isinstance(m, ast.FunctionDef) and not m.name.startswith("_"):
                            fns.append({"nome": f"{no.name}.{m.name}()", "tipo": "método", "doc": (ast.get_docstring(m) or "").strip().split("\n")[0][:170]})
            out.append({"pasta": pasta, "arquivo": arq.name, "caminho": f"{pasta}/{arq.name}", "descricao": (doc[0] if doc else "")[:220], "itens": fns})
    return out


def dados() -> dict:
    d = sqlite3.connect(DB)
    d.row_factory = sqlite3.Row
    q = lambda s, *a: d.execute(s, a).fetchall()
    ents, doms = sb.carregar_modelo()

    # ---- números gerais
    tipos = {r[0]: r[1] for r in q("select tipo, count(*) from tabelas group by 1")}
    rel = [dict(origens=r[0], tipo=r[1], n=r[2]) for r in q("select origens, tipo, count(*) from relacoes group by 1,2 order by 3 desc")]
    stats = {
        "objetos": sum(tipos.values()), "tabelas_base": tipos.get("BASE", 0), "temporarias": tipos.get("GBL TEMP", 0), "views": tipos.get("VIEW", 0),
        "colunas": q("select count(*) from colunas")[0][0], "indices": q("select count(*) from indices")[0][0], "fks": q("select count(*) from fks")[0][0],
        "legiveis": q("select count(*) from tabelas where tipo='BASE' and legivel=1 and na_lista_gerador=1")[0][0],
        "linhas": q("select sum(linhas) from tabelas where tipo='BASE' and legivel=1 and na_lista_gerador=1")[0][0],
        "joins_pares": q("select count(*) from joins_observados")[0][0], "joins_ocorrencias": q("select sum(ocorrencias) from joins_observados")[0][0],
        "relacoes": sum(r["n"] for r in rel if r["tipo"] != "temporaria"), "relacoes_origem": rel,
        "programas": q("select count(distinct arquivo) from uso_tabela_arquivo")[0][0], "vinculos_programa_tabela": q("select count(*) from uso_tabela_arquivo")[0][0],
        "perfil_colunas": q("select count(*) from perfil_colunas")[0][0],
        "entidades": len(ents), "dominios": len(doms), "dominios_confirmados": sum(1 for x in doms.values() if x.get("confirmado") is True),
        "colunas_sensiveis": sum(1 for e in ents.values() for v in e["colunas"].values() if isinstance(v, dict) and v.get("sensivel")),
    }
    # ---- departamentos x cobertura
    usadas = set()
    for e in ents.values():
        usadas.add(e["tabela"].lower())
        for v in e.get("vinculos", {}).values():
            usadas.add(v["tabela"].lower())
    deps = collections.OrderedDict()
    for r in q("select nome_lower, departamento, linhas from tabelas where tipo='BASE' and legivel=1 and na_lista_gerador=1"):
        x = deps.setdefault(r["departamento"], {"departamento": r["departamento"], "tabelas": 0, "modeladas": 0, "linhas": 0, "linhas_modeladas": 0})
        x["tabelas"] += 1; x["linhas"] += r["linhas"] or 0
        if r["nome_lower"] in usadas:
            x["modeladas"] += 1; x["linhas_modeladas"] += r["linhas"] or 0
    deps = sorted(deps.values(), key=lambda x: -x["tabelas"])

    # ---- módulos: tabelas, entidades e relações
    info = {r["nome_lower"]: dict(r) for r in q("select * from tabelas")}
    pk = collections.defaultdict(list)
    for r in q("select lower(tabela) t, nome from colunas where pk=1 order by ordem"):
        pk[r["t"]].append(r["nome"])
    mods, raiz_por_mod = {}, collections.defaultdict(set)
    for nome, e in ents.items():
        m = mods.setdefault(e["_modulo"], {"entidades": [], "tabelas": set()})
        ac = e.get("acesso", {})
        campos = []
        for api, v in e["colunas"].items():
            v = v if isinstance(v, dict) else {"coluna": v}
            campos.append({"campo": api, "coluna": v["coluna"], "dominio": v.get("dominio"), "sensivel": v.get("sensivel")})
        m["entidades"].append({
            "nome": nome, "titulo": e.get("titulo"), "tabela": e["tabela"], "modulo": e["_modulo"], "volume": ac.get("volume"),
            "descricao": " ".join((e.get("descricao") or "").split()), "chave": e["chave"], "empresa": ac.get("empresa"),
            "periodo": (ac["periodo"] if isinstance(ac.get("periodo"), str) else (f"{ac['periodo']['vinculo']}.{ac['periodo']['coluna']}" if ac.get("periodo") else None)),
            "exige_algum": ac.get("exige_algum"), "campos": campos,
            "vinculos": {k: {"tabela": v["tabela"], "liga": v["liga"], "colunas": list(v["colunas"])} for k, v in e.get("vinculos", {}).items()},
            "filtros": {k: {"coluna": v["coluna"], "ops": v["ops"]} for k, v in e.get("filtros", {}).items()},
            "filhos": {k: v["entidade"] for k, v in e.get("filhos", {}).items()}, "regras": e.get("regras", []),
            "calculadas": e.get("calculadas", {}), "coalescidas": e.get("coalescidas", {}), "privacidade": e.get("privacidade"),
        })
        m["tabelas"].add(e["tabela"].lower()); raiz_por_mod[e["_modulo"]].add(e["tabela"].lower())
        for v in e.get("vinculos", {}).values():
            m["tabelas"].add(v["tabela"].lower())

    todas_rel = q("select id, lower(filha) f, lower(pai) p, tipo, origens, confianca, ocorrencias from relacoes where tipo<>'temporaria' and confianca>=?", CONF_MIN)
    cols_rel = collections.defaultdict(list)
    for r in q("select relacao_id, col_filha, col_pai from relacao_colunas"):
        cols_rel[r["relacao_id"]].append([r["col_filha"], r["col_pai"]])

    saida_mods = {}
    for mn, m in mods.items():
        tabs = m["tabelas"]
        # ---- nível de cada tabela, pela hierarquia das ENTIDADES (cadastro -> documento -> itens -> pagamentos); apoio à esquerda
        por_nome = {e["nome"]: e for e in m["entidades"]}
        filhos_de = {n: [f for f in e["filhos"].values() if f in por_nome] for n, e in por_nome.items()}
        eh_filho = {f for fs in filhos_de.values() for f in fs}
        prof = {n: 0 for n in por_nome if n not in eh_filho}
        fila = list(prof)
        while fila:
            n = fila.pop(0)
            for f in filhos_de.get(n, []):
                if f not in prof or prof[f] < prof[n] + 1:
                    if prof[n] + 1 <= 5:
                        prof[f] = prof[n] + 1; fila.append(f)
        for n in por_nome:
            prof.setdefault(n, 0)
        nivel_tab = {}
        for n, e in por_nome.items():
            t = e["tabela"].lower()
            nivel_tab[t] = min(nivel_tab.get(t, 99), prof[n])
        apoio = {}
        for n, e in por_nome.items():
            for v in e["vinculos"].values():
                t = v["tabela"].lower()
                if t not in nivel_tab:
                    apoio[t] = min(apoio.get(t, 99), prof[n] - 1)
        for t, nv in apoio.items():
            nivel_tab[t] = -1 if nv >= -1 else nv
        piso = min(nivel_tab.values()) if nivel_tab else 0
        nivel_tab = {t: nv - piso for t, nv in nivel_tab.items()}
        melhores = {}
        for r in todas_rel:
            if r["tipo"] not in ("fk", "vigencia") or r["confianca"] < 0.9:      # só ligações de chave: sem 'ligacao' nem inferidas
                continue
            if r["f"] in tabs and r["p"] in tabs and r["f"] != r["p"] and HUB not in (r["f"], r["p"]):
                chave = (r["f"], r["p"])
                if chave not in melhores or r["confianca"] > melhores[chave]["confianca"]:
                    melhores[chave] = r
        edges, fks = [], collections.defaultdict(list)
        for (f, p), r in melhores.items():
            cs = cols_rel[r["id"]]
            edges.append({"filha": info[f]["nome"], "pai": info[p]["nome"], "tipo": r["tipo"], "origens": r["origens"], "confianca": r["confianca"], "colunas": cs[:6], "usos": r["ocorrencias"]})
            for cf, cp in cs:
                if cf.lower() != "codi_emp":
                    fks[f].append({"col": cf, "pai": info[p]["nome"]})
        tabelas = []
        for t in sorted(tabs):
            i = info[t]
            vistos, fkl = set(), []
            for x in fks.get(t, []):
                if (x["col"], x["pai"]) not in vistos:
                    vistos.add((x["col"], x["pai"])); fkl.append(x)
            tabelas.append({"nome": i["nome"], "nivel": nivel_tab.get(t, 0), "descricao": i["comentario"], "linhas": i["linhas"], "departamento": i["departamento"], "pk": pk.get(t, []),
                            "fks": fkl[:6], "raiz": t in raiz_por_mod[mn], "entidades": [e["nome"] for e in m["entidades"] if e["tabela"].lower() == t],
                            "tem_empresa": any(c["nome"].lower() == "codi_emp" for c in [dict(x) for x in q("select nome from colunas where table_id=?", i["table_id"])])})
        saida_mods[mn] = {"entidades": sorted(m["entidades"], key=lambda x: x["nome"]), "tabelas": tabelas, "relacoes": edges}

    # ---- elos entre módulos (apenas tabelas-raiz das entidades, sem a empresa)
    dono = {}
    for mn, ts in raiz_por_mod.items():
        for t in ts:
            dono.setdefault(t, mn)
    cross = collections.Counter(); exemplos = collections.defaultdict(list)
    for r in q("select lower(filha) f, lower(pai) p, confianca from relacoes where tipo<>'temporaria' and confianca>=0.9"):
        a, b = dono.get(r["f"]), dono.get(r["p"])
        if a and b and a != b and HUB not in (r["f"], r["p"]):
            k = tuple(sorted((a, b))); cross[k] += 1
            if len(exemplos[k]) < 4:
                exemplos[k].append(f"{info[r['f']]['nome']} → {info[r['p']]['nome']}")
    hub = {mn: sum(1 for r in todas_rel if (r["p"] == HUB and r["f"] in ts)) for mn, ts in raiz_por_mod.items()}
    cross_l = [{"a": a, "b": b, "n": n, "exemplos": exemplos[(a, b)]} for (a, b), n in cross.most_common()]

    # ---- arquivos de dados e inventário
    artefatos = []
    for rel_ in ("data/catalog/dominio_catalog.db", "data/raw/inventario_fontes_gerador.csv", "data/raw/valores_distintos.json", "exports/grafo.json",
                 "exports/tabelas_sem_relacao.txt", "docs/relacionamentos.md", "docs/modelo-fiscal.md", "docs/modelo-contabil.md", "docs/modelo-folha.md",
                 "docs/modelo-honorarios.md", "docs/modelo-geral.md", "docs/modelo-comum.md", "docs/uso-mcp.md", "docs/formato-modelo.md", "docs/descobertas-rea.md",
                 "PLANO.md", "STATUS.md", "config/seguranca.yaml"):
        p = RAIZ / rel_
        if p.exists():
            artefatos.append({"caminho": rel_, "kb": round(p.stat().st_size / 1024)})
    modelos = [{"caminho": f"src/model/modulos/{p.name}", "kb": round(p.stat().st_size / 1024)} for p in sorted((RAIZ / "src/model/modulos").glob("*.yaml"))]
    return {"gerado_em": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "stats": stats, "departamentos": deps, "modulos": saida_mods,
            "cross": cross_l, "hub": hub, "pastas": PASTAS, "artefatos": artefatos + modelos, "codigo": inventario_codigo(),
            "ferramentas_mcp": [t for t in _ferramentas()]}


def _ferramentas():
    arq = (RAIZ / "src" / "server" / "mcp_server.py").read_text(encoding="utf-8")
    tree = ast.parse(arq)
    for no in tree.body:
        if isinstance(no, ast.FunctionDef) and any(isinstance(dc, ast.Name) and dc.id == "ferramenta" for dc in no.decorator_list):
            yield {"nome": no.name, "doc": " ".join((ast.get_docstring(no) or "").split())}


def main() -> None:
    dd = dados()
    html = (pathlib.Path(__file__).with_name("visual_template.html")).read_text(encoding="utf-8")
    blob = json.dumps(dd, ensure_ascii=False, default=str).replace("</", "<\\/")
    SAIDA.parent.mkdir(exist_ok=True)
    SAIDA.write_text(html.replace("/*__DADOS__*/null", blob), encoding="utf-8")
    n_t = sum(len(m["tabelas"]) for m in dd["modulos"].values())
    n_r = sum(len(m["relacoes"]) for m in dd["modulos"].values())
    print(f"{SAIDA}  ({SAIDA.stat().st_size/1024:.0f} KB) | módulos={len(dd['modulos'])} entidades={dd['stats']['entidades']} tabelas no desenho={n_t} relações no desenho={n_r}")


if __name__ == "__main__":
    main()
