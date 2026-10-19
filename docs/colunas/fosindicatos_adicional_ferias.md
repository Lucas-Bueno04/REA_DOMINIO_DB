# FOSINDICATOS_ADICIONAL_FERIAS — Cadastro de sindicatos - Percentual de adicional de férias
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato |
| I_REGRAS | integer(4) | PK |  | Código da regra |
| I_REGRASEQ | integer(4) | PK |  | Sequencial da regra |
| CAMPO | smallint(2) |  |  | Campo. (1=Meses trabalhados/2=Falta justificada/3=Falta injustificada/4=Forma de cálculo/5=Salário base) |
| OPERADOR_COMPARACAO | smallint(2) |  |  | Operador de comparação: (1=Igual/2=Diferente/3=Maior que/4=Menor que/5=Maior igual/6=Menor igual) |
| VALOR_COMPARACAO | numeric(13) |  |  | Valor de comparação |
| OPERADOR_LOGICO | smallint(2) |  |  | Operador lógico: (1=E/2=OU/3=Resultado) |
| VALOR_RESULTADO | numeric(13) |  | S | Adicional de férias |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
| BASE_CALCULO | smallint(2) |  | S | Base de cálculo. (1=Salário contratual/2=Salário base/3=Piso salarial/10=Salário, médias e adicionais) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
