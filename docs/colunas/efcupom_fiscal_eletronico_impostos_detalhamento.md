# EFCUPOM_FISCAL_ELETRONICO_IMPOSTOS_DETALHAMENTO — Cupom Fiscal Eletrônico - CF-e - Impostos - Detalhamento
7.744.304 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CFE | integer(4) | PK |  | Código do CF-e |
| I_IMPOSTO | integer(4) | PK |  | Sequencial do imposto |
| I_DETALHAMENTO | integer(4) | PK |  | Sequencial do detalhamento |
| CODI_IMP | integer(4) |  |  | Código do imposto |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do imposto |
| VALOR_ISENTAS | numeric(13) |  |  | Valor de isentas |
| VALOR_OUTROS | numeric(13) |  |  | Valor de outros |
| CST | integer(4) |  | S | CST |
| CODI_NAT | integer(4) |  | S | CFOP |
| VERSAO_NAT | smallint(2) |  | S | Versão da CFOP |
| CODIGO_OBSERVACAO | integer(4) |  | S | Observação |
| DESCRICAO_OBSERVACAO | varchar(360) |  | S | Descrição da observação |
