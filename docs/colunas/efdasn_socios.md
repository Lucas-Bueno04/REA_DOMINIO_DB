# efdasn_socios — DASN - outros dados socios
2.104 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| data | date(4) | PK |  | Data |
| i_socio | integer(4) | PK |  | Socio |
| tipo | char(1) | PK |  | Tipo (S - Socio/A - Administrador/R - Representante Legal/E - Empresario) |
| ano | integer(4) | PK |  | Ano do informativo |
| isentos | numeric(13) |  |  | Rendimentos isentos |
| tributaveis | numeric(13) |  |  | Rendimentos tributaveis |
| irrf | numeric(13) |  |  | Imposto de renda retido na fonte |
| participacao | numeric(5) |  |  | Participacao no capital social |
