# EFSDOIMP_SUBTRI_POR_UF_RJ — Saldo dos Impostos - Substituição Tributária Por RJ
508 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| DEBITO_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| DEBITO_FECP_ST | numeric(13) |  |  | Débito FECP/ST |
| SALDO_DEVEDOR_FECP_ST | numeric(13) |  |  | Saldo devedor FECP/ST |
| VALOR_FECP_ST_APROVEITADO | numeric(13) |  |  | Valor FECP/ST Aproveitado |
| VALOR_STAT_DEVOLUCAO_RESP_SOLIDARIO | numeric(13) |  |  | Valor ST/AT Responsavel Solidario |
| COMPLEMENTO_SUBTRI | numeric(13) |  |  | Complemento de ICMS ST |
| RESSARCIMENTO_SUBTRI | numeric(13) |  |  | Ressarcimento de ICMS ST |
| RESSARCIMENTO_SUBTRI_PERIODO_ANTERIOR | numeric(13) |  |  | Ressarcimento de ICMS ST período anterior |
| RESSARCIMENTO_SUBTRI_PERIODO_SEGUINTE | numeric(13) |  |  | Ressarcimento de ICMS ST período seguinte |
