# efmovacu — Outros Movimentos - Impostos Calculados
171 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_acu | integer(4) |  |  | Acumulador |
| data_mac | date(4) |  |  | Data |
| vlor_mac | numeric(13) |  |  | Valor |
| oper_mac | integer(4) |  |  | Operacao |
| obse_mac | varchar(60) |  | S | Observacao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ganhos_mac | tinyint(1) |  | S | Ganhos/Lucros e Aplicações Financeiras |
| dacon_origem_mac | char(1) |  | S | Origem das receitas/despesas (I-interna/E-externa) |
| IMPOSTO_PATRIMONIO_MAC | numeric(13) |  | S | Valor do imposto gerado no patrimônio |
| CODI_MAC | integer(4) | PK |  | Codigo |
| TIPO_CREDITO_MAC | integer(4) |  | S | Tipo de crédito do PIS e COFINS |
| MOVIMENTO_PATRIMONIO_MAC | char(1) |  |  | Movimento efetuado pelo Patrimonio (S/N) |
| CODIGO_MUNICIPIO | integer(4) |  | S | Município |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| CODI_PDI_VINCULADO_DEDUCAO | char(14) |  | S | Produto vinculado a dedução |
