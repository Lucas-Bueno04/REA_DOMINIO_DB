# FOMEDIDAS_PROTECAO_EMPREGO_COVID_19_PRORROGACAO_ANTECIPACAO — Relacionamento entre medidas (prorrogadas, antecipadas) de proteção ao empregado devido a COVID-19
43 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| DATA_INICIO | date(4) | PK |  | Data do início da vigência da medida |
| SEQUENCIAL | integer(4) | PK |  | Sequencial da tabela pai, chave primária. |
| SEQUENCIAL_PRORROGACAO_ANTECIPACAO | integer(4) | PK |  | Sequencial |
| TIPO | smallint(2) |  |  | Tipo de medida. (1=Prorrogação/2=Antecipação) |
| DATA_INICIO_PRORROGACAO_ANTECIPACAO | date(4) |  |  | Data do início da vigência da prorrogação/antecipação |
| DATA_FIM_PRORROGACAO_ANTECIPACAO | date(4) |  |  | Data do fim da vigência da prorrogação/antecipação |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
