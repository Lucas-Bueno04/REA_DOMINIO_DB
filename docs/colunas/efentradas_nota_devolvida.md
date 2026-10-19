# EFENTRADAS_NOTA_DEVOLVIDA — Notas Fiscais de Entrada - Complementar - Geral - Nota Devolvida
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ENT | integer(4) | PK |  | Código da Entrada |
| I_NOTA_DEVOLVIDA | integer(4) | PK |  | Sequencial |
| TIPO_DOC_DEVOLVIDO | char(1) |  | S | TIPO DO DOCUMENTO FISCAL(S-SAÍDA/C-CUPOM FISCAL/F-CFE/Z-REDUÇÃO Z 2D) |
| I_SAIDA_DEVOLVIDA | integer(4) |  | S | Código da Saída |
| I_REDUCAO_DEVOLVIDA | integer(4) |  | S | Código da ReduçãoZ |
| I_CUPOM_DEVOLVIDO | integer(4) |  | S | Código do Cupom Fiscal |
| DATA_DEVOLVIDA | date(4) |  |  | Data da Devolução |
| VALOR_NOTA | numeric(13) |  |  | Valor da Nota |
| VALOR_PAGO | numeric(13) |  |  | Valor Pago |
| VALOR_ABERTO | numeric(13) |  |  | Valor em Aberto |
| VALOR_DEVOLUCAO | numeric(13) |  |  | Valor da Devolução |
| VALOR_DEDUCAO | numeric(13) |  |  | Valor da Dedução |
| VALOR_BAIXA | numeric(13) |  |  | Valor Baixa |
| VALOR_JA_DEVOLVIDO | numeric(13) |  |  | Valor já Devolvido |
| VALOR_RETENCOES | numeric(13) |  |  | Valor Retenções |
| I_CFE_DEVOLVIDA | integer(4) |  | S | Código da CFE |
