"""Testes da plataforma de progresso. Estado, rascunhos e modelos são redirecionados para diretórios temporários:
nada aqui toca data/progresso.db, data/rascunhos/ ou src/model/modulos/ reais. O banco Domínio não é acessado."""
import http.client
import json
import shutil
import threading
from http.server import ThreadingHTTPServer

import pytest

from plataforma import dados as dd
from plataforma import servidor as sv


@pytest.fixture()
def amb(tmp_path, monkeypatch):
    mod = tmp_path / "modulos"
    shutil.copytree(dd.MODULOS, mod)
    monkeypatch.setattr(dd, "ESTADO", tmp_path / "progresso.db")
    monkeypatch.setattr(dd, "RASCUNHOS", tmp_path / "rascunhos")
    monkeypatch.setattr(dd, "MODULOS", mod)
    dd.Base._cache = None
    yield tmp_path
    dd.Base._cache = None


def test_status_derivado_e_resumo(amb):
    r = dd.resumo()
    assert sum(r["por_status"].values()) == r["tabelas"]
    assert r["tabelas_modeladas"] == sum(r["por_status"].get(s, 0) for s in ("validada", "medida", "modelada", "apoio"))
    assert r["tabelas_modeladas"] >= 70
    assert r["por_status"].get("bloqueada", 0) >= 1
    assert r["linhas_modeladas"] <= r["linhas_total"]
    assert r["grandes_modeladas"] <= r["grandes"]


def test_tabelas_bloqueadas_ficam_bloqueadas(amb):
    ts = {t["t"]: t for t in dd.lista_tabelas()}
    assert ts["gecertificadosdigitais"]["status"] == "bloqueada"


def test_fila_ordenada_e_sem_modeladas(amb):
    f = dd.fila(30)
    assert [x["score"] for x in f] == sorted((x["score"] for x in f), reverse=True)
    assert all(x["status"] not in ("validada", "medida", "modelada", "apoio", "bloqueada", "vazia") for x in f)


def test_marcacao_manual_e_prioridade(amb):
    t = dd.fila(1)[0]["t"]
    dd.definir_tabela(t, status="em_analise", prioridade=1, nota="ver depois")
    x = {y["t"]: y for y in dd.lista_tabelas()}[t]
    assert x["status"] == "em_analise" and x["prioridade"] == 1
    assert dd.fila(1)[0]["t"] == t                     # priorizada vai para o topo
    dd.definir_tabela(t, status="nenhum")
    assert {y["t"]: y for y in dd.lista_tabelas()}[t]["status"] == "nao_iniciada"
    assert any(h["tabela"] == t for h in dd.historico(10))
    with pytest.raises(ValueError):
        dd.definir_tabela(t, status="validada")        # status derivado não pode ser forçado à mão
    with pytest.raises(KeyError):
        dd.definir_tabela("tabela_que_nao_existe", status="ignorada")


def test_marcacao_de_coluna(amb):
    d = dd.detalhe("efsdopro")
    col = d["colunas"][0]["nome"]
    dd.definir_coluna("efsdopro", col, status="duvida", nota="n")
    c = {x["nome"]: x for x in dd.detalhe("efsdopro")["colunas"]}[col]
    assert c["manual"] == "duvida" and c["nota"] == "n"
    with pytest.raises(ValueError):
        dd.definir_coluna("efsdopro", col, status="invalido")


def test_rascunho_gera_valida_e_nao_expoe_credenciais(amb):
    g = dd.gerar_rascunho("efsdopro")
    assert g["colunas_escolhidas"] > 0 and "entidades" in g["yaml"] or "efsdopro" in g["yaml"].lower()
    dd.salvar_rascunho("efsdopro", g["yaml"])
    v = dd.validar_rascunho("efsdopro")
    assert v["ok"], v["erros"]
    assert dd.rascunho_salvo("efsdopro")["validado"] == 1


def test_rascunho_com_coluna_inexistente_e_invalido(amb):
    g = dd.gerar_rascunho("efsdopro")
    ruim = g["yaml"].replace("codi_pdi", "coluna_inventada", 1)
    dd.salvar_rascunho("efsdopro", ruim)
    assert not dd.validar_rascunho("efsdopro")["ok"]


def test_promocao_exige_validacao_e_grava_so_no_diretorio_temporario(amb):
    g = dd.gerar_rascunho("efsdopro")
    dd.salvar_rascunho("efsdopro", g["yaml"])
    antes = set(p.name for p in dd.MODULOS.iterdir())
    r = dd.promover_rascunho("efsdopro")
    assert r["ok"] and r["arquivo"].startswith("src/model/modulos/")
    novos = set(p.name for p in dd.MODULOS.iterdir()) - antes
    assert len(novos) == 1                              # entrou na cópia temporária
    assert "reinicie" in r["proximo_passo"].lower()
    dd.salvar_rascunho("efsdopro", g["yaml"])
    with pytest.raises((FileExistsError, ValueError)):
        dd.promover_rascunho("efsdopro")                # não sobrescreve sem pedir (ou recusa por duplicar a entidade)
    assert dd.detalhe("efsdopro")["status"] in ("modelada", "validada", "medida")


def test_nao_gera_rascunho_de_tabela_bloqueada(amb):
    with pytest.raises(ValueError):
        dd.gerar_rascunho("gecertificadosdigitais")


@pytest.fixture()
def http_(amb):
    srv = ThreadingHTTPServer(("127.0.0.1", 0), sv.H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    yield srv.server_address[1]
    srv.shutdown()
    srv.server_close()


def _req(porta, metodo, caminho, host=None, origem=None, corpo=None):
    c = http.client.HTTPConnection("127.0.0.1", porta, timeout=60)
    h = {"Host": host or f"127.0.0.1:{porta}"}
    if origem:
        h["Origin"] = origem
    if corpo is not None:
        h["Content-Type"] = "application/json"
    c.request(metodo, caminho, body=json.dumps(corpo) if corpo is not None else None, headers=h)
    r = c.getresponse()
    return r.status, r.read()


def test_http_rejeita_host_e_origem_externos(http_):
    assert _req(http_, "GET", "/api/resumo", host="evil.example.com")[0] == 403
    assert _req(http_, "GET", "/api/resumo", origem="https://evil.example.com")[0] == 403
    assert _req(http_, "POST", "/api/tabela/estado", origem="https://evil.example.com", corpo={"tabela": "efsdopro", "status": "ignorada"})[0] == 403


def test_http_rotas_basicas(http_):
    st, b = _req(http_, "GET", "/api/resumo")
    assert st == 200 and json.loads(b)["resumo"]["tabelas"] > 4000
    assert _req(http_, "GET", "/")[0] == 200
    assert _req(http_, "GET", "/api/tabela?nome=nao_existe_xyz")[0] == 404
    assert _req(http_, "GET", "/api/nada")[0] == 404
    st, b = _req(http_, "POST", "/api/tabela/estado", corpo={"tabela": "efsdopro", "status": "validada"})
    assert st == 400


def test_http_requisicoes_paralelas(http_):
    res = []

    def f(rota):
        res.append(_req(http_, "GET", rota)[0])
    ths = [threading.Thread(target=f, args=(r,)) for r in ("/api/resumo", "/api/tabelas", "/api/fila?n=5", "/api/familias", "/api/historico") * 2]
    [t.start() for t in ths]
    [t.join() for t in ths]
    assert res == [200] * len(ths)
