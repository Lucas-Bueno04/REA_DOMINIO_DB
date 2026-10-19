# CTCONTAS_COSIF — Plano de contas COSIF
3.884 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_COSIF | integer(4) | PK |  | Codigo |
| CLASSIFICACAO_COSIF | varchar(20) |  |  | Classificacao |
| DESCRICAO_COSIF | varchar(80) |  |  | Descricao |
| VALIDADE_INICIO_COSIF | date(4) |  | S | Inicio validade |
| VALIDADE_FIM_COSIF | date(4) |  | S | Fim validade |
| UTILIZACAO_COSIF | char(1) |  |  | Utilização (F=Fiscal / S=Societária / A=Ambas) |
| NATUREZA_COSIF | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
