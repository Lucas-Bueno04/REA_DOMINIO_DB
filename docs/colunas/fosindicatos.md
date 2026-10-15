# fosindicatos — Convenção Coletiva - Cadastro
155 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_sindicatos | integer(4) | PK |  | Código da convenção coletiva |
| nome | varchar(115) |  |  | Nome |
| mes_contribuicao | integer(4) |  |  | Mes de contribuicao |
| meses_fer_prop | integer(4) |  |  | Meses ferias proporcionais |
| meses_medias | integer(4) |  |  | Meses media |
| piso_salarial | numeric(13) |  | S | Piso Salarial |
| endereco | char(40) |  | S | ** SEM USO ** |
| complemento | char(25) |  | S | ** SEM USO ** |
| numero | integer(4) |  | S | ** SEM USO ** |
| bairro | char(30) |  | S | ** SEM USO ** |
| cidade | char(40) |  | S | ** SEM USO ** |
| estado | char(2) |  | S | ** SEM USO ** |
| cep | char(8) |  | S | ** SEM USO ** |
| codi_entidade | char(18) |  | S | ** SEM USO ** |
| cgc | char(18) |  | S | ** SEM USO ** |
| corrigir_medias | char(1) |  |  | Corrige medias |
| i_indcorrecao | integer(4) |  | S | Indice correcao |
| medias_nmes | char(1) |  |  | Media por meses com valor |
| mes_base | tinyint(1) |  |  | Mes Base |
| multa_db | char(1) |  |  | Multa rescisao |
| dias_multa_db | integer(4) |  |  | Dias multa |
| perc_multa_db | numeric(5) |  |  | Percentual multa |
| form_dias_adm | char(1) |  |  | Salario mes admissao |
| med_fer_periodo | tinyint(1) |  |  | Media ferias |
| med_fer_nmeses | smallint(2) |  |  | Ultimos meses ferias |
| med_13_nmeses | smallint(2) |  |  | Ultimos meses 13 |
| med_aviso_nmeses | smallint(2) |  |  | Ultimos meses aviso previo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ferias_descartar_dias | tinyint(1) |  | S | Se é para descartar dias nas ferias |
| ferias_descartar_domingo | tinyint(1) |  | S | Se é para descartar dias nas ferias |
| adic_noturno | numeric(13) |  |  | Perc. do adicional noturno |
| avo_13fer_reaviso | tinyint(1) |  | S | Adiconal 13/ferias para aviso reavido |
| fone | char(15) |  | S | ** SEM USO ** |
| fax | char(15) |  | S | ** SEM USO ** |
| agencia | integer(4) |  | S | ** SEM USO ** |
| tipo_entidade | tinyint(1) |  | S | ** SEM USO ** |
| criterio_dias_aviso | tinyint(1) |  |  | Indica se é para utilizar E ou OU no calculo de dias de aviso |
| med_mes_resc | char(1) |  |  | Considera o mês da rescisão para pagar médias. 0 - Não/ 1- Sim |
| med_resc_dias | smallint(2) |  | S | Dias trabalhados no mês da rescisão para contar nas médias. |
| PAGAR_AVOS_PERDIDOS_POR_AFASTAMENTO | smallint(2) |  |  | PAGAR AVOS DOS DIAS TRABALHADOS NO PERÍODO AQUISITIVO COM MAIS DE 180 DIAS AFASTADOS PELA PREVIDÊNCIA |
| FERIAS_COLETIVAS_ANO_ADMISSAO | smallint(2) |  |  | INDICA SE DEVE ALTERAR PERIODO AQUISITIVO PARA EMPREGADOS COM MENOS DE UM ANO DE ADMISSAO EM FERIAS COLETIVAS |
| MED_FER_FORMA_CALCULO | smallint(2) |  |  | 1 CLT 2 ConvenCAo Coletiva |
| MED_13_FORMA_CALCULO | smallint(2) |  |  | 1 CLT 2 ConvenCAo Coletiva |
| MED_AVISO_FORMA_CALCULO | smallint(2) |  |  | 1 CLT 2 ConvenCAo Coletiva |
| PAGAR_AVOS_13_PERDIDOS_POR_AFASTAMENTO_LIMITADO | smallint(2) |  |  | Pagar avos do período afastado pela previdência limitado a 6 avos no ano corrente |
| PAGAR_AVOS_13_PERDIDOS_POR_AFASTAMENTO | smallint(2) |  |  | Pagar avos do período afastado pela previdência quando o número de dias afastados for inferior ou igual ao especificado no ano corrente |
| CONSIDERAR_MEDIA_MAIS_FAVORAVEL | smallint(2) |  |  | Calcular mais de uma média e considerar a média mais favorável ao empregado: 0=Não/1=Sim |
| EMAIL | char(255) |  | S | ** SEM USO ** |
| PAGINA_INTERNET | char(40) |  | S | ** SEM USO ** |
| APELIDO | char(20) |  | S | ** SEM USO ** |
| CONFIGURACAO_MEDIA_13_DISTINTA | smallint(2) |  |  | Configurar médias diferentes para o cálculo de 13º: 0=Não/1=Sim |
| DIA_BASE | smallint(2) |  |  | Dia base |
| ADIANTAR_PARCELA_13_PROPORCIONAL_AVOS_DIREITO | smallint(2) |  |  | Adiantar 1º parcela do 13º salário proporcional ao direito do empregado no ano-corrente (0=Não/1=Sim) |
| DIAS_INDENIZACAO_DATA_BASE | integer(4) |  |  | Total de dias que antecedem a data base para indenização no calculo da rescisão |
| DIAS_AFASTAMENTO_PAGA_AVOS_13_PERDIDOS | integer(4) |  | S | Número máximo de dias afastados no ano corrente |
| DIAS_GOZO_DESCONSIDERAR_MES | integer(4) |  | S | Quantidade de dias de gozo para desconsiderar o mês do gozo de férias |
| DIAS_AFASTADO_DESCONSIDERAR_MES | integer(4) |  | S | Quantidade de dias afastados para desconsiderar o mês do afastamento |
| FORMA_CALCULO_GRATIFICACAO_FERIAS | smallint(2) |  | S | Forma de cálculo da gratificação de férias: (1=Férias/2=Competência inicial do gozo das férias/3=Competência final do gozo das férias/4=Competência posterior a competência fim de gozo das férias/5=Competência retorno de gozo das férias) |
| DIAS_LIMITE_CONTRATO_EXPERIENCIA | integer(4) |  | S | Quantidade de dias limite para o contrato de experiência |
| DEFINE_DATA_PAGAMENTO_MENSAL | smallint(2) |  |  | Define data de pagamento folha mensal: (0=Não/1=Sim) |
| TIPO_MES_PAGAMENTO_MENSAL | smallint(2) |  | S | Tipo do mês do pagamento: (1=No 1º mês subsequente da competência/2=No último dia útil do mês da competência) |
| TOTAL_DIAS_MENSAL | integer(4) |  | S | Total de dias |
| FORMA_APURACAO_DIAS_MENSAL | smallint(2) |  | S | Forma de apuração dos dias: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis) |
| DEFINE_DATA_PAGAMENTO_FERIAS | smallint(2) |  |  | Define data de pagamento: (0=Não/1=Sim) |
| TOTAL_DIAS_FERIAS | integer(4) |  | S | Total de dias anteriores ao início do gozo |
| FORMA_APURACAO_DIAS_FERIAS | smallint(2) |  | S | Forma de apuração dos dias: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis) |
| OBSERVACAO | varchar(32000) |  | S | Observação |
| DIAS_ASSISTENCIA_HOMOLOGACAO | integer(4) |  |  | Dias para assistência na homologação |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_ASSISTENCIAL | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_ASSISTENCIAL | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_ASSISTENCIAL | integer(4) |  | S | Total de dias |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_ASSOCIATIVA | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_ASSOCIATIVA | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_ASSOCIATIVA | integer(4) |  | S | Total de dias |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_CONFEDERATIVA | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_CONFEDERATIVA | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_CONFEDERATIVA | integer(4) |  | S | Total de dias |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_ASSISTENCIAL_13 | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_ASSISTENCIAL_13 | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_ASSISTENCIAL_13 | integer(4) |  | S | Total de dias |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_ASSOCIATIVA_13 | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_ASSOCIATIVA_13 | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_ASSOCIATIVA_13 | integer(4) |  | S | Total de dias |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_CONFEDERATIVA_13 | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_CONFEDERATIVA_13 | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_CONFEDERATIVA_13 | integer(4) |  | S | Total de dias |
| CONSIDERAR_MEDIA_PERIODO_FERIAS | smallint(2) |  |  | Considerar o período de férias para o cálculo das médias.(0-Não/1-Sim) |
| DIAS_CONSIDERAR_FRACAO_AVO_FERIAS | integer(4) |  | S | Dias trabalhados considera fração avos férias |
| CALCULAR_MEDIAS_SOBRE_SALDO_SALARIO | smallint(2) |  |  | Calcular médias sobre saldo de salário: (0=Não/1=Sim) |
| FORMA_CALCULO_GRATIFICACAO_FERIAS_INDENIZADAS | smallint(2) |  | S | Forma de cálculo da gratificação de férias indenizadas. (0=Não calcular/1=Somente vencidas/2=Somente proporcional/3=Vencidas e prop./4=Vencidas, proporcional e indenizada/5=Somente indenizada) |
| CALCULAR_MEDIAS_AVISO_REAVIDO | smallint(2) |  |  | Calcular médias no aviso reavido. (0=Não/1=Sim) |
| DIAS_ESTABILIDADE_FERIAS_PERIODO_GOZO | smallint(2) |  |  | Calcular os dias de estabilidade após o retorno do gozo de férias com o mesmo número de dias do período de gozo. (0=Não/1=Sim) |
| CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES | smallint(2) |  |  | Calcular salário proporcional aos dias do mês. (0=Não/1=Sim, quando a competência calculada for inferior a 30 dias/2=Sim, quando a competência calculada for superior a 30 dias/3=Sim, para todas as competências calculadas) |
| CONSIDERAR_VALOR_AVISO_PREVIO_INDEN_PARA_INDENIZACAO_FERIAS_13 | smallint(2) |  |  | Considerar o valor do Aviso Prévio Indenizado como base de cálculo para os avos de Férias e 13º salário indenizados. (0=Não/1=Sim) |
| CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES_SOMENTE_FERIAS_GOZADAS | smallint(2) |  | S | Calcular salário proporcional aos dias do mês somente em competência com férias gozadas. (0=Não/1=Sim) |
| CALCULAR_MULTA_ESTAB_ARTIGO_479_CLT_COM_MEDIDAS_E_ADICIONAIS | smallint(2) |  | S | Calcular multa estabilidade artigo 479/CLT com médias e adicionais. (0=Não/1=Sim) |
| CALCULAR_MULTA_ESTAB_ARTIGO_480_CLT_COM_MEDIDAS_E_ADICIONAIS | smallint(2) |  | S | Calcular multa estabilidade artigo 480/CLT com médias e adicionais. (0=Não/1=Sim) |
| CONSIDERAR_SEMPRE_30_DIAS_MEDIAS_VANTAGENS_HORISTA | smallint(2) |  |  | Considerar sempre 30 dias para as médias/vantagens do empregado horista. (0=Não/1=Sim) |
| CALCULAR_MEDIAS_ADICIONAIS_INDENIZACAO_ADICIONAL | smallint(2) |  |  | ** SEM USO ** |
| POSSUI_AVISO_PREVIO_MISTO | smallint(2) |  | S | Substituir o aviso prévio da Lei 12.506/2011. (0=Não/1=Sim) |
| PAGAR_AVOS_13_PERIODO_AFASTAMENTO_ACIDENTE_TRABALHO | smallint(2) |  |  | Paga avos do período afastado por acidente de trabalho. (0=Não/1=Sim) |
| DIAS_PAGAMENTO_RESCISAO | smallint(2) |  |  | Dias para pagamento rescisão. |
| CONSIDERAR_DIA_NOTIFICACAO_AVISO_PREVIO_DATA_PAGAMENTO_RESCISAO | smallint(2) |  |  | Considerar o dia da notificação do aviso prévio para a data de pagamento da rescisão. (0=Não/1=Sim) |
| DEFINIR_DIAS_NAO_PERMITIR_INICIO_GOZO_FERIAS | smallint(2) |  | S | Definir dias em que não é permitido iniciar o gozo de férias. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_SEGUNDA_FEIRA | smallint(2) |  | S | Permitir o início do gozo de férias na segunda-feira. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_TERCA_FEIRA | smallint(2) |  | S | Permitir o início do gozo de férias na terça-feira. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_QUARTA_FEIRA | smallint(2) |  | S | Permitir o início do gozo de férias na quarta-feira. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_QUINTA_FEIRA | smallint(2) |  | S | Permitir o início do gozo de férias na quinta-feira. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_SEXTA_FEIRA | smallint(2) |  | S | Permitir o início do gozo de férias na sexta-feira. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_SABADO | smallint(2) |  | S | Permitir o início do gozo de férias na sábado. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_DOMINGO | smallint(2) |  | S | Permitir o início do gozo de férias no domingo. (0=Não/1=Sim) |
| POSSUI_LIMINAR_PARA_NAO_RECOLHER_INSS_AVISO_INDENIZADO | smallint(2) |  |  | Empresa possui liminar para não recolher INSS sobre o Aviso Prévio Indenizado. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_IND_DATA_BASE_CONTRATO_EXP_LEI_479_480_CLT | smallint(2) |  |  | Considerar para contrato de experiência regido pelo art. 479/480 da CLT os dias para indenização data base. (0=Não/1=Sim) |
| DEFINIR_MESES_ADIANTAR_13_SALARIO_NAS_FERIAS | smallint(2) |  |  | Adiantar 13º nas férias quando calculada nos meses. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_JANEIRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em janeiro. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_FEVEREIRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em fevereiro. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_MARCO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em março. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_ABRIL | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em abril. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_MAIO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em maio. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_JUNHO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em junho. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_JULHO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em julho. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_AGOSTO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em agosto. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_SETEMBRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em setembro. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_OUTUBRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em outubro. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_NOVEMBRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em novembro. (0=Não/1=Sim) |
| ADIANTAR_13_SALARIO_FERIAS_CALCULADAS_DEZEMBRO | smallint(2) |  |  | Adiantar o 13º salário para férias calculadas em dezembro. (0=Não/1=Sim) |
| CALCULAR_GRATIFICACAO_FERIAS_COLETIVAS | smallint(2) |  |  | Calcular gratificação nas férias coletivas. (0=Não/1=Sim) |
| CALCULAR_GRATIFICACAO_PROPORCIONAL_FERIAS_COLETIVAS | smallint(2) |  |  | Calcular gratificação proporcional nas férias coletivas. (0=Não/1=Sim) |
| PAGAR_INDENIZACAO_MENSAL_FERIAS_VENCIDAS | smallint(2) |  |  | Pagar indenização mensal por férias vencidas. (0=Não/1=Sim) |
| QUANTIDADE_MES_APOS_VENCIMENTO_FERIAS_PAGAR_INDENIZACAO_MENSAL | smallint(2) |  | S | Quantidade de meses após o vencimento das férias que deverá ser iniciado o cálculo da indenização mensal. |
| VALOR_INDENIZACAO_MENSAL_FERIAS_VENCIDAS | numeric(13) |  | S | Valor da indenização mensal por férias vencidas. |
| CALCULAR_GARANTIA_MINIMA_COMISSIONADO | smallint(2) |  | S | Calcular garantia mínima para empregados comissionados. (0=Não/1=Sim) |
| CONFIGURAR_MEDIAS_AFASTAMENTOS | smallint(2) |  |  | Configurar médias para os afastamentos. (0=Não/1=Sim) |
| CALCULAR_DIFERENCA_CONTRIBUICAO_ASSISTENCIAL_ALTERACAO_SALARIAL | smallint(2) |  |  | Calcular diferença de Contribuição Assistencial devido alteração salarial. |
| CONSIDERAR_MAIOR_GRADE_ULTIMOS_MESES_FERIAS_RESCISAO_PROFESSOR | smallint(2) |  |  | Utilizar a maior grade dos últimos meses para cálculo das férias na rescisão de empregado professor. (0=Não/1=Sim) |
| NUMERO_MESES_CONSIDERAR_MAIOR_GRADE_FERIAS_RESCISAO_PROFESSOR | smallint(2) |  | S | Número de meses para buscar a maior grade para cálculo das férias na rescisão de empregado professor. |
| CONSIDERAR_MAIOR_GRADE_ULTIMOS_MESES_13_SAL_RESCISAO_PROFESSOR | smallint(2) |  |  | Utilizar a maior grade dos últimos meses para cálculo do 13º salário na rescisão de empregado professor. (0=Não/1=Sim) |
| NUMERO_MESES_CONSIDERAR_MAIOR_GRADE_13_SALARIO_RESCISAO_PROFESSOR | smallint(2) |  | S | Número de meses para buscar a maior grade para cálculo do 13º salário na rescisão de empregado professor. |
| CONSIDERAR_MEDIA_LICENCA_MAT_COMPOR_MEDIA_FERIAS_13_SALARIO | smallint(2) |  |  | Considerar médias da licença maternidade para compor médias de férias e 13º salário. (0=Não/1=Sim) |
| UTILIZAR_CONFIGURACAO_PROPORCIONALIDADE_SOMENTE_RESCISAO | smallint(2) |  |  | Utilizar a configuração do cálculo da proporcionalidade somente para a rescisão. (0=Não/1=Sim) |
| CALCULAR_CONTRIBUICAO_ASSISTENCIAL_SEM_DESCONTO_EMPREGADO | smallint(2) |  |  | Calcular Contribuição Assistencial sem descontar do empregado. (0=Não/1=Sim) |
| CONFIGURAR_MEDIAS_DIFERENTES_FERIAS | smallint(2) |  |  | Configurar médias diferentes para férias gozadas e para férias pagas em rescisão (0=Não/1=Sim) |
| DETERMINAR_QTD_DIAS_CONSIDERAR_MES_TRABALHADO_AVISO_PREVIO | smallint(2) |  |  | Determinar a quantidade de dias para considerar o mês como trabalhado para o aviso prévio. (0=Não/1=Sim) |
| QUANTIDADE_DIAS_CONSIDERAR_MES_TRABALHADO_AVISO_PREVIO | smallint(2) |  | S | Quantidade de dias para considerar o mês como trabalhado para o aviso prévio. |
| CONSIDERAR_DIAS_AVISO_PREVIO_LEI_12506_AVISO_INDENIZADO | smallint(2) |  |  | Considerar os dias de aviso prévio acrescidos pela Lei 12.506/2011 como dias de aviso indenizado. (0=Não/1=Sim) |
| CONFIGURAR_MEDIA_DIFERENCIADA_COMISSOES | smallint(2) |  |  | Configurar média diferenciada para comissões. (0=Não/1=Sim) |
| CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES_COMPETENCIA_ADMISSAO | smallint(2) |  |  | Calcular salário proporcional aos dias do mês na competência de admissão quando a empresa estiver parametrizada para calcular sempre 30 dias. (0=Não/1=Sim) |
| CALCULAR_MEDIA_INDIVIDUAL_EVENTO | smallint(2) |  |  | Calcular média individual para cada evento. (0=Não/1=Sim) |
| LIMITAR_DIVISOR_MEDIAS_FERIAS_PROPORCIONAL_RESCISAO | smallint(2) |  |  | Limitar o divisor das médias de férias proporcionais na rescisão a quantidade de avos de férias. (0=Não/1=Sim) |
| ADIANTAR_PARCELA_13_SALARIO_RETORNO_FERIAS | smallint(2) |  |  | Adiantar parcela do 13º salário no retorno das férias. (0=Não/1=Sim) |
| INICIAR_NOVO_PERIODO_AQUISITIVO_DATA_RETORNO_FERIAS_COLETIVAS | smallint(2) |  |  | Iniciar novo período aquisitivo para empregados com menos de 12 meses trabalhados conforme data de retorno das férias coletivas. (0=Não/1=Sim) |
| PAGAR_13_PROPORCIONAL_EMPREGADOS_TROCA_MENSALISTA_COMISSIONADO | smallint(2) |  |  | Pagar 13º salário proporcionalmente aos meses como Mensalista e aos meses como Comissionado quando houver troca de categoria. (0=Não/1=Sim) |
| CALCULAR_FERIAS_PROPORCIONAIS_RESCISAO_JUSTA_CAUSA | smallint(2) |  |  | Calcular férias proporcionais para rescisão com justa causa. (0=Não/1=Sim) |
| INICIAR_PERIODO_AQUISITIVO_FERIAS_COLETIVAS_MENORES_DIAS_DIREITO | smallint(2) |  |  | Iniciar novo período aquisitivo nas férias coletivas quando os dias de gozo forem menores que os dias de direito. (0=Não/1=Sim) |
| CALCULO_PROPORCIONALIDADE_HORISTA | smallint(2) |  |  | Cálculo de proporcionalidade para Horista. (1=Sempre 30 dias/2=Conforme dias do mês) |
| PERMITIR_INICIO_GOZO_FERIAS_FERIADO | smallint(2) |  |  | Permitir o início do gozo de férias em feriado. (0=Não/1=Sim) |
| DATA_LIMITE_AVISO_PREVIO_NAO_CALCULAR_INDENIZACAO_DATA_BASE | date(4) |  | S | Data limite do aviso prévio para não calcular a indenização da data base. |
| DEFINIR_LIMITE_DIAS_AUSENCIA_JUSTIFICADA | smallint(2) |  |  | Definir limite de dias de afastamento por ausência justificada. (0=Não/1=Sim) |
| LIMITE_DIAS_AUSENCIA_JUSTIFICADA | smallint(2) |  | S | Limite de dias de afastamento por ausência justificada. |
| PAGAR_MAIOR_VALOR_ENTRE_GRATIFICACAO_E_TERCO_FERIAS | smallint(2) |  |  | Pagar maior entre 1/3 de férias e gratificação de férias. (0=Não/1=Sim) |
| PAGAR_PLR_PROPORCIONAL_MESES_TRABALHADOS | smallint(2) |  |  | Considerar PLR de forma proporcional aos meses trabalhados e considerar o mês apenas quando houver mais de 15 dias trabalhados. (0=Não/1=Sim) |
| DESCONTAR_CONTRIBUICAO_ASSISTENCIAL_COMPETENCIA_ADMISSAO | smallint(2) |  |  | Descontar a contribuição assistencial na competência da admissão. (0=Não/1=Sim) |
| PERCENTUAL_DESC_CONTRIBUICAO_ASSISTENCIAL_COMPETENCIA_ADMISSAO | numeric(5) |  | S | Percentual de desconto da contribuição assistencial na competência da admissão. |
| CALCULAR_RESCISAO_PARCIAL_PROFESSOR | smallint(2) |  |  | Calcular rescisão parcial professor. (0=Não/1=Sim) |
| CALCULAR_SALDO_SALARIO_RESCISAO_PARCIAL_PROFESSOR | smallint(2) |  |  | Calcular saldo de salário na rescisão parcial professor. (0=Não/1=Sim) |
| CALCULAR_13_SALARIO_RESCISAO_PARCIAL_PROFESSOR | smallint(2) |  |  | Calcular 13º salário na rescisão parcial professor. (0=Não/1=Sim) |
| CALCULAR_FERIAS_VENCIDAS_RESCISAO_PARCIAL_PROFESSOR | smallint(2) |  |  | Calcular férias vencidas na rescisão parcial professor. (0=Não/1=Sim) |
| CALCULAR_FERIAS_PROPORCIONAIS_RESCISAO_PARCIAL_PROFESSOR | smallint(2) |  |  | Calcular férias proporcionais na rescisão parcial professor. (0=Não/1=Sim) |
| CALCULAR_RESCISAO_PARCIAL_PROFESSOR_FOLHA_MENSAL | smallint(2) |  |  | Calcular a rescisão parcial professor na folha mensal. (0=Não/1=Sim) |
| INCLUIR_MOVIMENTO_RESCISAO_PARCIAL_PROFESSOR_FOLHA_MENSAL | smallint(2) |  |  | Incluir movimento da rescisão parcial professor na folha mensal. (0=Não/1=Sim) |
| POSSUI_LICENCA_PREMIO | smallint(2) |  |  | Possui licença prêmio. (0=Não/1=Sim) |
| PAGAR_MEDIAS_LICENCA_PREMIO | smallint(2) |  |  | Pagar médias na licença prêmio. (0=Não/1=Sim) |
| PAGAR_ADICIONAL_LICENCA_PREMIO | smallint(2) |  |  | Pagar adicional na licença prêmio. (0=Não/1=Sim) |
| INDENIZAR_QUANDO_NAO_GOZOU_LICENCA_PREMIO_ATE_A_RESCISAO | smallint(2) |  |  | Indenizar na rescisão quando o empregado não gozou a licença prêmio até a data da rescisão. (0=Não/1=Sim) |
| FERIAS_DESCARTAR_DIAS_NAO_CONSIDERAR_SABADO | smallint(2) |  |  | Considerar os dias de férias no sábado. (0=Não/1=Sim) |
| CONSIDERAR_PROJECAO_AVISO_PREVIO_INDENIZADO_CALCULO_ESTAB | smallint(2) |  |  | Considerar a projeção do aviso prévio indenizado para o cálculo da estabilidade. (0=Não/1=Sim) |
| CALCULAR_GARANTIA_MINIMA_CONFORME_REGIME_FEDERAL | smallint(2) |  |  | Calcular garantia mínima conforme regime federal da empresa. (0=Não/1=Sim) |
| PAGAR_MAIOR_VALOR_ENTRE_TERCO_FERIAS_E_ADICIONAL_CONFIGURADO | smallint(2) |  |  | Pagar somente o maior valor entre o 1/3 de férias e o adicional configurado. (0=Não/1=Sim) |
| CONSIDERAR_PROJECAO_AVISO_PREVIO_IND_CALCULO_ESTAB_DISSIDIO | smallint(2) |  |  | Considerar a projeção do aviso prévio indenizado para o cálculo da estabilidade. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_COMISSIONADO_SOMENTE_COMP_RECEBER_GARANTIA_MIN | smallint(2) |  |  | Descontar as faltas somente na competência em que o comissionado receber garantia mínima. (0=Não/1=Sim) |
| UTILIZAR_DIVISOR_QUANTIDADE_DIAS_MES_ADMISSAO | smallint(2) |  |  | Utilizar como divisor a quantidade de dias do mês na competência da admissão. (0=Não/1=Sim) |
| CONSIDERAR_AVO_FERIAS_DIV_MEDIAS_RESC_MENOS_12_MES_TRABALHADOS | smallint(2) |  |  | Considerar a quantidade exata de avos de férias para o divisor de médias na rescisão quando o colaborador possuir menos de 12 meses dentro do período aquisitivo. (0=Não/1=Sim) |
| CORRIGIR_MEDIAS_PERIODO_AFASTAMENTO | smallint(2) |  |  | Corrigir médias durante o afastmaento. (1=Não/0=Sim) |
| DESCONTAR_CONTRIBUICAO_CONF_COMP_DESC_ASSISTENCIAL_SINDICAL | smallint(2) |  |  | Descontar a contribuição confederativa quando na competência houver desconto de contribuição assistencial e/ou sindical. (0=Não/1=Sim) |
| CONSIDERAR_INDICE_CORRECAO_INFERIOR_UM | smallint(2) |  |  | Gerar o índice 1 quando o índice informado for inferior a 1. (0=Não/1=Sim) |
| CONSIDERAR_VALOR_MEDIA_MES_GOZO_FERIAS | smallint(2) |  |  | Considerar o valor de médias do mês de gozo de férias. (0=Não/1=Sim) |
| UTILIZAR_INICIO_PROPORCIONALIDADE_AVISO_PREVIO_CONFORME_PARAMETRO | smallint(2) |  |  | Utilizar a data de início do cálculo de proporcionalidade do aviso prévio configurado nos parâmetros. (0=Não/1=Sim) |
| DEFINIR_DIAS_SEMANA_INICIO_AVISO_PREVIO | smallint(2) |  |  | Definir dias da semana para o início do aviso prévio. (0=Não/1=Sim) |
| DIAS_SEMANA_INICIO_AVISO_PREVIO | smallint(2) |  | S | Dias da semana para o início do aviso prévio. |
| CALCULAR_PLR_EMPREGADOS_DEMITIDOS_JUSTA_CAUSA | smallint(2) |  |  | Calcular PLR para empregados demitidos por justa causa. (0=Não/1=Sim) |
| CALCULAR_PLR_RESC_COMP_ANTERIOR_PAGAMENTO_PARTICIPACAO_LUCROS | smallint(2) |  |  | Calcular PLR na rescisão para empregado demitido antes da competência de pagamento do PLR. (0=Não/1=Sim) |
| CALCULAR_PLR_PROPORCIONAL_RESCISAO_PERIODO_VIGENCIA | smallint(2) |  |  | Calcular PLR proporcional na rescisão para empregado demitido dentro da vigência. (0=Não/1=Sim) |
| DEFINIR_QUANTOS_MESES_POSTERIORES_VENCIMENTO_FERIAS_PAGAR_DOBRO | smallint(2) |  |  | Definir quantidade de meses após o vencimento das férias para o pagamento das férias em dobro. (0=Não/1=Sim) |
| QUANTIDADE_MESES_POSTERIORES_VENCIMENTO_FERIAS_PAGAR_DOBRO | smallint(2) |  | S | Quantidade de meses após o vencimento das férias para o pagamento das férias em dobro. |
| CALCULAR_GARANTIA_SEMESTRAL_PROFESSOR_AULISTA_VARIAVEL | smallint(2) |  |  | Calcular garantia semestral para professor aulista variável. (0=Não/1=Sim) |
| PERMITIR_INICIO_GOZO_FERIAS_ENTRE_FERIADO_FIM_SEMANA | smallint(2) |  | S | Permitir o início do gozo de férias entre feriado e fim de semana. (0=Não/1=Sim) |
| CONSIDERAR_COMPETENCIA_ANTERIOR_CALCULO_MEDIAS_FERIAS | smallint(2) |  |  | Considerar a competência anterior ao mês das férias. (0=Não/1=Sim) |
| CONSIDERAR_VALOR_CALCULADO_CALCULO_MEDIAS_RUBRICAS_HORAS | smallint(2) |  |  | Considerar para o cálculo de médias horas o valor calculado. (0=Não/1=Sim) |
| REDUZIR_VALOR_DESCONTAR_DSR_FALTA_INTEGRAL | smallint(2) |  |  | Reduzir o valor a descontar de DSR por falta integral. (0=Não/1=Sim) |
| VALOR_DESCONTAR_DSR_FALTA_INTEGRAL | smallint(2) |  |  | Valor a descontar de DSR por falta integral. (1=1/5 do valor de DSR/2=1/6 do valor de DSR) |
| CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES_FOLHA_MENSAL_NORMAL | smallint(2) |  |  | Calcular o salário proporcional ao número de dias do mês em competência que não possua férias gozadas, rescisão ou admissão. |
| DETALHAR_DIAS_AUSENCIA_JUSTIFICADA_ABONADAS | smallint(2) |  |  | Detalhar os dias de ausência justificada abonadas. (0=Não/1=Sim) |
| ABONAR_DIAS_AUSENCIA_JUSTIFICADA_MORTE | smallint(2) |  |  | Abonar os dias de ausência justificada por morte. (0=Não/1=Sim) |
| DIAS_ABONO_AUSENCIA_JUSTIFICADA_MORTE | smallint(2) |  | S | Dias de abono de ausência justificada por morte. |
| ABONAR_DIAS_AUSENCIA_JUSTIFICADA_CASAMENTO | smallint(2) |  |  | Abonar os dias de ausência justificada casamento. (0=Não/1=Sim) |
| DIAS_ABONO_AUSENCIA_JUSTIFICADA_CASAMENTO | smallint(2) |  | S | Dias de abono de ausência justificada casamento. |
| ABONAR_DIAS_AUSENCIA_JUSTIFICADA_OUTROS_MOTIVOS | smallint(2) |  |  | Abonar os dias de ausência justificada outros motivos. (0=Não/1=Sim) |
| DIAS_ABONO_AUSENCIA_JUSTIFICADA_OUTROS_MOTIVOS | smallint(2) |  | S | Dias de abono de ausência outros motivos. |
| ABONAR_DIAS_AUSENCIA_JUSTIFICADA_OUTROS_DOENCA_FAMILIA | smallint(2) |  |  | Abonar os dias de ausência justificada por doença em família. (0=Não/1=Sim) |
| DIAS_ABONO_AUSENCIA_JUSTIFICADA_DOENCA_FAMILIA | smallint(2) |  | S | Dias de abono de ausência por doença em família. |
| CALC_VALOR_ESTAB_APOS_RETORNO_FERIAS_CONFORME_VALOR_AVISO_IND | smallint(2) |  |  | Calcular valor de estabilidade após o retorno do gozo de férias conforme valor de aviso prévio indenizado. (0=Não/1=Sim) |
| UTILIZAR_INDICE_CORRECAO_CONFORME_TAB_COMP_ANT_CALC_INDICE_ACUM | smallint(2) |  |  | Utilizar o índice de correção conforme a tabela na competência anterior ao cálculo para índices acumulados. (0=Não/1=Sim) |
| UTILIZAR_ULTIMO_VALOR_CALCULADO_RUBRICA_VANTAGEM_13_SALARIO | smallint(2) |  |  | Utilizar o último valor calculado nas rubricas de adicional para gerar as vantagens do 13º salário. (0=Não/1=Sim) |
| CONSIDERAR_CONFIGURACOES_ESTABILIDADE_AFASTAMENTO_RESCISAO | smallint(2) |  |  | Considerar as configurações de estabilidade para motivo de rescisão informado (0=Não/1=Sim) |
| TIPO_MES_PAGAMENTO_CONTRIBUICAO_SINDICAL | smallint(2) |  |  | Tipo mês do pagamento: (1=1º mês subsequente/2=No mesmo mês/3=2º mês subsequente/4=1ª quinzena/5=2ª quinzena) |
| FORMA_APURACAO_DIAS_CONTRIBUICAO_SINDICAL | smallint(2) |  |  | Forma de vencimento: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| TOTAL_DIAS_CONTRIBUICAO_SINDICAL | integer(4) |  | S | Total de dias para o cálculo da data de vencimento da contribuição sindical. |
| CALCULAR_VANTAGEM_13_SALARIO_ULTIMOS_MESES_ANO_CORRENTE_HORISTA | smallint(2) |  |  | Calcular vantagem de 13º salário sobre os últimos meses do ano corrente para empregados horistas. (0=Não/1=Sim) |
| CALCULAR_GARANTIA_MIN_EMPREGADO_COMISSIONADO_COM_SALARIO_FIXO | smallint(2) |  |  | Calcular garantia mínima para empregado comissionado com salário fixo. (0=Não/1=Sim) |
| SUSPENDER_AVISO_PREVIO_PERIODO_FERIAS_COLETIVAS | smallint(2) |  |  | Suspender aviso prévio quando em gozo de férias coletivas. (0=Não/1=Sim) |
| CALCULAR_GARANTIA_MINIMA_MESES_TRABALHADOS | smallint(2) |  |  | Calcular garantia mínima conforme meses trabalhados. (0=Não/1=Sim) |
| CAL_MULTA_ESTAB_TERMI_CONT_EXP_ANTEC_20_CENTO_DIR_REST_CONTRATO | smallint(2) |  |  | Calcular multa estabilidade para término de contrato de experiência antecipado, no valor de 20% sobre a remuneração de direito até o final do contrato. (0=Não/1=Sim) |
| DEMONSTRAR_MENSAGEM_ESTABILIDADE_AVISO_PREVIO_TRABALHADO_RESCISAO_POSTERIOR_FIM_ESTABILIDADE | smallint(2) |  |  | Demonstrar mensagem de estabilidade para aviso prévio trabalhado se a data fim da estabilidade for anterior a data da rescisão. (0=Não/1=Sim) |
| COMPETENCIA_PAGAMENTO_CONTRIBUICAO_ASSISTENCIAL | smallint(2) |  |  | Competência de desconto da contribuição assistencial. (1=Competência de admissão/2=Competência subsequente à admissão/3=Rescisão/4=Admissão e rescisão) |
| CONSIDERAR_PROJECAO_AVISO_PREVIO_INDENIZADO_CALCULO_PLR | smallint(2) |  |  | Considerar a projeção do aviso prévio indenizado para o cálculo de PLR. (0=Não/1=Sim) |
| PROPORC_GARANTIA_MIN_COMIS_REGIME_TEMPO_PARC_CONFORME_HORAS_MES | smallint(2) |  |  | Proporcionalizar o valor da garantia mínima conforme horas mês para empregado com Regime de Tempo Parcial. (0=Não/1=Sim) |
| DESCONTAR_GRATIFICACOES_GARANTIA_COMISSIONADO | smallint(2) |  |  | Descontar valores de gratificações para o cálculo de garantia do comissionado. (0=Não/1=Sim) |
| PAGAR_GRATIFICACAO_FERIAS_RESCISAO | smallint(2) |  |  | Pagar gratificação de férias por motivo de rescisão. (0=Não/1=Sim) |
| PAGAR_GRATIFICACAO_FERIAS_RESCISAO_MOTIVO_01 | smallint(2) |  |  | Pagar gratificação de férias rescisão por pedido de demissão sem justa causa. (0=Não/1=Sim) |
| PAGAR_GRATIFICACAO_FERIAS_RESCISAO_MOTIVO_04 | smallint(2) |  |  | Pagar gratificação de férias rescisão por demissão com justa causa. (0=Não/1=Sim) |
| CONSIDERAR_MES_RESCISAO_MEDIAS_AVISO_PREVIO | smallint(2) |  |  | Considerar o mês da rescisão para as médias de aviso prévio. (0=Não/1=Sim) |
| CONSIDERAR_PLR_APENAS_MESES_TRABALHADOS_PERIODO_VIGENCIA | smallint(2) |  |  | Considerar como meses trabalhados para o PLR, apenas os meses entre a vigência inicial e a vigência final. (0=Não/1=Sim) |
| CALCULAR_MEDIAS_INDENIZACAO_ADICIONAL | smallint(2) |  |  | Calcular médias na indenização adicional. (0=Não/1=Sim) |
| CALCULAR_ADICIONAIS_INDENIZACAO_ADICIONAL | smallint(2) |  |  | Calcular adicionais na indenização adicional. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AVISO_PREVIO_ESPECIAL_PROJECAO_AVISO_PREVIO_IND | smallint(2) |  |  | Considerar os dias de aviso prévio especial para somar aos dias de projeção do aviso prévio indenizado. (0=Não/1=Sim) |
| UTILIZAR_DATA_PAGTO_RESCISAO_AVISO_TRABALHADO_MESMA_DATA_RESC | smallint(2) |  |  | Utilizar como data de pagamento para rescisão com aviso prévio trabalhado a mesma data da rescisão. (0=Não/1=Sim) |
| CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES_COMPETENCIA_AFASTAMENTOS | smallint(2) |  |  | Calcular salário proporcional aos dias do mês na competência com afastamentos quando a empresa estiver parametrizada para calcular sempre 30 dias. (0=Não/1=Sim) |
| LISTA_AFAST_CALCULAR_SALARIO_PROPORCIONAL_DIAS_MES_COMPETENCIA | integer(4) |  | S | Lista de afastamentos que devem ser considerador para o cálculo do salário proporcional. |
| CONSIDERAR_SABADO_DIA_UTIL_APURACAO_DATA_PAGAMENTO_FERIAS | smallint(2) |  |  | Considerar sábado como dia útil na apuração da data de pagamento das férias. (0=Não/1=Sim) |
| UTILIZAR_VALOR_INTEGRAL_GARANTIA_MINIMA_MEDIA_HORA_EXTRA | smallint(2) |  |  | Utilizar valor integral de garantia mínima para média de hora extra. (0=Não/1=Sim) |
| DETALHAR_DIAS_ASSISTENCIA_HOMOLOGACAO_RESCISAO_CONFORME_CBO | smallint(2) |  |  | Detalhar os dias para assistência da homologação da rescisão conforme o CBO. (0=Não/1=Sim) |
| I_BANCOS | integer(4) |  | S | ** SEM USO ** |
| CONSIDERAR_MEDIA_PERIODO_FERIAS_CALCULO_MEDIA_AFASTAMENTOS | integer(4) |  |  | Considerar a média apurada no período de férias para o cálculo de média dos afastamentos. (0=Não/1=Sim) |
| LISTA_AFAST_CONSIDERAR_MEDIA_PER_FERIAS_CALC_MEDIA_AFAST | integer(4) |  | S | Lista de afastamentos que consideram o período de média das férias para o cálculo de médias do afastamentos. |
| DEFINIR_DIAS_SEMANA_INICIO_AVISO_PREVIO_INDENIZADO | smallint(2) |  |  | Definir dias da semana para o início do aviso prévio indenizado. (0=Não/1=Sim) |
| DIAS_SEMANA_INICIO_AVISO_PREVIO_INDENIZADO | smallint(2) |  | S | Dias da semana para o início do aviso prévio indenizado. |
| PAGAR_PLR_PROPORCIONAL_APENAS_MESES_MAIS_15_DIAS_TRABALHADOS | smallint(2) |  |  | Considerar apenas os meses com mais de 15 dias trabalhados para o cálculo proporcional do PLR. (0=Não/1=Sim) |
| CALCULAR_PLR_EMPREGADOS_DEMITIDOS_SEM_JUSTA_CAUSA | smallint(2) |  |  | Calcular PLR para empregados demitidos sem justa causa. (0=Não/1=Sim) |
| UTILIZA_GARANTIA_MIN_COMISSIONADO_BASE_CALC_VANT_INF_GARANTIA | smallint(2) |  |  | Utilizar o valor de garantia mínima comissionado para base de cálculo de vantagem quando o total da base for inferior ao valor da garantia mínima. (0=Não/1=Sim) |
| LIMITAR_CARGA_HORARIA_MINIMA_MENSAL | smallint(2) |  |  | Limitar a carga horário mínima das horas mensais. (0=Não/1=Sim) |
| CARGA_HORARIA_MINIMA_MENSAL | numeric(5) |  | S | Carga horário mínima das horas mensais. |
| LIMITAR_CARGA_HORARIA_MAXIMA_MENSAL | smallint(2) |  |  | Limitar a carga horário máxima das horas mensais. (0=Não/1=Sim) |
| CARGA_HORARIA_MAXIMA_MENSAL | numeric(5) |  | S | Carga horário máxima das horas mensais. |
| CALCULA_GRATIFICACAO_FERIAS_PROPORC_QUANT_AVOS_FERIAS_PROPORC | smallint(2) |  |  | Calcular gratificação férias proporcional a quantidade de avos de férias proporcionais. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_AVISO_PREVIO_ESPECIAL_PAGTO_AVOS_INDENIZACAO | smallint(2) |  |  | Considerar os dias de aviso prévio especial para o pagamento dos avos de férias e 13º indenizados. (0=Não/1=Sim) |
| CONSIDERAR_SABADO_DOMINGO_FERIADO_COMO_DIA_UTIL_DATA_PAGTO_RESC | smallint(2) |  |  | Considerar sábado, domingo e feriado como dia útil para data de pagamento de rescisão com tipo trabalhado. (0=Não/1=Sim) |
| UTILIZAR_AVISO_PREVIO_INDENIZADO_EMPREGADO_DEMITIDO_SEM_JUSTA_CAUSA | smallint(2) |  |  | Utilizar aviso prévio indenizado quando o empregado for demitido sem justa causa. (0=Não/1=Sim) |
| LIMITAR_QUANTIDADE_DIAS_AVISO_PREVIO | smallint(2) |  |  | Limitar a quantidade de dias de aviso prévio. (0=Não/1=Sim) |
| QUANTIDADE_MAXIMA_DIAS_AVISO_PREVIO | numeric(5) |  | S | Quantidade máxima de dias de aviso prévio. |
| DEFINIR_DIAS_HOMOLOGACAO_RESCISAO_CONFORME_FORMA_PAGAMENTO | smallint(2) |  |  | Definir dias para homologação da rescisão conforme forma de pagamento. (0=Não/1=Sim) |
| DEFINIR_DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_CHEQUE | smallint(2) |  |  | Definir dias para homologação da rescisão forma de pagamento cheque. (0=Não/1=Sim) |
| DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_CHEQUE | integer(4) |  | S | Dias para homologação da rescisão forma de pagamento cheque. |
| DEFINIR_DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_CREDITO_CONTA | smallint(2) |  |  | Definir dias para homologação da rescisão forma de pagamento crédito em conta. (0=Não/1=Sim) |
| DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_CREDITO_CONTA | integer(4) |  | S | Dias para homologação da rescisão forma de pagamento crédito em conta. |
| DEFINIR_DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_DINHEIRO | smallint(2) |  |  | Definir dias para homologação da rescisão forma de pagamento dinheiro. (0=Não/1=Sim) |
| DIAS_HOMOLOGACAO_RESCISAO_FORMA_PAGAMENTO_DINHEIRO | integer(4) |  | S | Dias para homologação da rescisão forma de pagamento dinheiro. |
| DEFINIR_AFASTAMENTOS_CONSIDERAR_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Definir os afastamentos para considerar como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_ACIDENTE_TRABALHO_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento acidente de trabalho como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_AUXILIO_DOENCA_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento auxílio doença como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_SERVICO_MILITAR_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento serviço militar como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_LICENCA_MATERNIDADE_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento licença maternidade como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_LICENCA_SEM_VENCIMENTO_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento licença sem vencimento como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_MANDATO_SINDICAL_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento exercício mandato sindical como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_ABORTO_NAO_CRIMINOSO_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento aborto não criminoso como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_OUTROS_MOTIVOS_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento outros motivos como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_CARCERE_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento cárcere como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_PARTICIPACAO_CURSO_PROGRAMA_QUALIFICACAO_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento participação em curso ou programa de qualificação como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_DOENCA_PROFISSIONAL_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento doença profissional como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_LICENCA_MATERNIDADE_MORTE_GENITORA_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento licença maternidade por morte da genitora como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_LICENCA_PATERNIDADE_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento licença paternidade como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_PROJECAO_AVISO_PREVIO_INDENIZADO_PAGAMENTO_INDENIZACAO_ESPECIAL | smallint(2) |  |  | Considerar os dias de projeção do aviso prévio indenizado para o pagamento da indenização especial. (0=Não/1=Sim) |
| CONSIDERAR_DIAS_GOZO_DILATAR_PERIODO_ESTABILIDADE | smallint(2) |  |  | Considerar os dias de gozo dentro do período de estabilidade para dilatar o mesmo. (0=Não/1=Sim) |
| CONSIDERA_REFLEXO_DSR_COMISSAO_CALC_GARANTIA_MIN_COMISSIONADO | smallint(2) |  |  | Considerar o reflexo do DSR da comissão para o cálculo da garantia mínima do comissionado. (0=Não/1=Sim) |
| CALCULAR_DSR_PROFESSOR_MENSALISTA_UM_SEXTO_SALARIO | smallint(2) |  |  | Calcular DSR professor mensalista no valor de 1/6 sobre o salário. (0=Não/1=Sim) |
| CONSIDERAR_MESES_ENTRE_PERIODO_VIGENCIA_PAGTO_PROPORC_PLR | smallint(2) |  |  | Considerar os meses entre as vigências inicial e final para o pagamento proporcional do PLR. (0=Não/1=Sim) |
| CONFIGURAR_AVISO_PREVIO_LEI_12506_2011 | smallint(2) |  |  | Configurar o aviso prévio conforme lei 12.506/2011. (0=Não/1=Sim) |
| INICIO_CALCULO_LEI_12506_2011 | smallint(2) |  | S | Início do cálculo proporcional para o aviso prévio - Lei 12.506/2011: (1=A partir do primeiro ano trabalhado completo/2=A partir do segundo ano trabalhado completo) |
| MOTIVO_DEMISSAO_LEI_12506_2011 | smallint(2) |  | S | Soma binária dos motivos de demissão que serão considerados para o cálculo dos dias de aviso prévio conforme a Lei 12.506/2011. |
| CONSIDERAR_PROJECAO_AVISO_PREVIO_INDENIZADO_DIAS_TRABALHADOS_LEI_12506_2011 | smallint(2) |  |  | Considerar a projeção do aviso prévio indenizado como dias trabalhados conforme a Lei 12.506/2011. (0=Não/1=Sim) |
| CONS_AVISO_PREVIO_INDENI_AVOS_INDENI_13_FERIAS_LEI_12506_2011 | smallint(2) |  |  | Considerar os dias de aviso prévio acrescidos pela Lei 12.506/2011 para projeção do aviso prévio na contagem de avos indenizados de 13º e Férias. |
| CONSIDERAR_DATA_INICIO_AVISO_PREVIO_TRABALHADO_CALCULO_ESTAB | smallint(2) |  |  | Considerar a data de início do aviso prévio trabalhado para o cálculo da estabilidade. (0=Não/1=Sim) |
| DESCONTAR_VALORES_COMISSAO_COMPETENCIA_INICIO_FIM_PERIODO_AFASTADO_GARANTIA_MINIMA_COMISSIONADO | smallint(2) |  |  | Descontar valores de comissão na competência inicio e fim do período afastado para o cálculo da garantia mínima do comissionado. (0=Não/1=Sim) |
| INICIAR_CONTAGEM_AVISO_PREVIO_INDENIZADO_PROXIMO_DIA_UTIL_QUANDO_CONCEDIDO_SEXTA_SABADO | smallint(2) |  |  | Iniciar a contagem do aviso prévio indenizado no próximo dia útil subsequente quando esse for concedido em sexta-feira ou sábado. (0=Não/1=Sim) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| CALCULAR_MULTA_ESTABILIDADE_DISSIDIO_CONFORME_PERCENTUAL | smallint(2) |  |  | Calcular o valor da multa devido estabilidade pelo dissídio conforme percentual. (0=Não/1=Sim) |
| FORMA_APURACAO_DIAS_PAGAMENTO_RESCISAO | smallint(2) |  |  | Forma de apuração dos dias: (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis) |
| CONSIDERAR_DIAS_AVISO_PREVIO_APENAS_EMPREGADOS_SEM_SUSPENSAO | smallint(2) |  |  | Considerar os dias de aviso prévio apenas para os empregados sem suspensão. (0=Não/1=Sim) |
| MESES_SEM_SUSPENSAO_CONSIDERAR_DIAS_AVISO_PREVIO | smallint(2) |  | S | Meses sem suspensão para considerar os dias de aviso prévio. |
| CONSIDERAR_FERIADOS_SINDICAIS_LANCAMENTO_VALE_TRANSPORTE | smallint(2) |  |  | Considerar os feriados de nível sindical como dias não úteis para o lançamento de vale transporte. (0=Não/1=Sim) |
| DEFINIR_DIAS_PAGAMENTO_RESCISAO_CONFORME_TIPO_AVISO_PREVIO | smallint(2) |  |  | Definir dias para pagamento da rescisão conforme tipo de aviso prévio rescisão. (0=Não/1=Sim) |
| DEFINIR_PERCENTUAL_MAXIMO_DESCONTO_VALE_TRANSPORTE | smallint(2) |  |  | Definir o percentual máximo para desconto de vale transporte. (0=Não/1=Sim) |
| PERCENTUAL_MAXIMO_DESCONTO_VALE_TRANSPORTE | numeric(5) |  | S | Percentual máximo para desconto de vale transporte. |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| GUID_CONTABIL | uniqueidentifier(16) |  |  | Identificador único do registro no banco do Contábil |
| GUID_ONVIO | uniqueidentifier(16) |  | S | Identificador único do registro no banco do Atendimento Onvio |
| CONSIDERAR_AVISO_PREVIO_DIAS_ANTECEDEM_DATA_BASE_LEI_12506_2011 | smallint(2) |  |  | considerar os dias de aviso prévio acrescidos pela Lei 12.506/2011 para projeção do aviso prévio na contagem dos dias que antecedem a data base. |
| CONSIDERAR_AFASTAMENTO_SUSPENSAO_SEM_AJUDA_COMPENSATORIA_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento suspensão sem ajuda compensatória como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_SUSPENSAO_COM_AJUDA_COMPENSATORIA_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento suspensão com ajuda compensatória como período trabalhado para o PLR. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| DESCONSIDERAR_MES_POR_DIAS_AFASTAMENTO | integer(4) |  |  | Afastamento que não irão considerar o mês como divisor para cálculo de médias se empregado ficou afastado por X dias. |
| DESCONSIDERAR_MES_POR_DIAS_REDUCAO | smallint(2) |  |  | Não considerar o mês como divisor para cálculo de médias se empregado possui redução por X dias. |
| RESILICAO_CALCULAR_13_PROPORCIONAL | smallint(2) |  |  | Resilição Professor - Calcular 13° salário proporcional a redução de grade. (0=Não/1=Sim) |
| RESILICAO_CALCULAR_FERIAS_PROPORCIONAL_VENCIDA_EMDOBRO | smallint(2) |  |  | Resilição Professor - Calcular Férias (proporcional, vencidas e em dobro) referente a redução de grade. (0=Não/1=Sim) |
| INICIAR_CONTAGEM_AVISO_PREVIO_A_PARTIR_DATA_INICIO_ESTABELECIDA | smallint(2) |  |  | Iniciar a contagem do aviso prévio a partir da data de início estabelecida. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_SUSPENSAO_CONTRATUAL_ACAO_TRAB_RESCISAO_INDIRETA_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento Suspensão contratual decorrente ação trabalhista por rescisão indireta como período trabalhado para o PLR. (0=Não/1=Sim) |
| CONSIDERAR_AFASTAMENTO_SUSPENSAO_CONTRATUAL_INQUERITO_APURACAO_FALTA_GRAVE_PERIODO_TRABALHADO_PLR | smallint(2) |  |  | Considerar afastamento Suspensão contratual para inquérito de apuração de falta grave como período trabalhado para o PLR. (0=Não/1=Sim) |
| DIAS_CONSIDERAR_FRACAO_AVO_FERIAS_NA_RESCISAO | integer(4) |  | S | Considerar a fração igual a [ ] dias trabalhados para cálculo de avos proporcionais de férias na rescisão |
| I_SINDICATOS_CADASTRO | integer(4) |  | S | Código do cadastro do sindicato |
