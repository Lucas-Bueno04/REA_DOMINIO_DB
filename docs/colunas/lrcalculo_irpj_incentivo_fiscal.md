# LRCALCULO_IRPJ_INCENTIVO_FISCAL — Cálculo do Lalur - Imposto IRPJ - Detalhamento de Incentivos Fiscais
212 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| I_IRPJ_INCENTIVO_FISCAL | integer(4) | PK |  | Código do movimento do Incentivo Fiscal |
| VALOR_REAL | numeric(13) |  |  | Valor aproveitado - Real |
| VALOR_ESTIMADO | numeric(13) |  |  | Valor aproveitado - Estiamdo |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
| VALOR_ANTES_LC224_REAL | numeric(13) |  | S | Valor real do incentivo fiscal antes da redução LC 224/25 (sem fator 0,90) |
| VALOR_ANTES_LC224_ESTIMADO | numeric(13) |  | S | Valor estimado do incentivo fiscal antes da redução LC 224/25 (sem fator 0,90) |
