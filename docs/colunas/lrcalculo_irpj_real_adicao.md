# LRCALCULO_IRPJ_REAL_ADICAO — Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Adições
815 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CALCULO | integer(4) | PK |  | Código do cálculo |
| I_ADICAO | integer(4) | PK |  | Adição |
| VALOR | numeric(13) |  |  | Valor |
| VALOR_GERAL | numeric(13) |  |  | Valor - Geral |
| VALOR_RURAL | numeric(13) |  |  | Valor - Rural |
| AJUSTE_ANUAL | integer(4) | PK |  | Ajuste Anual |
