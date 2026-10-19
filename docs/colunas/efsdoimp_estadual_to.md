# EFSDOIMP_ESTADUAL_TO — Saldo dos Impostos - Estadual TO
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Imposto |
| CODI_EMP | integer(4) | PK |  | Empresa |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_ATACADISTA_ST_SUL_SUDESTE | numeric(13) |  |  | Crédito Presumido Atacadista ST Sul e Suldeste |
| CREDITO_PRESUMIDO_ATACADISTA_ST_DEMAIS_ESTADOS | numeric(13) |  |  | Crédito Presumido Atacadista ST Demais Estados |
| DEVOLUCAO_CREDITO_PRESUMIDO_ATACADISTA_ST_SUL_SUDESTE | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST Sul e Suldeste |
| DEVOLUCAO_CREDITO_PRESUMIDO_ATACADISTA_ST_DEMAIS_ESTADOS | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST Demais Estados |
| DEVOLUCAO_CREDITO_PRESUMIDO_ATACADISTA_ST | numeric(13) |  |  | Devolução Crédito Presumido Atacadista ST |
| CREDITO_PRESUMIDO_75_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 75% - Lei Nº 1.201/2000, Art. 1º, I |
| CREDITO_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| CREDITO_EXCLUSAO_SIMPLES_NACIONAL | numeric(13) |  |  | Crédito Exclusão Simples Nacional |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| SALDO_INFERIOR_QUANT_MINIMA_RECOLHIMENTO_SST | numeric(13) |  |  | Saldo inferior a quantidade mínima para recolhimento |
| SALDO_ANT_INFERIOR_QUANT_MINIMA_RECOLHIMENTO_SST | numeric(13) |  |  | Saldo anterior inferior a quantidade mínima para recolhimento |
| CREDITO_PRESUMIDO_70_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 70% sobre o ICMS apurado |
| CREDITO_PRESUMIDO_ATACADISTA_OP_INTERNAS | numeric(13) |  |  | Crédito presumido nas operações internas de comércio atacadista - Lei Nº 1.201/2000, Art. 1º, I |
| CREDITO_PRESUMIDO_ATACADISTA_OP_INTERESTADUAIS | numeric(13) |  |  | Crédito presumido nas operações interestaduais de comércio atacadista - Lei Nº 1.201/2000, Art. 1º, I |
| CREDITO_PRESUMIDO_ATACADISTA_ESTORNO_CREDITO | numeric(13) |  |  | Estorno de crédito operações comércio atacadista - Lei 1.201/00, Art. 1º, I |
| CREDITO_PRESUMIDO_50_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 50% - Lei Nº 1.201/2000, Art. 1º, III |
| CREDITO_PRESUMIDO_80_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 80% - Lei Nº 1.201/2000, Art. 1º, I |
| CREDITO_PRESUMIDO_80_III_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 80% - Lei Nº 1.201/2000, Art. 1º, III |
| CREDITO_PRESUMIDO_75_III_ICMS_APURADO | numeric(13) |  |  | Crédito presumido de 75% - Lei Nº 1.201/2000, Art. 1º, III |
| CREDITO_PRESUMIDO_20_TRANSPORTADORA_CONVENIO_ICMS_106_96 | numeric(13) |  |  | Crédito presumido de 20% para transportadoras -  Art. 9º, III do RICMS |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_CREDITO_PRESUMIDO_TRANSPORTE_CTE_CTEOS_SUBSTITUTO | numeric(13) |  |  | Estorno de crédito presumido transportes - Operações com CT-e e/ou CT-eOS substituto |
| CREDITO_PRESUMIDO_LEI_1790_2007_OP_INTERESTADUAIS | numeric(13) |  |  | Crédito presumido op. interestaduais comércio atacadista - Lei 1.790/2007, Art. 1º, I |
| CREDITO_PRESUMIDO_LEI_1790_2007_OP_INTERNAS | numeric(13) |  |  | Crédito presumido op. Internas comércio atacadista - Lei 1.790/2007, Art. 1º, I |
| CREDITO_PRESUMIDO_LEI_1790_2007_ESTORNO_CREDITO | numeric(13) |  |  | Estorno de crédito operações comércio atacadista - Lei Nº 1.790/2007, Art. 1º, §7º |
