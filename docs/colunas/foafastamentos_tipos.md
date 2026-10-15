# FOAFASTAMENTOS_TIPOS — TIPOS DE AFASTAMENTOS
82 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_AFASTAMENTOS | integer(4) | PK |  | CODIGO DO AFASTAMENTO |
| DESCRICAO | char(70) |  |  | DESCRICAO |
| AGRUPADORES_FERIAS | integer(4) |  |  | AGRUPAMENTO DE AFASTAMENTOS PARA FERIAS |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
