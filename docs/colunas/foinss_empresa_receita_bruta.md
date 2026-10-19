# FOINSS_EMPRESA_RECEITA_BRUTA — INSS Empresa Receita Bruta
73 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) |  |  | Código da empresa |
| I_FILIAIS | integer(4) |  | S | Código da filial |
| COMPETENCIA | date(4) |  |  | Competência |
| VALOR_NAO_RELACIONADO | numeric(13) |  |  | Valor dos produtos não relacionados |
| VALOR_EXCLUSAO | numeric(13) |  |  | Valor das exclusões |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| I_INSS_EMPRESA_RECEITA_BRUTA | integer(4) | PK |  | Código sequencial |
| VALOR_AJUSTE_ACRESCIMO | numeric(13) |  |  | Valor de ajuste de acréscimo |
| VALOR_AJUSTE_REDUCAO | numeric(13) |  |  | Valor de ajuste de redução |
| VALOR_RELACIONADO | numeric(13) |  |  | Valor dos produtos relacionados. |
| PERCENTUAL_REDUCAO | numeric(13) |  |  | Valor do percentual de redução |
| DEMONSTRAR_REGISTRO_FOLHA | smallint(2) |  |  | Demonstrar registro na nova tela do módulo Folha. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
