# HRCONTA_CORRENTE_ESCRITORIO_LANCTO — Conta corrente do escritorio X Lancamentos Contabeis
6.781 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_MOVIMENTO_ESCRITORIO | integer(4) | PK |  | Conta corrente escritorio |
| EMPRESA_LAN | integer(4) | PK |  | Empresa do lancamento contabil |
| NUME_LAN | integer(4) | PK |  | Numero do lancamento contabil |
| FILI_LAN | integer(4) |  |  | Empresa que originou o lancamento contabil |
| CODI_LOTE | integer(4) |  |  | Codigo do lote |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo do lancamento contabil S Sistema U Usuario |
