"""Servidor MCP do banco Domínio (SOMENTE LEITURA). Fase 5.

Executar (stdio, para o Claude Code):   python -m server.mcp_server            (a partir de src/, ou com PYTHONPATH=src)
Executar (HTTP na rede interna):        python -m server.mcp_server --transport streamable-http --host 127.0.0.1 --port 8765
Credenciais: variáveis DOM_UID/DOM_PWD (ou config/.env). Nenhuma escrita é possível: o acesso passa por db.select (SELECT/WITH).
"""
from __future__ import annotations

import argparse
import functools
import sys
from typing import Any

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

from server.motor import ErroUso, Motor
from server.sqlbuilder import ErroConsulta

INSTRUCOES = """
Servidor SOMENTE LEITURA do banco do Sistema Domínio (contabilidade). Três camadas:
1) DESCOBERTA: listar_modulos, listar_entidades, descrever_entidade, buscar_tabelas, descrever_tabela, relacionamentos, caminho_entre, dominio.
2) CONSULTA CURADA: consultar_entidade (75 entidades de negócio: notas, itens, impostos, lançamentos, folha, honorários...). Prefira SEMPRE
   esta camada: ela já resolve joins, nomes legíveis e armadilhas. Leia descrever_entidade antes (regras validadas + filtros obrigatórios).
3) CONSULTA GENÉRICA: consultar_tabela (qualquer uma das ~4.700 tabelas legíveis) quando não houver entidade.
Consultas prontas: balancete (contabilidade) e contas_a_receber (honorários).

REGRAS QUE EVITAM RESPOSTAS ERRADAS (todas validadas contra os dados):
- Quase toda tabela é multiempresa: informe 'empresa' (= codi_emp). Em Honorários, 'empresa'/'escritorio' é o ESCRITÓRIO (1 ou 930), não o cliente.
- Contas contábeis e históricos pertencem ao PLANO da empresa (plano_empresa), que pode ser de outra empresa; as entidades já tratam isso.
- Apuração fiscal: o total de um imposto soma o valor contábil POR IMPOSTO (imposto_nota_*), não o valor da nota; o mês é o da data de movimento.
- 'situacao' das notas NÃO é sinônimo de cancelada; use 'cancelada'. 'competencia' das notas é quase sempre 1900-01-01 (não informada).
- Folha: totais só contam eventos que aparecem no recibo; empresas sem eventos próprios usam os eventos padrão (evento_padrao).
- Honorários só tem dados até 2025-12. Inativas (status 'I') são 62% das empresas: filtre status = 'A' para clientes atuais.
- Resultados são paginados (limite máx. 500; use proximo_offset). Datas: AAAA-MM-DD. Valores monetários vêm como números decimais.
- Colunas de credencial (senhas, tokens, certificados) NUNCA são retornadas; algumas tabelas são bloqueadas.
Os dados são retornados em claro (sem mascaramento) nesta versão do servidor.
""".strip()

srv = MCPServer("dominio-db", title="Banco Domínio (somente leitura)", instructions=INSTRUCOES)
_motor: Motor | None = None


def ferramenta(fn):
    """Registra a ferramenta e garante que o cliente RECEBA a mensagem de erro útil.

    No SDK 2.x só `ToolError` chega ao cliente com o texto; qualquer outra exceção vira "Error executing tool" genérico, o que
    impediria o modelo de se corrigir (ex.: esqueceu a empresa, nome de entidade errado). Erros de uso e do banco são convertidos.
    """
    @functools.wraps(fn)
    def envoltorio(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (ErroUso, ErroConsulta) as e:
            raise ToolError(str(e)) from None
        except ToolError:
            raise
        except Exception as e:                      # erro do banco/ODBC: mensagem curta, sem traceback
            raise ToolError(f"Erro ao consultar o banco ({type(e).__name__}): {str(e)[:300]}") from None
    return srv.tool()(envoltorio)


def motor() -> Motor:
    global _motor
    if _motor is None:
        _motor = Motor()
    return _motor


# ------------------------------------------------------------------------------------------------ descoberta
@ferramenta
def listar_modulos() -> dict:
    """Visão geral: módulos modelados (fiscal, contabil, folha, honorarios, geral, comum), nº de entidades e departamentos do banco com contagem de tabelas e linhas."""
    return motor().listar_modulos()


@ferramenta
def listar_entidades(modulo: str | None = None) -> dict:
    """Lista as entidades de negócio consultáveis com consultar_entidade (nome, tabela, volume, se exige empresa, filtros disponíveis).
    modulo: fiscal | contabil | folha | honorarios | geral | comum (opcional)."""
    return motor().listar_entidades(modulo)


@ferramenta
def descrever_entidade(entidade: str) -> dict:
    """Descreve uma entidade: campos (com tipo, domínio de códigos e descrição do banco), vínculos, filtros e operadores, filtros obrigatórios,
    filhos, e as REGRAS DE NEGÓCIO validadas contra os dados. Leia antes de consultar entidades com muitas armadilhas (notas, folha, lançamentos)."""
    return motor().descrever_entidade(entidade)


@ferramenta
def dominio(nome: str) -> dict:
    """Significado dos códigos de um domínio (ex.: situacao_documento, tipo_folha, origem_lancamento). Mostra se o significado foi CONFIRMADO nos dados ou é hipótese."""
    return motor().dominio(nome)


@ferramenta
def buscar_tabelas(termo: str, departamento: str | None = None, so_modeladas: bool = False, limite: int = 25) -> dict:
    """Busca tabelas do banco por texto no nome, na descrição da tabela ou no nome/descrição das colunas (ex.: 'cupom fiscal', 'saldo', 'dependente').
    departamento: Fiscal | Pessoal | Contábil | Geral | 'Financeiro do escritório' | Processos | Societário | Sistema. Indica quais são consultáveis e quais têm entidade."""
    return motor().buscar_tabelas(termo, departamento, so_modeladas, limite)


@ferramenta
def descrever_tabela(tabela: str) -> dict:
    """Estrutura de uma tabela: colunas (tipo, PK, descrição, % de preenchimento), chave primária, índices, nº de linhas, entidades que a usam e se há bloqueio."""
    return motor().descrever_tabela(tabela)


@ferramenta
def relacionamentos(tabela: str, confianca_minima: float = 0.5, limite: int = 60) -> dict:
    """Relações de uma tabela (pai/filha) com as colunas de ligação. Confiança 1,0 = FK declarada no banco; 0,5–0,9 = JOIN que os programas da Domínio realmente usam;
    0,6 = inferida por nome. Útil para montar JOINs fora das entidades."""
    return motor().relacionamentos(tabela, confianca_minima, limite)


@ferramenta
def caminho_entre(origem: str, destino: str, max_saltos: int = 4, confianca_minima: float = 0.7) -> dict:
    """Caminho mais curto de JOINs entre duas tabelas no grafo de relações, com as colunas de ligação de cada salto (não passa pela tabela de empresas)."""
    return motor().caminho_entre(origem, destino, max_saltos, confianca_minima)


# ------------------------------------------------------------------------------------------------ consulta
@ferramenta
def consultar_entidade(entidade: str, empresa: int | list[int] | None = None, filtros: dict[str, Any] | None = None,
                       colunas: list[str] | None = None, ordem: list[str] | None = None, limite: int = 50, offset: int = 0,
                       contar: bool = False, decodificar: bool = False) -> dict:
    """Consulta uma entidade de negócio (use listar_entidades / descrever_entidade).
    empresa: codi_emp (obrigatório na maioria; em Honorários é o escritório). filtros: {nome_do_filtro: valor | [lista] | {"entre":[a,b]} | {"contem":"x"} | {"gte":v} | {"lte":v} | {"prefixo":"x"}};
    use "periodo" com {"de":"2025-01-01","ate":"2025-01-31"}. colunas: campos desejados (padrão: todos). ordem: ["data_saida desc","numero"].
    limite: até 500; paginação por offset/proximo_offset; contar=true devolve o total (mais lento); decodificar=true acrescenta <campo>_descricao nos códigos."""
    return motor().consultar_entidade(entidade, empresa, filtros, colunas, ordem, limite, offset, contar, decodificar)


@ferramenta
def consultar_tabela(tabela: str, empresa: int | list[int] | None = None, filtros: dict[str, Any] | list[dict[str, Any]] | None = None,
                     colunas: list[str] | None = None, ordem: list[str] | None = None, limite: int = 50, offset: int = 0, contar: bool = False) -> dict:
    """Consulta GENÉRICA de qualquer tabela legível (use buscar_tabelas/descrever_tabela). Prefira consultar_entidade quando existir entidade.
    filtros: {coluna: valor | [lista] | {"entre":[a,b]} | {"contem":"x"} | {"gte":v} | {"lte":v} | {"prefixo":"x"} | {"diferente":v} | {"nulo":true}}
    ou lista de {"coluna","op","valor"}. Tabelas com mais de 200 mil linhas exigem filtro por coluna indexada (ou 'empresa').
    Sem 'colunas' devolve só as primeiras 40 (há tabelas com 400). Colunas de credencial nunca são retornadas."""
    return motor().consultar_tabela(tabela, empresa, filtros, colunas, ordem, limite, offset, contar)


# ------------------------------------------------------------------------------------------------ agregadas
@ferramenta
def balancete(empresa: int, data_inicial: str, data_final: str, filial: int | None = None, somente_com_movimento: bool = True) -> dict:
    """Balancete de verificação por conta analítica no período: saldo anterior, débitos, créditos e saldo final (positivo = devedor), com totais.
    Calculado dos lançamentos (não há saldo armazenado). Datas AAAA-MM-DD. Os totais devem fechar (débitos = créditos; saldo final = 0)."""
    return motor().balancete(empresa, data_inicial, data_final, filial, somente_com_movimento)


@ferramenta
def contas_a_receber(escritorio: int, vencimento_de: str | None = None, vencimento_ate: str | None = None, situacao: str | None = None,
                     cliente_codigo: int | None = None, limite: int = 50, offset: int = 0, contar: bool = False) -> dict:
    """Contas a receber de Honorários por parcela: faturado, recebido e saldo. situacao: aberta | quitada | inconsistente.
    escritorio = CODI_EMP do escritório (1 ou 930). Só há dados até 2025-12."""
    return motor().contas_a_receber(escritorio, vencimento_de, vencimento_ate, situacao, cliente_codigo, limite, offset, contar)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Servidor MCP do banco Domínio (somente leitura)")
    ap.add_argument("--transport", choices=["stdio", "streamable-http", "sse"], default="stdio")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args(argv)
    print(f"[dominio-db] iniciando ({a.transport})", file=sys.stderr, flush=True)
    if a.transport == "stdio":
        srv.run("stdio")
    else:
        srv.run(a.transport, host=a.host, port=a.port)


if __name__ == "__main__":
    main()
