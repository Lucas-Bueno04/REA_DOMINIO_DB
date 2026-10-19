# eftabela_simples_nacional_estadual — Tabela de calculo do Simples Nacional - Impostos Estaduais
75.965 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| uf | char(2) | PK |  | Sigla da UF |
| vigencia | date(4) | PK |  | Vigencia |
| anexo | tinyint(1) | PK |  | Anexo |
| secao | tinyint(1) | PK |  | Secao |
| tabela | tinyint(1) | PK |  | Tabela |
| faixa | integer(4) | PK |  | Numero da faixa |
| inicial | numeric(13) |  |  | Valor inicial da faixa |
| final | numeric(13) |  |  | Valor final da faixa |
| icms | numeric(5) |  |  | Aliquota do ICMS |
| base_calculo | numeric(13) |  |  | Base de calculo do imposto |
| VALIDADE | date(4) |  | S | Data de validade da tabela |
| PORTE | char(1) | PK |  | Porte (E - EPP/M - ME/N - Normal/T - Todos) |
| ALIQUOTA_NOMINAL | numeric(7) |  |  | Alíquota Nominal |
| VALOR_A_DEDUZIR | numeric(13) |  |  | Valor a Deduzir |
| PR_USAR_5_FAIXA_PARA_CALCULAR_ALIQUOTA_EFETIVA_ICMS | char(1) |  |  | PR - Quando enquadrada na 6° faixa, aplicar a redução da 5° faixa na base de cálculo do ICMS |
| BASE_CALCULO_REGIME_CAIXA | numeric(13) |  |  | Base de calculo do imposto - Regime de Caixa |
