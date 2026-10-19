# EFSAIDAS_ESTADUAL_BA — Notas Fiscais de Saídas - Dados estaduais - BA
13 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da saída |
| TIPO_OPERACAO | integer(4) |  |  | Tipo da operação |
| AQUISICAO_EFETUADA_RECURSO_CONVENIADO | char(1) |  |  | Aquisição efetuada com recursos conveniados |
| AQUISICAO_EFETUADA_RECURSO_CONVENIADO_TIPO | integer(4) |  |  | Aquisição efetuada com recursos conveniados - Tipo (1/2/3) |
| NUMERO_CONVENIO | varchar(16) |  |  | Número Convênio |
| NUMERO_EMPENHO | varchar(9) |  |  | Número Empenho |
| CODIGO_MUNICIPIO | integer(4) |  | S | Codigo sequencial do Município |
| BASE_CALCULO_ICMS_SN | numeric(13) |  |  | Base de Cálculo |
| ALIQUOTA_ICMS_SN | numeric(5) |  |  | Alíquota |
| VALOR_ICMS_SN | numeric(13) |  |  | Valor |
