# GESCP_VIGENCIA_INFORMATIVOS — Sociedade em Conta de Participação - SCP - Vigência Informativos
57 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_SCP | integer(4) | PK |  | Sequencial do SCP |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(100) |  |  | Descrição |
| FORMA_TRIBUTACAO | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO LUCRO (1 - LUCRO REAL / 2 - LUCRO REAL/ARBITRADO / 3 - LUCRO PRESUMIDO/REAL / 5 - LUCRO PRESUMIDO / 6 - LUCRO ARBITRADO / 7 - LUCRO PRESUMIDO/ARBITRADO / 8 - IMUNE DE IRPJ / 9 - ISENTO DO IRPJ) |
| PERIODO_APURACAO_IRPJ_CSLL | char(1) |  |  | Período de apuração do IRPJ e CSLL (T - Trimestral / A - Anual) |
| FORMA_TRIBUTACAO_TRIMESTRE_1 | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_2 | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_3 | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| FORMA_TRIBUTACAO_TRIMESTRE_4 | integer(4) |  |  | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
