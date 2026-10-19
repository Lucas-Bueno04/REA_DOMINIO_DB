# FOFILIAIS_SINDICATOS_PATRONAIS — Filiais/Contribuição Sindical Patronal - Cadastro
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_FILIAIS | integer(4) | PK |  | Código da filial |
| I_SINDICATOS_P | integer(4) | PK |  | Código do sindicato patronal |
| CAPITAL_SOCIAL | numeric(13) |  | S | Capital social |
| CNAE | double(8) |  | S | CNAE |
| CNAE20 | char(15) |  | S | CNAE 2.0 |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
| NUMERO_ALUNOS | numeric(11) |  | S | Número de alunos. |
| RECEITA_BRUTA | numeric(15) |  | S | Receita bruta. |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
