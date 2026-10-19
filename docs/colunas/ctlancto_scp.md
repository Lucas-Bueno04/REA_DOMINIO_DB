# CTLANCTO_SCP — Lancamento SCP
2.742 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| NUME_LAN | integer(4) | PK |  | Número do lançamento |
| TIPO | char(1) | PK |  | Tipo (D=Débito/ C=Crédito) |
| CODI_LOTE | integer(4) |  |  | Número do lote |
| FILIAL | integer(4) |  |  | Empresa do SCP |
| I_SCP | integer(4) |  |  | SCP |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
