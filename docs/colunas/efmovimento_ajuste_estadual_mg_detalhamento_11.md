# EFMOVIMENTO_AJUSTE_ESTADUAL_MG_DETALHAMENTO_11 — MG - Ajuste Impostos lançados estaduais - Detalhamento 11
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| TIPO | char(1) |  |  | Tipo (R/ O/ T/ D/ A) |
| NOTA_FISCAL | integer(4) |  | S | Nota fiscal |
| SERIE | varchar(8) |  | S | Série |
| DATA_EMISSAO | date(4) |  | S | Data emissão |
| AUTO_DE_INFRACAO | varchar(14) |  | S | Auto de infração |
