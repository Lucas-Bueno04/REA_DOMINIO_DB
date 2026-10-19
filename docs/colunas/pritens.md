# prItens — Itens - Cadastro
356 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_ite | integer(4) | PK |  | Codigo |
| desc_ite | char(40) |  |  | Descricao |
| impo_ite | char(1) |  |  | Tipo (I=Imposto, L=Livro, O=Outro) |
| cimp_esc | integer(4) |  | S | Imposto |
| peri_ite | char(2) |  | S | Periodicidade (M=Mensal, 1Q=1aQ, 2Q=2aQ, 1D=1oD, 2D=2oD, 3D=3oD, 1T=1oT, 2T=2oT, 3T=3oT, 4T=4oT) |
| reto_ite | char(1) |  | S | Deve Retornar (S=Sim, N=Nao) |
| depe_ite | char(1) |  | S | Depende de Sistema (S=Sim, N=Nao) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
