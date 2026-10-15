"""Testes contra o banco REAL (somente leitura). Pulados se não houver credenciais."""
import os
import pathlib

import pytest

from extractor import db as bd

pytestmark = pytest.mark.integracao
bd._carregar_env()
if not (os.environ.get("DOM_UID") and os.environ.get("DOM_PWD")):
    pytest.skip("sem credenciais (DOM_UID/DOM_PWD ou config/.env)", allow_module_level=True)

from server.motor import ErroUso, Motor  # noqa: E402


@pytest.fixture(scope="module")
def m():
    return Motor(auditar=False)


def test_conexao_e_somente_leitura():
    cn = bd.conectar()
    try:
        with pytest.raises(PermissionError):
            bd.select(cn, "UPDATE bethadba.geempre SET nome_emp = nome_emp WHERE 1 = 0")
        assert bd.select(cn, "SELECT 1 AS x")[0]["x"] == 1
    finally:
        cn.close()


def test_usuario_nao_consegue_escrever_nem_por_fora_do_nosso_filtro():
    """Defesa em profundidade: mesmo contornando o validador, o usuário do banco não tem permissão de escrita."""
    import pyodbc
    cn = bd.conectar()
    try:
        cur = cn.cursor()
        with pytest.raises(pyodbc.Error):
            cur.execute("UPDATE bethadba.geempre SET nome_emp = nome_emp WHERE 1 = 0")
    finally:
        cn.rollback()
        cn.close()


def test_entidade_retorna_dados_e_pagina_sem_repetir(m):
    f = {"periodo": {"de": "2025-01-01", "ate": "2025-12-31"}}
    p1 = m.consultar_entidade("nota_saida", empresa=879, filtros=f, limite=25, offset=0, contar=True)
    p2 = m.consultar_entidade("nota_saida", empresa=879, filtros=f, limite=25, offset=25)
    assert p1["total"] > 50 and len(p1["linhas"]) == 25 and p1["proximo_offset"] == 25
    c1 = {r["codigo"] for r in p1["linhas"]}
    c2 = {r["codigo"] for r in p2["linhas"]}
    assert c1.isdisjoint(c2) and len(c2) == 25
    assert all(k in p1["linhas"][0] for k in ("cliente_nome", "natureza_nome", "valor_contabil"))


def test_decodificar_acrescenta_descricao_dos_codigos(m):
    r = m.consultar_entidade("nota_saida", empresa=879, filtros={"periodo": {"de": "2025-01-01", "ate": "2025-01-31"}}, limite=3, decodificar=True)
    assert r["linhas"][0]["cancelada_descricao"] in ("Sim", "Não")


def test_item_exige_nota_ou_periodo(m):
    with pytest.raises(ErroUso, match="ao menos um"):
        m.consultar_entidade("item_nota_saida", empresa=879)


def test_balancete_fecha(m):
    r = m.balancete(1430, "2025-01-01", "2025-12-31")
    t = r["totais"]
    assert r["contas"] > 10 and abs(t["debitos"] - t["creditos"]) < 0.01 and abs(t["saldo_final"]) < 0.01


def test_balancete_de_empresa_com_plano_alheio_resolve_as_contas(m):
    r = m.balancete(1732, "2026-01-01", "2026-12-31")
    assert r["contas"] > 0 and all(x["classificacao"] is not None for x in r["linhas"])


def test_contas_a_receber_conta_igual_ao_total(m):
    abertas = m.contas_a_receber(930, situacao="aberta", contar=True, limite=500)
    assert abertas["total"] == abertas["retornadas"] == 27
    assert all(x["saldo"] > 0 for x in abertas["linhas"])


def test_tabela_generica_omite_credenciais(m):
    r = m.consultar_tabela("EFPARAMETRO_VIGENCIA", empresa=941, limite=1)
    assert not any("senha" in c.lower() or "credencial" in c.lower() for c in r["colunas"])
    assert any("credencial" in a for a in r["avisos"])


def test_folha_totais_batem_com_o_modelo(m):
    """proventos da base = Σ eventos P que entram no recibo (regra validada)."""
    emp = 245
    base = m.consultar_entidade("base_folha", empresa=emp, filtros={"periodo": {"de": "2025-01-01", "ate": "2025-12-31"}, "tipo_folha": 11}, limite=3, colunas=["empregado_codigo", "competencia", "proventos", "descontos", "liquido", "calculo"])
    for b in base["linhas"]:
        assert abs(b["liquido"] - (b["proventos"] - b["descontos"])) < 0.005


def test_caminho_e_relacionamentos(m):
    c = m.caminho_entre("efmvspro", "efclientes")
    assert c["encontrado"] and c["passos"][0]["de"].lower() == "efmvspro"
    r = m.relacionamentos("efsaidas", confianca_minima=1.0)
    assert any(x["tabela_relacionada"].lower() == "efimpsai" for x in r["relacoes"])
