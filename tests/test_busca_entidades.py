"""Busca e listagem de entidades (sem acesso ao banco)."""
import pytest

from server.motor import ErroUso, Motor


@pytest.fixture(scope="module")
def motor():
    return Motor(auditar=False)


def test_busca_prefere_entidade_curada(motor):
    r = motor.buscar_entidades("saldo produto", limite=5)
    assert r["entidades"][0]["entidade"] == "saldo_produto" and r["entidades"][0]["origem"] == "curada"
    assert all(e["pontos"] > 0 for e in r["entidades"])


def test_busca_sem_acento_e_todas_as_palavras(motor):
    a = motor.buscar_entidades("previdenciária guia")["entidades"]
    b = motor.buscar_entidades("previdenciaria guia")["entidades"]
    assert a and [x["entidade"] for x in a] == [x["entidade"] for x in b]
    assert motor.buscar_entidades("saldo produto zzzzqq")["total"] == 0


def test_busca_exige_palavra(motor):
    with pytest.raises(ErroUso):
        motor.buscar_entidades("a")


def test_listar_entidades_pagina(motor):
    p1 = motor.listar_entidades(limite=10)
    assert len(p1["entidades"]) == 10 and p1["proximo_offset"] == 10 and p1["total"] == len(motor.ents)
    p2 = motor.listar_entidades(limite=10, offset=10)
    assert {e["entidade"] for e in p1["entidades"]}.isdisjoint({e["entidade"] for e in p2["entidades"]})
    with pytest.raises(ErroUso):
        motor.listar_entidades(modulo="nao_existe")


def test_listar_modulos_e_compacto(motor):
    r = motor.listar_modulos()
    assert r["total_entidades"] == len(motor.ents)
    assert all(len(v["exemplos"]) <= 6 for v in r["modulos_modelados"].values())
