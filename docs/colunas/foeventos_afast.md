# foeventos_afast — Eventos pagos em afastamento
214.085 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_eventos | integer(4) | PK |  | Código do evento |
| situacao | integer(4) | PK |  | Situacao |
| i_eventos_afast | integer(4) |  |  | Código do evento de afastamento |
| calcular | tinyint(1) |  |  | Calcular: 1=Sim, 0=Nao |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
