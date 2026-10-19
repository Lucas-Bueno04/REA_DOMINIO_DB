# EFPLANEJAMENTO_TRIBUTARIO_TABELA_SIMPLES_FAIXAS — Planejamento Tributário - Tabela Simples Faixas
120 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ANEXO | integer(4) | PK |  | Anexo |
| TIPO_ANEXO | char(1) | PK |  | Tipo (Normal - Exportacao) |
| VIGENCIA | date(4) | PK |  | Vigencia |
| FAIXA | integer(4) | PK |  | Faixa |
| RECEITA_INICIAL | numeric(13) |  |  | Receita Bruta Inicial |
| RECEITA_FINAL | numeric(13) |  |  | Receita Bruta Final |
| ALIQUOTA | numeric(5) |  |  | Aliquota |
| VALOR_DEDUCAO | numeric(13) |  |  | Valor a deduzir |
| PERC_IRPJ | numeric(5) |  |  | Percentual IRPJ |
| PERC_CSLL | numeric(5) |  |  | Percentual CSLL |
| PERC_INSS | numeric(5) |  |  | Percentual INSS |
| PERC_IPI | numeric(5) |  |  | Percentual IPI |
| PERC_ICMS | numeric(5) |  |  | Percentual ICMS |
| PERC_ISS | numeric(5) |  |  | Percentual ISS |
| PERC_CBS | numeric(5) |  |  | Percentual CBS |
| PERC_IBS | numeric(5) |  |  | Percentual IBS |
