# EFSDOIMP_PIS_COFINS_DETALHAMENTO_RETENCAO — Saldo do Impostos - Detalhamentos do PIS/COFINS - Retenções
20.569 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| NATUREZA_RETENCAO | integer(4) | PK |  | Natureza da retenção |
| PERIODO_APURACAO | date(4) | PK |  | Período de apuração da retenção |
| VALOR_DISPONIVEL | numeric(13) |  |  | Valor disponível |
| VALOR_UTILIZADO | numeric(13) |  |  | Valor utilizado |
| VALOR_A_TRANSPORTAR | numeric(13) |  |  | Valor a transportar |
| VALOR_RESTITUICAO | numeric(13) |  |  | Valor da retenção da restituição - Restituição, Ressarcimento e Compensação |
| VALOR_COMPENSACAO | numeric(13) |  |  | Valor da retenção da compensação - Restituição, Ressarcimento e Compensação |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| SALDO_RECEBIDO_POR_TRANSFERENCIA | numeric(13) |  |  | Saldo Recebido por Transferência |
| SALDO_ENVIADO_POR_TRANSFERENCIA | numeric(13) |  |  | Saldo Enviado por Transferência |
| VALOR_POSTERGADO | numeric(13) |  |  | Valor Postergado |
| VALOR_TOTAL_RETENCAO_MES | numeric(13) |  |  | Valor Total das Retenções no Mês |
| VALOR_DEVOLUCOES_VENDAS | numeric(13) |  |  | Valor de devoluções de vendas |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
