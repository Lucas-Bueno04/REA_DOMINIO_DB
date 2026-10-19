# eftabela_simples_nacional_federal — Tabela de calculo do Simples Nacional - Impostos Federais
5.782 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| vigencia | date(4) | PK |  | Vigencia |
| faixa | integer(4) | PK |  | Numero da faixa |
| anexo | tinyint(1) | PK |  | Anexo |
| secao | tinyint(1) | PK |  | Secao |
| tabela | tinyint(1) | PK |  | Tabela |
| inicial | numeric(13) |  |  | Valor inicial da faixa |
| final | numeric(13) |  |  | Valor final da faixa |
| aliquota | numeric(5) |  |  | Aliquota total |
| irpj | numeric(5) |  |  | Aliquota do IRPJ |
| csll | numeric(5) |  |  | Aliquota da CSLL |
| cofins | numeric(5) |  |  | Aliquota da COFINS |
| pis | numeric(5) |  |  | Aliquota do PIS |
| inss | numeric(6) |  |  | Aliquota do INSS |
| ipi | numeric(5) |  |  | Aliquota do IPI |
| tipo | char(1) |  |  | Tipo dos percentuais(A- Aliquota/P - Partilha) |
| VALIDADE | date(4) |  | S | Data de validade da tabela |
| VALOR_A_DEDUZIR | numeric(13) |  |  | Valor a Deduzir |
