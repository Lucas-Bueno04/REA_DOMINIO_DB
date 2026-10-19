# efmovacu_compensacoes — Outros Movimentos - Impostos Calculados - Outras compensacoes
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| tipo | tinyint(1) |  |  | Tipo do credito |
| formalizacao | tinyint(1) |  |  | Formalizacao do pedido |
| numero | char(24) |  |  | Numero do PERDCOMP ou processo |
| medida | tinyint(1) |  |  | Medida judicial |
| vara | char(2) |  |  | Vara |
| uf | char(2) |  |  | UF |
| municipio | char(50) |  |  | Municipio |
| origem_reg | tinyint(1) |  | S | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| periodo_origem | date(4) |  | S | Periodo origem de credito |
| imposto | integer(4) |  | S | Imposto origem de credito |
| gera_ressarcimento_ipi | char(1) |  | S | Gera ressarcimento de credito de IPI(S/N) |
| CODI_MAC | integer(4) | PK |  | Codigo |
