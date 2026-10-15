# efservicospag — Notas Fiscais de Servico - Pagamento das Parcelas
215.111 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ser | integer(4) | PK |  | Servico |
| pgto_serp | date(4) | PK |  | Data do pagamento |
| tipo_serp | tinyint(1) | PK |  | TIPO (1-NORMAL/ 2-JUROS/ 3-MULTA/ 4-DESCONTO/ 5-DEVOLUCAO/ 6-PIS/ 7-COFINS/ 8-CSLL/ 9-IRRF/ 11-PISOP/ 12-COFINSOP/ 13-CSLLOP/ 14-IRPJOP/ 15-IRRFP/ 16-JUROS VALOR PRESENTE/ 17-OUTRAS/ 18-PROFISSIONAL PARCEIRO) |
| vpag_serp | numeric(13) |  | S | Valor do Pagamento |
| nlan_serp | integer(4) |  | S | Numero do lancamento na contabilidade |
| origempg_serp | char(1) |  | S | Origem do pagamento (B - baixa/L - Lancamento) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg, 5 - API |
| parc_serp | tinyint(1) | PK |  | Numero da parcela |
| nropag_serp | tinyint(1) | PK |  | Numero do pagamento(sequencial) |
| NUMERO_TITULO_SERP | char(60) |  | S | Número do título |
| HISTORICO_DE_RECEBIMENTO | varchar(200) |  | S | Histórico de recebimento |
