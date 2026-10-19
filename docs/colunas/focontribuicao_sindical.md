# FOCONTRIBUICAO_SINDICAL — Tabela de valores de contribuições sindicais
1.260 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTRIBUICAO_SINDICAL_OLD | integer(4) |  | S | Código da contribuição sindical - Renomeado |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| I_FILIAIS | integer(4) |  |  | Código da filial |
| COMPETENCIA | date(4) |  |  | Competência da contribuição |
| TIPO_PROCESS | smallint(2) |  |  | Tipo do processo (11=Mensal/42=Complementar/52=13º salário integral) |
| TIPO | smallint(2) |  |  | Tipo da contribuição. (1=Sindical/2=Associativa/3=Assistencial/4=Confederativa/5=Patronal/6=Assistencial empresa) |
| VALOR | numeric(13) |  |  | Valor da contribuição |
| VENCIMENTO | date(4) |  | S | Data de vencimento |
| I_PAGTO | integer(4) |  | S | Código do pagamento |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CONTRIBUICAO_SINDICAL | uniqueidentifier(16) | PK |  | Código da contribuição sindical |
| I_CONTRIBUICAO_SINDICAL_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Coluna utilizada durante o exporta/importa |
