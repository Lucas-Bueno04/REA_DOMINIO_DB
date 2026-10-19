# CTCONTAS_BC_GERAL — Plano de contas Banco Central - Geral
9.017 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_BC_GERAL | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| UTILIZACAO | char(1) |  |  | Utilização (F=Fiscal / S=Societária / A=Ambas) |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
| CLAS_CTA_GRAU | varchar(20) |  | S | Grau para calcular o valor do pai |
