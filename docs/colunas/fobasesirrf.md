# fobasesirrf — Bases de IRRF
683.502 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_BASESIRRF_OLD | integer(4) |  | S | Numero sequencial que identifica a base - Renomeado |
| tipo | integer(4) |  |  | Tipo da base |
| classificacao | integer(4) |  |  | Classificacao da base de irrf(normal, 13o., dif 13o. etc...) |
| data_pagto | date(4) |  |  | Data de pagamento |
| base | numeric(13) |  |  | Base de IRRF |
| base_desc_lei | numeric(13) |  |  | Desconto por lei de R$100,00 usado no periodo de 2004 |
| abatimentos | numeric(13) |  |  | Abatimentos da base (Inss, pensao...) |
| depend_no | integer(4) |  |  | Numero de dependentes |
| depend_desconto | numeric(13) |  |  | Valor total descontado por causa dos dependentes |
| taxa | numeric(13) |  |  | Taxa |
| valor | numeric(13) |  |  | Valor de irrf do calculo |
| deducao | numeric(13) |  |  | Deducoes do valor(valor da tabela de calculo) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| I_BASESIRRF_EXPIMP_OLD | integer(4) |  | S | Renomeado |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| TIPO_DEDUCAO | integer(4) |  |  | Tipo de dedução IRRF (1=Deduções Legais/2=Dedução Simplificada Mensal) |
| DEDUCAO_SIMPLIFICADA | numeric(13) |  | S | Valor da dedução simplificada. |
| I_BASESIRRF | uniqueidentifier(16) | PK |  | Numero sequencial que identifica a base |
| BASESIRRF_DATA_HORA | timestamp(8) |  | S | Data e hora da gravação da base |
| I_BASESIRRF_EXPIMP | uniqueidentifier(16) |  | S | Identificador único exp/imp |
| REDUCAO | numeric(13) |  | S | Valor de redução. |
