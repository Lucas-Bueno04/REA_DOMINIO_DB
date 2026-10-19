# efincentivosmuni_faixas — Incentivos Municipais - Cadastro - Faixas
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codigo_fed | integer(4) | PK |  | Codigo do municipio federal |
| sigl_est | char(2) | PK |  | Sigla do estado |
| vigencia_inc | date(4) | PK |  | Vigencia |
| sequ_fax | smallint(2) | PK |  | Sequencial |
| inic_fax | numeric(10) |  |  | Valor inicial |
| fina_fax | numeric(10) |  |  | Valor final |
| taxa_fax | numeric(8) |  |  | Valor ou Percentual |
| tipo_fax | char(1) |  |  | Tipo (V=Valor, I=Percentual de Imposto ou D=Percentual de Desconto) |
| origem_fax | char(1) |  |  | Origem (I=Informar/C=Do cadastro/N=Da nota) |
