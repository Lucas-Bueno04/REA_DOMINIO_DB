# EFMVEPRO_MG_SUB_APURACAO — Notas Fiscais de Entrada - Produtos - MG Sub Apuração
14 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| I_SUB_APURACAO | integer(4) | PK |  | Sequencial |
| CODI_PDI | char(14) |  |  | Código do produto |
| BASE_CALCULO | numeric(13) |  |  | Base de cálculo |
| VALOR_ICMS | numeric(13) |  |  | Valor ICMS |
| PROPORCAO | numeric(5) |  |  | Proporção |
| COMPETENCIA | date(4) |  |  | Competência |
| ESTORNO_FEM_MERCADORIAS_CREDITO_PRESUMIDO_DEVOLUCAO | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |
