"""Fecha um lote gerado por mapear_lote.py: mede fatos, marca sensíveis, valida, gera documentação e dicionário de colunas e registra o ponto do dia.
Uso: python scripts/fechar_lote.py <prefixo_dos_modulos>     (ex.: pessoal  -> pessoal_*.yaml)
"""
import pathlib, subprocess, sys
import yaml

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PY = str(RAIZ / ".venv" / "Scripts" / "python.exe")
MOD = RAIZ / "src" / "model" / "modulos"


def run(*args):
    r = subprocess.run([PY, *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8", "PYTHONPATH": str(RAIZ / "src")})
    return r.stdout + r.stderr


def main():
    pre = sys.argv[1]
    mods = [p.stem for p in sorted(MOD.glob(f"{pre}_*.yaml"))]
    print(f"{len(mods)} módulos {pre}_*")
    out = run("scripts/medir_fatos.py", *mods)
    falhas = [l for l in out.splitlines() if "FALHA" in l or "Traceback" in l]
    print("medir_fatos:", sum(int(l.split(":")[1].split()[0]) for l in out.splitlines() if "entidades medidas" in l), "entidades medidas;", len(falhas), "falhas")
    for l in falhas[:15]:
        print("   ", l[:200])
    print("marcar_sensiveis:", run("scripts/marcar_sensiveis.py").strip())
    print("proteger_acesso:", run("scripts/proteger_acesso.py").strip())
    print("validação:", run("src/model/validar_modelo.py").strip().splitlines()[-1])
    tabs = []
    for m in mods:
        run("src/model/gerar_docs_modelo.py", m)
        tabs += [e["tabela"] for e in yaml.safe_load((MOD / f"{m}.yaml").read_text(encoding="utf-8"))["entidades"].values()]
    for i in range(0, len(tabs), 60):
        run("scripts/dump_colunas.py", *tabs[i:i + 60])
    print(f"docs: {len(mods)} módulos, {len(tabs)} dicionários de colunas")
    print(run("-c", "from plataforma import dados; print(dados.snapshot_hoje())").strip())


if __name__ == "__main__":
    main()
