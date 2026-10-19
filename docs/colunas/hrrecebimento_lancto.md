# HRRECEBIMENTO_LANCTO — Recebimento de contas a receber X Lancamentos Contabeis
41.380 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| I_RECEBIMENTO | integer(4) | PK |  | Recebimento |
| EMPRESA_LAN | integer(4) | PK |  | Empresa do lancamento contabil |
| NUME_LAN | integer(4) | PK |  | Numero do lancamento contabil |
| FILI_LAN | integer(4) |  |  | Empresa que originou o lancamento contabil |
| CODI_LOTE | integer(4) |  |  | Codigo do lote |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo do lancamento contabil S Sistema U Usuario |
