# efincentivosmuni — Incentivos Municipais - Cadastro
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codigo_fed | integer(4) | PK |  | Codigo do municipio federal |
| sigl_est | char(2) | PK |  | Sigla do estado |
| vigencia_inc | date(4) | PK |  | Vigencia |
| indice_inc | char(8) |  |  | Indice |
| tipocalc_inc | char(1) |  |  | Tipo de calculo (C - Cascata/D - Direto) |
| valores_inc | char(1) |  |  | Valores (A=Anual/M=Mensal) |
| BASE_CALCULO_INC | char(1) |  |  | Base de calculo (R=Receita bruta / Q=Quantidade de profissional habilitado) |
