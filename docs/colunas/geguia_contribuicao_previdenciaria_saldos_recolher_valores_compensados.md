# GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER_VALORES_COMPENSADOS — Guia da contribuição previdenciária - Valores compensados do saldo a recolher.
3.219.687 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| TIPO_SALDO_RECOLHER | smallint(2) | PK |  | Tipo de saldo a recolher. |
| TIPO_SALDO_COMPENSAR | smallint(2) | PK |  | Tipo de saldo a compensar. |
| VALOR_COMPENSADO | numeric(13) |  |  |  |
| CODI_EMP_ESCRITA_FISCAL | integer(4) |  | S |  |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
