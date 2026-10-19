# LRPARAMETRO_SALDO_INICIAL_BASE_NEGATIVA — Parâmetros Lalur - Saldo inicial Base Negativa CSLL
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SALDO | integer(4) | PK |  | Sequencial |
| I_SCP | integer(4) |  | S | SCP |
| I_BASE_NEGATIVA | integer(4) |  |  | Conta Base Negativa |
| VALOR | numeric(13) |  |  | Valor |
| HISTORICO | varchar(250) |  |  | Histórico |
| TIPO | char(1) |  |  | Tipo (C = Credor / D = Devedor) |
