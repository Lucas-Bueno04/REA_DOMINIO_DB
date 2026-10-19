# CTCONTAS_BC_SOCIEDADE_CORRETORA_TITULOS — Plano de contas Banco Central - Sociedade Corretora de Títulos e Valores Mobiliários
3.199 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_BC_SOC_COR_TITULOS | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
