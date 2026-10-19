# CTCONTAS_SPED_ECF_GERAL_REF_SA_SCP — Plano de contas SPED ECF Geral Referencial - Saldo anterior por SCP
26.875 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_CTA | integer(4) | PK |  | Conta contábil |
| CODI_EMP_CORRENTE | integer(4) | PK |  | Empresa corrente |
| CODIGO_CTA_SPED_ECF_GERAL | integer(4) | PK |  | Conta SPED ECF |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_SCP | integer(4) |  | S | SCP |
| SALDO_ANTERIOR | numeric(13) |  |  | Saldo Anterior |
| TIPO_SALDO_ANTERIOR | char(1) |  | S | Tipo do Saldo Anterior (C=Crédito / D-Débito) |
| SOCIO_OSTENSIVO | char(1) |  |  | SÃ³cio Ostensivo (S=SIM/N=NÃƒO) |
