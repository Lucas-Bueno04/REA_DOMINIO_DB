# LRCSLL_REAL_EXCLUSAO — Lançamentos de Exclusões da Contribuição Social
119 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_REAL_EXCLUSAO | integer(4) | PK |  | Código |
| DATA_LANCAMENTO | date(4) |  |  | Data do lançamento |
| COMPLEMENTO | varchar(100) |  |  | Complemento |
| I_SCP | integer(4) |  | S | SCP |
| I_GRUPO_CSLL_EXCLUSAO_GERAL | integer(4) |  | S | Grupo - Geral |
| I_GRUPO_CSLL_EXCLUSAO_SF | integer(4) |  | S | Grupo - Sistema Financeiro |
| I_GRUPO_CSLL_EXCLUSAO_S | integer(4) |  | S | Grupo - Sociedade Seguradora |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo de lançamento(G=Geral, R=Rural) |
