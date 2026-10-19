# EFSAIDAS_NOTA_DEVOLVIDA — Notas Fiscais de Saída - Complementar - Geral - Nota Devolvida
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da Saída |
| I_NOTA_DEVOLVIDA | integer(4) | PK |  | Sequencial |
| I_ENTRADA_DEVOLVIDA | integer(4) |  | S | Código da Entrada |
| DATA_DEVOLVIDA | date(4) |  |  | Data da Devolução |
| VALOR_NOTA | numeric(13) |  |  | Valor da Nota |
| VALOR_PAGO | numeric(13) |  |  | Valor Pago |
| VALOR_ABERTO | numeric(13) |  |  | Valor em Aberto |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor da Devolução |
| VALOR_DEDUCAO | numeric(13) |  |  | Valor da Dedução |
| VALOR_BAIXA | numeric(13) |  |  | Valor Baixa |
| VALOR_JA_DEVOLVIDO | numeric(13) |  |  | Valor já Devolvido |
| VALOR_RETENCOES | numeric(13) |  |  | Valor Retenções |
