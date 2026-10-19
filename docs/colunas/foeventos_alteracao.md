# FOEVENTOS_ALTERACAO — Tabela de alterações.
1.331.191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa do evento. |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| NOME | varchar(50) |  |  | Nome da rubrica. |
| PROV_DESC | char(2) |  |  | Tipo rubrica. |
| TAXA | numeric(7) |  | S | **SEM USO** |
| SOMA_ADICIONAL_AVISO_PREVIO | smallint(2) |  | S | **SEM USO** |
| COMP_13FER | char(1) |  | S | **SEM USO** |
| SOMA_MEDIA_AVISO_PREVIO | smallint(2) |  | S | **SEM USO** |
| SOMA_MED_13 | char(1) |  | S | **SEM USO** |
| SOMA_MED_FER | char(1) |  | S | **SEM USO** |
| BASE_RDSR | char(1) |  | S | **SEM USO** |
| DESCONTA_DSR | smallint(2) |  | S | **SEM USO** |
| SOMA_MEDIA_LICENCA_PREMIO | smallint(2) |  | S | **SEM USO** |
| SOMA_ADICIONAL_LICENCA_PREMIO | smallint(2) |  | S | **SEM USO** |
| TIPO_VALOR_CONSIDERAR_CALCULO_MEDIAS | smallint(2) |  | S | **SEM USO** |
| DETALHAR_LANCAMENTO_POR_SERVICO | smallint(2) |  | S | **SEM USO** |
| NATUREZA_FOLHA_MENSAL | integer(4) |  | S | Natureza do evento para folha mensal. |
| NATUREZA_13_INTEGRAL | integer(4) |  | S | Natureza do evento para 13° integral. |
| CODIGO_INCIDENCIA_IRRF_ESOCIAL | integer(4) |  |  | Código da incidências do IRRF para o eSocial. |
| CODIGO_INCIDENCIA_INSS_ESOCIAL | integer(4) |  |  | Código da incidências do INSS para o eSocial. |
| CODIGO_INCIDENCIA_FGTS_ESOCIAL | integer(4) |  | S | Código da incidências do FGTS para o eSocial. |
| CODIGO_INCIDENCIA_SINDICAL_ESOCIAL | integer(4) |  | S | Código da incidências sindical para o eSocial. |
| ENVIAR_ALTERACAO_ESOCIAL | smallint(2) |  |  | Alteração de informações que devem ser enviadas ao eSocial. |
| ALTERACAO_FASEAMENTO_ESOCIAL | smallint(2) |  | S | Alteração inserida pela troca de faseamento do eSocial. |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| UTILIZA_PARA_ESOCIAL_DOMESTICO | smallint(2) |  | S | **SEM USO** |
| CODIGO_ESOCIAL_DOMESTICO | varchar(15) |  | S | **SEM USO** |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| CODIGO_INCIDENCIA_RPPS_ESOCIAL | integer(4) |  | S | Código de incidência do RPPS para o eSocial. |
| CODIGO_INCIDENCIA_PIS_ESOCIAL | integer(4) |  | S | Código de incidência do PIS para o eSocial |
