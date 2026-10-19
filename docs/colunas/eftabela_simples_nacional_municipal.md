# eftabela_simples_nacional_municipal — Tabela de calculo do Simples Nacional - Impostos Municipais
11.151 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| municipio | integer(4) | PK |  | Codigo federal do municipio |
| vigencia | date(4) | PK |  | Vigencia |
| faixa | integer(4) | PK |  | Numero da faixa |
| anexo | tinyint(1) | PK |  | Anexo |
| secao | tinyint(1) | PK |  | Secao |
| tabela | tinyint(1) | PK |  | Tabela |
| inicial | numeric(13) |  |  | Valor inicial da faixa |
| final | numeric(13) |  |  | Valor final da faixa |
| iss | numeric(5) |  |  | Aliquota do ISS |
| base_calculo | numeric(13) |  |  | Base de calculo do imposto |
| VALIDADE | date(4) |  | S | Data de validade da tabela |
| REDUCAO_ISS | char(1) |  |  | Redução ISS |
| ALIQUOTA_REDUCAO_ISS | numeric(5) |  |  | Percentual de redução do ISS - Alíquota |
| PERCENTUAL_REDUCAO_ISS | numeric(5) |  |  | Percentual de redução do ISS - Percentual |
