# EFMVSPRO_IS — Nota Fiscais de Saidas - Produtos - IS (Imposto Seletivo)
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_SAI | integer(4) | PK |  | Código sequencial da nota de saida |
| NUME_MSP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código produto |
| CCLASS_TRIB_IS | char(6) |  |  | Classificação tributaria do imposto seletivo - IS |
| CST | integer(4) |  |  | CST do imposto IS |
| BASE_CALCULO | numeric(13) |  |  | Base cálculo IS |
| ALIQUOTA_AD_VALOREM_IS | numeric(5) |  |  | Alíquota Ad valorem (%) |
| QTDE_TRIB | numeric(13) |  |  | Quantidade tributada |
| ALIQUOTA_AD_REM_FIXA_IS | numeric(13) |  |  | Alíquota ad rem (Fixa) |
| VALOR | numeric(13) |  |  | Valor imposto |
