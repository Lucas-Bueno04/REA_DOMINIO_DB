# efsaidaspag_lancto — Baixas de saidas X Lancamentos contabeis
322 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa do lancamento |
| nume_lan | integer(4) | PK |  | Numero do lancamento |
| fili_lan | integer(4) | PK |  | Empresa do pagamento |
| codi_sai | integer(4) | PK |  | Codigo da nota |
| pgto_saip | date(4) | PK |  | Data do pagamento |
| tipo_saip | tinyint(1) | PK |  | TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO) |
| parc_saip | integer(4) | PK |  | Numero da parcela |
| nropag_saip | tinyint(1) | PK |  | Numero do pagamento(sequencial) |
| grupo | integer(4) | PK |  | Grupo do lancamento |
| tipo | tinyint(1) |  |  | Tipo do lancamento |
| contra_partida | integer(4) |  |  | Codigo do lancamento contrapartida para pagamentos em grupo |
| ORIGEM_LAN | char(1) |  | S | Origem do lançamento da baixa (I - Individual / G - Grupo) |
