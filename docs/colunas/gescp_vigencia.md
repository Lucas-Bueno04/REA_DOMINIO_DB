# GESCP_VIGENCIA — Sociedade em Conta de Participação - SCP - Vigência
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| VIGENCIA | date(4) | PK |  | Vigência |
| REGIME_FEDERAL | integer(4) |  |  | REGIME FEDERAL (5-LUCRO PRESUMIDO / 1-LUCRO REAL / 6-RET - REGIME ESPECIAL TRIB.) |
| REGIME_COMPETENCIA | char(1) |  |  | Regime apuração (C-Regime de Competência / X-Regime de Caixa) |
| COD_REC_IRPJ | char(6) |  | S | Código de recolhimento IRPJ |
| COD_REC_CSLL | char(6) |  | S | Código de recolhimento CSLL |
| LUCRO_PRESUMIDO_FORMA_CALCULO | char(1) |  |  | Forma de cálculo (S/C) |
| LUCRO_PRESUMIDO_LANCAMENTO | char(1) |  |  | Lançamento (N/P) |
| DESCRICAO | varchar(80) |  |  | Descrição |
| REGIME_APURACAO_INSS_RB | integer(4) |  |  | Regime INSS Receita Bruta |
| FORMA_CALCULO_INSS_RB | integer(4) |  | S | Forma de Cálculo INSS Receita Bruta |
| I_CNAE_INSS_RB | char(15) |  | S | CNAE Principal INSS Receita Bruta |
| I_ATIVIDADE_INSS_RB | char(8) |  | S | Código de atividade INSS Receita Bruta |
| ALIQUOTA_INSS_RB | numeric(7) |  |  | Alíquota INSS Receita Bruta |
| ATIVIDADE_INDUSTRIA_INSS_RB | char(1) |  |  | Atividade Indústria INSS Receita Bruta |
| ATIVIDADE_COMERCIO_INSS_RB | char(1) |  |  | Atividade Comércio INSS Receita Bruta |
| ATIVIDADE_SERVICO_TRANSPORTE_INSS_RB | char(1) |  |  | Atividade Serviço de Transporte INSS Receita Bruta |
| ATIVIDADE_DEMAIS_SERVICOS_INSS_RB | char(1) |  |  | Atividade Demais Serviços INSS Receita Bruta |
| ALIQUOTA_RECEITAS_NAO_REL_INFERIOR_5_INSS_RB | numeric(5) |  | S | Alíquota Não Relacionada Inferior 5% INSS Receita Bruta |
| FORMA_LANCAMENTO_INSS_RB | integer(4) |  | S | Forma de lançamento INSS Receita Bruta |
| CONSIDERAR_FRETE_SEGURO_DESPESA_TIPO | integer(4) |  |  | Considerar receita Frete INSS Receita Bruta |
| UTILIZAR_CREDITO_PER_SEM_REC_DESONERADA_INSS_RB | char(1) |  |  | Não utilizar o crédito da devolução quando no período de ocorrência não ter receita desonerada |
| CALCULAR_CREDITO_PISCOFINS_DEPRECIACAO | char(1) |  |  | Calcular credito PIS e COFINS sobre depreciação |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO | char(1) |  |  | Calcular credito PIS e COFINS sobre aquisição |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO_MP | char(1) |  |  | Calcular credito PIS e COFINS sobre aquisição conforme MP 540/1 |
| DEDUZIR_VALOR_CREDITO_ICMS_DO_PIS_COFINS | char(1) |  |  | Deduzir o valor total do crédito de ICMS da base de cálculo de PIS e COFINS |
| POSSUI_CODIGO_RECOLHIMENTO_PIS_COFINS | char(1) |  |  | Possui mais de um código de recolhimento do crédito de PIS e COFINS |
| INFORMAR_CODIGO_RECOLHIMENTO_PIS_COFINS | char(1) |  |  | Possui mais de um código de recolhimento do crédito de PIS e COFINS |
| CODIGO_RECOLHIMENTO_PIS | varchar(6) |  | S | Código recolhimento PIS |
| CODIGO_RECOLHIMENTO_COFINS | varchar(6) |  | S | Código recolhimento COFINS |
| CALCULAR_CREDITO_PISCOFINS_AQUISICAO_BAIXA_PARCIAL | char(1) |  |  | Calcular crÃ©dito de PIS/COFINS sobre valor de aquisiÃ§Ã£o com baixa parcial(S/N) |
