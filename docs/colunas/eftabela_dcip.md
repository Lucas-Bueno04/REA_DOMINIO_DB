# EFTABELA_DCIP — Tabela - Códigos DCIP
125 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_DCIP | integer(4) | PK |  | Código DCIP |
| DESCRICAO | varchar(512) |  |  | Descrição |
| VIGENCIA_INICIAL | date(4) |  |  | Vigência inicial |
| VIGENCIA_FINAL | date(4) |  | S | Vigência final |
| DISPOSITIVO_LEGAL | varchar(512) |  |  | Dispositivo Legal |
| TIPO | integer(4) | PK |  | TIPO (1 - CRÉDITO PRESUMIDO/2 - ESTORNO DE DÉBITO/3 - OUTROS CRÉDITOS) |
