# lacsadex — Adicoes e Exclusoes da CS - Cadastro
22.800 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_aec | integer(4) | PK |  | Codigo da Adicao e Exclusao |
| desc_aec | char(140) |  |  | Descricao |
| orig_aec | char(1) |  | S | Origem do Dado (L=Lancado, C=Contabilidade) |
| adex_aec | char(1) |  |  | Adicao = A, Exclusao = E, Ganhos = G |
| regi_aec | tinyint(1) |  |  | Regime (1=Real, 2=Estimado, 3=Presumido) |
| padr_aec | tinyint(1) |  | S | Adicao ou Exclusao Padrao (1=Sim, 2=Nao) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codi_emp | integer(4) | PK |  | Empresa |
