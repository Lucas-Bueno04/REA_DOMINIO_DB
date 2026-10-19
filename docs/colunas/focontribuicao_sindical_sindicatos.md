# FOCONTRIBUICAO_SINDICAL_SINDICATOS — Tabela de valores de contribuições sindicais por sindicato
1.424 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTRIBUICAO_SINDICAL_OLD | integer(4) |  | S | Código da contribuição sindical - Renomeado |
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato |
| VALOR | numeric(13) |  |  | Valor da contribuição |
| VENCIMENTO | date(4) |  | S | Data de vencimento |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CONTRIBUICAO_SINDICAL | uniqueidentifier(16) | PK |  | Código da contribuição sindical |
