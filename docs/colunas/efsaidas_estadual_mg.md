# EFSAIDAS_ESTADUAL_MG — Notas Fiscais de Saídas - Dados estaduais - MG
35 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código da saída |
| TIPO_TRANSPORTE_REALIZADO | char(1) |  |  | Tipo do transporte realizado(C - Com Conhecimento de Transportes - CTRC/S - Sem Conhecimento de Transportes - CTRC) |
| BASE_CALCULO_ICMS_SN | numeric(13) |  |  | Base de Cálculo |
| ALIQUOTA_ICMS_SN | numeric(5) |  |  | Alíquota |
| VALOR_ICMS_SN | numeric(13) |  |  | Valor |
