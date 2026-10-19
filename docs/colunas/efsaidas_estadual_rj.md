# EFSAIDAS_ESTADUAL_RJ — Notas Fiscais de Saídas - Dados estaduais - RJ
8.745 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da saída |
| CODIGO_VALOR_ADICIONADO | integer(4) |  |  | Código do valor adicionado para a DECLAN-IPM |
| VALOR_ADICIONADO | numeric(13) |  |  | Valor adicionado para a DECLAN-IPM |
| PRECO_SEM_ABATIMENTO | numeric(13) |  |  | Preço da mercadoria sem abatimento |
| VALOR_ICMS_ABATIDO | numeric(13) |  |  | Valor do ICMS abatido |
| I_DUB_ICMS | integer(4) |  | S | Outros benefícios para informação no DUB-ICMS - Código |
| DUB_ICMS_VALOR_OPERACAO | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor da operação |
| DUB_ICMS_ALIQUOTA | numeric(5) |  |  | Outros benefícios para informação no DUB-ICMS - Alíquota |
| DUB_ICMS_VALOR_ICMS_NAO_RECOLHIDO | numeric(13) |  |  | Outros benefícios para informação no DUB-ICMS - Valor do ICMS não recolhido |
