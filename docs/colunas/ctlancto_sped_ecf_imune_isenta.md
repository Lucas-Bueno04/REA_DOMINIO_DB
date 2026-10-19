# CTLANCTO_SPED_ECF_IMUNE_ISENTA — Lançamento Referencial SPED ECF Imunes e Isentas
469.590 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| NUME_LAN | integer(4) | PK |  | Número do lançamento |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| CODI_LOTE | integer(4) |  |  | Lançamento em lote |
| VALOR | numeric(14) |  |  | Valor |
| CONTA_DEBITO | integer(4) |  |  | Conta Débito |
| CONTA_CREDITO | integer(4) |  |  | Conta Crédito |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
