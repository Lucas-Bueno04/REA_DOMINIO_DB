# EFPISCOFINS_OUTROS_SALDO_RETENCAO_ITEM — Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções - Retenções
26 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_COMPENSACAO_RETENCAO | integer(4) | PK |  | Código sequencial |
| PERIODO_APURACAO | date(4) | PK |  | Período da retenção |
| NATUREZA_RETENCAO | integer(4) | PK |  | Natureza da retenção |
| VALOR_TOTAL_RETENCAO | numeric(13) |  |  | Valor total da retenção |
| VALOR_JA_APROVEITADO | numeric(13) |  |  | Valor já aproveitado |
| VALOR_UTILIZADO_MEDIANTE_RESTITUICAO | numeric(13) |  |  | Valor utilizado mediante restituição |
| VALOR_UTILIZADO_MEDIANTE_DCOMP | numeric(13) |  |  | Valor utilizado mediante DCOMP |
| VALOR_RETENCAO_DISPONIVEL | numeric(13) |  |  | Valor da retenção disponível |
