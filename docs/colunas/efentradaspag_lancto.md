# efentradaspag_lancto — Baixas de entradas X Lancamentos contabeis
28.525 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa do lancamento |
| nume_lan | integer(4) | PK |  | Numero do lancamento |
| fili_lan | integer(4) | PK |  | Empresa do pagamento |
| codi_ent | integer(4) | PK |  | Codigo da nota |
| pgto_entp | date(4) | PK |  | Data do pagamento |
| tipo_entp | tinyint(1) | PK |  | Tipo (1-Normal/ 2-Juros/ 3-Multa/ 4-Descto/ 5-Devolucao/ 6-PIS/ 7-COFINS/ 8-CSOC/ 9-CRF/ 10-IRRF/ 11-IRRFPF/ 12-Juros Valor Presente/ 13-ISS/ 14-Outras) |
| parc_entp | integer(4) | PK |  | Numero da parcela |
| nropag_entp | tinyint(1) | PK |  | Numero do pagamento(sequencial) |
| grupo | integer(4) | PK |  | Grupo do lancamento |
| tipo | tinyint(1) |  |  | Tipo do lancamento |
| contra_partida | integer(4) |  |  | Codigo do lancamento contrapartida para pagamentos em grupo |
| ORIGEM_LAN | char(1) |  | S | Origem do lançamento da baixa (I - Individual / G - Grupo) |
