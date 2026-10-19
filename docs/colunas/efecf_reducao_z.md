# EFECF_REDUCAO_Z — ECF - Dados da redução Z
459 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_REDUCAO | integer(4) | PK |  | Código da redução Z |
| CODIGO_MAQUINA | integer(4) |  |  | Código da máquina ECF |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CONTADOR_REINICIO | integer(4) |  |  | Contador de reinício |
| DATA_REDUCAO | date(4) |  |  | Data da redução Z |
| CONTADOR_REDUCAO | integer(4) |  |  | Contador da redução Z |
| CUPOM_INICIAL | integer(4) |  |  | COO - Contador de Ordem de Operação Inicial |
| CUPOM_FINAL | integer(4) |  |  | COO - Contador de Ordem de Operação Final |
| DOCUMENTOS_CANCELADOS | integer(4) |  |  | Quantidade de documentos cancelados |
| NUMERO_CAIXA | integer(4) |  |  | Número do caixa |
| MAPA_RESUMO | integer(4) |  |  | Número do mapa resumo |
| GT_ANTERIOR | numeric(16) |  |  | Grande total anterior |
| GT_FINAL | numeric(16) |  |  | Grande total final |
| VENDA_BRUTA | numeric(13) |  |  | Valor da venda bruta |
| CANCELAMENTOS | numeric(13) |  |  | Valor dos cancelamentos |
| DESCONTOS | numeric(13) |  |  | Valor dos descontos |
| VENDA_LIQUIDA | numeric(13) |  |  | Valor da venda líquida |
| I_CONFIGURACAO | integer(4) |  | S | Código da configuração |
| DATA_ORIGEM | date(4) |  |  | Data em que foi feito o lançamento |
| CODIGO_OBSERVACAO | integer(4) |  | S | Código da observação da nota |
| OBSERVACAO_REDUCAO | varchar(300) |  | S | Observação da nota |
| CODI_USU | char(30) |  | S | Usuário |
| CONFERIDO | char(1) |  |  | Conferido (S/N) |
