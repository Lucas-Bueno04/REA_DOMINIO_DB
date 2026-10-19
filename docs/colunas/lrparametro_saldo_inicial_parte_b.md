# LRPARAMETRO_SALDO_INICIAL_PARTE_B — Parâmetros Lalur - Saldo inicial Parte B
16 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SALDO | integer(4) | PK |  | Sequencial |
| I_SCP | integer(4) |  | S | SCP |
| I_PARTE_B | integer(4) |  |  | Conta parte B |
| VALOR | numeric(13) |  |  | Valor |
| HISTORICO | varchar(250) |  |  | Histórico |
| TIPO | char(1) |  |  | Tipo (C = Credor / D = Devedor) |
