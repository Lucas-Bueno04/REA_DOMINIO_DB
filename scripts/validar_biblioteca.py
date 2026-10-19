"""Valida as ferramentas da biblioteca contra o banco (SOMENTE LEITURA) e grava o resultado em data/biblioteca_estado.db.
Retoma de onde parou (só valida o que ainda não foi validado, salvo --refazer). Uso:
  python scripts/validar_biblioteca.py [--modulo M] [--entidade E] [--max N] [--refazer] [--so-falhas] [--threads 4]"""
import concurrent.futures as cf, json, pathlib, sys, threading, time
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from biblioteca import estado, validacao
from biblioteca.registro import carregar
from server.motor import Motor


def main():
    a = sys.argv[1:]
    g = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    modulo, ent, maximo, nthreads = g("--modulo"), g("--entidade"), int(g("--max", 0)), int(g("--threads", 4))
    refazer, so_falhas = "--refazer" in a, "--so-falhas" in a
    b = carregar()
    c = estado.abrir(); estado.sincronizar(c, b)
    ja = {r["nome"]: r["status"] for r in c.execute("select nome, status from ferramenta")}
    por_ent: dict[str, list] = {}
    for f in b.ferramentas.values():
        if f.tipo not in ("consultar", "obter", "totais") or not f.entidade:
            continue
        if modulo and f.modulo != modulo or ent and f.entidade != ent:
            continue
        por_ent.setdefault(f.entidade, []).append(f)
    alvo = []
    for en, fs in por_ent.items():
        st = {ja.get(f.nome) for f in fs}
        if refazer or (so_falhas and "falhou" in st) or (not so_falhas and st != {"validada"}):
            alvo.append(en)
    if maximo:
        alvo = alvo[:maximo]
    print(f"{len(alvo)} entidades a validar (de {len(por_ent)})", flush=True)
    loc = threading.local(); lock = threading.Lock(); t0 = time.time(); feitos = [0, 0]

    def trabalhar(en):
        if not hasattr(loc, "m"):
            loc.m = Motor(auditar=False)
        cn = estado.abrir()
        am = estado.amostra(cn, en)
        try:
            if am is None:
                emp, filt, nota = validacao.montar_amostra(loc.m.ents[en])
                if not nota:
                    am = {"empresa": emp, "filtros": filt}
                    with lock:
                        estado.gravar_amostra(cn, en, emp, filt)
            out = validacao.validar_entidade(loc.m, en, por_ent[en], am)
        except Exception as ex:
            out = {f.nome: (False, {"execucao": {"ok": False, "msg": f"bateria quebrou: {type(ex).__name__}: {str(ex)[:200]}"}}, 0, None) for f in por_ent[en]}
        with lock:
            for nome, (ok, checks, ms, n) in out.items():
                estado.gravar_resultado(cn, nome, ok, checks, ms, n)
            feitos[0] += 1; feitos[1] += sum(1 for v in out.values() if not v[0])
            if feitos[0] % 50 == 0:
                print(f"{feitos[0]}/{len(alvo)} ({round(time.time() - t0)}s) falhas: {feitos[1]}", flush=True)
        cn.close()
        return en, out

    # casos de uso (cruzam várias tabelas): validados um a um
    cu = [f for f in b.ferramentas.values() if f.tipo == "caso_de_uso" and (not modulo or f.modulo == modulo) and not ent
          and (refazer or ja.get(f.nome) != "validada")]
    if cu:
        m0 = Motor(auditar=False)
        for f in cu:
            ok, checks, ms, n = validacao.validar_caso_de_uso(m0, f)
            estado.gravar_resultado(c, f.nome, ok, checks, ms, n)
            print(("  ok   " if ok else "  FALHA ") + f.nome, "" if ok else {k: v["msg"] for k, v in checks.items() if not v["ok"]}, flush=True)

    with cf.ThreadPoolExecutor(nthreads) as ex:
        for en, out in ex.map(trabalhar, alvo):
            for nome, (ok, checks, ms, n) in out.items():
                if not ok:
                    print("  FALHA", nome, {k: v["msg"] for k, v in checks.items() if not v["ok"]}, flush=True)
    r = estado.resumo(c)
    print(json.dumps(estado.snapshot_hoje(c, r), ensure_ascii=False))
    print("por status:", r["por_status"])


if __name__ == "__main__":
    main()
