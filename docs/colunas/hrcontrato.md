# HRCONTRATO — Contrato
1.064 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CONTRATO | integer(4) | PK |  | Codigo |
| DESCRICAO | varchar(60) |  |  | Descricao |
| I_CLIENTE | integer(4) |  |  | Cliente |
| I_TIPO_CONTRATO | integer(4) |  |  | Tipo de contrato |
| I_EVENTO | integer(4) |  |  | Evento honorarios |
| DATA_EMISSAO | date(4) |  |  | Data de emissao |
| DATA_INICIO | date(4) |  |  | Inicio do contrato |
| DIA_VENCIMENTO | tinyint(1) |  |  | Dia de vencimento |
| DATA_INICIO_FATURAMENTO | date(4) |  |  | Inicio do faturamento |
| MES_VENCIMENTO | char(1) |  |  | Mes do vencimento N No mesmo mes A Apos o mes S No segundo mes |
| DEFINIR_TERMINO | char(1) |  |  | Definir data termino S N |
| DATA_TERMINO | date(4) |  | S | Data de termino |
| VALOR_CONTRATO | numeric(13) |  |  | Valor do contrato |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor original |
| NUMERO_CONTABIL | char(1) |  |  | Numero de lancamentos contabeis S N |
| ULTRAPASSAR_CONTABIL | integer(4) |  |  | Ultrapassar numero de lancamentos contabeis |
| MANUALMENTE_CONTABIL | char(1) |  |  | Lancamentos contabeis realizados manualmente S N |
| OUTRO_MODULO_CONTABIL | char(1) |  |  | Lancamentos contabeis gerador por outros modulos S N |
| IMPORTADO_CONTABIL | char(1) |  |  | lancamentos contabeis importados via arquivo S N |
| DATA_CONTABIL | char(1) |  |  | Considerar a data do lancamento contabil L Lancamento D Documento |
| NUMERO_FISCAL | char(1) |  |  | Numero de lancamentos fiscal S N |
| ULTRAPASSAR_FISCAL | integer(4) |  |  | Ultrapassar numero de lancamentos fiscais |
| MANUALMENTE_FISCAL | char(1) |  |  | Lancamentos fiscais realizados manualmente S N |
| IMPORTADO_FISCAL | char(1) |  |  | lancamentos fiscais importados via arquivo S N |
| DATA_FISCAL | char(1) |  |  | Considerar a data do lancamento fiscal L Lancamento D Documento |
| NUMERO_HORA | char(1) |  |  | Horas trabalhadas S N |
| MODULO_HORA | char(1) |  |  | Considerar modulo de horas trabalhadas T Todos E Especificar |
| ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas de todos os modulos |
| CONTABILIDADE_HORA | char(1) |  |  | Considerar modulo contabilidade horas trabalhadas S N |
| CONTABILIDADE_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo contabilidade |
| FOLHA_HORA | char(1) |  |  | Considerar modulo folha horas trabalhadas S N |
| FOLHA_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo folha |
| ESCRITA_HORA | char(1) |  |  | Considerar modulo escrita horas trabalhadas S N |
| ESCRITA_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo escrita |
| PATRIMONIO_HORA | char(1) |  |  | Considerar modulo patrimonio horas trabalhadas S N |
| PATRIMONIO_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo patrimonio |
| LALUR_HORA | char(1) |  |  | Considerar modulo lalur horas trabalhadas S N |
| LALUR_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo lalur |
| ATUALIZAR_HORA | char(1) |  |  | Considerar modulo atualizar horas trabalhadas S N |
| ATUALIZAR_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo atualizar |
| REGISTRO_HORA | char(1) |  |  | Considerar modulo registro horas trabalhadas S N |
| REGISTRO_ULTRAPASSAR_HORA | integer(4) |  |  | Ultrapassar horas trabalhadas do modulo registro |
| NUMERO_FUNCIONARIO | char(1) |  |  | Numero de funcionarios S N |
| ULTRAPASSAR_FUNCIONARIO | integer(4) |  |  | Ultrapassar numero de funcionarios |
| ATIVO_FUNCIONARIO | char(1) |  |  | Considerar funcionarios ativos no mes S N |
| DEMITIDO_FUNCIONARIO | char(1) |  |  | Considerar funcionarios demitidos no mes S N |
| CONTRIBUINTE_FUNCIONARIO | char(1) |  |  | Considerar contribuintes S N |
| VALOR_FATURAMENTO | char(1) |  |  | Valor do faturamento S N |
| VALOR_FATURAMENTO_ULTRAPASSAR | numeric(13) |  |  | Ultrapassar valor do faturamento |
| VALOR_FATURAMENTO_FILIAIS | char(1) |  |  | Considerar as filiais para o valor do faturamento S N |
| MODELO_CONTRATO | varchar(80) |  | S | Modelo de relatorio de contrato |
| I_OLE | integer(4) |  | S | Codigo do modelo ole |
| ADICIONAL_ANUAL | char(1) |  |  | Cobrar adicional anual S N |
| I_EVENTO_ADICIONAL | integer(4) |  | S | Evento da taxa adicional |
| VALOR_ADICIONAL | char(1) |  |  | Valor do adicional anul P Percentual I Informar valor |
| PERCENTUAL_ADICIONAL | numeric(5) |  |  | Percentual sobre o valor do contrato no adicional anul |
| INFORMAR_ADICIONAL | numeric(13) |  |  | Informar valor do adicional anul |
| PROPORCIONAL_ADICIONAL | char(1) |  |  | Proporcional a data de inicio do contrato S N |
| MESES_FATURAR_ADICIONAL | varchar(50) |  |  | Meses para faturar o adicional anul |
| FATURAR_CONTRATO_ADICIONAL | char(1) |  |  | Faturar com o contrato o adicional anul S N |
| MES_VENCIMENTO_ADICIONAL | char(1) |  |  | Mes do vencimento N No mesmo mes A Apos o mes S No segundo mes |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DATA_INICIO_ADICIONAL | date(4) |  | S | Inicio do faturamento do adicional anual |
| DIAS_FATURAR_ADICIONAL | varchar(128) |  |  | Dias para faturar o adicional anual |
| CALCULAR_EXCEDENTE_FATURAMENTO | char(1) |  |  | Calcular excedentes no faturamento (S/N) |
| DESCONTO_POR_ADIMPLENCIA | char(1) |  |  | Desconto por adrimplência |
| DESCONTO_POR_ADIMPLENCIA_MESES | integer(4) |  |  | Quantidade de meses adimplente |
| DESCONTO_POR_ADIMPLENCIA_PERCENTUAL | numeric(5) |  |  | Percentual adimplente |
| CONSIDERAR_VALOR_EVENTO_FIXO_ADICIONAL | char(1) |  |  | Considerar valor dos eventos fixos do adicional anual (S/N) |
| CONSIDERAR_VALOR_EVENTO_FIXO_OPCAO_ADICIONAL | char(1) |  |  | Considerar valor dos eventos fixos do adicional anual (V - Valor do último faturamento / M - Média dos últimos meses) |
| MEDIA_ULTIMO_MES_ADICIONAL | integer(4) |  |  | Média dos últimos X meses do adicional anual |
| CONSIDERAR_SOMENTE_MESES_COM_VALOR_ADICIONAL | char(1) |  |  | Considerar somente meses com valor (S/N) |
| CONSIDERAR_VALOR_COMPETENCIA_CALCULO_ADICIONAL | char(1) |  |  | Considerar os valores da competência de cálculo do adicional anual (S/N) |
| MODELO_DISTRATO | varchar(80) |  | S | Modelo do relatorio de distrato |
| I_OLE_DISTRATO | integer(4) |  | S | Codigo do modelo de ole |
| CONSIDERAR_VALOR_EXCEDENTE_CONTRATO_ADICIONAL | char(1) |  |  | Considerar valor dos excedentes de contrato |
| CONSIDERAR_VALOR_EXCEDENTE_CONTRATO_OPCAO_ADICIONAL | char(1) |  |  | Considerar valor dos excedentes de contrati do adicional anual (V - Valor do último faturamento / M - Média dos últimos meses) |
| CONSIDERAR_VALOR_EXCEDENTE_CONTRATO_MEDIA_ULTIMO_MES_ADICIONAL | integer(4) |  | S | Considerar valor da média dos últimos meses dos excedentes de contrato |
| CONSIDERAR_VALOR_EXCEDENTE_SOMENTE_MESES_COM_VALOR_ADICIONAL | char(1) |  |  | Considerar somente meses com valor adicional |
| CONSIDERAR_VALOR_EXCEDENTE_VALORES_COMPETENCIA_CALCULO_ADICIONAL | char(1) |  |  | Considerar os valores da competência de cálculo do adicional |
