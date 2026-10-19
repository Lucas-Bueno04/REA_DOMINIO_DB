# CTCONTAS_BC_SOCIEDADE_CORRETORA_CAMBIO — Plano de contas Banco Central - Sociedade Corretora de Câmbio
3.199 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CONTA | integer(4) | PK |  | Código |
| CLASSIFICACAO_BC_SOC_COR_CAMBIO | varchar(20) |  |  | Classificação |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VALIDADE_INICIO | date(4) |  | S | Início validade |
| VALIDADE_FIM | date(4) |  | S | Fim validade |
| NATUREZA | char(1) |  |  | Natureza (S=Sintética / A=Analítica) |
| EXIGE_SALDO | integer(4) |  |  | Exibe Saldo (1=Saldo somente na coluna total / 2=Saldo na coluna total e realizável até 90 dias / 3=Saldo na coluna total e em pelo menos mais uma coluna |
