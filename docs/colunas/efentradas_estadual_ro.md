# EFENTRADAS_ESTADUAL_RO — Notas Fiscais de Entradas - Dados Estaduais - RO
695 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| CODI_ENT | integer(4) | PK |  | Código da Nota de Entrada |
| I_ESTOQUE | integer(4) |  | S | Código do Lançamento do Estoque |
| DATA_LEVANTAMENTO | date(4) |  | S | Data do Levantamento do Estoque |
| VALOR_TOTAL_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Valor total do ICMS sobre o Estoque |
| VALOR_PARCELA_CREDITO | numeric(13) |  |  | Valor da parcela do crédito do Estoque |
| BASE_CALCULO_ICMS_SN | numeric(13) |  |  | Base de Cálculo ICMS Simples Nacional |
| ALIQUOTA_ICMS_SN | numeric(5) |  |  | Alíquota ICMS Simples Nacional |
| VALOR_ICMS_SN | numeric(13) |  |  | Valor ICMS Simples Nacional |
