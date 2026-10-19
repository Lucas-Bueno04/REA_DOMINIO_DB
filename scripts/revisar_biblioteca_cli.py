"""Interface de linha de comando da biblioteca para REVISÃO INDEPENDENTE (um agente lê só o que um cliente MCP leria e testa as ferramentas).
SOMENTE LEITURA do banco Domínio; a única escrita é o veredito no estado local (data/biblioteca_estado.db).

  python scripts/revisar_biblioteca_cli.py amostra [--semente N] [--n 60]   lista a amostra estratificada (nomes de ferramentas)
  python scripts/revisar_biblioteca_cli.py descrever <ferramenta>           descrição e parâmetros, como o gateway devolve
  python scripts/revisar_biblioteca_cli.py executar <ferramenta> '<json>'   executa com os argumentos (limite sugerido: 5)
  python scripts/revisar_biblioteca_cli.py veredito <ferramenta> <aprovada|revisar> "<nota curta>" --revisor <nome>
  python scripts/revisar_biblioteca_cli.py pendentes                        ferramentas reprovadas na rodada anterior (para reteste)
  python scripts/revisar_biblioteca_cli.py resumo                           contagem de vereditos
"""
import json, pathlib, random, sys
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from biblioteca import estado
from biblioteca.base import validar_argumentos
from biblioteca.registro import carregar
from biblioteca.servidor import descrever


def amostra(semente: int, n: int):
    b = carregar()
    rnd = random.Random(semente)
    cons = [f for f in b.ferramentas.values() if f.tipo == "consultar"]
    cur = [f for f in cons if not f.gerada]
    ger = [f for f in cons if f.gerada]
    por_mod = {}
    for f in ger:
        por_mod.setdefault(f.modulo, []).append(f)
    escolha = rnd.sample(cur, min(len(cur), n // 3))
    mods = sorted(por_mod)
    rnd.shuffle(mods)
    i = 0
    while len(escolha) < n and mods:
        m = mods[i % len(mods)]
        if por_mod[m]:
            escolha.append(por_mod[m].pop(rnd.randrange(len(por_mod[m]))))
        i += 1
        if i > 10 * n:
            break
    # para cada tabela sorteada, avalia a consulta e as irmãs (obter/totais) quando existem
    out = []
    for f in escolha:
        out.append({"ferramenta": f.nome, "irmas": [g.nome for g in b.por_tabela[f.tabelas[0]] if g.nome != f.nome], "curada": not f.gerada, "modulo": f.modulo})
    return out


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    cmd = a[0]
    if cmd == "amostra":
        sem = int(a[a.index("--semente") + 1]) if "--semente" in a else 1
        n = int(a[a.index("--n") + 1]) if "--n" in a else 60
        print(json.dumps(amostra(sem, n), ensure_ascii=False, indent=1))
    elif cmd == "descrever":
        d = descrever(a[1])
        print(json.dumps(d, ensure_ascii=False, indent=1, default=str))
    elif cmd == "executar":
        from server.motor import Motor
        f = carregar().ferramentas[a[1]]
        try:
            args = validar_argumentos(f, json.loads(a[2]) if len(a) > 2 else {})
            r = f.executar(Motor(auditar=False), **args)
        except Exception as ex:          # o cliente MCP veria só a mensagem de erro, sem traceback
            print(f"ERRO ({type(ex).__name__}): {str(ex)[:600]}")
            return
        txt = json.dumps(r, ensure_ascii=False, indent=1, default=str)
        print(txt[:6000] + ("\n... (cortado)" if len(txt) > 6000 else ""))
    elif cmd == "veredito":
        c = estado.abrir(); estado.sincronizar(c, carregar())
        revisor = a[a.index("--revisor") + 1] if "--revisor" in a else "agente"
        nota = f"[{a[2]}] {a[3]}"
        estado.gravar_revisao(c, a[1], nota, revisor)
        print("registrado:", a[1], nota)
    elif cmd == "pendentes":
        c = estado.abrir()
        print(json.dumps([r["nome"] for r in c.execute("select nome from ferramenta where nota_revisao like '[revisar]%' order by nome")], ensure_ascii=False, indent=1))
    elif cmd == "resumo":
        c = estado.abrir()
        for r in c.execute("select substr(nota_revisao,1,10) v, count(*) n from ferramenta where nota_revisao is not null group by 1"):
            print(dict(r))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
