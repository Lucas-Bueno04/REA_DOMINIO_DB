# CTCONTAS_SRF — Plano de contas SRF
809 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_SRF | integer(4) | PK |  | Codigo |
| CLASSIFICACAO_SRF | varchar(20) |  |  | Classificacao |
| DESCRICAO_SRF | varchar(100) |  |  | Descricao |
| VALIDADE_INICIO_SRF | date(4) |  | S | Inicio validade |
| VALIDADE_FIM_SRF | date(4) |  | S | Fim validade |
| UTILIZACAO_SRF | char(1) |  |  | Utilização (F=Fiscal / S=Societária / A=Ambas) |
| NATUREZA_SRF | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
