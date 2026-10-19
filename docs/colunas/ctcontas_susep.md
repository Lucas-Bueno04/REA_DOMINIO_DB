# CTCONTAS_SUSEP — Plano de contas SUSEP
3.399 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_SUSEP | integer(4) | PK |  | Código |
| CLASSIFICACAO_SUSEP | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| TIPO | char(1) |  |  | Tipo (A = Analítica / S = Sintética) |
