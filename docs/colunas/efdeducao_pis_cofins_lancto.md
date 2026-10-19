# EFDEDUCAO_PIS_COFINS_LANCTO — Restituição, Ressarcimento e Compensação de PIS/COFINS - Deduções - Lançamentos contábeis
22 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa do lancamento |
| I_DEDUCAO | integer(4) | PK |  | Codigo da dedução |
| NUME_LAN | integer(4) | PK |  | Numero do lancamento |
| FILI_LAN | integer(4) | PK |  | Empresa do ajuste no calculo do PIS/COFINS por movimento de produtos |
| TIPO | tinyint(1) |  |  | Tipo do lancamento |
