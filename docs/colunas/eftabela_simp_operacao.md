# EFTABELA_SIMP_OPERACAO — Tabela de Operações - SIMP
151 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_OPERACAO | integer(4) | PK |  | Sequencial da Operação |
| CODIGO_OPERACAO | varchar(9) |  |  | Código da Operação |
| ESPECIFICACAO | varchar(255) |  |  | Especificação da Operação |
| CODIGO_TOTALIZADOR_OPERACAO | varchar(9) |  |  | Código Totalizador por Operação |
| CODIGO_TOTALIZADOR_GERAL | varchar(9) |  |  | Código Totalizador Geral |
| TIPO_OPERACAO | varchar(1) |  |  | Tipo da Operação (E - Entrada/ S - Saída) |
