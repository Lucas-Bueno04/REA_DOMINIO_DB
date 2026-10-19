# lairadex — Adicoes e Exclusoes do IR - Cadastro
27.360 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_aei | integer(4) | PK |  | Codigo Adicao ou Exclusao |
| desc_aei | char(140) |  |  | Descricao |
| adex_aei | char(1) |  |  | Tipo (A=Adicao, E=Exclusao) |
| regi_aei | tinyint(1) |  |  | Regime (1=Real, 2=Estimado, 3=Presumido) |
| padr_aei | tinyint(1) |  | S | Conta Padrao (1=Sim, 2=Nao) |
| codi_ctb | integer(4) |  | S | Conta da Contabilidade |
| orig_aei | char(1) |  | S | Origem (L=Lancado, C=Contabilidade) |
| codi_gru | integer(4) |  | S | Grupo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codi_emp | integer(4) | PK |  | Empresa |
