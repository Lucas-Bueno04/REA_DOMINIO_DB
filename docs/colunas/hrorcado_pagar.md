# HRORCADO_PAGAR — Lancamentos orcados de contas a pagar
20 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_ORCADO_PAGAR | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(60) |  |  | Descricao |
| I_CATEGORIA_PAGAR | integer(4) |  |  | Categoria |
| I_FORNECEDOR | integer(4) |  | S | Possivel fornecedor |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Possivel conta para pagamento |
| VALOR | numeric(13) |  |  | Valor |
| VENCIMENTO | date(4) |  |  | Vencimento |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
