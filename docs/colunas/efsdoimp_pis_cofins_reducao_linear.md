# EFSDOIMP_PIS_COFINS_REDUCAO_LINEAR — Saldo do Impostos - PIS/COFINS Reducao Linear
144 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Sequencial do Recolhimento |
| CST | integer(4) | PK |  | CST |
| ALIQUOTA | numeric(7) | PK |  | Aliquota do Imposto |
| PERCENTUAL_LINEAR | numeric(5) | PK |  | Percentual da Reducao Linear |
| OPERACAO | char(1) | PK |  | Operacao (A - Acrescimo / R - Reducao) |
| BASE_CALCULO | numeric(13) |  |  | Base de Calculo |
| VALOR_IMPOSTO | numeric(13) |  |  | Valor do Imposto |
