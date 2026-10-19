# FOEMPRESTIMOS_CONSIGNADOS — Empréstimos consignados.
757 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| I_EMPRESTIMO | integer(4) | PK |  | Código do empréstimo. |
| DESCRICAO | varchar(100) |  |  | Descrição. |
| DATA_INICIO_CONTRATO | date(4) |  |  | Data de início do contrato. |
| DATA_INICIO_DESCONTO | date(4) |  |  | Data de início do desconto na empresa |
| VALOR | numeric(13) |  |  | Valor do empréstimo. |
| QUANTIDADE_PARCELAS | smallint(2) |  |  | Quantidade de parcelas em que será pago o desconto. |
| RUBRICA_DESCONTO | integer(4) |  |  | Rubrica para desconto do empréstimo. |
| RUBRICA_DESCONTO_FERIAS | integer(4) |  | S | Rubrica para desconto do empréstimo no cálculo de férias. |
| DESCONTAR_CALCULO_AFASTAMENTO | smallint(2) |  |  | Descontar durante o período de afastamento. (0=Não/1=Sim) |
| LISTA_AFASTAMENTOS_DESCONTAR | smallint(2) |  |  | Afastamentos que descontam o empréstimo. |
| DESCONTAR_CALCULO_FERIAS | smallint(2) |  |  | Descontar no cálculo de férias. (0=Não/1=Sim) |
| DESCONTAR_CALCULO_13_INTEGRAL | smallint(2) |  |  | Descontar no cálculo de 13º integral. (0=Não/1=Sim) |
| DESCONTAR_SOMENTE_PARCELA_MENSAL_RESCISAO | smallint(2) |  |  | Descontar somente a parcela mensal na rescisão. (0=Não/1=Sim) |
| DESCONTAR_RESTANTE_EMPRESTIMO_RESCISAO | smallint(2) |  |  | Descontar o valor restante de empréstimo na rescisão. (0=Não/1=Sim) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| TIPO_DESCONTO_MENSAL_COMPETENCIA_FERIAS | smallint(2) |  |  | Tipo de desconto na folha mensal em competência com cálculo de férias. (0=Não descontar na folha mensal em competência com dias de férias/1=Descontar na competência de início das férias/2=Descontar na competência fim das férias/3=Descontar nas competência |
| LIMITAR_DESCONTO_LIQUIDO_RESCISAO | smallint(2) |  |  | Limitar o desconto a um percentual do líquido da rescisão. (0=Não/1=Sim) |
| PERCENTUAL_LIMITAR_DESCONTO_LIQUIDO_RESCISAO | numeric(5) |  | S | Percentual para limitar o desconto ao líquido da rescisão. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| LIMITAR_DESCONTO_LIQUIDO_FOLHA | smallint(2) |  |  | Limitar o desconto a um percentual do líquido da folha mensal. (0=Não/1=Sim). |
| PERCENTUAL_LIMITAR_DESCONTO_LIQUIDO_FOLHA | numeric(5) |  |  | Percentual para limitar o desconto ao líquido da folha mensal. |
| DESCONTO_DIFERENCA_PARCELA | smallint(2) |  |  | Não descontar do colaborador a diferença entre o valor da parcela e o efetivamente pago. (0=Não/1=Sim) |
| I_BANCOS | integer(4) |  | S | Codigo de identificacao do banco na tabela fobancos |
| NUMERO_CONTRATO | varchar(15) |  | S | Numero de contrato do eConsignado |
| TIPO_EMPRESTIMO | smallint(2) |  |  | 1/Crédito do Trabalhador 2/Crédito Consignado |
| LIMITAR_DESCONTO_LIQUIDO_RESCISAO_PARCELAS | smallint(2) |  |  | 1/Para quitar parcela mensal 2/Para quitar parcelas abertas |
| DATA_FIM_CONTRATO | date(4) |  | S | Data final do contrato de empréstimo |
| DATA_INICIO_DESCONTO_EMPRESTIMO | date(4) |  | S | Data de início do desconto do emprestímo |
| PROVISIONAR_VALOR_PARCELA_FOLHA_ADIANTAMENTO | smallint(2) |  |  | Provisionar o valor da parcela do empréstimo na Folha de Adiantamento (0=Não/1=Sim) |
| PROVISIONAR_VALOR_PARCELA_FOLHA_ADIANTAMENTO_RUBRICA | integer(4) |  | S | Provisionar o valor da parcela do empréstimo na Folha de Adiantamento - Rubrica |
| PROVISIONAR_VALOR_PARCELA_FERIAS | smallint(2) |  |  | Provisionar o valor da parcela do empréstimo nas Férias (0=Não/1=Sim) |
| PROVISIONAR_VALOR_PARCELA_FERIAS_RUBRICA | integer(4) |  | S | Provisionar o valor da parcela do empréstimo nas Férias - Rubrica |
| FORMA_PROVISIONAR_VALOR_PARCELA_FERIAS | smallint(2) |  |  | 1 - integral, independete dos dias gozados, 2 - proporcional aos dias gozados |
| PERCENTUAL_GARANTIA_RESCISAO | numeric(5) |  | S | Percentual da garantia ofertada para desconto na rescisao |
| VALOR_SALDO_DEVEDOR_GARANTIA | numeric(13) |  | S | Saldo devedor da garantia ofertada para desconto na rescisao |
| DATA_CADASTRO | date(4) |  | S | Data de cadastro do emprestimo |
