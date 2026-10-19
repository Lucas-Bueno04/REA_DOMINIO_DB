# EFAM_CODIGO_TRIBUTACAO_PRODUTO_ALIQUOTA — AM - Código de Tributação do Produto - DIA - Alíquotas
514 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TRIBUTACAO | integer(4) | PK |  | Sequencial |
| VIGENCIA | date(4) | PK |  | Vigência |
| I_CODIGO_TRIBUTACAO | integer(4) | PK |  | Sequencial do Código |
| CODIGO_TRIBUTACAO | varchar(10) |  |  | Código |
| DESCRICAO | varchar(1024) |  |  | Descrição |
| AMAZONAS_ALIQUOTA_N_NE_CO | numeric(7) |  |  | Amazonas Alíquota N, NE, CO |
| AMAZONAS_ALIQUOTA_S_SE | numeric(7) |  |  | Amazonas Alíquota S, SE |
| AMAZONAS_ALIQUOTA_4 | numeric(7) |  |  | Amazonas Alíquota 4% |
| ZONA_FRANCA_ALIQUOTA_N_NE_CO | numeric(7) |  |  | Zona Franca Alíquota N, NE, CO |
| ZONA_FRANCA_ALIQUOTA_S_SE | numeric(7) |  |  | Zona Franca Alíquota S, SE |
| ZONA_FRANCA_ALIQUOTA_4 | numeric(7) |  |  | Zona Franca Alíquota 4% |
| IMPOSTO_RELACIONADO | integer(4) |  | S | Imposto Relacionado |
