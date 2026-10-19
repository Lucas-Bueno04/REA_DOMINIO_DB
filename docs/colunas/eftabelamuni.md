# eftabelamuni — Tabelas Municipais - Cadastro
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_tabela | integer(4) | PK |  | Codigo |
| sigl_est | char(2) |  |  | Estado |
| codigo_fed | integer(4) |  |  | Codigo do municipio federal |
| descricao | char(60) |  |  | Descricao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| tipo | char(1) |  |  | Tipo(I=Selecao de itens/L=Campo livre) |
| formato | char(1) |  |  | Formato(C=Caracter/D=Data/V=Valor) |
