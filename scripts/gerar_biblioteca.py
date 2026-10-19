"""Gera a estrutura da biblioteca de tools MCP: src/biblioteca/<modulo>/<tabela>.py (uma tabela por arquivo) a partir do modelo de entidades.
Arquivos cujo cabeçalho NÃO começa com "# GERADO" são curados à mão e nunca são sobrescritos. Remove arquivos GERADOS cuja entidade saiu do modelo.
Somente leitura do banco (nem toca nele). Uso: python scripts/gerar_biblioteca.py"""
import pathlib, re, shutil, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
import yaml
from server.sqlbuilder import carregar_modelo

BIB = RAIZ / "src" / "biblioteca"
MODULOS = RAIZ / "src" / "model" / "modulos"
CAB = "# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais)."
RESERVADAS = {"casos_de_uso", "__pycache__"}


def ident(t: str) -> str:
    t = re.sub(r"[^a-z0-9_]", "_", t.lower())
    return t if t[:1].isalpha() else f"t_{t}"


def main():
    ents, _ = carregar_modelo()
    titulos = {}
    for arq in MODULOS.glob("*.yaml"):
        txt = arq.read_text(encoding="utf-8")
        m = re.search(r"^modulo:\s*(\S+)", txt, re.M); ti = re.search(r"^titulo:\s*(.+)$", txt, re.M)
        titulos[m.group(1) if m else arq.stem] = (ti.group(1).strip().strip("'\"") if ti else "")
    por_mod: dict[str, dict[str, list[str]]] = {}
    for n, e in ents.items():
        por_mod.setdefault(e["_modulo"], {}).setdefault(e["tabela"].lower(), []).append(n)
    esperados = set()
    novos = mantidos = 0
    for mod, tabs in sorted(por_mod.items()):
        pasta = BIB / ident(mod)
        pasta.mkdir(parents=True, exist_ok=True)
        init = pasta / "__init__.py"
        if not init.exists() or init.read_text(encoding="utf-8").startswith("# GERADO"):
            init.write_text(f'{CAB}\n"""Módulo {mod}: {titulos.get(mod) or ""}. Uma tabela por arquivo."""\nMODULO = "{mod}"\n', encoding="utf-8")
        esperados.add(init)
        for tab, nomes in sorted(tabs.items()):
            arq = pasta / f"{ident(tab)}.py"
            esperados.add(arq)
            if arq.exists() and not arq.read_text(encoding="utf-8").startswith("# GERADO"):
                mantidos += 1
                continue
            tit = ents[nomes[0]].get("titulo", tab).replace('"', "'")
            arq.write_text(f'''{CAB}
"""Tabela {tab} ({tit}) - módulo {mod}."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "{tab}"
MODULO = "{mod}"
ENTIDADES = {nomes!r}
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
''', encoding="utf-8")
            novos += 1
    # limpeza de arquivos gerados que ficaram órfãos
    removidos = 0
    for d in BIB.iterdir():
        if not d.is_dir() or d.name in RESERVADAS or not (d / "__init__.py").exists():
            continue
        for f in d.glob("*.py"):
            if f not in esperados and f.read_text(encoding="utf-8").startswith("# GERADO"):
                f.unlink(); removidos += 1
        if not any(p for p in d.glob("*.py") if p.name != "__init__.py"):
            shutil.rmtree(d, ignore_errors=True)
    print(f"{len(por_mod)} módulos, {sum(len(v) for v in por_mod.values())} tabelas | escritos {novos}, curados preservados {mantidos}, removidos {removidos}")


if __name__ == "__main__":
    main()
