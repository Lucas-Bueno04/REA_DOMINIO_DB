# EFSDOIMP_IRPJ_IRRF_RETIDO — Saldo dos Impostos - IRRF Retido
4.062 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Data |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| NATUREZA | integer(4) | PK |  | Natureza |
| PERIODO_APURACAO | date(4) | PK |  | Período de apuração da retenção |
| TIPO_RETENCAO | integer(4) | PK |  | Tipo retenção - 1-Retido / 2-Propaganda |
| VALOR_RETIDO | numeric(13) |  |  | Valor Retido |
| VALOR_RETIDO_UTILIZADO | numeric(13) |  |  | Valor Retido Utilizado |
| VALOR_RETIDO_DISPONIVEL | numeric(13) |  |  | Valor Retido Disponível |
