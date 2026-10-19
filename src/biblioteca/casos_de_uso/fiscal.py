"""Casos de uso FISCAIS: receita do Simples Nacional, perfil/regime, guias do mês, DAS, REINF, informativos e classificação de produto."""
from biblioteca.casos_de_uso._construtor import de_funcao, descobrir

TOOLS = [
    de_funcao("receita_bruta_simples", "Receita bruta do mês no Simples Nacional (recalculada × apurada)",
              "conferir a receita bruta do mês de uma empresa do Simples e ver se bate com a base que a Domínio apurou (saídas + serviços + CF-e − devoluções)",
              {"empresa": 679, "competencia": "2026-09"}),
    de_funcao("receita_bruta_mensal", "Receita bruta mês a mês (série)", "ver a evolução mensal da receita bruta de uma empresa do Simples em um intervalo",
              {"empresa": 679, "de": "2026-01", "ate": "2026-09"}),
    de_funcao("perfil_fiscal", "Perfil fiscal da empresa (regime, impostos, apuração)", "saber o regime tributário e quais impostos a empresa apura numa data",
              {"empresa": 679, "data": "2026-09-30"}),
    de_funcao("guias_do_mes", "Guias de recolhimento do mês (apurado, pago e saldo)", "listar o que a empresa tem a recolher no mês por imposto, com vencimento e pagamentos",
              {"empresa": 614, "competencia": "2026-06"}),
    de_funcao("situacao_das", "Situação do DAS (Simples Nacional) no mês", "saber se o DAS do mês foi apurado, transmitido pela API, retificado ou rejeitado",
              {"empresa": 679, "competencia": "2023-05"}),
    de_funcao("situacao_reinf", "Situação da EFD-Reinf no mês", "saber se a EFD-Reinf do mês foi aceita, rejeitada ou está pendente e se a competência foi fechada",
              {"empresa": 679, "competencia": "2026-06"}),
    de_funcao("informativos_da_empresa", "Informativos e obrigações acessórias da empresa", "ver quais informativos (DCTF, ECD, etc.) foram gerados ou entregues num intervalo",
              {"empresa": 614, "de": "2026-01", "ate": "2026-06"}),
    de_funcao("classificacao_produto", "Classificação fiscal do produto na data (NCM, CST, alíquotas)", "descobrir como um produto estava classificado fiscalmente em uma data",
              {"empresa": 354, "produto": "1", "data": "2026-09-30"},
              teste=descobrir("SELECT TOP 1 v.codi_emp AS e, TRIM(v.codi_pdi) AS p FROM bethadba.efprodutos_vigencia v WHERE v.vigencia_pdi >= '2020-01-01' "
                              "AND v.codigo_cst_saida IS NOT NULL ORDER BY v.codi_emp, v.codi_pdi", empresa="e", produto="p", data="2026-09-30")),
]
