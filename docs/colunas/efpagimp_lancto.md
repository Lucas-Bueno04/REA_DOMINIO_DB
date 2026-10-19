# efpagimp_lancto — Pagamento de impostos X Lancamentos contabeis
36.128 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa do lancamento |
| nume_lan | integer(4) | PK |  | Numero |
| fili_lan | integer(4) | PK |  | Empresa do pagamento |
| codi_imp | integer(4) | PK |  | Imposto |
| data_pim | date(4) | PK |  | Competencia |
| pdic_pim | integer(4) | PK |  | Periodicidade |
| parc_pim | integer(4) | PK |  | Parcela |
| nbaixa_pim | integer(4) | PK |  | Numero da baixa |
| tipo | tinyint(1) |  |  | Tipo do lancamento(0 - Usuario/1 - Principal/2 - Juros/3 - Multa/4-Valor pago a maior/5 - Correção/6 - Desconto) |
| grupo | integer(4) | PK |  | Grupo do lancamento |
| contra_partida | integer(4) |  |  | Codigo do lancamento contrapartida para pagamentos em grupo |
| IMPOSTO_PARCELADO | char(1) | PK |  | Imposto parcelado |
| I_PARCELAMENTO | integer(4) | PK |  | Sequencial do parcelamento |
| I_PARCELAMENTO_PARCELA_PARCELAMENTO | integer(4) | PK |  | Sequencial do parcelamento parcela |
| I_PARCELAMENTO_PARCELA_PARCELA | integer(4) | PK |  | Sequencial do parcelamento parcela parcela |
