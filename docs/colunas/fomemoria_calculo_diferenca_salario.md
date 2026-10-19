# FOMEMORIA_CALCULO_DIFERENCA_SALARIO — MEMÓRIA DE CÁLCULO DE DIFERENÇA DE SALÁRIO
53.380 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | CÓDIGO DO CÁLCULO DA DIFERENÇA - Renomeado |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | CÓDIGO DO CÁLCULO AJUSTADO - Renomeado |
| CODI_EMP | integer(4) |  |  | CÓDIGO DA EMPRESA |
| I_EVENTOS | integer(4) | PK |  | CÓDIGO DO EVENTO |
| VALOR | numeric(13) |  |  | VALOR DO EVENTO AJUSTADO |
| I_FORMA_AJUSTE_PARCELAMENTO | integer(4) |  | S | Código da forma de ajuste conforme parcelamento. |
| I_SERVICOS | integer(4) | PK |  | Serviço. |
| RATEIO | smallint(2) | PK |  | Rateio. |
| CONSIDERAR_REMUNERACAO_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_RETENCAO_PAGAMENTO_ESOCIAL | smallint(2) |  |  | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |
| DIFERENCA_CCT_ESOCIAL | integer(4) |  | S | Rubrica referente a Convenção Coletiva de Trabalho para o eSocial (0-Não/1-Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_PAGAMENTO_ADICIONAL_MP_927_OLD | integer(4) |  | S | Código do cálculo do pagamento do adicional MP 927 - Renomeado |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | CÓDIGO DO CÁLCULO AJUSTADO |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | CÓDIGO DO CÁLCULO DA DIFERENÇA |
| I_CALCULOS_PAGAMENTO_ADICIONAL_MP_927 | uniqueidentifier(16) |  | S | Código do cálculo do pagamento do adicional MP 927 |
