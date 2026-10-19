# FOSINDICATOS_GARANTIA_SEMESTRAL — Garantia semestral.
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato |
| I_REGRAS | integer(4) | PK |  | Código da regra |
| I_REGRASEQ | integer(4) | PK |  | Sequencial da regra |
| CAMPO | smallint(2) |  |  | Campo. (1=Motivo da rescisão/2=Meses trabalhados/3=Data admissão/4=Data demissão) |
| QUANTIDADE | smallint(2) |  | S | Quantidade de meses trabalhados/Motivo da rescisão. |
| OPERADOR_COMPARACAO | smallint(2) |  |  | Operador de comparação. (1-Igual/2=Maior que/3=Menor que/4=Maior igual/5=Menor igual) |
| OPERADOR_LOGICO | smallint(2) |  |  | Operador lógico: (1=E/2=Ou/3=Resultado) |
| TIPO_PAGAMENTO | smallint(2) |  |  | Tipo de pagamento. (1=Dias restantes do semestre/2=Pagar 1/12 avos a cada mês até o restante do semestre/3=Pagar durante o recesso escolar/4=Pagar até a data fim) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| DATA_COMPARACAO | date(4) |  | S | Data para comparaÃ§Ã£o. |
| VIGENCIA_INICIAL | date(4) |  | S | Vigência inicial. |
| VIGENCIA_FINAL | date(4) |  | S | Vigência final. |
| INICIO_PAGAMENTO | date(4) |  | S | Início pagamento. |
| FIM_PAGAMENTO | date(4) |  | S | Fim pagamento. |
| SOMAR_CONDICOES | smallint(2) |  |  | Somar condições. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
