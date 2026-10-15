"""Gera docs/modelo-<modulo>.md a partir do YAML + catálogo + perfil de colunas.
Uso: python src/model/gerar_docs_modelo.py [modulo ...]     (padrão: fiscal)
"""
import pathlib
import sqlite3
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[2]
MODULOS = RAIZ / "src" / "model" / "modulos"
d = sqlite3.connect(RAIZ / "data/catalog/dominio_catalog.db")

cat = {(t, c): (tp, tam, com) for t, c, tp, tam, com in d.execute("select lower(tabela), lower(nome), tipo, tamanho, comentario from colunas")}
perfil = {(t, c): (n, nn or 0, br or 0, ze or 0, se or 0, mn, mx)
          for t, c, n, nn, br, ze, se, mn, mx in d.execute("select tabela, coluna, linhas, nao_nulos, em_branco, zeros, sentinela, minimo, maximo from perfil_colunas")}
linhas_tab = {t: n for t, n in d.execute("select nome_lower, linhas from tabelas")}


def real(v):
    return (v["coluna"] if isinstance(v, dict) else v).lower()


def milhar(n) -> str:
    return f"{int(n or 0):,}".replace(",", ".")


def preench(t, c, codigo):
    p = perfil.get((t, c))
    if not p or not p[0]:
        return ""
    n, nn, br, ze, se, _, _ = p
    if codigo:      # coluna de código: zero é um valor legítimo
        return f"{100*(nn-br-se)/n:.0f}%"
    return f"{100*(nn-br-ze-se)/n:.0f}%"


def esc(s):
    return (s or "").replace("|", "/").replace("\n", " ")


def gerar(modulo: str) -> None:
    y = yaml.safe_load((MODULOS / f"{modulo}.yaml").read_text(encoding="utf-8"))
    comum = yaml.safe_load((MODULOS / "comum.yaml").read_text(encoding="utf-8"))
    doms = {**comum.get("dominios", {}), **y.get("dominios", {})}
    L = [f"# Modelo — {y['titulo']}", "",
         "> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/" + modulo + ".yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**", "",
         f"{len(y['entidades'])} entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).", ""]

    # --- diagrama
    L += ["## Diagrama", "", "```mermaid", "erDiagram"]
    desenhadas = set()
    for n, e in y["entidades"].items():
        for fn, f in e.get("filhos", {}).items():
            if f["entidade"] in y["entidades"] and (n, f["entidade"]) not in desenhadas:
                L.append(f"    {n} ||--o{{ {f['entidade']} : \"{fn}\"")
                desenhadas.add((n, f["entidade"]))
    for n, e in y["entidades"].items():
        for vn, v in e.get("vinculos", {}).items():
            alvo = next((m for m, x in y["entidades"].items() if x["tabela"].lower() == v["tabela"].lower() and m != n), None)
            if alvo and (alvo, n) not in desenhadas and (n, alvo) not in desenhadas:
                L.append(f"    {alvo} ||--o{{ {n} : \"{vn}\"")
                desenhadas.add((alvo, n))
    L += ["```", ""]

    # --- índice
    L += ["## Entidades", "", "| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |", "|---|---|---|---|---|"]
    for n, e in y["entidades"].items():
        ac = e.get("acesso", {})
        obr = []
        if ac.get("empresa"):
            obr.append("empresa")
        if ac.get("exige_algum"):
            obr.append("um de: " + ", ".join(ac["exige_algum"]))
        L.append(f"| [{n}](#{n}) | `{e['tabela']}` | {milhar(linhas_tab.get(e['tabela'].lower(), 0))} | {ac.get('volume', '')} | {'; '.join(obr) or '—'} |")
    L.append("")

    # --- fichas
    for n, e in y["entidades"].items():
        t = e["tabela"].lower()
        ac = e.get("acesso", {})
        L += [f"## {n}", "", f"**{e['titulo']}** — tabela `{e['tabela']}` ({milhar(linhas_tab.get(t, 0))} linhas)", ""]
        if e.get("descricao"):
            L += [e["descricao"].strip(), ""]
        per = ac.get("periodo")
        pstr = f"{per['vinculo']}.{per['coluna']}" if isinstance(per, dict) else per
        L += [f"- **Chave:** `{', '.join(e['chave'])}`",
              f"- **Empresa:** `{ac.get('empresa') or 'não se aplica (tabela global)'}`",
              f"- **Período:** `{pstr or '—'}`" + (f" · exige um de: `{', '.join(ac['exige_algum'])}`" if ac.get("exige_algum") else ""),
              f"- **Ordem padrão:** {', '.join(f'`{c} {dd}`' for c, dd in e.get('ordem', []))}", ""]
        if e.get("regras"):
            L += ["**Regras de negócio validadas:**", ""] + [f"- {r}" for r in e["regras"]] + [""]
        L += ["| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |", "|---|---|---|---|---|---|"]
        for api, v in e["colunas"].items():
            c = real(v)
            tp, tam, com = cat.get((t, c), ("?", "", ""))
            dom = v.get("dominio", "") if isinstance(v, dict) else ""
            obs = ""
            if isinstance(v, dict) and v.get("sensivel"):
                obs += " 🔒"
            if isinstance(v, dict) and v.get("nota"):
                obs += f" ⚠️ {v['nota']}"
            L.append(f"| {api}{obs.split(' ⚠️')[0]} | `{c}` | {tp}({tam}) | {preench(t, c, bool(dom))} | {dom} | {esc(com)}{(' ⚠️ ' + esc(v['nota'])) if isinstance(v, dict) and v.get('nota') else ''} |")
        for cn_, expr in e.get("calculadas", {}).items():
            L.append(f"| {cn_} (calculada) | `{expr}` | — | — | | Calculada pelo modelo: {expr} |")
        for cn_, itens in e.get("coalescidas", {}).items():
            L.append(f"| {cn_} (coalescida) | `{' ⟶ '.join(itens)}` | — | — | | Primeiro valor disponível, nesta ordem: {', '.join(itens)} |")
        if e.get("vinculos"):
            L += ["", "**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**", ""]
            for vn, v in e["vinculos"].items():
                cond = " e ".join(f"`{a}` = `{b}`" for a, b in v["liga"].items())
                sens = set(v.get("sensiveis", []))
                L.append(f"- `{vn}` → `{v['tabela']}` por {cond}; colunas: {', '.join(f'`{a}`' + (' 🔒' if a in sens else '') for a in v['colunas'])}")
        if e.get("privacidade"):
            L += ["", f"> 🔒 **Privacidade:** {' '.join(str(e['privacidade']).split())}"]
        if e.get("filhos"):
            L += ["", "**Filhos (1:N):**", ""]
            for fn, f in e["filhos"].items():
                L.append(f"- `{fn}` → [{f['entidade']}](#{f['entidade']})")
        if e.get("filtros"):
            L += ["", "**Filtros:** " + ", ".join(f"`{fn}` ({'/'.join(f['ops'])})" for fn, f in e["filtros"].items())]
        L.append("")

    # --- domínios
    L += ["## Domínios (significado dos códigos)", "",
          "`confirmado`: **sim** = vem do comentário do banco e/ou foi conferido nos dados; **parcial** = parte dos valores; **não** = hipótese, não use como regra.", ""]
    for dn, dm in doms.items():
        if not dm.get("valores") and not dm.get("valores_observados"):
            continue
        conf = {True: "sim", False: "**não**", "parcial": "parcial"}.get(dm.get("confirmado"), str(dm.get("confirmado")))
        L += [f"### {dn}", ""]
        if dm.get("descricao"):
            L += [dm["descricao"], ""]
        L.append(f"Confirmado: {conf}")
        if dm.get("nota"):
            L += ["", "> " + " ".join(dm["nota"].split())]
        vals = dm.get("valores") or dm.get("valores_observados")
        L += ["", "| Código | Significado |", "|---|---|"] + [f"| {k} | {esc(str(v))} |" for k, v in vals.items()] + [""]
    out = RAIZ / "docs" / f"modelo-{modulo}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(L)} linhas, {len(y['entidades'])} entidades")


if __name__ == "__main__":
    for m in (sys.argv[1:] or ["fiscal"]):
        gerar(m)
