# EFSDOIMP_RECEITA_IMPOSTOS_MAJORACAO — Saldo dos Impostos - Receita Impostos Majoração
1.000 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Período |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| PERIODO_APURACAO | date(4) | PK |  | Período origem base majorada |
| ALIQUOTA_BASE_CALCULO_CSLL | numeric(7) | PK |  | Alíquota da base de cálculo CSLL |
| ALIQUOTA_BASE_CALCULO_IRPJ | numeric(7) | PK |  | Alíquota da base de cálculo IRPJ |
| ALIQUOTA_BASE_CALCULO_CSLL_EXCEDENTE | numeric(7) |  |  | Alíquota da base de cálculo CSLL excedente |
| ALIQUOTA_BASE_CALCULO_IRPJ_EXCEDENTE | numeric(7) |  |  | Alíquota da base de cálculo IRPJ excedente |
| VALOR_BASE_CALCULO | numeric(13) |  |  | Valor da base de cálculo |
| VALOR_BASE_CALCULO_NAO_EXCEDENTE | numeric(13) |  |  | Valor da base de cálculo não excedente |
| VALOR_BASE_CALCULO_EXCEDENTE | numeric(13) |  |  | Valor da base de cálculo excedente |
| VALOR_BASE_CALCULO_REDUZIDA_NAO_EXCEDENTE | numeric(13) |  |  | Valor da base de cálculo reduzida não Excedente |
| VALOR_BASE_CALCULO_REDUZIDA_EXCEDENTE | numeric(13) |  |  | Valor da base de cálculo reduzida excedente |
| VALOR_CREDITO_LIMITE_TRIMESTRAL | numeric(13) |  |  | Valor da base de cálculo reduzida excedente |
| VALOR_BASE_CALCULO_EXCEDENTE_COM_ALIQUOTA | numeric(13) |  |  | Valor da base de cálculo excedente com alíquota do imposto aplicada |
