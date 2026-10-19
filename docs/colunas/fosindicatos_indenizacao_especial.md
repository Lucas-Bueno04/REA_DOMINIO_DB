# FOSINDICATOS_INDENIZACAO_ESPECIAL — Cadastro de Sindicatos - Indenização Especial
27 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato |
| I_REGRAS | integer(4) | PK |  | Código da regra |
| I_REGRASEQ | integer(4) | PK |  | Sequencial da regra |
| CAMPO | smallint(2) |  |  | Campo. (1=Idade/2=Meses trabalhados/3=Motivo demissão/4=CBO 2002/5=Piso salarial/6=Salário base/7=Motivo afastamento/8=Vínculo empregatício/9=Data de demissão) |
| OPERADOR_COMPARACAO | smallint(2) |  |  | Operador de comparação: (1=Igual/2=Maior que/3=Menor que/4=Maior igual/5=Menor igual/6=A cada quantidade completa de/7=A cada quantidade completa ou superior a metade de) |
| VALOR_COMPARACAO | char(13) |  |  | Valor de comparação |
| OPERADOR_LOGICO | smallint(2) |  |  | Operador lógico: (1=E/2=Ou/3=Resultado) |
| DIAS_INDENIZADOS | numeric(5) |  | S | Dias indenizados |
| LIMITE | numeric(5) |  | S | Limite |
| BASE_CALCULO | smallint(2) |  | S | Base de cálculo: (1=Salário contratual/2=Salário base/3=Piso salarial/4=Mesma base do aviso prévio/5=Salário mínimo federal/6=Aviso prévio) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: 0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão |
| VALOR_COMPARACAO_FINAL | numeric(13) |  | S | Valor final de comparação |
| TIPO_INDENIZACAO | smallint(2) |  |  | Tipo de indenização.(1=Rescisão/2=Afastamento/3=Aviso Prévio) |
| UNIDADE_RESULTADO | smallint(2) |  |  | Unidade do resultado. (1=Dias/2=Valor/3=Percentual) |
| VALOR_INDENIZACAO | numeric(13) |  | S | Valor da indenização. |
| TIPO_FOLHA | smallint(2) |  |  | Tipo de folha. (1=Folha mensal do início do afastamento/2=Folha mensal do retorno do afastamento) |
| VINCULO_EMPREGATICIO | smallint(2) |  | S | Vínculo empregatício. (1=Cel./3=Trab. avulso não port./4=Trab. temp. Lei6.019/74/5=Cel. cont. prazo det./6=Trab. rural/9=Trab. rural cont. prazo det./10=Cont. prazo det. Lei9.601/98/52=Emp. dom./53=Aprendiz/54=Emp. Dom. Reg. Tempo Parc./55=Trab. Rural Tempo Parc./56=Celetista Contrato Intermitente/59=Trab. Avulso Port./60=Contrato verde amarelo com acordo./61=Contrato verde amarelo sem acordo./62=Celetista Trabalhador Cedido/99=Cel. reg. tempo parc.) |
| DATA_CONSIDERAR | date(4) |  | S | Data para considerar na regra. |
| PARCELAR | smallint(2) |  |  | Parcelar. (0=Não/1=Sim) |
| INICIO_PARCELAMENTO | smallint(2) |  | S | Início do parcelamento. (1=Na rescisão normal/2=Na rescisão complementar) |
| QUANTIDADE_PARCELAS | smallint(2) |  | S | Quantidade de parcelas. |
| ACRESCENTAR_DIAS_APOS_CADA_ANO_IDADE_COMPLETO | smallint(2) |  | S | Acrescentar dias informados para cada ano de idade completo. (0=Não/1=Sim) |
| CONSIDERAR_ANO_IDADE_COMPLETO_A_PARTIR_6_MESES_COMPLETOS | smallint(2) |  | S | Considerar ano de idade completo a partir de 6 meses completos. (0=Não/1=Sim) |
| SOMAR_CONDICOES | smallint(2) |  | S | Somar condições. (0=Não/1=Sim) |
| ACRESCENTAR_DIAS_INFORMADOS_ANO_COMPLETO_APOS_QUANTIDADE_MESES_TRABALHADOS_INFORMADOS | smallint(2) |  |  | Acrescentar os dias informados a cada ano completo após a quantidade de meses trabalhados informados. (0=Não/1=Sim) |
| ACRESCENTAR_PERCENTUAL_INFORMADO_CADA_ANO_COMPLETO_APOS_QUANTIDADE_MESES_TRABALHADOS | smallint(2) |  |  | Acrescentar o percentual informado a cada ano completo após a quantidade de meses trabalhados informados. (0=Não/1=Sim) |
| INFORMAR_PERIODO | smallint(2) |  |  | Informar período. (0=Não/1=Sim) |
| PERIODO_INICIAL | date(4) |  | S | Período inicial. |
| PERIODO_FINAL | date(4) |  | S | Período final. |
| DEFINIR_LIMITE_VALOR | smallint(2) |  |  | Definir limite para o valor de indenização. (0=Não/1=Sim) |
| VALOR_LIMITE_INICIAL | numeric(13) |  | S | Valor limite inicial. |
| VALOR_LIMITE_FINAL | numeric(13) |  | S | Valor limite final. |
| ACRESCENTAR_DIAS_INDENIZADOS_SOMENTE_A_PARTIR_INICIO_SEGUNDO_ANO_EMPRESA | smallint(2) |  |  | Acrescentar os dias indenizados somente a partir do segundo ano de empresa. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
