"""Biblioteca de tools MCP (src/biblioteca): estrutura, nomes, validação de entrada, gateway e regressões encontradas pela bateria contra o banco real."""
import asyncio
import json

import pytest

from biblioteca import estado
from biblioteca.base import validar_argumentos
from biblioteca.registro import carregar
from biblioteca.servidor import buscar, descrever
from server.motor import ErroUso, Motor


@pytest.fixture(scope="module")
def motor():
    return Motor(auditar=False)


@pytest.fixture(scope="module")
def bib():
    return carregar()


def test_biblioteca_carrega_sem_erros(bib):
    assert not bib.erros
    assert len(bib.ferramentas) >= 4000
    tipos = {f.tipo for f in bib.ferramentas.values()}
    assert {"consultar", "obter", "totais", "caso_de_uso"} <= tipos


def test_toda_entidade_tem_ferramenta_de_consulta(bib, motor):
    com = {f.entidade for f in bib.ferramentas.values() if f.tipo == "consultar"}
    assert com == set(motor.ents)


def test_nomes_validos_para_mcp(bib):
    import re
    for n, f in bib.ferramentas.items():
        assert re.fullmatch(r"[a-z0-9_]{1,64}", n), n
        assert f.descricao and f.parametros is not None


def test_uma_tabela_por_arquivo():
    import pathlib
    raiz = pathlib.Path(__file__).resolve().parents[1] / "src" / "biblioteca"
    arqs = [p for d in raiz.iterdir() if d.is_dir() and d.name not in ("casos_de_uso", "__pycache__") for p in d.glob("*.py") if p.name != "__init__.py"]
    assert len(arqs) >= 2000
    assert len({(p.parent.name, p.stem) for p in arqs}) == len(arqs)


def test_descricao_orienta_o_modelo(bib):
    d = bib.ferramentas["nota_saida_consultar"].descricao
    assert "efsaidas" in d and "OBRIGATÓRIO" in d and "REGRAS DE NEGÓCIO" in d and "limite" in d.lower()


def test_validacao_de_entrada(bib):
    f = bib.ferramentas["nota_saida_consultar"]
    with pytest.raises(ValueError, match="obrigat"):
        validar_argumentos(f, {})
    with pytest.raises(ValueError, match="Quis dizer: empresa"):
        validar_argumentos(f, {"empres": 1})
    with pytest.raises(ValueError, match="entre 1 e 500"):
        validar_argumentos(f, {"empresa": 1, "limite": 5000})
    assert validar_argumentos(f, {"empresa": 1, "uf": None}) == {"empresa": 1}


def test_gateway_busca_e_descreve():
    r = buscar("saldo produto")
    assert r["total"] >= 1 and any(x["nome"] == "saldo_produto_consultar" for x in r["ferramentas"])
    d = descrever("nota_saida_consultar")
    assert d["parametros"] and d["exemplos"]
    with pytest.raises(ValueError, match="não existe"):
        descrever("nota_saida_consultarr")


def test_consultar_exige_empresa_e_filtro_protetor(bib, motor):
    f = bib.ferramentas["nota_saida_consultar"]
    r = f.executar(motor, empresa=1430, periodo={"de": "2026-08-01", "ate": "2026-08-31"}, limite=3)
    assert 0 < r["retornadas"] <= 3
    g = next(x for x in bib.ferramentas.values() if x.tipo == "consultar" and motor.ents[x.entidade]["acesso"].get("exige_algum"))
    with pytest.raises(ErroUso, match="ao menos"):
        g.executar(motor, **({"empresa": 1} if motor.ents[g.entidade]["acesso"].get("empresa") else {}))


def test_totais_batem_com_a_contagem(bib, motor):
    tot = bib.ferramentas["nota_saida_totais"]
    cons = bib.ferramentas["nota_saida_consultar"]
    base = {"empresa": 1430, "periodo": {"de": "2026-01-01", "ate": "2026-09-30"}}
    t = tot.executar(motor, **base, agrupar_por=["data_saida:mes"], metricas=["valor_contabil"])
    c = cons.executar(motor, **base, limite=1, contar=True)
    assert t["total_geral"]["linhas"] == c["total"] == sum(g["linhas"] for g in t["grupos"])
    assert abs(t["total_geral"]["soma_valor_contabil"] - sum(g["soma_valor_contabil"] for g in t["grupos"])) < 0.05
    with pytest.raises(ErroUso, match="é data"):
        tot.executar(motor, **base, agrupar_por=["data_saida"])
    with pytest.raises(ErroUso, match="somável"):
        tot.executar(motor, **base, metricas=["cancelada"])


def test_char_com_brancos_a_direita_acha_pelo_valor_curto(motor):
    """Regressão: CHAR(8) guarda '0101    ' e `= '0101'` não casava; os valores passam a ser completados com brancos (mantendo o índice)."""
    assert motor.consultar_entidade("efncm", filtros={"ncm": "0101"})["retornadas"] == 1
    assert motor.consultar_entidade("efncm", filtros={"ncm": ["0101", "01012"]})["retornadas"] == 2
    assert motor.consultar_tabela("efncm", filtros={"ncm": "0101"})["retornadas"] == 1


def test_filtro_chamado_periodo_sem_coluna_de_periodo(motor):
    """Regressão: um filtro comum chamado 'periodo' (coluna PERIODO) era tratado como o período da tabela e falhava."""
    r = motor.consultar_entidade("efd_reinf_retorno_arquivos_r4099_periodo", empresa=1, filtros={"periodo": {"in": [202601, 202602]}}, limite=1)
    assert r["retornadas"] >= 0           # antes: ErroConsulta "esta entidade não tem coluna de período"


def test_caso_de_uso_pela_biblioteca(bib, motor):
    f = bib.ferramentas["receita_bruta_simples"]
    r = f.executar(motor, empresa=679, competencia="2026-09")
    assert r["situacao"] == "confere"


def test_servidor_compacto_e_completo():
    import server.mcp_server as ms
    from mcp.server.mcpserver import MCPServer
    from biblioteca.servidor import registrar
    srv = MCPServer("t")
    n = registrar(srv, ms.motor, "compacto")
    nomes = [t.name for t in asyncio.run(srv.list_tools())]
    assert n == len(nomes) and "executar_ferramenta" in nomes and "receita_bruta_simples" in nomes and len(nomes) < 40
    srv2 = MCPServer("t2")
    registrar(srv2, ms.motor, "completo", {"estoque"})
    nomes2 = [t.name for t in asyncio.run(srv2.list_tools())]
    assert "saldo_produto_consultar" in nomes2 and "nota_saida_consultar" not in nomes2


def test_estado_derivado_de_status():
    import sqlite3
    def lin(status, gerada=1, nota=None):
        return {"status": status, "gerada": gerada, "nota_revisao": nota}
    assert estado.status_tabela([]) == "sem_ferramenta"
    assert estado.status_tabela([lin("nao_validada")]) == "gerada"
    assert estado.status_tabela([lin("validada"), lin("falhou")]) == "falhou"
    assert estado.status_tabela([lin("validada"), lin("validada")]) == "validada"
    assert estado.status_tabela([lin("validada", 0)]) == "curada"
    assert estado.status_tabela([lin("validada", 1, "[aprovada] ok")]) == "revisada"
