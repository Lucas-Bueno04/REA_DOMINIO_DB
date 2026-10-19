# LRCSLL_REAL_ADICAO — Lançamentos de Adições da Contribuição Social
307 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_REAL_ADICAO | integer(4) | PK |  | Código |
| DATA_LANCAMENTO | date(4) |  |  | Data do lançamento |
| COMPLEMENTO | varchar(100) |  |  | Complemento |
| I_SCP | integer(4) |  | S | SCP |
| I_GRUPO_CSLL_ADICAO_GERAL | integer(4) |  | S | Grupo - Geral |
| I_GRUPO_CSLL_ADICAO_SF | integer(4) |  | S | Grupo - Sistema Financeiro |
| I_GRUPO_CSLL_ADICAO_S | integer(4) |  | S | Grupo - Sociedade Seguradora |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo de lançamento(G=Geral, R=Rural) |
