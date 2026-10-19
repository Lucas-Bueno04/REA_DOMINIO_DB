# fointegcontlanc — Numero do lancamentos
213.590 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| competencia | date(4) | PK |  | Competencia |
| nume_lanc | integer(4) | PK |  | Numero lancamento |
| tipo | integer(4) | PK |  | Tipo da integracao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codi_emp_cta | integer(4) |  |  | Codigo da empresa da contabilidade |
| TIPO_SEPARADOR | smallint(2) |  | S | Tipo de separador. (0=Sem separador/1=Centro de custos/2=Departamentos/3=Serviços/4=Filiais) |
| I_SEPARADOR | integer(4) |  | S | Código do separador. |
