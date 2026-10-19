"""Liga a biblioteca ao servidor MCP.

Perfis (quantas tools aparecem na lista do cliente):
  compacto (padrão): 3 tools de GATEWAY (buscar_ferramentas, descrever_ferramenta, executar_ferramenta) + as tools de casos de uso, escritas à mão.
                     Os clientes carregam a lista inteira de tools no contexto; com ~4.000 tools de tabelas (≈11 MB de schema) isso é inviável.
  completo         : todas as tools da biblioteca registradas individualmente (para clientes/servidores dedicados a um módulo, use --modulos).
"""
from __future__ import annotations

import functools
import unicodedata
from typing import Any

from mcp.server.mcpserver.exceptions import ToolError

from biblioteca.base import Ferramenta, como_funcao, validar_argumentos
from biblioteca.registro import carregar
from server.motor import ErroUso
from server.sqlbuilder import ErroConsulta


def _norm(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", (t or "").lower()) if unicodedata.category(c) != "Mn")


def _protegida(fn):
    @functools.wraps(fn)
    def w(*a, **k):
        try:
            return fn(*a, **k)
        except (ErroUso, ErroConsulta, ValueError) as e:
            raise ToolError(str(e)) from None
        except ToolError:
            raise
        except Exception as e:
            raise ToolError(f"Erro ao consultar o banco ({type(e).__name__}): {str(e)[:300]}") from None
    return w


def resumo(f: Ferramenta) -> dict:
    return {"nome": f.nome, "tipo": f.tipo, "modulo": f.modulo, "tabelas": f.tabelas, "titulo": f.titulo, "entidade": f.entidade,
            "curada": not f.gerada, "obrigatorios": [p.nome for p in f.parametros if p.obrigatorio]}


def buscar(termo: str, modulo: str | None = None, tipo: str | None = None, limite: int = 20) -> dict:
    b = carregar()
    palavras = [p for p in _norm(termo).split() if p]
    achados = []
    for f in b.ferramentas.values():
        if modulo and f.modulo != modulo:
            continue
        if tipo and f.tipo != tipo:
            continue
        alvo = _norm(" ".join([f.nome, f.titulo, f.entidade or "", " ".join(f.tabelas), f.descricao[:600]]))
        if all(p in alvo for p in palavras):
            nome_t = _norm(f.nome + " " + f.titulo)
            score = sum(p in nome_t for p in palavras) * 2 + (3 if not f.gerada else 0) + (1 if f.tipo == "caso_de_uso" else 0)
            achados.append((score, f))
    achados.sort(key=lambda x: (-x[0], x[1].nome))
    return {"termo": termo, "total": len(achados), "ferramentas": [resumo(f) for _, f in achados[:max(1, min(limite, 50))]],
            "dica": "Use descrever_ferramenta(nome) e depois executar_ferramenta(nome, argumentos)."}


def descrever(nome: str) -> dict:
    f = carregar().ferramentas.get(nome)
    if not f:
        import difflib
        sug = difflib.get_close_matches(nome, list(carregar().ferramentas), n=5)
        raise ValueError(f"Ferramenta '{nome}' não existe." + (f" Parecidas: {', '.join(sug)}." if sug else " Use buscar_ferramentas(termo)."))
    return {**resumo(f), "descricao": f.descricao, "parametros": [{"nome": p.nome, "obrigatorio": p.obrigatorio, "padrao": p.padrao, "descricao": p.descricao} for p in f.parametros],
            "exemplos": f.exemplos}


def registrar(srv, obter_motor, perfil: str = "compacto", modulos: set[str] | None = None) -> int:
    b = carregar()

    @_protegida
    def buscar_ferramentas(termo: str, modulo: str | None = None, tipo: str | None = None, limite: int = 20) -> dict:
        """Procura na BIBLIOTECA de ferramentas (uma ou mais por tabela do banco Domínio + casos de uso) por palavras: 'saldo produto', 'cupom fiscal', 'folha'...
        tipo: consultar | obter | caso_de_uso. Devolve nome, módulo, tabela e campos obrigatórios; depois use descrever_ferramenta e executar_ferramenta."""
        return buscar(termo, modulo, tipo, limite)

    @_protegida
    def descrever_ferramenta(nome: str) -> dict:
        """Descrição completa de uma ferramenta da biblioteca: o que é a tabela, parâmetros (obrigatórios, filtros, domínios de códigos), regras de negócio e exemplos."""
        return descrever(nome)

    @_protegida
    def executar_ferramenta(nome: str, argumentos: dict[str, Any] | None = None) -> dict:
        """Executa uma ferramenta da biblioteca pelo nome (veja buscar_ferramentas/descrever_ferramenta) com os argumentos validados. Somente leitura."""
        f = b.ferramentas.get(nome)
        if not f:
            descrever(nome)
        return f.executar(obter_motor(), **validar_argumentos(f, argumentos))

    for fn in (buscar_ferramentas, descrever_ferramenta, executar_ferramenta):
        srv.add_tool(fn)
    n = 3
    for f in b.ferramentas.values():
        if modulos and f.modulo not in modulos:
            continue
        if perfil == "completo" or f.tipo == "caso_de_uso":
            fn = _protegida(como_funcao(f, obter_motor))
            srv.add_tool(fn, name=f.nome, title=f.titulo or None, description=f.descricao)
            n += 1
    return n
