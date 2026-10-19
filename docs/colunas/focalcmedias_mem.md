# focalcmedias_mem — Memoria de calculo
103.306 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) |  |  | Empresa |
| i_empregados | integer(4) |  |  | Empregado |
| tipo_media | tinyint(1) |  |  | is Tipo de media |
| data_calculo | date(4) |  |  | Data calculo |
| MESES_MEDIA_INI_QUANTIDADE | date(4) |  |  | Mês inicial da média |
| MESES_MEDIA_FIM_QUANTIDADE | date(4) |  |  | Mês final da média |
| inicio_aquisitivo | date(4) |  |  | Inicio aquisitivo |
| fim_aquisitivo | date(4) |  | S | Fim aquisitivo |
| sequencia | tinyint(1) |  | S | Sequencia |
| medias_horas | numeric(13) |  |  | Medias horas |
| medias_valor | numeric(13) |  |  | Valor medias |
| vantagem | numeric(13) |  |  | Valor vantagem |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| medias_haula | numeric(13) |  | S | Media hora-aula |
| CODI_EMP_ORIGEM | integer(4) |  |  | Código da empresa de origem |
| I_EMPREGADOS_ORIGEM | integer(4) |  |  | Código do empregado de origem |
| BASE_MEDIA_HORA | numeric(13) |  | S | Base de cálculo da média hora |
| BASE_MEDIA_HORA_AULA | numeric(13) |  | S | Base de cálculo da média hora aula |
| BASE_MEDIA_VALOR | numeric(13) |  | S | Base de cálculo da média valor |
| BASE_ADICIONAL | numeric(13) |  | S | Base de cálculo do adicional |
| SIMULACAO | integer(4) |  |  | Código sequencial da simulação |
| MAIS_FAVORAVEL | smallint(2) |  |  | Simulação mais favorável: 0=Não/1=Sim |
| TIPO_PERIODO_QUANTIDADE | smallint(2) |  |  | Tipo de período. (1=Últimos meses/2=Período aquisitivo/3=Ano corrente/4=Últimos meses no período aquisitivo/5=Últimos meses no ano corrente/6=Selecionar meses no ano corrente) |
| TIPO_CONSIDERAR_QUANTIDADE | smallint(2) |  |  | Valores a considerar. (1=Todos/2=Somente com valor/3=Maiores/4=Maiores e menores) |
| NMESES_QUANTIDADE_QUANTIDADE | integer(4) |  |  | Quantidade de meses |
| NMESES_QUANTIDADE_MAIORES_QUANTIDADE | integer(4) |  |  | Número de meses com os maiores valores |
| TIPO_PERIODO_VALOR | smallint(2) |  |  | Tipo de período. (1=Últimos meses/2=Período aquisitivo/3=Ano corrente/4=Últimos meses no período aquisitivo/5=Últimos meses no ano corrente/6=Selecionar meses no ano corrente) |
| TIPO_CONSIDERAR_VALOR | smallint(2) |  |  | Valores a considerar. (1=Todos/2=Somente com valor/3=Maiores/4=Maiores e menores) |
| NMESES_QUANTIDADE_VALOR | integer(4) |  |  | Quantidade de meses |
| NMESES_QUANTIDADE_MAIORES_VALOR | integer(4) |  |  | Número de meses com os maiores valores |
| MESES_MEDIA_INI_VALOR | date(4) |  |  | Mês inicial da média |
| MESES_MEDIA_FIM_VALOR | date(4) |  |  | Mês final da média |
| TIPO_CALCULO_13 | smallint(2) |  | S | Tipo de cálculo de 13: 1=Adiantamento/2=Adiantamento nas férias/3=Integral/4=Pago em rescisão/5=Ajuste em dezembro |
| CONSIDEROU_SALARIO_MES_ANTERIOR | smallint(2) |  |  | Considerou o salário do mês anterior: (0=Não/1=Sim) |
| I_CALCMEDIAS_MEM_OLD | integer(4) |  | S | Código - Renomeado |
| CONSIDERAR_JANEIRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de janeiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_FEVEREIRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de fevereiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MARCO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de março para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_ABRIL_QUANTIDADE | smallint(2) |  | S | Considerar o mês de abril para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MAIO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de maio para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JUNHO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de junho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JULHO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de julho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_AGOSTO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de agosto para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_SETEMBRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de setembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_OUTUBRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de outubro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_NOVEMBRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de novembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_DEZEMBRO_QUANTIDADE | smallint(2) |  | S | Considerar o mês de dezembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JANEIRO_VALOR | smallint(2) |  | S | Considerar o mês de janeiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_FEVEREIRO_VALOR | smallint(2) |  | S | Considerar o mês de fevereiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MARCO_VALOR | smallint(2) |  | S | Considerar o mês de março para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_ABRIL_VALOR | smallint(2) |  | S | Considerar o mês de abril para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MAIO_VALOR | smallint(2) |  | S | Considerar o mês de maio para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JUNHO_VALOR | smallint(2) |  | S | Considerar o mês de junho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JULHO_VALOR | smallint(2) |  | S | Considerar o mês de julho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_AGOSTO_VALOR | smallint(2) |  | S | Considerar o mês de agosto para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_SETEMBRO_VALOR | smallint(2) |  | S | Considerar o mês de setembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_OUTUBRO_VALOR | smallint(2) |  | S | Considerar o mês de outubro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_NOVEMBRO_VALOR | smallint(2) |  | S | Considerar o mês de novembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_DEZEMBRO_VALOR | smallint(2) |  | S | Considerar o mês de dezembro para buscar os valores de médias. (0=Não/1=Sim) |
| NMESES_QUANTIDADE_MENORES_VALOR | integer(4) |  | S | Número de meses com os menores valores. |
| NMESES_QUANTIDADE_MENORES_QUANTIDADE | integer(4) |  | S | Número de meses com os menores valores. |
| MEDIA_COMISSOES | decimal(13) |  | S | Media comissoes |
| BASE_MEDIA_COMISSOES | decimal(13) |  | S | Base de cálculo média comissoes |
| CONFIGURACAO_MEDIA_COMISSOES | smallint(2) |  |  | Configuração de média para comissões. (0=Não/1=Sim) |
| TIPO_PERIODO_COMISSOES | smallint(2) |  |  | TIPO DE PERÍODO. (1=ÚLTIMOS MESES/2=PERÍODO AQUISITIVO/3=ANO CORRENTE/4=ÚLTIMOS MESES NO PERÍODO AQUISITIVO/5=ÚLTIMOS MESES NO ANO CORRENTE/6=SELECIONAR MESES NO ANO CORRENTE) |
| TIPO_CONSIDERAR_COMISSOES | smallint(2) |  |  | VALORES A CONSIDERAR. (1=TODOS/2=SOMENTE COM VALOR/3=MAIORES/4=MAIORES E MENORES) |
| NMESES_QUANTIDADE_COMISSOES | integer(4) |  |  | QUANTIDADE DE MESES |
| NMESES_QUANTIDADE_MAIORES_COMISSOES | integer(4) |  |  | NÚMERO DE MESES COM OS MAIORES VALORES |
| MESES_MEDIA_INI_COMISSOES | date(4) |  |  | MÊS INICIAL DA MÉDIA |
| MESES_MEDIA_FIM_COMISSOES | date(4) |  |  | MÊS FINAL DA MÉDIA |
| CONSIDERAR_JANEIRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE JANEIRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_FEVEREIRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE FEVEREIRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_MARCO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE MARÇO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_ABRIL_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE ABRIL PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_MAIO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE MAIO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_JUNHO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE JUNHO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_JULHO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE JULHO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_AGOSTO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE AGOSTO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_SETEMBRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE SETEMBRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_OUTUBRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE OUTUBRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_NOVEMBRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE NOVEMBRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| CONSIDERAR_DEZEMBRO_COMISSOES | smallint(2) |  | S | CONSIDERAR O MÊS DE DEZEMBRO PARA BUSCAR OS VALORES DE MÉDIAS. (0=NÃO/1=SIM) |
| NMESES_QUANTIDADE_MENORES_COMISSOES | integer(4) |  | S | NÚMERO DE MESES COM OS MENORES VALORES. |
| DIVISOR_QUANTIDADE | integer(4) |  | S | DIVISOR UTILIZADO PARA CALCULO DE MÉDIA QUANTIDADE |
| DIVISOR_VALOR | integer(4) |  | S | DIVISOR UTILIZADO PARA CALCULO DE MÉDIA VALOR |
| DIVISOR_COMISSOES | integer(4) |  | S | DIVISOR UTILIZADO PARA CALCULO DE MÉDIA COMISSÕES |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCMEDIAS_MEM | uniqueidentifier(16) | PK |  | Código |
| I_CALCMEDIAS_MEM_EXPORTA_IMPORTA | uniqueidentifier(16) |  | S | Coluna utilizada durante o exporta/importa |
| SEQUENCIAL_RELATORIO | integer(4) |  |  | Sequência de ordenação relatório |
