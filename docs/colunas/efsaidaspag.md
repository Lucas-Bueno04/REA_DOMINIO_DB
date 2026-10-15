# efsaidaspag — Notas Fiscais de Saida - Pagamento das Parcelas
2.970 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_sai | integer(4) | PK |  | Saida |
| pgto_saip | date(4) | PK |  | Data do pagamento |
| tipo_saip | tinyint(1) | PK |  | TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO/19 - ICMS ST/20-FETHAB) |
| vpag_saip | numeric(13) |  | S | Valor do pagamento |
| nlan_saip | integer(4) |  | S | Numero do lancamento na contabilidade |
| origempg_saip | char(1) |  | S | Origem do pagamento (B - baixa/L - Lancamento) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg, 5 - API |
| parc_saip | integer(4) | PK |  | Numero da parcela |
| nropag_saip | tinyint(1) | PK |  | Numero do pagamento(sequencial) |
| NUMERO_TITULO_SAIP | char(60) |  | S | Número do título |
| CODI_ENT | integer(4) |  | S | Código da Nota |
| I_NOTA_DEVOLVIDA | integer(4) |  | S | Código da Nota Devolvida |
| HISTORICO_DE_RECEBIMENTO | varchar(200) |  | S | Histórico de recebimento |
