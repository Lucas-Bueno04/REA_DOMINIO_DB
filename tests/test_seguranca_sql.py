"""Segurança do gerador de SQL e do motor — sem acesso ao banco."""
import datetime
import re

import pytest

from extractor.db import validar_select
from server import sqlbuilder as sb
from server.motor import ErroUso, Motor


@pytest.fixture(scope="module")
def motor():
    return Motor(auditar=False)


@pytest.fixture(scope="module")
def ents():
    return sb.carregar_modelo()[0]


# ------------------------------------------------------------------ somente leitura
@pytest.mark.parametrize("sql", [
    "UPDATE bethadba.geempre SET nome_emp = 'x'", "DELETE FROM bethadba.geempre", "INSERT INTO bethadba.geempre VALUES (1)",
    "DROP TABLE bethadba.geempre", "SELECT 1; DROP TABLE bethadba.geempre", "CALL sp_x()", "EXEC sp_x", "TRUNCATE TABLE x",
    "ALTER TABLE x ADD y int", "GRANT ALL ON x TO y", "CREATE TABLE x (a int)", "SET OPTION isolation_level = 3", "  update x set a=1",
    "WITH t AS (SELECT 1) DELETE FROM x", "SELECT * FROM x; UPDATE y SET a = 1",
])
def test_recusa_qualquer_escrita(sql):
    with pytest.raises(PermissionError):
        validar_select(sql)


def test_aceita_select_e_texto_com_palavras_de_escrita_em_literal():
    validar_select("SELECT * FROM bethadba.geempre WHERE nome_emp = 'UPDATE DELETE DROP'")
    validar_select("WITH t AS (SELECT 1 AS a) SELECT a FROM t")


# ------------------------------------------------------------------ todas as entidades geram SQL parametrizado e seguro
def _filtros_minimos(e):
    f, ac = {}, e.get("acesso", {})
    if ac.get("empresa"):
        f["empresa"] = 1
    for x in ac.get("exige_algum", []):
        f[x] = ("eq", 1) if x != "periodo" else ("entre", (datetime.date(2025, 1, 1), datetime.date(2025, 12, 31)))
    return f


def test_todas_as_entidades_geram_sql_seguro(ents):
    assert len(ents) >= 70
    for nome, e in ents.items():
        sql, params = sb.montar(e, _filtros_minimos(e), limite=10)
        assert sql.startswith("SELECT TOP 10 START AT 1 "), nome
        assert ";" not in sql and "--" not in sql, nome
        assert sql.count("?") == len(params), f"{nome}: {sql.count('?')} marcadores x {len(params)} parâmetros"
        sc, pc = sb.montar(e, _filtros_minimos(e), contar=True)
        assert sc.startswith("SELECT COUNT(*)") and sc.count("?") == len(pc), nome


def test_valor_malicioso_vira_parametro_nunca_sql(ents):
    e = ents["cliente"]
    mal = "x' OR 1=1; DROP TABLE bethadba.efclientes --"
    sql, params = sb.montar(e, {"empresa": 1, "nome": ("contem", mal)}, limite=5)
    assert "DROP" not in sql and "OR 1=1" not in sql
    assert any(mal.replace("%", "") in str(p) or "DROP" in str(p) for p in params)


def test_like_escapa_curingas(ents):
    sql, params = sb.montar(ents["cliente"], {"empresa": 1, "nome": ("contem", "100%_x\\")}, limite=5)
    assert "ESCAPE" in sql
    assert params[-1] == "%100\\%\\_x\\\\%"


def test_colunas_invalidas_sao_recusadas(ents):
    for mal in ["codigo; DROP TABLE x", "codigo, (SELECT senha FROM x)", "1=1", "codi_cli", "*"]:
        with pytest.raises(sb.ErroConsulta):
            sb.montar(ents["cliente"], {"empresa": 1}, colunas=[mal])


def test_limites_de_pagina(ents):
    sql, _ = sb.montar(ents["cliente"], {"empresa": 1}, limite=10**9, offset=-50)
    assert "TOP 500 START AT 1 " in sql
    sql, _ = sb.montar(ents["cliente"], {"empresa": 1}, limite=0, offset=100)
    assert f"TOP {sb.LIMITE_PADRAO} START AT 101 " in sql


def test_filtros_obrigatorios(ents):
    with pytest.raises(sb.ErroConsulta, match="empresa"):
        sb.montar(ents["nota_saida"], {})
    with pytest.raises(sb.ErroConsulta, match="ao menos um"):
        sb.montar(ents["item_nota_saida"], {"empresa": 1})            # 1,3 mi de linhas: exige nota ou período
    with pytest.raises(sb.ErroConsulta, match="não permitido"):
        sb.montar(ents["cliente"], {"empresa": 1, "nome": ("entre", ["a", "b"])})
    with pytest.raises(sb.ErroConsulta, match="desconhecido"):
        sb.montar(ents["cliente"], {"empresa": 1, "inexistente": ("eq", 1)})


def test_in_com_lista_gigante_e_recusado(ents):
    with pytest.raises(sb.ErroConsulta):
        sb.montar(ents["cliente"], {"empresa": 1, "codigo": ("in", list(range(501)))})
    with pytest.raises(sb.ErroConsulta):
        sb.montar(ents["cliente"], {"empresa": 1, "codigo": ("in", [])})


def test_filtro_de_varias_colunas_usa_or(ents):
    f = {"empresa": 1, "conta": ("eq", 5), "periodo": ("entre", (datetime.date(2025, 1, 1), datetime.date(2025, 12, 31)))}
    sql, params = sb.montar(ents["lancamento"], f, limite=5)
    assert "(t.cdeb_lan = ? OR t.ccre_lan = ?)" in sql and params.count(5) == 2


def test_lancamento_usa_o_plano_e_nao_a_empresa(ents):
    sql, _ = sb.montar(ents["lancamento"], {"empresa": 1, "numero": ("eq", 1)}, limite=5)
    assert "t.CODI_EMP_PLANO = v_conta_debito_cadastro.codi_emp" in sql
    assert "t.codi_emp = v_conta_debito_cadastro.codi_emp" not in sql


def test_balancete_e_contas_a_receber_parametrizados():
    sql, par = sb.montar_balancete(1430, datetime.date(2025, 1, 1), datetime.date(2025, 12, 31), filial=2)
    assert sql.count("?") == len(par) and ";" not in sql
    sql, par = sb.montar_contas_a_receber(1, vencimento_de=datetime.date(2025, 1, 1), situacao="aberta", cliente_codigo=7)
    assert sql.count("?") == len(par)
    with pytest.raises(sb.ErroConsulta):
        sb.montar_contas_a_receber(1, situacao="x'; DROP TABLE y --")


# ------------------------------------------------------------------ motor: salvaguardas (nenhuma chega ao banco)
def test_tabelas_de_credenciais_bloqueadas(motor):
    for t in ["GECERTIFICADOSDIGITAIS", "gesecusuarios", "GEAPURACAO_ASSISTIDA_CREDENCIAIS", "efdas_api_tokens_requisicao"]:
        with pytest.raises(ErroUso, match="bloqueada"):
            motor.consultar_tabela(t, limite=1)


@pytest.mark.parametrize("coluna", ["SENHA_PAR", "senha_certificado", "ACCESS_TOKEN", "CLIENT_SECRET", "SENHA_BACEN_ENVIO", "NFSE_FRASE_SECRETA", "arquivo_certificado_digital"])
def test_colunas_de_credencial_sao_detectadas(motor, coluna):
    assert motor._credencial(coluna)


@pytest.mark.parametrize("coluna", ["nome_emp", "cgce_emp", "vlor_lan", "codi_sai", "hash_referenciado", "certificado_digital"])
def test_colunas_comuns_nao_sao_credencial(motor, coluna):
    assert not motor._credencial(coluna)


def test_pedir_coluna_de_credencial_e_recusado(motor):
    with pytest.raises(ErroUso, match="credencial"):
        motor.consultar_tabela("EFPARAMETRO_VIGENCIA", empresa=1, colunas=["codi_emp", "SENHA_PAR"])
    with pytest.raises(ErroUso, match="credencial"):
        motor.consultar_tabela("EFPARAMETRO_VIGENCIA", empresa=1, filtros={"SENHA_PAR": "x"})


def test_tabela_grande_exige_filtro_indexado(motor):
    with pytest.raises(ErroUso, match="indexada"):
        motor.consultar_tabela("ctlancto", limite=1)
    with pytest.raises(ErroUso, match="indexada"):
        motor.consultar_tabela("ctlancto", filtros={"vlor_lan": 10}, limite=1)       # coluna sem índice líder


def test_nomes_inexistentes_sugerem_alternativas(motor):
    with pytest.raises(ErroUso, match="efsaidas"):
        motor.consultar_tabela("efsaida")
    with pytest.raises(ErroUso, match="nota_saida"):
        motor.consultar_entidade("nota_saidaa", empresa=1)
    with pytest.raises(ErroUso, match="Filtros"):
        motor.consultar_entidade("nota_saida", empresa=1, filtros={"datasaida": "2025-01-01"})


def test_tabela_interna_do_sistema_nao_e_consultavel(motor):
    internas = [r["nome"] for r in motor.cat.execute("select nome from tabelas where tipo='BASE' and na_lista_gerador=0 limit 1")]
    assert internas, "esperava ao menos uma tabela interna no catálogo"
    with pytest.raises(ErroUso, match="interna"):
        motor.consultar_tabela(internas[0], limite=1)


def test_ordenacao_so_por_campos_da_entidade(motor):
    with pytest.raises(ErroUso, match="Ordenação"):
        motor.consultar_entidade("cliente", empresa=1, ordem=["nome; DROP TABLE x"])
    with pytest.raises(ErroUso, match="Ordenação"):
        motor.consultar_entidade("cliente", empresa=1, ordem=["cliente_nome"])        # coluna de vínculo não ordena
    with pytest.raises(ErroUso, match="asc ou desc"):
        motor.consultar_entidade("cliente", empresa=1, ordem=["nome sideways"])


def test_empresa_em_tabela_global_e_recusada(motor):
    with pytest.raises(ErroUso, match="global"):
        motor.consultar_entidade("natureza_operacao", empresa=1)
