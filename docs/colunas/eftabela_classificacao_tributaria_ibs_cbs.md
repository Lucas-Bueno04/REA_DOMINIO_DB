# EFTABELA_CLASSIFICACAO_TRIBUTARIA_IBS_CBS — Tabela de Classificação Tributária de IBS e CBS
161 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TABELA_IBS_CBS | integer(4) | PK |  | Sequencial da Tabela |
| VIGENCIA | date(4) | PK |  | Vigencia da Tabela |
| CCLASSTRIB | varchar(6) | PK |  | Classificação Tributária |
| DESCRICAO_CCLASSTRIB | varchar(2000) |  |  | Descrição da Classificação Tributária |
| CST | integer(4) |  |  | CST |
| DESCRICAO_CST | varchar(1000) |  |  | Descrição da CST |
| PERCENTUAL_REDUCAO_IBS | numeric(5) |  |  | Percentual de Redução IBS (%) |
| PERCENTUAL_REDUCAO_CBS | numeric(5) |  |  | Percentual de Redução IBS (%) |
