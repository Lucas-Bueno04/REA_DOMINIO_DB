# FOPAGAMENTOS_AJUSTE_PARCELAMENTO — Pagamentos das diferenças do ajuste conforme parcelamento
526 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_PARCELA | integer(4) | PK |  | Índice da parcela |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  |  | Código da forma de ajuste conforme parcelamento. |
| CODI_EMP_DIFERENCA | integer(4) |  |  | Código da empresa onde foi calculada a diferença. |
| I_EMPREGADOS_DIFERENCA | integer(4) |  |  | Código do empregado onde foi calculada a diferença. |
| COMPETENCIA | date(4) |  |  | Competência |
| TIPO_FOLHA | smallint(2) |  |  | Tipo da folha: (11=Mensal, 42=Complementar) |
| I_CALCULOS_COMPLEMENTOS_OLD | integer(4) |  | S | Complemento de cálculo onde será paga a parcela - Renomeado |
| I_CALCULOS_PAGAMENTO_OLD | integer(4) |  | S | Código do cálculo do pagamento da parcela - Renomeado |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
| I_CALCULOS_PAGAMENTO | uniqueidentifier(16) |  | S | Código do cálculo do pagamento da parcela. |
| I_CALCULOS_COMPLEMENTOS | uniqueidentifier(16) |  | S | Complemento de cálculo onde será paga a parcela. |
