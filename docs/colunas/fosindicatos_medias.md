# FOSINDICATOS_MEDIAS — CADASTRO DE SINDICATOS - MÉDIAS
1.294 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_sindicatos | integer(4) | PK |  | Codigo |
| TIPO_MEDIA | smallint(2) | PK |  | Tipo de média. (1=Férias/2=13º salário/3=Aviso prévio/4=Saldo de salário/5=Afastamentos) |
| TIPO_UNIDADE | smallint(2) |  |  | Tipo de unidade: 1=Quantidade/2=Valor/3=Quantidade e valor |
| TIPO_PERIODO | smallint(2) |  |  | Tipo de período. (1=Últimos meses/2=Período aquisitivo/3=Ano corrente/4=Últimos meses no período aquisitivo/5=Últimos meses no ano corrente/6=Selecionar meses no ano corrente) |
| PERIODO_CONSIDERAR | smallint(2) |  |  | 1 Todos 2 Somente com Valor |
| NMESES_CONSIDERAR | smallint(2) |  |  | Valores a considerar. (1=Todos/2=Somente com valor/3=Maiores/4=Maiores e menores) |
| NMESES_QUANTIDADE | integer(4) |  |  | Quantidade de meses |
| NMESES_QUANTIDADE_MAIORES | integer(4) |  |  | Numero de meses com os maiores valores |
| CODIGO | integer(4) | PK |  | Código da configuração |
| TIPO_CALCULO_13 | smallint(2) |  | S | Tipo de cálculo de 13: 0=Todos/1=Adiantamento/2=Adiantamento nas férias/3=Integral/4=Pago em rescisão/5=Ajuste em dezembro |
| MESES_DESCONTO_MENOR_MEDIA_RESCISAO | integer(4) |  | S | Meses com menor valor a desconsiderar para o cálculo de médias em rescisão |
| CONSIDERAR_JANEIRO | smallint(2) |  | S | Considerar o mês de janeiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_FEVEREIRO | smallint(2) |  | S | Considerar o mês de fevereiro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MARCO | smallint(2) |  | S | Considerar o mês de março para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_ABRIL | smallint(2) |  | S | Considerar o mês de abril para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_MAIO | smallint(2) |  | S | Considerar o mês de maio para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JUNHO | smallint(2) |  | S | Considerar o mês de junho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_JULHO | smallint(2) |  | S | Considerar o mês de julho para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_AGOSTO | smallint(2) |  | S | Considerar o mês de agosto para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_SETEMBRO | smallint(2) |  | S | Considerar o mês de setembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_OUTUBRO | smallint(2) |  | S | Considerar o mês de outubro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_NOVEMBRO | smallint(2) |  | S | Considerar o mês de novembro para buscar os valores de médias. (0=Não/1=Sim) |
| CONSIDERAR_DEZEMBRO | smallint(2) |  | S | Considerar o mês de dezembro para buscar os valores de médias. (0=Não/1=Sim) |
| NMESES_CONSIDERAR_MENORES | integer(4) |  | S | Número de meses com os menores valores. |
| PERIODO_CONSIDERAR_ULTIMOS_MESES_FERIAS | smallint(2) |  |  | Período a considerar na média da opção últimos meses das férias. (1=Anteriores ao gozo/2=Anteriores ao pagamento) |
| TIPO_CALCULO_FERIAS | smallint(2) |  | S | Tipo de cálculo de férias. (0=Todos/1=Férias gozadas/2=Férias pagas em rescisão) |
| CONFIGURACAO_MEDIA_COMISSOES | smallint(2) | PK |  | Configuração de média para comissões. (0=Não/1=Sim) |
| CONSIDERAR_MES_ADMISSAO_PERIODO_TRABALHADO_INFERIOR_15_DIAS | smallint(2) |  |  | Considerar o mês da admissão se o empregado trabalhou período inferior a 15 dias. (0=Não/1=Sim) |
| CONSIDERAR_COMPETENCIA_SOMA_MEDIAS_MESMA_UNIDADE_MAIOR_VALOR | smallint(2) |  |  | Considerar a competência que possua a soma das médias de mesma unidade com maior valor. (0=Não/1=Sim) |
| CONSIDERAR_EXISTENCIA_VALOR_ULTIMOS_MESES_CALCULO_MEDIA | smallint(2) |  |  | Considerar a existência de valor nos últimos meses para calcular a média. (0=Não/1=Sim) |
| QUANTIDADE_ULTIMOS_MESES_VERIFICAR_VALOR | smallint(2) |  | S | Quantidade de meses que devem ter valor para calcular a média. |
| CALCULAR_MEDIA_PROPORCIONAL_AVOS_DIREITO | smallint(2) |  |  | Calcular a média proporcional aos avos de direito. (0=Não/1=Sim) |
| CONSIDERAR_MESES_SEM_VALOR_LANCADO_PARA_DIVISOR | smallint(2) |  |  | Considerar os meses em que não houver valor lançado para o divisor. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
