# EFSDOIMP_ESTADUAL_CE — Saldo dos Impostos - Estadual CE
129 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Valor Crédito Presumido Transporte |
| CREDITO_PRESUMIDO_SUINOS | numeric(13) |  |  | Valor Crédito Presumido Suínos |
| CREDITO_PRESUMIDO_SUINOS_ESTORNO_ENTRADAS | numeric(13) |  |  | Valor Crédito Presumido Suínos Estorno Entradas |
| CREDITO_PRESUMIDO_SUINOS_ESTORNO_DEVOLUCAO | numeric(13) |  |  | Valor Crédito Presumido Suínos Estorno Devolução |
| ESTORNO_SALDO_CREDOR_ESTIMATIVA_FIXA | numeric(13) |  |  | Estorno do saldo credor de ICMS - Art. 4º, § 3º da IN nº 15/2005 |
| PARCELA_MENSAL_ESTIMATIVA_FIXA | numeric(13) |  |  | Parcela mensal da Estimativa Fixa - Art. 805 do RICMS |
| CREDITO_ICMS_RECOLHIDO_ANTECIPADAMENTE | numeric(13) |  |  | Crédito ICMS recolhido antecipadamente |
| TRANSFERENCIA_SALDO_CREDITO_ART_59_OUTROS_DEBITOS | numeric(13) |  |  | Transferência de saldo credor - Art. 59-A do RICMS - Outros débitos |
| TRANSFERENCIA_SALDO_CREDITO_ART_59_OUTROS_CREDITOS | numeric(13) |  |  | Transferência de saldo credor - Art. 59-A do RICMS - Outros créditos |
| DEBITO_FECOP_ICMS | numeric(13) |  |  | FECOP-CE - Débitos pelas saídas |
| TRANSFERENCIA_CREDITO_ICMS_ACUMULADO_OUTROS_DEBITOS | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros débitos |
| TRANSFERENCIA_CREDITO_ICMS_ACUMULADO_OUTROS_CREDITOS | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros créditos |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
