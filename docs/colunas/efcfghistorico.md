# efcfghistorico — Configuracao de historico
38.445 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_tipo | integer(4) | PK |  | Tipo (1=Entradas/2=Entradas Sintetica/3=Entradas Imposto/4=Saidas/5=Saidas Sintetica/6=Saidas Imposto/7=Servicos/8=Servicos Sintetica/9=Servicos Imposto/10=Apuracao/11=Pagamento de Impostos/12=Pagamento de Parcelas) |
| historico | varchar(200) |  |  | Historico |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
