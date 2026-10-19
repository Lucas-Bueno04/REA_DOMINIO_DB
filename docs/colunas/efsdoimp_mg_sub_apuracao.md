# EFSDOIMP_MG_SUB_APURACAO — Saldo dos Impostos - Sub Apuração MG
34 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| I_SUB_APURACAO | integer(4) | PK |  | Sequencial sub apuração |
| VALOR_CONTABIL_SAIDA | numeric(13) |  |  | Valor contábil saída |
| BASE_CALCULO_SAIDA | numeric(13) |  |  | Base de cálculo saídas |
| VALOR_SAIDA | numeric(13) |  |  | Valor saídas |
| BASE_CALCULO_ENTRADA_PROPORCAO | numeric(13) |  |  | Base de cálculo entradas - Proporção |
| PROPORCAO_ACABADO | numeric(5) |  |  | Proporção acabados |
| VALOR_ENTRADA_PROPORCAO | numeric(13) |  |  | Valor entradas - Proporção |
| VALOR_CONTABIL_ENTRADA | numeric(13) |  |  | Valor contábil entrada |
| BASE_CALCULO_ENTRADA | numeric(13) |  |  | Base de cálculo entrada |
| VALOR_ENTRADA | numeric(13) |  |  | Valor entradas |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor devolução |
| VALOR_CREDITO_ESTORNO | numeric(13) |  |  | Valor crédito estorno |
| VALOR_RECOLHIMENTO_EFETIVO_SAIDA | numeric(13) |  |  | Valor total do recolhimento efetivo pelas saídas |
| VALOR_CREDITO_PRESUMIDO | numeric(13) |  |  | Valor crédito presumido |
| SALDO_RECOLHER | numeric(13) |  |  | Saldo a recolher |
| SALDO_CREDOR | numeric(13) |  |  | Saldo credor |
| SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | Saldo credor anterior |
| PARCELA | integer(4) |  |  | Parcela |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| DATA_VENCIMENTO | date(4) |  |  | Data vencimento |
| VALOR_ESTORNO_CREDITO_ESTORNO | numeric(13) |  |  | Valor do estorno do crédito estorno (Devolução da compra) |
| OUTROS_DEBITOS | numeric(13) |  |  | Outros débitos |
| ESTORNO_CREDITOS | numeric(13) |  |  | Estorno créditos |
| OUTROS_CREDITOS | numeric(13) |  |  | Outros créditos |
| ESTORNO_DEBITOS | numeric(13) |  |  | Estorno débitos |
| DESCONTO_CONFORME_TERMO_ACEITE_LEI_22549_17 | numeric(13) |  |  | Desconto conforme Termo de Aceite da Lei 22.549/17 e Decreto 47.226/17 |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo Devedor |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido |
| VALOR_CONTABIL_REDUCAO_Z | numeric(13) |  |  | Valor Contábil Redução Z |
| BASE_CALCULO_REDUCAO_Z | numeric(13) |  |  | base de Cálculo Redução Z |
| VALOR_REDUCAO_Z | numeric(13) |  |  | Valor Redução Z |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO_SAIDAS | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido - Saídas |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO_REDUCAO_Z | numeric(13) |  |  | Estorno do FEM de mercadorias alcançadas pelo crédito presumido - Redução Z |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO_DEVOLUCAO | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |
