# EFENTRADAS_INFO_PAG — Notas Fiscais de Entradas - Informação Pagamento
1.701 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Codigo |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| INDICADOR_FORMA_PAGAMENTO | integer(4) |  | S | Indicador da forma de pagamento |
| MEIO_PAGAMENTO | integer(4) |  | S | Meio de pagamento |
| VALOR_PAGAMENTO | numeric(13) |  |  | Valor do pagamento |
| TIPO_INTEGRACAO_PAGAMENTO | integer(4) |  | S | Tipo de integracao para pagamento |
| CNPJ_INSTITUICAO_PAGAMENTO | char(14) |  | S | CNPJ da instituicao de pagamento |
| BANDEIRA_OPERADORA_CARTAO_CRED_DEB | integer(4) |  | S | Bandeira da operadora de cartao de credito e/ou debito |
| NUMERO_AUTORIZACAO_OPERACAO_CARTAO_CRED_DEB | varchar(20) |  | S | Numero de autorizacao da operacao cartao de credito e/ou debito |
| VALOR_TROCO | numeric(13) |  |  | Valor do troco |
