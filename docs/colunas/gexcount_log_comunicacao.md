# GEXCOUNT_LOG_COMUNICACAO — XCOUNT - Log de Comunicação
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_SEQUENCIAL | integer(4) | PK |  | Código sequencial de erros |
| USUARIO | varchar(128) |  |  | Usuário |
| VERSAO_SISTEMA | varchar(40) |  |  | Versão do sistema |
| ATUALIZACAO | integer(4) |  |  | Arquivo de atualização |
| VERSAO_BANCO | integer(4) |  |  | Versão do banco de dados |
| DATA_HORA | timestamp(8) |  |  | Data e Hora do erro |
| PROCESSO_CONTABIL | integer(4) |  |  | Código do processo no contábil |
| XCOUNT_ID_PROCESSO | varchar(20) |  |  | ID do processo na XCOUNT |
| XCOUNT_PROCESSO_VALIDADO | char(1) |  |  | Indica se o token obtido foi validado e utilizado |
| XCOUNT_MOTIVO_NAO_REPORTADO | char(1) |  |  | Motivo do token não ser reportado(I-Invalidado, T-Tempo, E-Erro de comunicação) |
