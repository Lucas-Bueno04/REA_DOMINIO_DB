# LRPAGAMENTO_IMPOSTO_LANCTO — Pagamento de impostos do Lalur - Lancamentos Contabeis
23 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| IMPOSTO | char(1) | PK |  | Imposto (C=Contribuição Social/ I=IRPJ) |
| TIPO_CALCULO | char(1) | PK |  | Tipo de cálculo (R=Real/ E=Estimado) |
| I_PARCELA | integer(4) | PK |  | Sequencial da parcela |
| NUMERO_PARCELA | integer(4) | PK |  | Número da parcela |
| I_PAGAMENTO | integer(4) | PK |  | Sequencial do pagamento |
| EMPRESA_LAN | integer(4) | PK |  | Empresa do lancamento contabil |
| NUME_LAN | integer(4) | PK |  | Numero do lancamento contabil |
| FILI_LAN | integer(4) |  |  | Empresa que originou o lancamento contabil |
| CODI_LOTE | integer(4) |  |  | Codigo do lote |
| TIPO_LANCAMENTO | char(1) |  |  | Tipo do lancamento contabil (S=Sistema/U=Usuario) |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
