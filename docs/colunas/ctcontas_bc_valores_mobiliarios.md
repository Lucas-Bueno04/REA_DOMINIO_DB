# CTCONTAS_BC_VALORES_MOBILIARIOS — Plano de contas Banco Central - Distribuidora de Títulos e Valores Mobiliários
4.273 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_BC_VALORES_MOBILIARIOS | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
