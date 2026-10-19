"""Fumaça de TODAS as entidades pelo caminho real do MCP (Motor.consultar_entidade): chama cada uma com os filtros obrigatórios, serializa o
resultado em JSON e relata falhas. Somente leitura. Uso: python scripts/testar_motor_entidades.py [--modulo M] [--max N]
Saída: data/lotes/motor_entidades.json. Também usado por tests/test_todas_entidades.py."""
import datetime, decimal, json, pathlib, sys, time, uuid
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from extractor import db as bd
from server.motor import Motor


def nat(v):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()
    if isinstance(v, decimal.Decimal):
        return int(v) if v == v.to_integral_value() else float(v)
    if isinstance(v, uuid.UUID):
        return str(v)
    return v


def montar_chamada(e):
    ac = e.get("acesso", {}); f = {}; emp = None
    cn = bd.conectar()
    try:
        if ac.get("empresa"):
            r = bd.select(cn, f"SELECT {ac['empresa']} AS e, COUNT(*) AS n FROM bethadba.{e['tabela']} GROUP BY {ac['empresa']} ORDER BY n", timeout=120)
            if not r:
                return None, {}, "tabela sem linhas"
            emp = nat(r[len(r) // 2]["e"])
        for x in ac.get("exige_algum", [])[:1]:            # basta atender UM dos filtros obrigatórios
            if x == "periodo":
                f["periodo"] = {"de": "2000-01-01", "ate": "2100-12-31"}
            else:
                col = e["filtros"][x]["coluna"]
                col = col[0] if isinstance(col, list) else col
                vals = bd.select(cn, f"SELECT DISTINCT TOP 3 {col} AS c FROM bethadba.{e['tabela']}" + (f" WHERE {ac['empresa']} = ?" if emp is not None else ""), (emp,) if emp is not None else (), timeout=120)
                ops = e["filtros"][x]["ops"]
                vs = [nat(v["c"]) for v in vals]
                f[x] = {"in": vs} if "in" in ops else (vs[0] if "eq" in ops else {"gte": vs[0]})
        return emp, f, None
    finally:
        cn.close()


def executar(modulo=None, maximo=0, motor=None, progresso=None):
    motor = motor or Motor(auditar=False)
    res = {}
    nomes = [n for n, e in motor.ents.items() if (not modulo or e["_modulo"] == modulo)]
    if maximo:
        nomes = nomes[:maximo]
    t0 = time.time()
    for i, n in enumerate(nomes, 1):
        e = motor.ents[n]
        try:
            emp, f, nota = montar_chamada(e)
            if nota:
                res[n] = {"ok": True, "nota": nota}; continue
            t1 = time.time()
            r = motor.consultar_entidade(n, empresa=emp, filtros=f or None, limite=5)
            json.dumps(r, default=str)
            res[n] = {"ok": True, "linhas": len(r.get("linhas", r.get("dados", []))), "ms": round((time.time() - t1) * 1000)}
        except Exception as ex:
            res[n] = {"ok": False, "erro": f"{type(ex).__name__}: {str(ex)[:250]}"}
        if progresso and i % 100 == 0:
            progresso(i, len(nomes), time.time() - t0, sum(1 for v in res.values() if not v["ok"]))
    return res


def main():
    args = sys.argv[1:]
    modulo = args[args.index("--modulo") + 1] if "--modulo" in args else None
    maximo = int(args[args.index("--max") + 1]) if "--max" in args else 0
    t0 = time.time()
    res = executar(modulo, maximo, progresso=lambda i, n, s, f: print(f"{i}/{n} ({round(s)}s) falhas até agora: {f}", flush=True))
    falhas = {n: v for n, v in res.items() if not v["ok"]}
    (RAIZ / "data" / "lotes").mkdir(parents=True, exist_ok=True)
    (RAIZ / "data" / "lotes" / "motor_entidades.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"fim: {len(res)} entidades, {len(falhas)} falhas, {round(time.time() - t0)}s")
    for n, v in list(falhas.items())[:40]:
        print("  FALHA", n, v["erro"][:200])


if __name__ == "__main__":
    main()
