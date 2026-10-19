# FOAVISOS_VENCIMENTO_AFASTAMENTOS — Avisos de vencimento de retorno de afastamentos.
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_AVISOSCONF | integer(4) | PK |  | Código do aviso de vencimento. |
| I_AFASTAMENTOS | integer(4) | PK |  | Tipo do afastamento referente a FOAFASTAMENTOS_TIPO |
| EXIBIR_AVISO | smallint(2) |  |  | Exibir aviso. (0=Não/1=Sim) |
| DIAS_ANTECEDENCIA | integer(4) |  | S | Dias de antecedência para exibir o aviso. |
