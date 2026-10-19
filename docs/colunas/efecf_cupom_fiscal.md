# EFECF_CUPOM_FISCAL — ECF - Cupom fiscal
34.381 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| I_CUPOM | integer(4) | PK |  | Sequencial do cupom fiscal |
| NUMERO | integer(4) |  | S | Número do cupom fiscal |
| EMISSAO | date(4) |  |  | Data de emissão |
| CODI_CLI | integer(4) |  |  | Código do cliente |
| SITUACAO | integer(4) |  |  | Situação (0 - Documento regular/1 - Documento regular extemporâneo/2 - Documento cancelado) |
| VALOR_PRODUTO | numeric(13) |  |  | Valor dos produtos |
| VALOR_DESCONTO | numeric(13) |  |  | Valor do desconto |
| VALOR_TOTAL | numeric(13) |  |  | Valor total |
| GERAR_PARCELAS | char(1) |  |  | Gerar parcelas(S/N) |
| ACRESCIMO | numeric(13) |  |  | Valor do acréscimo |
| TIPO_TITULO | tinyint(1) |  |  | Tipo do Titulo (0=Duplicata/1=Cheque/2=Promissória/3=Recibo/4=Clientes/5=Documento Fiscal/99=Outros) |
| IDENTIFICACAO | varchar(255) |  | S | Identificação |
| ORDEM_OPERACAO | integer(4) |  |  | Orderm de operação (COO) |
