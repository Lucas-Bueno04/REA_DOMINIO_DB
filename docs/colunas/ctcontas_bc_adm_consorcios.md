# CTCONTAS_BC_ADM_CONSORCIOS — Plano de contas Banco Central - Administradoras de Consórcio
1.202 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_BC_ADM_CONSORCIOS | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
