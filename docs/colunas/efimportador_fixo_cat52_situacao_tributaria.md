# EFIMPORTADOR_FIXO_CAT52_SITUACAO_TRIBUTARIA — Configuração do leiaute CAT52 do Importador Fixo - Situação tributária
7.140 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_SITUACAO | integer(4) | PK |  | Sequencial da situação tributária |
| OPERACAO | integer(4) |  |  | Operação |
| CFOP | integer(4) |  |  | CFOP |
| VERSAO_CFOP | smallint(2) |  |  | Versão CFOP |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| SELECAO_MEIO_PAGAMENTO | char(1) |  |  | Seleção do meio de pagamento |
| SELECAO_PRODUTO | char(1) |  |  | Seleção do produto |
| SELECAO_ALIQUOTA | char(1) |  |  | Seleção da alíquota |
| DETALHAMENTO_OUTROS_VALORES_MG | integer(4) |  |  | MG - Detalhamento de outros valores |
| SELECAO_NCM | char(1) |  |  | Seleção do NCM |
| SELECAO_GRUPO | char(1) |  |  | Seleção do grupo |
