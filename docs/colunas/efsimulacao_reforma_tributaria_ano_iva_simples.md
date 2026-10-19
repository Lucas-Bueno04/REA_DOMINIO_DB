# EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA_SIMPLES — Simulador Reforma Tributaria - IVA Detalhamento Simples Nacional
14 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| REFORMA_TRIBUTARIA_ANO | integer(4) | PK |  | Reforma tributaria conforme ano |
| CODI_IVA | integer(4) | PK |  | Codigo imposto IVA |
| VALOR_IRPJ | numeric(13) |  |  | Valor IRPJ |
| VALOR_CSLL | numeric(13) |  |  | Valor CSLL |
| VALOR_INSS | numeric(13) |  |  | Valor INSS |
| VALOR_IPI | numeric(13) |  |  | Valor IPI |
| VALOR_ICMS | numeric(13) |  |  | Valor ICMS |
| VALOR_ISS | numeric(13) |  |  | Valor ISS |
