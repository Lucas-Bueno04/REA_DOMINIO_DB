# EFSDOIMP_ESTADUAL_AM — Saldo dos Impostos - Estadual AM
56 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| DEBITO_RECEBIDO | numeric(13) |  |  | Débito Recebido |
| CREDITO_RECEBIDO | numeric(13) |  |  | Crédito Recebido |
| DEBITO_TRANSFERIDO | numeric(13) |  |  | Débito Transferido |
| CREDITO_TRANSFERIDO | numeric(13) |  |  | Crédito Transferido |
| PARCELA_MENSAL_ESTIMATIVA | numeric(13) |  |  | Parcela Mensal Estimativa |
| SALDO_A_TRANSPORTAR_ESTIMATIVA | numeric(13) |  |  | Saldo a Transportar Estimativa |
| SALDO_ANTERIOR_ESTIMATIVA | numeric(13) |  |  | Saldo Anterior Estimativa |
| CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 20, V do RICMS/AM |
| BASE_CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | numeric(13) |  |  | Base Crédito presumido de 20% para transportadoras - Art. 20, V do RICMS/AM |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
