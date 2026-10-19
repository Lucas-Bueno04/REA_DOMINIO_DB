# HRLANCAMENTO_PAGAR_PARCELA — Lancamentos de contas a pagar - Parcelas
8.259 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_PAGAR | integer(4) | PK |  | Lancamento a pagar |
| I_PARCELA | integer(4) | PK |  | Codigo |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| VALOR | numeric(13) |  |  | Valor da parcela |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Possivel conta para pagamento |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_IRRF | numeric(13) |  |  | Valor IRRF aproveitado |
| VALOR_ISS_RETIDO | numeric(13) |  |  | Valor de ISS Retido |
| VALOR_INSS_RETIDO | numeric(13) |  |  | Valor de INSS Retido |
| VALOR_CRF | numeric(13) |  |  | Valor de CRF aproveitado |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor original sem retenções |
| DOCUMENTO | integer(4) |  |  | Documento da Parcela |
