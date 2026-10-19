# EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA — Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Vigência
632 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CREDITO_PRESUMIDO | integer(4) | PK |  | Sequencial |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(80) |  |  | Descrição |
| ALIQUOTA_PIS | numeric(7) |  |  | Alíquota PIS |
| ALIQUOTA_COFINS | numeric(7) |  |  | Alíquota COFINS |
