# EFSDOIMP_SUBTRI_POR_UF_RJ_COMPL_REST_ICMS_ST — Saldo dos Impostos - Substituição Tributária Por RJ - Complemento/Restituição de ICMS ST
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| DEBITOS_SAIDAS | numeric(13) |  |  | Débitos pelas saídas |
| CREDITOS_ENTRADAS | numeric(13) |  |  | Créditos pelas entradas |
| COMPLEMENTO_SUBTRI | numeric(13) |  |  | Complemento de ICMS ST |
| RESSARCIMENTO_SUBTRI | numeric(13) |  |  | Ressarcimento de ICMS ST |
| RESSARCIMENTO_SUBTRI_PERIODO_ANTERIOR | numeric(13) |  |  | Ressarcimento de ICMS ST período anterior |
| RESSARCIMENTO_SUBTRI_PERIODO_SEGUINTE | numeric(13) |  |  | Ressarcimento de ICMS ST período seguinte |
| SEQUENCIAL_RESSARCIMENTO_ACUMULADO | integer(4) |  |  | Sequencial indicador do valor de ressarcimento acumulado |
