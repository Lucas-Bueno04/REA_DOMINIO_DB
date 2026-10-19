"""Casos de uso de PESSOAL: eSocial, resumo e memória de cálculo da folha, histórico salarial."""
from biblioteca.casos_de_uso._construtor import de_funcao, descobrir

TOOLS = [
    de_funcao("situacao_esocial", "Situação do eSocial no mês (eventos, aceite, fechamento)", "saber se os eventos do eSocial da competência foram enviados e aceitos e se a folha foi fechada",
              {"empresa": 614, "competencia": "2026-06"}),
    de_funcao("resumo_folha", "Resumo da folha de pagamento do mês", "ver totais de proventos, descontos e líquido da folha de uma empresa na competência",
              {"empresa": 354, "competencia": "2026-08"}),
    de_funcao("memoria_calculo_folha", "Memória de cálculo da folha de um empregado", "explicar como INSS, FGTS e IRRF de um empregado foram calculados (bases, taxas, valores)",
              {"empresa": 354, "empregado": 1, "competencia": "2026-08"},
              teste=descobrir("SELECT TOP 1 s.i_empregados AS emp FROM bethadba.fobasesserv s WHERE s.codi_emp = 354 AND s.tipo_process = 11 AND s.competencia = '2026-08-01' "
                              "AND EXISTS (SELECT 1 FROM bethadba.focalculosbases b WHERE b.i_calculos = s.i_calculos AND b.valor <> 0) ORDER BY s.i_empregados",
                              empresa=354, empregado="emp", competencia="2026-08", tipo_folha=11)),
    de_funcao("historico_salarial", "Histórico salarial de um empregado", "ver as alterações de salário (percentual ou aditivo) ao longo do tempo",
              {"empresa": 354, "empregado": 1},
              teste=descobrir("SELECT TOP 1 codi_emp AS e, i_empregados AS x FROM bethadba.foaltesal WHERE tipo_alt_grade = 1 AND competencia >= '2010-01-01' "
                              "GROUP BY codi_emp, i_empregados HAVING COUNT(*) >= 3 ORDER BY codi_emp", empresa="e", empregado="x")),
]
