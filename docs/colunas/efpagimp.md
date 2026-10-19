# efpagimp — Pagamentos de Impostos
35.248 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_pim | date(4) | PK |  | Competencia |
| pdic_pim | integer(4) | PK |  | Periodicidade |
| parc_pim | integer(4) | PK |  | Parcela |
| dpag_pim | date(4) |  | S | Data do pagamento |
| vpag_pim | numeric(13) |  | S | Valor |
| vjur_pim | numeric(13) |  | S | Valor dos juros |
| vmul_pim | numeric(13) |  | S | Valor da multa |
| banco_pim | integer(4) |  |  | Codigo do Banco |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Imp. API, 5 - Digital Bank |
| nbaixa_pim | integer(4) | PK |  | Numero da baixa |
| crec_pim | char(6) |  | S | Codigo da receita para o IRRF |
| dare_pim | char(25) |  | S | Calcula adicional de ICMS (S/N) |
| compensar_pim | integer(4) |  | S | Codigo do imposto a compensar (ICMS adicional) - GO |
| PAGTO_OPERACOES_PIM | integer(4) |  |  | Pagamento referente a operacoes(1=interna/2=interestadual) |
| CODIGO_ESCRITORIO | integer(4) |  | S | Codigo do escritorio Honorarios |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritorio Honorarios |
| I_MOVIMENTO_CLIENTE | integer(4) |  | S | Conta corrente cliente Honorarios |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) |  | S | Conta corrente cliente sequencial Honorarios |
| I_HISTORICO_HR | integer(4) |  | S | Codigo do historico Honorarios |
| HISTORICO_HR | varchar(512) |  | S | Historico Honorarios |
| CODI_SAI_PIM | integer(4) |  | S | Código da nota fiscal de saída |
| NUMERO_DARE_PIM | varchar(19) |  | S | Número DARE |
| DESCRICAO_COMPLEMENTAR_PIM | varchar(256) |  | S | Descrição complementar |
| ORGAO_ARRECADADOR | varchar(512) |  |  | Orgão arrecadador |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| PERIODO | date(4) |  | S | Período |
| NUMERO_SAT_DARE | varchar(15) |  | S | Número S@T DARE |
| TIPO_INSCRICAO | integer(4) |  | S | Tipo da inscrição do fornecedor |
| INSCRICAO | char(14) |  | S | Inscrição do fornecedor |
| I_PARCELAMENTO | integer(4) | PK |  | Sequencial do parcelamento |
| I_PARCELAMENTO_PARCELA_PARCELAMENTO | integer(4) | PK |  | Sequencial do parcelamento parcela |
| VALOR_PAGO_A_MAIOR | numeric(13) |  |  | Valor Pago a Maior |
| IMPOSTO_PARCELADO | char(1) | PK |  | Imposto parcelado |
| I_PARCELAMENTO_PARCELA_PARCELA | integer(4) | PK |  | Sequencial do parcelamento parcela parcela |
| NUMERO_DAR | varchar(13) |  |  | Número DAR |
| NUMERO_GUIA | varchar(14) |  |  | Número da guia |
| UF_FAVORECIDA | char(2) |  |  | Valor Pago |
| VERSAO_PAGAMENTO | integer(4) |  |  | Versão pagamento |
| TIPO | integer(4) |  |  | Tipo |
| VALOR_CORRECAO | numeric(13) |  |  | Valor da Correção |
| CODI_ENT | integer(4) |  | S | Código da nota fiscal de entrada |
| CODI_SAI | integer(4) |  | S | Código da nota fiscal de saída |
| TIPO_DOCUMENTO_ARRECADACAO | integer(4) |  | S | Tipo do Documento de Arrecadação |
| NUMERO_DOCUMENTO_ARRECADACAO | varchar(255) |  |  | Número do Documento de Arrecadação |
| I_CNO | integer(4) |  | S | Código CNO |
| VALOR_ENCARGOS_HONORARIOS | numeric(13) |  |  | Valor encargos/honorários |
| I_SCP | integer(4) |  | S | Código SCP |
| TIPO_NOTA | char(1) |  |  | Tipo Nota |
| VALOR_ACRESCIMO | numeric(13) |  |  | Valor Acrescimo |
| VALOR_DESCONTO | numeric(13) |  |  | Valor Desconto |
| I_PAGAMENTO_CONTA_AZUL | integer(4) |  |  | Sequencial Baixa parcial Conta Azul |
