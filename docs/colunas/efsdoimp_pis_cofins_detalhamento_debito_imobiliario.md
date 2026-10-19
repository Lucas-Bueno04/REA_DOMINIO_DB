# EFSDOIMP_PIS_COFINS_DETALHAMENTO_DEBITO_IMOBILIARIO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Débito Imobiliário
14 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| FILIAL | integer(4) | PK |  | Código da Filial |
| I_EMPREENDIMENTO | integer(4) | PK |  | Código do empreendimento |
| I_UNIDADE | integer(4) | PK |  | Código da unidade |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| VALOR_TOTAL_VENDA | numeric(13) |  |  | Valor total da unidade imobiliária vendida atualizado até o período da escrituração |
| VALOR_RECEBIDO_ACUMULADO | numeric(13) |  |  | Valor recebido acumulado até o mês anterior ao da escrituração |
| VALOR_TOTAL_RECEBIDO | numeric(13) |  |  | Valor total recebido no mês da escrituração |
| CST | integer(4) |  |  | Código da Situação Tributária |
| BASE_CALCULO | numeric(13) |  |  | Base de Cálculo |
| ALIQUOTA | numeric(12) |  |  | Alíquota |
| VALOR | numeric(13) |  |  | Valor |
| PERCENTUAL_RECEITA_RECEBIDA | numeric(13) |  |  | Percentual da receita total recebida até o mês |
| VALOR_CORRECAO | numeric(13) |  |  | Valor da correção |
| VALOR_JUROS | numeric(13) |  |  | Valor dos juros |
| VALOR_MULTA | numeric(13) |  |  | Valor da multa |
| VALOR_DESCONTO | numeric(13) |  |  | Valor do desconto |
| I_CONTRATO | integer(4) | PK |  | Código do contrato |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
