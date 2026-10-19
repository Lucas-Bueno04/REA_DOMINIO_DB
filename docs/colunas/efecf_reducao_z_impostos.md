# EFECF_REDUCAO_Z_IMPOSTOS — ECF - Dados da redução Z - Impostos
1.493 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| I_IMPOSTO | integer(4) | PK |  | Sequencial do imposto |
| CODI_ACU | integer(4) |  |  | Acumulador |
| CODI_NAT | integer(4) |  |  | CFOP |
| VERSAO_NAT | smallint(2) |  |  | Versão da CFOP |
| CODI_IMP | integer(4) |  |  | Código do imposto |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contábil |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA | numeric(5) |  |  | Alíquota |
| IMPOSTO | numeric(13) |  |  | Valor do imposto |
| ISENTAS | numeric(13) |  |  | Valor isento |
| OUTROS | numeric(13) |  |  | Valor de outros |
| NAO_TRIBUTADAS | numeric(13) |  |  | Valor de não tributadas |
| PARCELA_REDUZIDA | numeric(13) |  |  | Valor de parcela reduzida |
| VALOR_FUNDO_AMPARA | numeric(13) |  |  | Valor Fundo Ampara/RS |
| ALIQUOTA_FUNRURAL | numeric(6) |  |  | Alíquota Funrural |
