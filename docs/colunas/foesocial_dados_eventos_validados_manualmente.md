# FOESOCIAL_DADOS_EVENTOS_VALIDADOS_MANUALMENTE — Tabela com eventos que foram validados manualmente pelo sistema.
1.963 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do dado evento da tabela FOESOCIAL_DADOS_EVENTOS. |
| DATA_VALIDADO | date(4) |  |  | Data da validação. |
| NUMERO_RECIBO | varchar(64) |  |  | Número de Recibo validado. |
| DATA_INSERCAO | timestamp(8) |  |  | Data e hora da inserção do registro. |
| DATA_HORA_PROCESSAMENTO | timestamp(8) |  | S | Data e hora do processamento do registro. |
| STATUS | integer(4) |  |  | Status do processamento: 1 - Pendente, 2 - Concluido |
| USUARIO | varchar(16) |  |  | Nome do usuário que validou manualmente. |
