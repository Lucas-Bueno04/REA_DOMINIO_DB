# EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA — Simulador Reforma Tributaria - Impostos IVA
128 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| REFORMA_TRIBUTARIA_ANO | integer(4) | PK |  | Reforma tributaria conforme ano |
| CODI_IVA | integer(4) | PK |  | Codigo imposto IVA |
| COMPETENCIA_TRIBUTACAO | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal) |
| BASE_CREDITO_ENTRADAS | numeric(13) |  |  | Base de credito pelas entradas |
| BASE_DEBITO_SAIDAS | numeric(13) |  |  | Base de debito pelas saidas |
| ALIQUOTA | numeric(5) |  |  | Aliquota |
| REDUCAO_ALIQUOTA | numeric(5) | PK |  | Reducao Aliquota |
| CREDITO_ENTRADAS | numeric(13) |  |  | Valor de credito pelas entradas |
| DEBITO_SAIDAS | numeric(13) |  |  | Valor de debito pelas saidas |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do Imposto |
| BASE_DEBITO_ENTRADAS | numeric(13) |  |  | Base de debito pelas entradas |
| DEBITO_ENTRADAS | numeric(13) |  |  | Valor de debito pelas entradas |
| REDUCAO_ALIQUOTA_AGRUPADOR | char(15) | PK |  | Agrupador de redução de aliquota |
