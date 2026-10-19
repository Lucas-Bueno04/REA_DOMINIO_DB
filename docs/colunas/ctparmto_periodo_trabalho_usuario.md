# CTPARMTO_PERIODO_TRABALHO_USUARIO — Parametros - Período de trabalho por usuário
213 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PERIODO | integer(4) | PK |  | Sequencial |
| I_RESPONSAVEL | integer(4) |  |  | Código do responsável |
| RESPONSAVEL_TIPO | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
| ACAO | char(1) |  |  | Ação do período de trabalho (L=Livre, A=Avisar N=Não permitir) |
