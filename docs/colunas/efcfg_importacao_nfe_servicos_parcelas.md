# EFCFG_IMPORTACAO_NFE_SERVICOS_PARCELAS — Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas
25 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo da empresa |
| NOTA | integer(4) | PK |  | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| QUANTIDADE_PARCELAS | integer(4) |  |  | Quantidade de parcelas |
| VENCIMENTO | varchar(1) |  |  | Vencimento M-Mesma data da nota/I-Informar |
| QUANTIDADE_DIAS | integer(4) |  |  | Quantidade de dias |
| TIPO_TITULO | integer(4) |  |  | Tipo do Titulo D/C/P/R |
| IDENTIFICACAO_TITULO | varchar(255) |  | S | Identificacao S/N |
| GERAR_NUMERO_TITULO | varchar(1) |  |  | Gerar n. do titulo S/N |
| TIPO_NUMERO_TITULO | varchar(1) |  | S | Tipo do numero do titulo N-Mesmo número do documento/D-Mesma data de emissao |
