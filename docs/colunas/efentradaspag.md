# efentradaspag — Notas Fiscais de Entrada - Pagamento das Parcelas
104.582 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Entrada |
| pgto_entp | date(4) | PK |  | Data do pagamento |
| tipo_entp | tinyint(1) | PK |  | Tipo (1-Normal/ 2-Juros/ 3-Multa/ 4-Descto/ 5-Devolucao/ 6-PIS/ 7-COFINS/ 8-CSOC/ 9-CRF/ 10-IRRF/ 11-IRRFPF/ 12-Juros Valor Presente/ 13-ISS/ 14-Outras) |
| vpag_entp | numeric(13) |  | S | Valor do pagamento |
| nlan_entp | integer(4) |  | S | Numero do lancamento na contabilidade |
| origempg_entp | char(1) |  | S | Origem do pagamento (B - baixa/L - Lancamento) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg, 5 - API |
| parc_entp | integer(4) | PK |  | Numero da parcela |
| nropag_entp | tinyint(1) | PK |  | Numero do pagamento(sequencial) |
| CODIGO_RECOLHIMENTO | char(6) |  | S | Código de recolhimento do imposto |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| CODI_SAI | integer(4) |  | S | Código da Nota |
| I_NOTA_DEVOLVIDA | integer(4) |  | S | Código da Nota Devolvida |
| HISTORICO_DE_PAGAMENTO | varchar(200) |  | S | Histórico de pagamento |
| NUMERO_TITULO_ENTP | char(60) |  | S | Numero do Título/Parcela |
| BASE_IRRF_ENTP | numeric(13) |  |  | Valor da base de cálculo do IRRF |
| TIPO_ISENCAO | integer(4) |  | S | Tipo de isenção para rendimentos isentos |
| DESCRICAO_ISENCAO | varchar(100) |  | S | Descrição de isenção para rendimentos isentos |
