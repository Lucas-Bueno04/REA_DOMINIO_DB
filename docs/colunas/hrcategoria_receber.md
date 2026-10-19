# HRCATEGORIA_RECEBER — Categorias contas a receber
84 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CATEGORIA_RECEBER | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(60) |  |  | Descricao |
| TIPO | char(1) |  |  | Tipo T Totalizadora N Nao totalizadora |
| SUBORDINADA_RECEBER | integer(4) |  | S | Subordinado a |
| CLASSIFICACAO | char(1) |  |  | Classificacao R Receitas O Outras receitas I Impostos T Taxas U Outros |
| CONSIDERAR_CONTRATO | char(1) |  |  | Considerar para o fluxo de caixa projetado contratos S N |
| CONSIDERAR_ADICIONAL | char(1) |  |  | Considerar para o fluxo de caixa projetado adicional anual S N |
| CONSIDERAR_FIXO | char(1) |  |  | Considerar para o fluxo de caixa projetado lancamentos de eventos fixos S N |
| CONSIDERAR_MENSAL | char(1) |  |  | Considerar para o fluxo de caixa projetado lancamentos de eventos mensais S N |
| CONSIDERAR_ORCADO | char(1) |  |  | Considerar para o fluxo de caixa projetado lancamentos orcados S N |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CONTA_CREDITO | integer(4) |  | S | Código da conta crédito |
| HISTORICO_CREDITO | integer(4) |  | S | Código do histórico de crédito |
