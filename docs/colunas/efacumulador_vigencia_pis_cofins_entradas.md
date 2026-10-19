# EFACUMULADOR_VIGENCIA_PIS_COFINS_ENTRADAS — Acumuladores - Cadastro - PIS/COFINS - Entradas
21 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Codigo |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| I_PIS_COFINS_ENTRADAS | integer(4) | PK |  | Sequencial |
| CST | integer(4) |  |  | CST |
| BASE_CREDITO | integer(4) |  |  | Base do crédito |
| NATUREZA_FRETE | integer(4) |  | S | Natureza do frete |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota do PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota do COFINS |
| VINCULO_CREDITO | integer(4) |  | S | Vínculo do Crédito |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
