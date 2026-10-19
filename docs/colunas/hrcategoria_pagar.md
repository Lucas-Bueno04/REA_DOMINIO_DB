# HRCATEGORIA_PAGAR — Categorias de contas a receber
201 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CATEGORIA_PAGAR | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(60) |  |  | Descricao |
| TIPO | char(1) |  |  | Tipo T Totalizadora N Nao totalizadora |
| SUBORDINADA_PAGAR | integer(4) |  | S | Subordinado a |
| CONTA_DESPESA | integer(4) |  |  | Conta de despesa |
| HISTORICO_CONTABIL | integer(4) |  |  | Historico |
| GERA_LANCAMENTO | char(1) |  |  | Gerar lancamentos na conta do fornecedor para lancamentos de contas a pagar a vista |
| I_FORNECEDOR | integer(4) |  | S | Fornecedor |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira para pagamento |
| CONSIDERAR_FLUXO_CAIXA | char(1) |  |  | Considerar para o fluxo de caixa projetado S N |
| LANCAMENTO_FLUXO_CAIXA | char(1) |  |  | Considerar para o fluxo de caixa projetado lancamentos C Contas a pagar O Orcados |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
