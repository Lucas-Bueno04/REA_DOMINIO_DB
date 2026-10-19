# EFMVEPRO_ICMSA — Notas Fiscais de Entrada - Produtos - ICMS Antecipado
1.182 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_ENT | integer(4) | PK |  | Código sequencial da nota de entrada |
| NUME_MEP | integer(4) | PK |  | Código sequencial do estoque |
| CODI_PDI | char(14) |  |  | Código do produto |
| I_RECOLHIMENTO_ICMSA | integer(4) |  | S | Código Sequencial do Recolhimento - ICMS Antecipado |
| CODIGO_RECOLHIMENTO_ICMSA | char(6) |  | S | Código do Recolhimento - ICMS Antecipado |
| CODIGO_TRIBUTACAO_ICMSA | integer(4) |  | S | Código de tributação do produto ICMS Antecipado |
| BASE_CALCULO_ICMSA | numeric(13) |  |  | Base cálculo ICMS Antecipado |
| ALIQUOTA_ICMSA | numeric(7) |  |  | Alíquota ICMS Antecipado |
| VALOR_ICMSA | numeric(13) |  |  | Valor ICMS Antecipado |
