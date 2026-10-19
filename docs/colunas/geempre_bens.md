# geempre_bens — Empresa - Bens
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| sequencial | integer(4) | PK |  | Sequencial |
| classificacao | char(1) |  |  | Classificacao |
| tipo | char(1) |  | S | Tipo (U - Urbano/R - Rural) |
| descricao | char(100) |  | S | Descricao |
| localizacao | char(100) |  | S | Localizacao |
| valor | numeric(13) |  | S | Valor do bem |
| area | numeric(13) |  | S | Area (em m2 ou HA) |
| area_construida | numeric(13) |  | S | Area construida em m2 |
| onus | char(1) |  | S | Onus (S/N) |
| tipo_onus | char(1) |  | S | Tipo de Onus ( P - Penhora/H - Hipoteca) |
| valor_onus | numeric(13) |  | S | Valor do onus |
| credor | char(40) |  | S | Credor |
| matricula | char(20) |  | S | Matricula |
| cartorio | char(30) |  | S | Cartorio |
| data_matricula | date(4) |  | S | Data da matricula |
| livro | char(10) |  | S | Numero do livro |
| folha | char(10) |  | S | Numero da folha |
| cessao | char(1) |  | S | Cessao (S/N) |
| impenhoravel | char(1) |  | S | Bem impenhoravel (S/N) |
| rural_enquadrado | char(1) |  | S | Imovel rural enquadrado(S/N) |
| marca | char(30) |  | S | Marca |
| ano | integer(4) |  | S | Ano |
| alienado | char(1) |  | S | Alienado(S/N) |
| vencimento | date(4) |  | S | Vencimento final |
| leasing | char(1) |  | S | Leasing (S/N) |
| empresa | char(30) |  | S | Empresa do leasing |
| data_contrato | date(4) |  | S | Data do contrato de leasing |
