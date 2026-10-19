# FOEMPREGADOS_ATESTADOS_OCUPACIONAIS_RESULTADO_MONITORACAO_BIOLOGICA — Resultados da monitoração biológica.
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_ATESTADO_OCUPACIONAL | integer(4) | PK |  | Código sequencial do atestado ocupacional. |
| I_RESULTADO_MONITORACAO_BIOLOGICA | integer(4) | PK |  | Código sequencial do resultado da monitoração biológica. |
| DATA_INICIO | date(4) |  |  | Data de início da monitoração biológica |
| DATA_FIM | date(4) |  | S | Data final da monitoração biológica |
| CODIGO_AGENTE_QUIMICO | varchar(5) |  | S | Código do agente químico. |
| MATERIAL_BIOLOGICO_ANALISE | smallint(2) |  |  | Material biológico para análise. (1=Urina/2=Sangue) |
| CODIGO_ANALISE_EFETUADA | varchar(5) |  | S | Código da análise efetuada. |
| EXPOSICAO_EXCESSIVA | smallint(2) |  |  | Exposição excessica. (0=Não/1=Sim) |
| ORDEM_EXAME | smallint(2) |  |  | Ordem do exame. (1=Referencial/2=Sequencial) |
| INDICACAO_RESULTADO | smallint(2) |  | S | Indicação do resultado. (1=Normal/2=Alterado/3=Estável/4=Agravamento/5=Ocupacional/6=Não ocupacional) |
| NATUREZA_EXAME | varchar(50) |  | S | Natureza do exame. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. layout/2=Imp. tabelas/3=Conversão) |
| INTERPRETACAO_EXAME | smallint(2) |  |  | Interpretação do exame. (1=EE/2=SC/3=SC+) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
