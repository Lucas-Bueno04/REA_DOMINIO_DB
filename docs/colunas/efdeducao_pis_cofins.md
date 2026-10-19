# EFDEDUCAO_PIS_COFINS — Restituição, Ressarcimento e Compensação de PIS/COFINS - Deduções
177 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo |
| I_DEDUCAO | integer(4) | PK |  | Código |
| PERIODO | date(4) |  |  | Período |
| CODI_IMP | integer(4) |  |  | Imposto |
| TIPO_CREDITO | integer(4) |  |  | Tipo de crédito |
| FORMALIZACAO_PEDIDO | integer(4) |  | S | Formalização do pedido |
| NUMERO_DCOMP_PROCESSO | varchar(24) |  | S | Número do DComp ou processo |
| VALOR | numeric(13) |  |  | Valor |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| DEDUZIR_IPI_APURACAO | char(1) |  |  | Deduzir o valor do ressarcimento de IPI na apuração |
| DEDUZIR_IPI_APURACAO_IMPOSTO | integer(4) |  | S | Deduzir o valor do ressarcimento de IPI na apuração - Opções (2-IPI / 30-IPI-M) |
| I_RECOLHIMENTO_IPI | integer(4) |  | S | Código de recolhimento para o imposto IPI |
| DEDUZIR_IPI_CREDITO_NA_COMPETENCIA | date(4) |  |  | Deduzir o crédito na competência |
| I_RECOLHIMENTO | integer(4) |  | S | Código Sequencial do Recolhimento |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código do Recolhimento |
| PERIODO_PARA_APURACAO | date(4) |  |  | Período para apuração |
| DEMONSTRAR_VALORES_DEDUCOES | char(1) |  |  | Demonstrar os valores de deduções (A - Na tela de apuração do imposto/P - Somente no pagamento do imposto) |
