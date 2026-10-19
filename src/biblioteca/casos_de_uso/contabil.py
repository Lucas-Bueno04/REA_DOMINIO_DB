"""Casos de uso CONTÁBEIS e da empresa: apuração do Lalur e visões consolidadas."""
from biblioteca.casos_de_uso._construtor import de_funcao, descobrir

TOOLS = [
    de_funcao("apuracao_lalur", "Apuração do lucro real (IRPJ e CSLL) na competência", "ver lucro antes do IR, base, IRPJ 15%, adicional, CSLL 9% e valor a recolher",
              {"empresa": 1430, "competencia": "2026-09"},
              teste=descobrir("SELECT TOP 1 c.codi_emp AS e, c.competencia AS comp FROM bethadba.lrcalculo c JOIN bethadba.lrcalculo_irpj_real i ON i.codi_emp = c.codi_emp "
                              "AND i.i_calculo = c.i_calculo WHERE i.valor_irpj_devido > 0 AND i.valor_adicional > 0 ORDER BY c.competencia DESC", empresa="e", competencia="comp")),
    de_funcao("perfil_empresa", "Perfil completo da empresa (cadastro, fiscal, contábil, folha)", "ter, numa só chamada, o retrato da empresa: regime, parâmetros, empregados e envios",
              {"empresa": 614, "data": "2026-09-30"}),
    de_funcao("visao_mensal", "Visão mensal consolidada da empresa", "responder como está a empresa no mês: receita, guias, folha, eSocial, REINF, DAS e informativos",
              {"empresa": 679, "competencia": "2026-09"}),
]
