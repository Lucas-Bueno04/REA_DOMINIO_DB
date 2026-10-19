# EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA_DETALHAMENTO — Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Relação de NCM
4.424 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CREDITO_PRESUMIDO | integer(4) | PK |  | Sequencial |
| VIGENCIA | date(4) | PK |  | Vigência |
| I_CREDITO_PRESUMIDO_DETALHAMENTO | integer(4) | PK |  | Sequencial detalhamento |
| NCM | char(8) |  |  | NCM |
| DESCRICAO | char(1024) |  |  | Descrição NCM |
| PERCENTUAL_CREDITO_PRESUMIDO | numeric(4) |  |  | Percentual Crédito Presumido |
| ALIQUOTA_PIS_AJUSTADA | numeric(6) |  |  | Alíquota PIS Ajustada |
| ALIQUOTA_COFINS_AJUSTADA | numeric(6) |  |  | Alíquota COFINS Ajustada |
| UTILIZADO_COMO_INSUMO | char(1) |  |  | Utilizado como insumo |
