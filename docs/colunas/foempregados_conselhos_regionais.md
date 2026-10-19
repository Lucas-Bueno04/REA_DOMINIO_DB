# FOEMPREGADOS_CONSELHOS_REGIONAIS — Cadastro de Empregados - Conselhos Regionais
936 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| I_CONSELHO_REGIONAL | integer(4) | PK |  | Código do conselho regional |
| CONSELHO | char(14) |  |  | Conselho |
| NUMERO_REGISTRO | char(14) |  | S | Número do registro |
| REGIAO | char(14) |  | S | Região |
| DATA_EXPEDICAO | date(4) |  | S | Data de expedição |
| DATA_VALIDADE | date(4) |  | S | Data de validade |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| CODIGO_UF | integer(4) |  | S | Código da UF. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
