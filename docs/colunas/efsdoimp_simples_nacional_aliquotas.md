# EFSDOIMP_SIMPLES_NACIONAL_ALIQUOTAS — Saldo dos Impostos - Alíquotas Simples Nacional
34.074 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| ANEXO | integer(4) | PK |  | Anexo |
| SECAO | integer(4) | PK |  | Seção |
| TABELA | integer(4) | PK |  | Tabela |
| ALIQUOTA_IRPJ | numeric(23) |  |  | Alíquota IRPJ |
| ALIQUOTA_CSLL | numeric(23) |  |  | Alíquota CSLL |
| ALIQUOTA_COFINS | numeric(23) |  |  | Alíquota COFINS |
| ALIQUOTA_PIS | numeric(23) |  |  | Alíquota PIS |
| ALIQUOTA_INSS | numeric(23) |  |  | Alíquota INSS |
| ALIQUOTA_ICMS | numeric(23) |  |  | Alíquota ICMS |
| ALIQUOTA_ISS | numeric(23) |  |  | Alíquota ISS |
| ALIQUOTA_TOTAL | numeric(23) |  |  | Alíquota Total |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador Único do registro no banco do Atendimento Onvio |
