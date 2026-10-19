# CTCOEFICIENTE_FORMULA — Coeficientes de análises - Fórmula
77 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_COEFICIENTE | integer(4) | PK |  | Coeficiente de análise |
| I_FORMULA | integer(4) | PK |  | Código |
| OPERACAO | char(1) |  | S | Operação |
| TEXTO_PREFIXO | varchar(50) |  |  | Texto prefixo |
| DESCRICAO | varchar(100) |  |  | Descrição |
| VALOR_FIXO | numeric(13) |  | S | Valor fixo |
| TEXTO_SUFIXO | varchar(50) |  |  | Texto sufixo |
| EXIBIR_OPERACAO | char(1) |  |  | Exibir operação (S/N) |
| FINAL_LINHA | char(1) |  |  | Final de linha (S/N) |
| ORDEM | integer(4) |  |  | Ordem |
| DESCRICAO_RELATORIO | varchar(100) |  |  | Descrição do relatorio |
