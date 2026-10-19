# EFSDOIMP_POR_RECOLHIMENTO_POR_DATA — Saldo dos Impostos - Detalhamento dos Impostos por Código de Recolhimento - Por Data
2.557 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Imposto |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_SIM | date(4) | PK |  | Competencia |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| PERIODO | date(4) | PK |  | Período |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código do recolhimento |
| VALOR_CONTABIL_ENTRADA | numeric(13) |  |  | Valor Contábil Entrada |
| BASE_CALCULO_ENTRADA | numeric(13) |  |  | Base Cálculo Entrada |
| VALOR_IMPOSTO_ENTRADA | numeric(13) |  |  | Valor Imposto Entrada |
| VALOR_ISENTAS_ENTRADA | numeric(13) |  |  | Valor Isentas Entrada |
| VALOR_OUTRAS_ENTRADA | numeric(13) |  |  | Valor Outras Entrada |
| BASE_CALCULO | numeric(13) |  |  | Base Cálculo |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo Devedor |
| VALOR_A_RECOLHER | numeric(13) |  |  | Valor a Recolher |
| VALOR_DIFERIDO | numeric(13) |  |  | Valor Diferido |
| VALOR_DIFERIDO_ANTERIOR | numeric(13) |  |  | Valor Diferido Anterior |
| COMPENSACAO_PAGAMENTO_INDEVIDO_MAIOR | numeric(13) |  |  | Valor da Compensação de pagamento indevido ou a maior |
| RESSARCIMENTO_COMPENSACAO_PIS_COFINS | numeric(13) |  |  | Valor de Ressarcimento/Compensação de PIS/COFINS |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  |  | Data do vencimento |
| OUTRAS_COMPENSACOES | numeric(13) |  |  | Outras compensações |
