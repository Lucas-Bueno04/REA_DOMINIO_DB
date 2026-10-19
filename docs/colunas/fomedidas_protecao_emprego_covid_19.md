# FOMEDIDAS_PROTECAO_EMPREGO_COVID_19 — Medidas de proteção ao empregado devido a COVID-19
777 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado |
| TIPO_MEDIDA | smallint(2) |  |  | Tipo de medida. (1=Redução de salário e carga horária/2=Suspensão integral sem remuneração/3=Suspensão integral com remuneração) |
| DATA_INICIO | date(4) | PK |  | Data do início da vigência da medida |
| DATA_FIM | date(4) |  |  | Data do fim da vigência da medida |
| TIPO_PERCENTUAL_REDUCAO | smallint(2) |  | S | Tipo de percentual de redução do salário. (1=Redução 25% MP 936/2=Redução 50% MP 936/3=Redução 70% MP 936/4=Percentual redução CCT) |
| DATA_ACORDO | date(4) |  | S | Data do acordo da medida |
| SITUACAO | smallint(2) |  |  | Situação da medida de proteção do emprego. (1=Válida/2=Alterada/3=Cancelada/4=Prorrogada/5=Antecipada) |
| SEQUENCIAL | integer(4) | PK |  | Sequencial usado para quando houver uma medida cancelada na mesma data de início ao empregado |
| REDUZIR_SALARIO_HORISTA | integer(4) |  |  | Reduzir o salario do horista. |
| REDUZIR_CARGA_HORARIA | integer(4) |  |  | Reduzir automaticamente a carga horária. |
| PERCENTUAL_REDUCAO | numeric(5) |  | S | Percentual de redução. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
