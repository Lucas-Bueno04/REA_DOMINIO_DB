# FOMEMORIA_CALCULO_DIFERENCA_SALARIAL_CCT_ESOCIAL — Memória de cálculo do cálculo de diferença salarial CCT com algumas considerações do eSocial
1.678 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | Código do cálculo ajustado - Renomeado |
| I_EVENTOS | integer(4) | PK |  | Código do evento |
| I_SERVICOS | integer(4) | PK |  | Serviço. |
| RATEIO | smallint(2) | PK |  | Rateio. |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| VALOR | numeric(30) |  |  | Valor do evento ajustado |
| CONSIDERAR_REMUNERACAO_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração do esocial. (0=Não/1=Sim) |
| CONSIDERAR_RETENCAO_PAGAMENTO_ESOCIAL | smallint(2) |  |  | Considerar para a retenção de pagamentos do esocial. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração para compor liquido evento s-1210 do esocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | Código do cálculo ajustado |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
