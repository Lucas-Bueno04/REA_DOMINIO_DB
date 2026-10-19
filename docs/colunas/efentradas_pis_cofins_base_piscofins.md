# EFENTRADAS_PIS_COFINS_BASE_PISCOFINS — Notas Fiscais de Entrada - PIS/COFINS - Base PIS COFINS
24.348 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Código da entrada |
| I_PIS_COFINS | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) | PK |  | Imposto |
| TIPO_CREDITO | integer(4) | PK |  | Tipo de crédito |
| RECEITA_CUMULATIVA | numeric(13) |  |  | Receita cumulativa |
| RECEITA_NAO_CUMULATIVA | numeric(13) |  |  | Receita não cumulativa |
| INTERNA_TRIBUTADA | numeric(13) |  |  | Interna tributada |
| INTERNA_NAO_TRIBUTADA | numeric(13) |  |  | Interna não tributada |
| EXTERNA | numeric(13) |  |  | Externa |
| COMPETENCIA | date(4) |  |  | Competencia |
