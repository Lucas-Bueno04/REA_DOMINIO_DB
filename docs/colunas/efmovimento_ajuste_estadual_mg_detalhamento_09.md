# EFMOVIMENTO_AJUSTE_ESTADUAL_MG_DETALHAMENTO_09 — MG - Ajuste Impostos lançados estaduais - Detalhamento 09
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| TIPO | char(1) |  |  | Tipo (O/ S/ A/ E/ T/ R) |
| CODI_ESP | integer(4) |  | S | Código da espécie |
| CODI_CLI | integer(4) |  | S | Código do cliente |
| DATA_EMISSAO | date(4) |  | S | Data emissão |
| NOTA_FISCAL | integer(4) |  | S | Nota fiscal |
| SERIE | varchar(3) |  | S | Série |
| JUSTIFICATIVA | varchar(60) |  | S | Justificativa |
| CHAVE_NFE_CTE | varchar(44) |  | S | Chave NFe ou CTe |
