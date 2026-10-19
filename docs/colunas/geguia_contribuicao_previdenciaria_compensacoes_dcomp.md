# GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP — Guia da contribuição previdenciária - Valores compensados do saldo a recolher.
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) | PK |  | Competência. |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| TIPO_CREDITO | smallint(2) | PK |  | Tipo de crédito. (1=Pagamento indevido ou a maior/2=Retenções/3=Outros) |
| NUMERO_DCOMP | varchar(50) |  | S | Número da DCOMP. |
| VALOR | numeric(13) |  |  | Valor compensado. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| SEQUENCIAL | integer(4) | PK |  | sequencial unico |
| IMPOSTO_COMPENSAR | varchar(255) |  | S | Descrição de impostos |
| REGISTRO_SALVO | char(1) |  |  | Resgistrando que salvou a coluna Tipo de crédito DCOMP |
