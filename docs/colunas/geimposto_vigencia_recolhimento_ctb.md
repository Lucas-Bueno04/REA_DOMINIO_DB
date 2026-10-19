# GEIMPOSTO_VIGENCIA_RECOLHIMENTO_CTB — Impostos - Cadastro - Codigo de Recolhimento - Contabilidade
3.213 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Codigo |
| VIGENCIA_IMP | date(4) | PK |  | Vigencia |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial |
| CT_RECOLHER | integer(4) |  | S | Imposto a recolher - Conta |
| HT_RECOLHER | integer(4) |  | S | Imposto a recolher - Histórico |
| CT_VENDAS | integer(4) |  | S | Imposto a recolher - Imposto Venda |
| CT_PRINCIPAL_DEBITO | integer(4) |  | S | Pagamento - Valor Principal - Conta débito |
| CT_PRINCIPAL_CREDITO | integer(4) |  | S | Pagamento - Valor Principal - Conta crédito |
| HT_PRINCIPAL | integer(4) |  | S | Pagamento - Valor Principal - Histórico |
| CT_JUROS_DEBITO | integer(4) |  | S | Pagamento - Valor Juros - Conta débito |
| CT_JUROS_CREDITO | integer(4) |  | S | Pagamento - Valor Juros - Conta crédito |
| HT_JUROS | integer(4) |  | S | Pagamento - Valor Juros - Histórico |
| CT_MULTA_DEBITO | integer(4) |  | S | Pagamento - Valor Multa - Conta débito |
| CT_MULTA_CREDITO | integer(4) |  | S | Pagamento - Valor Multa - Conta crédito |
| HT_MULTA | integer(4) |  | S | Pagamento - Valor Multa - Histórico |
| GERA_LANCAMENTO_CONTABEIS_POR_NOTA | char(1) |  |  | Gera Lançamento Contábeis por Nota |
| CT_RECUPERAR | integer(4) |  | S | Devoluções - Imposto a recuperar - Conta |
| CT_DEVOLUCAO_VENDAS | integer(4) |  | S | Devoluções - Devoluções vendas - Conta |
| HT_DEVOLUCAO_VENDAS | integer(4) |  | S | Devoluções - Histórico |
| HT_ZERAMENTO | integer(4) |  | S | Zeramento - Histórico |
| HT_RECUPERAR | integer(4) |  | S | Imposto a recuperar - Histórico |
| CT_COMPRAS | integer(4) |  | S | Imposto a recuperar - Imposto Compras |
| CT_DEBITO_ESTORNO_DEBITOS_SUBTRI | integer(4) |  | S | Estorno de débitos - Subtri - Débito |
| CT_CREDITO_ESTORNO_DEBITOS_SUBTRI | integer(4) |  | S | Estorno de débitos - Subtri - Crédito |
| HT_ESTORNO_DEBITOS_SUBTRI | integer(4) |  | S | Estorno de débitos - Subtri - Histórico |
| CT_DEBITO_ESTORNO_CREDITOS_SUBTRI | integer(4) |  | S | Debito estorno creditos SUBTRI - Conta |
| CT_CREDITO_ESTORNO_CREDITOS_SUBTRI | integer(4) |  | S | Credito estorno creditos SUBTRI - Conta |
| HT_ESTORNO_CREDITOS_SUBTRI | integer(4) |  | S | Estorno creditos SUBTRI - Historico |
