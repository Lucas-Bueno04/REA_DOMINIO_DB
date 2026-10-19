# EFACUMULADOR_VIGENCIA_IMPOSTOS_FUNRURAL — Acumuladores - Cadastro - Aliquotas FUNRURAL
53 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| CODI_IMP | integer(4) | PK |  | Imposto |
| ALIQ_IMP | numeric(6) |  |  | Aliquota do FUNRURAL |
| ALIQ_INSS | numeric(5) |  |  | Aliquota do INSS |
| ALIQ_OUTRAS | numeric(6) |  |  | Aliquota outras entidades |
| PERCENTUALBC_IMP | numeric(7) |  |  | Percentual da base de calculo |
| ALIQUOTA_RAT | numeric(5) |  |  | Alíquota RAT |
| COMERCIALIZACAO_PRODUCAO_ISENTA_FUNRURAL | char(1) |  |  | Comercialização da Produção Isenta - Lei nº 13.606/2018 |
