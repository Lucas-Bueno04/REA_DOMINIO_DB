# EFOUTRAS_DEDUCOES_PIS_COFINS — Outras Deduções de PIS/COFINS
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_OUTRA_DEDUCAO | integer(4) | PK |  | Código sequencial |
| DATA_AJUSTE | date(4) |  |  | Data do ajuste |
| NATUREZA_DEDUCAO | integer(4) |  |  | Natureza da dedução |
| ORIDEM_DEDUCAO | integer(4) |  |  | Origem da dedução |
| INFORMACAO_COMPLEMENTAR | varchar(255) |  |  | Informação complementar |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota COFINS |
| VALOR_PIS | numeric(13) |  |  | Valor PIS |
| VALOR_COFINS | numeric(13) |  |  | Valor COFINS |
| CNPJ | varchar(14) |  | S | CNPJ da pessoa relacionada |
| I_RECOLHIMENTO_PIS | integer(4) |  | S | Código Sequencial do Recolhimento do PIS |
| CODIGO_RECOLHIMENTO_PIS | char(6) |  |  | Código do Recolhimento do PIS |
| I_RECOLHIMENTO_COFINS | integer(4) |  | S | Código Sequencial do Recolhimento do COFINS |
| CODIGO_RECOLHIMENTO_COFINS | char(6) |  |  | Código do Recolhimento do COFINS |
