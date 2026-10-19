# EFCUPOM_FISCAL_ELETRONICO_PARCELAS — Cupom Fiscal Eletrônico - CF-e - Parcelas
378 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CFE | integer(4) | PK |  | Código do CF-e |
| I_PARCELA | integer(4) | PK |  | Número da parcela |
| VENCIMENTO | date(4) |  |  | Data de vencimento da parcela |
| VALOR | numeric(13) |  |  | Valor da Parcela |
| NUMERO_TITULO | varchar(60) |  | S | Número do título |
| CODI_ACU | integer(4) |  | S | Acumulador |
