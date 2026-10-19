# EFMVEPRO_EXTEMPORANEO_PISCOFINS — Notas Fiscais de Entrada - Produtos - Extemporâneo PIS COFINS
56 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Entrada |
| NUME_MEP | integer(4) | PK |  | Sequencial |
| CODI_IMP | integer(4) | PK |  | Imposto |
| TIPO_CREDITO | integer(4) | PK |  | Tipo de crédito |
| RECEITA_CUMULATIVA | numeric(13) |  |  | Receita cumulativa |
| RECEITA_NAO_CUMULATIVA | numeric(13) |  |  | Receita não cumulativa |
| INTERNA_TRIBUTADA | numeric(13) |  |  | Interna tributada |
| INTERNA_NAO_TRIBUTADA | numeric(13) |  |  | Interna não tributada |
| EXTERNA | numeric(13) |  |  | Externa |
| COMPETENCIA | date(4) |  |  | Competencia |
