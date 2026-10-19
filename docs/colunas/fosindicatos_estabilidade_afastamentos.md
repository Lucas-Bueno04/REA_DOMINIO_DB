# FOSINDICATOS_ESTABILIDADE_AFASTAMENTOS — Cadastro de Sindicatos - Estabilidade Afastamentos
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato |
| I_REGRAS | integer(4) | PK |  | Código da regra |
| I_REGRASEQ | integer(4) | PK |  | Sequencial da regra |
| I_AFASTAMENTOS | integer(4) |  | S | Código do afastamento |
| OPERADOR_COMPARACAO | smallint(2) |  |  | Operador de comparação. (1-Igual/2=Maior que/3=Menor que/4=Maior igual/5=Menor igual/6=A cada) |
| DIAS_AFASTAMENTO | integer(4) |  |  | Quantidade de dias afastamento |
| OPERADOR_LOGICO | smallint(2) |  |  | Operador lógico: (1=E/2=Ou/3=Resultado) |
| DIAS_APOS_RETORNO | integer(4) |  | S | Quantidade de dias após o retorno |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| CAMPO | smallint(2) |  |  | Campo. (1=Meses trabalhados/2=Afastamento/3=Data do parto) |
| LIMITE | integer(4) |  | S | Quantidade limite de dias de estabilidade. |
| FORMA_CALCULO_INDENIZACAO | smallint(2) |  |  | Forma de cálculo quando indenizado. (1=Valor fixo/2=Valor proporcional) |
| BASE_CALCULO_INDENIZACAO | smallint(2) |  |  | Base de cálculo quando indenizado. (1=Salário mínimo/2=Salário contratual/3=Salário base/4=Piso salarial/5=Valor informado) |
| VALOR_INDENIZACAO | numeric(13) |  | S | Valor quando indenizado. |
| UTILIZAR_DIAS_AFASTADOS | smallint(2) |  |  | Utilizar os dias afastados como dias de estabilidade. (0=Não/1=Sim) |
| DEFINIR_UNIDADE_CALCULO | smallint(2) |  |  | Definir a unidade de cálculo. (0=Não/1=Sim) |
| UNIDADE_CALCULO | smallint(2) |  |  | Unidade de cálculo. (1=Percentual) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
