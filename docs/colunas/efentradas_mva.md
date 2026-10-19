# efentradas_mva — Notas Fiscais de Entradas - MVA
12.109 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Nota |
| codi_imp | integer(4) | PK |  | Imposto |
| sequencial | integer(4) | PK |  | Sequencial |
| aliquota | numeric(5) |  |  | Aliquota |
| valor_produto | numeric(13) |  |  | Valor do produto |
| mva | numeric(5) |  |  | Percentual MVA |
| reducao_mva | numeric(7) |  |  | Percentual de reducao do MVA |
| VALOR_CONTABIL | numeric(13) |  |  | Valor Contábil |
| MVA_FIDELIDADE | numeric(5) |  |  | Percentual MVA Fidelidade |
