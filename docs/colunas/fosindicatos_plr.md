# FOSINDICATOS_PLR — Configuração das regras para pagamento de PLR.
8 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato. |
| I_REGRAS | integer(4) | PK |  | Código da regra. |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial da regra. |
| VIGENCIA_INICIAL | date(4) |  |  | Vigência inicial. |
| VIGENCIA_FINAL | date(4) |  |  | Vigência final. |
| CAMPO | smallint(2) |  |  | Campo. (1=Faltas justificadas/2=Faltas injustificadas/3=Meses trabalhados/4=Idade/5=Cargo/6=Data admissão/7=Quant. de Empregados/8=Motivo afastamento/9=Faltas justificadas/injustificadas/10=Advertências/11=Suspensões/12=Advertências/Suspensões/13=Salário Base/14=Faltas parciais/15=Mês aniversário) |
| OPERADOR_COMPARACAO | smallint(2) |  |  | Operador de comparação. (1=Igual/2=Diferente/3=Maior que/4=Menor que/5=Maior igual/6=Menor igual/7=Entre/8=A cada) |
| OPERADOR_LOGICO | smallint(2) |  |  | Operador lógico. (1=E/2=Ou/3=Resultado) |
| VALOR_COMPARACAO | integer(4) |  |  | Valor de comparação. |
| UNIDADE | smallint(2) |  | S | Unidade. (1=Valor/2=Percentual/3=Dias/4=Mês/5=Semestre/6=Horas) |
| VALOR_UNIDADE | numeric(13) |  | S | Valor da unidade. |
| BASE_CALCULO | smallint(2) |  | S | Base de cálculo. (1=Salário contratual/2=Salário base/3=Piso salarial/4=Salário contratual da competência/5=Média vigência/6=Salário base da competência) |
| COMPETENCIA_PAGAMENTO | date(4) |  | S | Competência de pagamento. |
| TIPO_PROCESSO_PAGAMENTO | smallint(2) |  | S | Tipo processo pagamento. (11=Mensal/42=Complementar/52=Décimo terceiro integral/70=Participação de lucros) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| DATA_ADMISSAO | date(4) |  | S | Data de admissão para consideração na regra. |
| DESCONTAR_1_365_AVOS_VALOR_POR_CADA_FALTA_INJUSTIFICADA_PERIODO_VIGENCIA | smallint(2) |  |  | Desocntar o correspondente a 1/365 avos a cada falta injustificada dentro do período de vigência. (0=Não/1=Sim) |
| DEFINIR_LIMITE | smallint(2) |  |  | Definir limite. (0=Não/1=Sim) |
| VALOR_LIMITE | numeric(13) |  | S | Valor limite para pagamento do PLR. |
| UNIDADE_LIMITE | smallint(2) |  |  | Unidade. (1=Valor/2=Percentual/3=Dias/4=Mês/5=Semestre/6=Horas) |
| CALCULAR_PROPORCIONAL_MES_ADMISSAO | smallint(2) |  |  | Calcular proporcional ao mês de admissão. (0=Não/1=Sim) |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_01 | numeric(7) |  | S | Percentual proporcional para 01 mês trabalhado. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_02 | numeric(7) |  | S | Percentual proporcional para 02 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_03 | numeric(7) |  | S | Percentual proporcional para 03 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_04 | numeric(7) |  | S | Percentual proporcional para 04 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_05 | numeric(7) |  | S | Percentual proporcional para 05 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_06 | numeric(7) |  | S | Percentual proporcional para 06 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_07 | numeric(7) |  | S | Percentual proporcional para 07 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_08 | numeric(7) |  | S | Percentual proporcional para 08 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_09 | numeric(7) |  | S | Percentual proporcional para 09 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_10 | numeric(7) |  | S | Percentual proporcional para 10 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_11 | numeric(7) |  | S | Percentual proporcional para 11 meses trabalhados. |
| PERCENTUAL_PROPORCIONAL_ADMISSAO_MES_12 | numeric(7) |  | S | Percentual proporcional para 12 meses trabalhados. |
| DESCONTAR_20_POR_CENTO_VALOR_TOTAL_PLR_POR_CADA_FALTA_PERIODO_VIGENCIA | smallint(2) |  |  | Descontar 20% do valor total do PLR a cada falta justificada/injustificada dentro do período de vigência. (0=Não/1=Sim) |
| COMPETENCIA_SALARIO_BASE_CALCULO | date(4) |  | S | Competência do salário para a base de cálculo. |
| CALCULAR_AVOS | smallint(2) |  |  | Calcular em avos. (0=Não/1=Sim) |
| TIPO_DESCONTO_AVOS | smallint(2) |  | S | Tipo de desconto dos avos. (1=1/365/2=1/12/3=1/6) |
| TIPO | smallint(2) | PK |  | Tipo de configuração. (1=Pagamento/2=Desconto) |
| SALARIO_INICIAL | numeric(13) |  | S | Salário inicial. |
| SALARIO_FINAL | numeric(13) |  | S | Salário inicial. |
| VALOR_LIMITE_FINAL | numeric(13) |  | S | Valor final do limite. |
| PAGAMENTO_PARCELADO | smallint(2) |  |  | Pagamento parcelado. (0=Não/1=Sim) |
| QUANTIDADE_PARCELAS | smallint(2) |  | S | Quantidade de parcelas. |
| MESES_PAGAMENTO_PARCELAMENTO | smallint(2) |  | S | Soma binária dos meses para pagamento do parcelamento. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
