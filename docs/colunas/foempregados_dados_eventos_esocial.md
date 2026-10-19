# FOEMPREGADOS_DADOS_EVENTOS_ESOCIAL — Tabela de relacionamento entre o cadastro de empregados e os registros de envio para o eSocial.
844 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_DADOS_EVENTOS | integer(4) | PK |  | Código do registro de envio. |
| STATUS_EXCLUSAO | smallint(2) |  |  | Status da exclusao dos eventos. (1=Não enviado/2=Enviado/3=Em Processamento/4=Invalidado) |
| CODI_EMP_ENVIO | integer(4) |  |  | Código da empresa do envio do evento. |
| I_EMPREGADOS_ENVIO | integer(4) |  |  | Código do empregado do envio do evento. |
| REENVIAR_DADOS_EVENTOS_EXCLUSAO | smallint(2) |  |  | Cria uma fila com o evento eSocial excluído para que a informação seja reenviada. |
