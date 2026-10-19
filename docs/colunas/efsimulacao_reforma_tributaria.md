# EFSIMULACAO_REFORMA_TRIBUTARIA — Simulador Reforma Tributaria
38 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| TIPO_CALCULO | char(1) |  |  | Tipo Calculo (Simples/Normal) |
| ALIQUOTA_CBS | numeric(5) |  |  | Alíquota CBS |
| ALIQUOTA_IBS | numeric(5) |  |  | Alíquota IBS |
| BASE_CALCULO_IVA | char(1) |  |  | Base calculo IVA |
| REDUCAO_ALIQUOTA | numeric(5) |  |  | Reducao aliquota |
| CALCULAR_CREDITO_FORNECEDOR_SIMPLES | char(1) |  |  | Calcular credito de IVA para fornecedor simples nacional |
| FORMA_CALCULO | integer(4) |  |  | FORMA_CALCULO IN (1, 2) |
| PRODUTOS_REDUCAO_ALIQUOTA | char(1) |  |  | Produtos com redução de alíquota |
| CONSIDERA_IMPOSTOS_RETIDOS_COMPENSAR | char(1) |  |  | Considerar os impostos retidos a compensar |
| ATIVIDADE_REDUCAO_ALIQUOTA | char(1) |  |  | Atividade com redução de aliquota |
