# FOVALORES_PAGAMENTO_AJUSTE_PARCELAMENTO_ESOCIAL — Valores do pagamento da alteração retroativa com parcelamento por competência retroativa.
6.502 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOS_DIFERENCA_OLD | integer(4) |  | S | Código do cálculo da diferença - Renomeado |
| I_PARCELA | integer(4) | PK |  | Código da parcela |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica |
| I_CALCULOS_AJUSTADO_OLD | integer(4) |  | S | Código do cálculo ajustado - Renomeado |
| COMPETENCIA_AJUSTADO | date(4) |  |  | Competência do cálculo ajustado |
| VALOR | numeric(13) |  |  | Valor |
| CODI_EMP_SERVICOS | integer(4) | PK |  | Código da empresa serviço |
| I_SERVICOS | integer(4) | PK |  | Código do serviço |
| RATEIO | integer(4) | PK |  | Rateio do serviço |
| RETROATIVO_CCT | smallint(2) |  |  | Retroativo CCT. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_RETENCAO_PAGAMENTO_ESOCIAL | smallint(2) |  |  | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |
| CONVERSAO | smallint(2) |  |  | Criado na conversão. (0=Não/1=Sim) |
| I_CALCULOS_AJUSTADO | uniqueidentifier(16) | PK |  | Código do cálculo ajustado |
| I_CALCULOS_DIFERENCA | uniqueidentifier(16) | PK |  | Código do cálculo da diferença |
