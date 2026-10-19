# efsdoimp_aproveitamento_credito — Saldo dos impostos - Aproveitamento de credito
136 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_imp | integer(4) | PK |  | Imposto |
| data_sim | date(4) | PK |  | Competencia |
| pdic_sim | integer(4) | PK |  | Periodicidade |
| origem | tinyint(1) | PK |  | Origem do credito(1-interno/2-externo) |
| tipo | tinyint(1) | PK |  | Tipo (1-interno/2-nao tributado/3-externo) |
| periodo | date(4) | PK |  | Periodo de apuracao do credito |
| saldo_disponivel | numeric(13) |  |  | Saldo disponivel |
| saldo_utilizado | numeric(13) |  |  | Saldo utilizado |
| saldo_atransportar | numeric(13) |  |  | Saldo a transportar |
