# FOMONITORAMENTO_SAUDE_TRABALHADOR — Monitoramento da Saúde do Trabalhador.
198 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial. |
| DATA_ASO | date(4) |  |  | Data do ASO. |
| TIPO_ASO | smallint(2) |  |  | Tipo do ASO (1=Admissional/2=Periódico, conforme NR 07 ou planejamento do PCMSO/3=De retorno ao trabalho/4=De mudança de função/5=De monitoração pontual, não enquadrado nos demais casos/6=Demissional). |
| RESULTADO | smallint(2) |  |  | Resultado (1=Apto/2=Inapto). |
| VENCIMENTO_ASO | date(4) |  | S | Data de vencimento do ASO |
| I_MEDICOS_EMITENTE_ASO | integer(4) |  |  | Código do médico emitente do ASO. |
| I_MEDICOS_PCMSO | integer(4) |  | S | Código do médico PCMSO. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| ENVIAR_ESOCIAL_PERIODO_ANTERIOR_INICIO_BANCO_CONTABIL | smallint(2) |  | S | Enviar evento eSocial anterior ao início da utilização do banco de dados (0=Não/1=Sim) |
