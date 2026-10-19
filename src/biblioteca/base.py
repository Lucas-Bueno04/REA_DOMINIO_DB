"""Núcleo da biblioteca de ferramentas (tools) MCP do banco Domínio. SOMENTE LEITURA.

Uma `Ferramenta` é a unidade da biblioteca: nome, descrição para o modelo de IA (o que é a tabela, quando usar, regras de negócio, exemplos),
parâmetros tipados (viram o JSON Schema da tool MCP) e um executor `executar(motor, **args)` que só lê o banco pelo `Motor`
(SELECT/WITH, parâmetros sempre ligados, credenciais nunca saem).

Organização (padrão da biblioteca):
    biblioteca/<modulo>/<tabela>.py     TABELA, ENTIDADE(S), TOOLS = [Ferramenta, ...]   (uma tabela por arquivo)
    biblioteca/casos_de_uso/<tema>.py   ferramentas que cruzam várias tabelas (regras de negócio conferidas)
Arquivos com o cabeçalho "GERADO" são reescritos por scripts/gerar_biblioteca.py; os demais são curados à mão e nunca são sobrescritos.
"""
from __future__ import annotations

import hashlib
import inspect
import re
from dataclasses import dataclass, field
from typing import Annotated, Any, Callable

from pydantic import Field

TIPOS_FERRAMENTA = ("consultar", "obter", "totais", "caso_de_uso")
LIMITE_NOME = 64


@dataclass
class Param:
    """Um parâmetro de ferramenta (vira propriedade do JSON Schema)."""
    nome: str
    descricao: str
    tipo: Any = Any
    obrigatorio: bool = False
    padrao: Any = None
    minimo: int | None = None
    maximo: int | None = None


@dataclass
class Ferramenta:
    nome: str
    descricao: str
    parametros: list[Param]
    executar: Callable[..., Any]                     # executar(motor, **args)
    tipo: str = "consultar"
    modulo: str = ""
    tabelas: list[str] = field(default_factory=list)   # tabelas do banco que a ferramenta lê
    entidade: str | None = None
    titulo: str = ""
    gerada: bool = True
    exemplos: list[dict] = field(default_factory=list)  # [{"descricao": ..., "argumentos": {...}}]
    teste: Any = None                                # só casos de uso: argumentos da chamada real da validação (dict) ou callable(motor)->dict

    def esquema(self) -> dict:
        props, req = {}, []
        for p in self.parametros:
            props[p.nome] = {"description": p.descricao}
            if p.obrigatorio:
                req.append(p.nome)
        return {"type": "object", "properties": props, "required": req}


def nome_seguro(base: str, sufixo: str) -> str:
    """Nome de tool MCP: minúsculas/dígitos/_ e até 64 caracteres (trunca a base e acrescenta hash curto se preciso)."""
    base = re.sub(r"[^a-z0-9_]", "_", base.lower())
    nome = f"{base}_{sufixo}"
    if len(nome) <= LIMITE_NOME:
        return nome
    h = hashlib.sha1(base.encode()).hexdigest()[:4]
    corte = LIMITE_NOME - len(sufixo) - len(h) - 2
    return f"{base[:corte]}_{h}_{sufixo}"


def como_funcao(f: Ferramenta, obter_motor: Callable[[], Any]) -> Callable[..., Any]:
    """Cria a função Python (com assinatura tipada) que o SDK MCP transforma em tool. Os erros de uso são tratados por quem registra."""
    def fn(**kw):
        return f.executar(obter_motor(), **{k: v for k, v in kw.items()})

    ps = []
    ordenados = sorted(f.parametros, key=lambda p: (not p.obrigatorio,))        # obrigatórios primeiro (exigência do Python)
    for p in ordenados:
        campo = Field(description=p.descricao, ge=p.minimo, le=p.maximo) if (p.minimo is not None or p.maximo is not None) else Field(description=p.descricao)
        ann = Annotated[p.tipo, campo]
        ps.append(inspect.Parameter(p.nome, inspect.Parameter.KEYWORD_ONLY, annotation=ann,
                                    **({} if p.obrigatorio else {"default": p.padrao})))
    fn.__signature__ = inspect.Signature(ps, return_annotation=dict)
    fn.__annotations__ = {p.nome: q.annotation for p, q in zip(ordenados, ps)} | {"return": dict}
    fn.__name__ = f.nome
    return fn


def validar_argumentos(f: Ferramenta, args: dict | None) -> dict:
    """Validação de entrada usada pelo gateway (executar_ferramenta) e pela bateria de testes: parâmetros desconhecidos, obrigatórios ausentes e limites.
    Devolve os argumentos limpos (sem None). Lança ValueError com mensagem acionável para o modelo de IA."""
    import difflib
    args = dict(args or {})
    nomes = {p.nome: p for p in f.parametros}
    for k in list(args):
        if k not in nomes:
            sug = difflib.get_close_matches(k, list(nomes), n=3)
            raise ValueError(f"Parâmetro '{k}' não existe em {f.nome}." + (f" Quis dizer: {', '.join(sug)}?" if sug else "") + f" Parâmetros: {', '.join(nomes)}.")
    faltam = [p.nome for p in f.parametros if p.obrigatorio and args.get(p.nome) is None]
    if faltam:
        raise ValueError(f"Faltam parâmetros obrigatórios de {f.nome}: {', '.join(faltam)}.")
    for k, v in args.items():
        p = nomes[k]
        if v is not None and (p.minimo is not None or p.maximo is not None):
            if not isinstance(v, int) or isinstance(v, bool) or (p.minimo is not None and v < p.minimo) or (p.maximo is not None and v > p.maximo):
                raise ValueError(f"'{k}' deve ser inteiro entre {p.minimo} e {p.maximo}.")
    return {k: v for k, v in args.items() if v is not None}
