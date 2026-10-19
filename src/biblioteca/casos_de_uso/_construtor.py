"""Transforma as funções nomeadas de server/consultas.py (FUNCOES) em Ferramentas da biblioteca, sem duplicar regra: a descrição vem do docstring, a conferência
e as tabelas-fonte vêm do catálogo FUNCOES."""
from __future__ import annotations

import inspect
import re
import typing

from biblioteca.base import Ferramenta, Param
from server import consultas

SENSIVEIS = {"resumo_folha", "historico_salarial", "memoria_calculo_folha"}
_SEM_TESTE = object()


def descobrir(sql: str, **campos):
    """Teste que descobre uma chamada real no banco (SELECT): `campos` = {argumento: coluna_do_resultado}; `{extra}` constantes passam direto."""
    def run(motor):
        r = motor._sql(sql, ())[0]
        return {arg: (r[col] if isinstance(col, str) and col in r else col) for arg, col in campos.items()}
    return run


def _liso(t: str) -> str:
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n", "\n", t.strip()))


def de_funcao(nome: str, titulo: str, quando_usar: str, exemplo: dict, teste: typing.Any = _SEM_TESTE) -> Ferramenta:
    """`exemplo` aparece na documentação; `teste` (padrão: o próprio exemplo) é a chamada real da validação — dict, ou callable(motor)->dict
    quando o argumento precisa ser descoberto no banco; None = sem teste automático."""
    reg = consultas.FUNCOES[nome]
    fn = reg["executar"]
    dicas = typing.get_type_hints(fn)
    params = []
    for p in list(inspect.signature(fn).parameters.values())[1:]:        # pula o Motor
        t = dicas.get(p.name, typing.Any)
        obrig = p.default is inspect.Parameter.empty
        params.append(Param(p.name, reg["parametros"].get(p.name, p.name), t if obrig or type(None) in typing.get_args(t) else t | None,
                            obrigatorio=obrig, padrao=None if obrig else p.default))
    partes = [f"{titulo}.", _liso(fn.__doc__ or reg["descricao"]),
              "QUANDO USAR: " + quando_usar + ".",
              "FONTES (tabelas lidas): " + ", ".join(reg["fontes"]) + ".",
              "CONFERÊNCIA CONTRA OS DADOS: " + reg["validada"]]
    if nome in SENSIVEIS:
        partes.append("PRIVACIDADE: devolve dado financeiro por pessoa identificável; use só quando a pergunta exigir.")
    partes.append("Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.")
    fontes = [f.lower() for f in reg["fontes"] if f not in consultas.FUNCOES]
    return Ferramenta(nome=nome, descricao="\n".join(partes), parametros=params, executar=lambda motor, **kw: consultas.executar(motor, nome, **kw),
                      tipo="caso_de_uso", modulo="casos_de_uso", tabelas=fontes, titulo=titulo, gerada=False,
                      exemplos=[{"descricao": quando_usar, "argumentos": exemplo}], teste=exemplo if teste is _SEM_TESTE else teste)
