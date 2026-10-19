# HRADIANTAMENTO — Adiantamentos
158 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_ADIANTAMENTO | integer(4) | PK |  | Codigo |
| I_MOVIMENTO_CLIENTE | integer(4) |  |  | Conta corrente cliente |
| I_MOVIMENTO_CLIENTE_SEQ | integer(4) |  |  | Conta corrente cliente sequencial |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  |  | Conta corrente escritorio |
| I_CLIENTE | integer(4) |  |  | Cliente |
| DATA_ADIANTAMENTO | date(4) |  |  | Data |
| VALOR | numeric(13) |  |  | Valor |
| I_CONTA_FINANCEIRA | integer(4) |  |  | Conta financeira |
| I_HISTORICO | integer(4) |  | S | Codigo do historico |
| HISTORICO | varchar(512) |  |  | Historico |
| SOMENTE_EVENTO_CATEGORIA | char(1) |  |  | Somente eventos com categoria S N |
| I_CATEGORIA_RECEBER | integer(4) |  | S | Categoria |
| INCLUIR_EVENTO_DEPOIS | char(1) |  |  | Incluir eventos cadastrados depois do adiantamento S N |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ORIGEM | char(1) |  |  | Origem(M - Manual/R - Recebimento) |
