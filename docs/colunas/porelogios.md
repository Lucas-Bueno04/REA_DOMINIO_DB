# porelogios — Cadastro de relogios
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_relogios | smallint(2) | PK |  |  |
| local | char(25) |  |  |  |
| marca | char(15) |  | S |  |
| tem_cabecalho | char(1) |  | S |  |
| registro | char(120) |  | S |  |
| tipo | char(1) |  |  |  |
| tipo_reg | char(1) |  |  |  |
| desp_car | char(1) |  |  |  |
| codi_ascii_desp | integer(4) |  | S |  |
| posic_desp | integer(4) |  | S |  |
| TIPO_IMPORTACAO | tinyint(1) |  |  | TIPO DE IMPORTACAO DE MARCACOES. 1 - PADRAO PORTARIA 1510 MTE/2 - PERSONALIZADO |
| NUMERO_FABRICACAO | varchar(17) |  |  | NUMERO DE FABRICACAO DO RELOGIO. |
