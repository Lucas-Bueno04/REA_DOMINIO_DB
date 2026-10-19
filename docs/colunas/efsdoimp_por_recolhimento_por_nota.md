# EFSDOIMP_POR_RECOLHIMENTO_POR_NOTA — Saldo dos impostos - detalhamento dos impostos por nota e por código de recolhimento
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=COMPLEMENTAR, 52=13SAL) |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código de recolhimento |
| CODIGO_NOTA | integer(4) | PK |  | Código da nota de entrada |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_RECOLHER | numeric(13) |  |  | Saldo a recolher |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do imposto |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  |  | Data do vencimento |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do código de recolhimento |
| CLASSE_VENCIMENTO | integer(4) |  |  | Classe do vencimento |
| VALOR_REGIME_ESPECIAL | numeric(13) |  |  | Valor regime especial |
| VALOR_CREDITO_PRESUMIDO | numeric(13) |  |  | Valor crédito presumido |
| VALOR_ESTORNO_REGIME_ESPECIAL | numeric(13) |  |  | Valor estorno regime especial |
| VALOR_ESTORNO_CREDITO_PRESUMIDO | numeric(13) |  |  | Valor estorno crédito presumido |
| VALOR_ISENTAS | numeric(13) |  |  | Valor isentas |
| VALOR_OUTRAS | numeric(13) |  |  | Valor outras |
| DEBITOS_SAIDAS | numeric(13) |  |  | Débitos pelas saídas |
| DEBITOS_ENTRADAS | numeric(13) |  |  | Débitos pelas entradas |
| CREDITOS_DEVOLUCOES_SAIDAS | numeric(13) |  |  | Créditos pelas devoluções de saídas |
| CREDITOS_DEVOLUCOES_ENTRADAS | numeric(13) |  |  | Créditos pelas devoluções de entradas |
| RESSARCIMENTO_ICMS_ST_ACOBERTADO_NFE | numeric(13) |  |  | Ressarcimento de ICMS Substituição Tributária acobertado por NF-e |
