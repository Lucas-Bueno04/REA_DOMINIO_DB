# EFSDOIMP_ESTADUAL_PA — Saldo dos Impostos - Estadual PA
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS |
| CREDITO_PRESUMIDO_TRANSPORTE_CT_CONV_106 | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS - Conhecimento de transporte |
| CREDITO_PRESUMIDO_TRANSPORTE_BP_CONV_106 | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 7, Anexo IV do RICMS - Bilhete de passagem |
| VALOR_TAXA_SERVICO_ARRECADACAO_DAE | numeric(13) |  |  | Valor Taxa serviço arrecadação DAE |
| MERCADORIAS_SUJEITAS_ANTECIP_OPER_INTER | numeric(13) |  |  | Mercadorias sujeitas à Antecip. nas Operaç. Interestaduais - Art. 115, An I, RICMS |
| TRANSFERENCIA_CREDITO_ICMS_ACUMULADO_OUTROS_DEBITOS | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros débitos |
| TRANSFERENCIA_CREDITO_ICMS_ACUMULADO_OUTROS_CREDITOS | numeric(13) |  |  | Transferência de crédito de ICMS acumulado - Outros créditos |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e e/ou CT-eOS substituto |
| CREDITO_PRESUMIDO_SAIDA_INTERNA_CESTA_BASICA_ART126 | numeric(13) |  |  | Crédito Presumido saída interna produtos cesta básica - Art. 126 do RICMS |
