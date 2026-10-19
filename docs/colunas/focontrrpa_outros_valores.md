# FOCONTRRPA_OUTROS_VALORES — Outros valores RPA
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| NUMERO | numeric(10) | PK |  | Número do RPA. |
| SEQUENCIAL | smallint(2) | PK |  | Sequencial. |
| TIPO_VALOR | smallint(2) |  |  | Tipo de valor. (1=Outros proventos/2=Outros descontos) |
| I_EVENTOS | integer(4) |  |  | Código da rubrica. |
| VALOR | numeric(13) |  | S | Valor. |
