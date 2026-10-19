# LRPARAMETRO_VIGENCIA — Parâmetros Lalur - Vigência
164 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(80) |  |  | Descrição |
| TIPO_CALCULO | tinyint(1) |  |  | Tipo de cálculo (1=Anual/Balanço de Redução e Suspensão/ 2=Trimestral/ 3=Anual/Recolhimento por estimativa/ 4=Não enquadrada) |
| TIPO_ATIVIDADE | char(1) |  |  | Tipo de atividade (G=Atividade geral/ R=Atividade rural/ A=Ambos) |
| CALCULAR_LUCRO_ESTIMADO | char(1) |  |  | Calcular lucro Estimado (S/N) |
| OPTAR_MENOR_CALCULO_REAL_ESTIMADO | char(1) |  |  | Optar sempre pelo menor valor a recolher entre os cálculos Real e Estimado (S/N) |
| APURAR_LUCRO_PREJUIZO_NAO_OPERACIONAL | char(1) |  |  | Apurar lucro/prejuízo não operacional (S/N) |
| CONTA_LUCRO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Lucro operacional gera |
| CONTA_PREJUIZO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Prejuízo operacional geral |
| CONTA_LUCRO_NAO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Lucro não operacional geral |
| CONTA_PREJUIZO_NAO_OPERACIONAL_GERAL | integer(4) |  |  | Conta - Prejuízo não operacional geral |
| CONTA_LUCRO_OPERACIONAL_RURAL | integer(4) |  |  | Conta - Lucro operacional rural |
| CONTA_PREJUIZO_OPERACIONAL_RURAL | integer(4) |  |  | Conta - Lucro não operacional rural |
| LANCAR_ADICAO_EXCLUSAO_DETALHANDO_LANCTO | char(1) |  |  | Lançar adições e exclusões detalhando os lançamentos contábeis (S/N) |
| CALCULAR_LUCRO_EXPLORACAO | char(1) |  |  | Calcular Lucro da Exploração (S/N) |
| CALCULAR_BONUS_ADIMPLENCIA_FISCAL | char(1) |  |  | Calcular Bônus da Adimplência Fiscal (S/N) |
| POSSUI_SCP | char(1) |  |  | Possui Sociedade em Conta de Participação - SCP (S/N) |
| REGISTRAR_AUTO_BASE_NEGATIVA_PARTE_B_PREJUIZO | char(1) |  |  | Registrar automaticamente na Base Negativa e Parte B os prejuízos apurados (S/N) |
| REALIZAR_CALCULO_ADICAO_EXCLUSAO_NA_COMPETENCIA | char(1) |  |  | Realizar o cálculo considerando somente as adições e exclusões lançadas na competência do cálculo (S/N) |
| I_ADICAO_CSLL_PARA_IRPJ | integer(4) |  | S | Adição - Contribuição Social como adição para o cálculo do IRPJ |
| GERAR_LANCAMENTO_CONTABIL | char(1) |  |  | Gerar lançamentos contábeis (S/N) |
| IMPOSTO_CSLL_RECOLHER_CONTA_DEBITO | integer(4) |  |  | Impostos CSLL - Recolher - conta débito |
| IMPOSTO_CSLL_RECOLHER_CONTA_CREDITO | integer(4) |  |  | Impostos CSLL - Recolher - conta crédito |
| IMPOSTO_CSLL_RECOLHER_HISTORICO | integer(4) |  |  | Impostos CSLL - Recolher - histórico |
| IMPOSTO_CSLL_RECUPERAR_CONTA_DEBITO | integer(4) |  |  | Impostos CSLL - Recuperar - conta débito |
| IMPOSTO_CSLL_RECUPERAR_CONTA_CREDITO | integer(4) |  |  | Impostos CSLL - Recuperar - conta crédito |
| IMPOSTO_CSLL_RECUPERAR_HISTORICO | integer(4) |  |  | Impostos CSLL - Recuperar - histórico |
| IMPOSTO_IRPJ_RECOLHER_CONTA_DEBITO | integer(4) |  |  | Impostos IRPJ - Recolher - conta débito |
| IMPOSTO_IRPJ_RECOLHER_CONTA_CREDITO | integer(4) |  |  | Impostos IRPJ - Recolher - conta crédito |
| IMPOSTO_IRPJ_RECOLHER_HISTORICO | integer(4) |  |  | Impostos IRPJ - Recolher - histórico |
| IMPOSTO_IRPJ_RECUPERAR_CONTA_DEBITO | integer(4) |  |  | Impostos IRPJ - Recuperar - conta débito |
| IMPOSTO_IRPJ_RECUPERAR_CONTA_CREDITO | integer(4) |  |  | Impostos IRPJ - Recuperar - conta crédito |
| IMPOSTO_IRPJ_RECUPERAR_HISTORICO | integer(4) |  |  | Impostos IRPJ - Recuperar - histórico |
| PAGAMENTO_CSLL_PRINCIPAL_CONTA_DEBITO | integer(4) |  |  | Pagamentos CSLL - Principal - conta débito |
| PAGAMENTO_CSLL_PRINCIPAL_CONTA_CREDITO | integer(4) |  |  | Pagamentos CSLL - Principal - conta crédito |
| PAGAMENTO_CSLL_PRINCIPAL_HISTORICO | integer(4) |  |  | Pagamentos CSLL - Principal - histórico |
| PAGAMENTO_CSLL_JUROS_CONTA_DEBITO | integer(4) |  |  | Pagamentos CSLL - Juros - conta débito |
| PAGAMENTO_CSLL_JUROS_CONTA_CREDITO | integer(4) |  |  | Pagamentos CSLL - Juros - conta crédito |
| PAGAMENTO_CSLL_JUROS_HISTORICO | integer(4) |  |  | Pagamentos CSLL - Juros - histórico |
| PAGAMENTO_CSLL_MULTA_CONTA_DEBITO | integer(4) |  |  | Pagamentos CSLL - Multa - conta débito |
| PAGAMENTO_CSLL_MULTA_CONTA_CREDITO | integer(4) |  |  | Pagamentos CSLL - Multa - conta crédito |
| PAGAMENTO_CSLL_MULTA_HISTORICO | integer(4) |  |  | Pagamentos CSLL - Multa - histórico |
| PAGAMENTO_IRPJ_PRINCIPAL_CONTA_DEBITO | integer(4) |  |  | Pagamentos IRPJ - Principal - conta débito |
| PAGAMENTO_IRPJ_PRINCIPAL_CONTA_CREDITO | integer(4) |  |  | Pagamentos IRPJ - Principal - conta crédito |
| PAGAMENTO_IRPJ_PRINCIPAL_HISTORICO | integer(4) |  |  | Pagamentos IRPJ - Principal - histórico |
| PAGAMENTO_IRPJ_JUROS_CONTA_DEBITO | integer(4) |  |  | Pagamentos IRPJ - Juros - conta débito |
| PAGAMENTO_IRPJ_JUROS_CONTA_CREDITO | integer(4) |  |  | Pagamentos IRPJ - Juros - conta crédito |
| PAGAMENTO_IRPJ_JUROS_HISTORICO | integer(4) |  |  | Pagamentos IRPJ - Juros - histórico |
| PAGAMENTO_IRPJ_MULTA_CONTA_DEBITO | integer(4) |  |  | Pagamentos IRPJ - Multa - conta débito |
| PAGAMENTO_IRPJ_MULTA_CONTA_CREDITO | integer(4) |  |  | Pagamentos IRPJ - Multa - conta crédito |
| PAGAMENTO_IRPJ_MULTA_HISTORICO | integer(4) |  |  | Pagamentos IRPJ - Multa - histórico |
| CSLL_CODIGO_RECOLHIMENTO | varchar(6) |  |  | Imposto CSLL - Código de recolhimento |
| CSLL_ALIQUOTA_IMPOSTO | integer(4) |  |  | Imposto CSLL - Alíquota do imposto |
| CSLL_FORMA_VENCIMENTO | tinyint(1) |  |  | Imposto CSLL - Forma de vencimento (1=Corridos direto/ 2=Corridos antecipados/ 3=Corridos adiados/ 4=Úteis/ 5=Último dia útil) |
| CSLL_DIA_VENCIMENTO | integer(4) |  |  | Imposto CSLL - Dia do vencimento |
| CSLL_CONSIDERAR_FERIADO_MUNICIPAL | char(1) |  |  | Imposto CSLL - Considerar feriados municipais para o vencimento do imposto (S/N) |
| IRPJ_CODIGO_RECOLHIMENTO | varchar(6) |  |  | Imposto IRPJ - Código de recolhimento |
| IRPJ_ALIQUOTA_IMPOSTO | numeric(5) |  |  | Imposto IRPJ - Alíquota do imposto |
| IRPJ_FORMA_VENCIMENTO | tinyint(1) |  |  | Imposto IRPJ - Forma de vencimento (1=Corridos direto/ 2=Corridos antecipados/ 3=Corridos adiados/ 4=Úteis/ 5=Último dia útil) |
| IRPJ_DIA_VENCIMENTO | integer(4) |  |  | Imposto IRPJ - Dia do vencimento |
| IRPJ_CONSIDERAR_FERIADO_MUNICIPAL | char(1) |  |  | Imposto IRPJ - Considerar feriados municipais para o vencimento do imposto (S/N) |
| PARTE_B_PREJUIZO_OPERACIONAL_GERAL_CONTA | integer(4) |  | S | Parte B - Prejuízo operacional geral - conta Parte B |
| PARTE_B_PREJUIZO_OPERACIONAL_GERAL_HISTORICO_PREJUIZO | varchar(250) |  |  | Parte B - Prejuízo operacional geral - histórico prejuízo |
| PARTE_B_PREJUIZO_OPERACIONAL_GERAL_HISTORICO_COMPENSACAO | varchar(250) |  |  | Parte B - Prejuízo operacional geral - histórico compensação |
| PARTE_B_PREJUIZO_NAO_OPERACIONAL_GERAL_CONTA | integer(4) |  | S | Parte B - Prejuízo não operacional geral - conta Parte B |
| PARTE_B_PREJUIZO_NAO_OPERACIONAL_GERAL_HISTORICO_PREJUIZO | varchar(250) |  |  | Parte B - Prejuízo não operacional geral - histórico prejuízo |
| PARTE_B_PREJUIZO_NAO_OPERACIONAL_GERAL_HISTORICO_COMPENSACAO | varchar(250) |  |  | Parte B - Prejuízo não operacional geral - histórico compensação |
| PARTE_B_PREJUIZO_NAO_OPERACIONAL_GERAL_HISTORICO_TRANSFERENCIA | varchar(250) |  |  | Parte B - Prejuízo não operacional geral - histórico transferência |
| PARTE_B_PREJUIZO_ATIVIDADE_RURAL_CONTA | integer(4) |  | S | Parte B - Prejuízo atividade rural - conta Parte B |
| PARTE_B_PREJUIZO_ATIVIDADE_RURAL_HISTORICO_PREJUIZO | varchar(250) |  |  | Parte B - Prejuízo atividade rural - histórico prejuízo |
| PARTE_B_PREJUIZO_ATIVIDADE_RURAL_HISTORICO_COMPENSACAO | varchar(250) |  |  | Parte B - Prejuízo atividade rural - histórico compensação |
| BASE_NEGATIVA_PREJUIZO_OPERACIONAL_GERAL_CONTA | integer(4) |  | S | Base Negativa - Prejuízo operacional geral - conta Base Negativa |
| BASE_NEGATIVA_PREJUIZO_OPERACIONAL_GERAL_HISTORICO_PREJUIZO | varchar(250) |  |  | Base Negativa - Prejuízo operacional geral - histórico prejuízo |
| BASE_NEGATIVA_PREJUIZO_OPERACIONAL_GERAL_HISTORICO_COMPENSACAO | varchar(250) |  |  | Base Negativa - Prejuízo operacional geral - histórico compensação |
| BASE_NEGATIVA_PREJUIZO_ATIVIDADE_RURAL_CONTA | integer(4) |  | S | Base Negativa - Prejuízo atividade rural - conta Base Negativa |
| BASE_NEGATIVA_PREJUIZO_ATIVIDADE_RURAL_HISTORICO_PREJUIZO | varchar(250) |  |  | Base Negativa - Prejuízo atividade rural - histórico prejuízo |
| BASE_NEGATIVA_PREJUIZO_ATIVIDADE_RURAL_HISTORICO_COMPENSACAO | varchar(250) |  |  | Base Negativa - Prejuízo atividade rural - histórico compensação |
| TIPO_QUALIFICACAO_PESSOA_JURIDICA | integer(4) |  |  | Tipo de qualificação da Pessoa Jurídica |
| AJUSTE_ANUAL_CSLL_CODIGO_RECOLHIMENTO | varchar(6) |  |  | Ajuste anual - Imposto CSLL - Código de recolhimento |
| AJUSTE_ANUAL_IRPJ_CODIGO_RECOLHIMENTO | varchar(6) |  |  | Ajuste anual - Imposto IRPJ - Código de recolhimento |
| DEFINIR_COMPETENCIA_INICIAL_LUCRO_REAL | char(1) |  |  | Definir competÃªncia da apuraÃ§Ã£o pelo Lucro Real |
| COMPETENCIA_INICIAL_LUCRO_REAL | integer(4) |  | S | CompetÃªncia da apuraÃ§Ã£o pelo Lucro Real (2-Fevereiro / 3-MarÃ§o / 4-Abril / 5-Maio / 6-Junho / 7-Julho / 8-Agosto/9-Setembro / 10-Outubro / 11-Novembro / 12-Dezembro) |
| REALIZAR_CALCULO_DEDUCAO_NA_COMPETENCIA | char(1) |  |  | Realizar o cálculo considerando somente as deduções lançadas na competência do cálculo (S/N) |
| I_ADICAO_LUCRO_EXPLORACAO_CSLL_PARA_IRPJ | integer(4) |  | S | Adição - Lucro da Exploração Contribuição Social como adição para o cálculo do IRPJ |
| PREJUIZO_APURADO | char(1) |  |  | PREJUÍZOS APURADOS (T-REGISTRAR TODOS OS MESES / D-REGISTRAR SOMENTE NO MÊS DE DEZEMBRO) |
| DEDUZIR_AUTOMATICAMENTE_CALCULO_VALOR_APURADO_MES_ANTERIOR | char(1) |  |  | Deduzir automaticamente no cálculo os valores apurados em meses anteriores |
| DEDUZIR_AUTOMATICAMENTE_CALCULO_SALDO_DEDUCAO_PERIODO_ANTERIOR | char(1) |  |  | Deduzir automaticamente no cálculo de deduções de período anterior |
| REGISTRAR_AUTO_PARTE_B_INCENTIVO_FISCAL_PAT | char(1) |  |  | Registrar automaticamente na Parte B os valores do incentivo fiscal PAT (S/N) |
| VALOR_APROVEITADO | char(1) |  |  | Valores aproveitados (T-Registrar todos os meses / D-Registrar somente no mês de dezembro) |
| PARTE_B_INCENTIVO_FISCAL_CONTA | integer(4) |  | S | Parte B - Incentivo fiscal - conta Parte B |
| PARTE_B_INCENTIVO_FISCAL_HISTORICO_VALOR_LANCADO | varchar(250) |  |  | Parte B - Incentivo fiscal - histórico valor lançado |
| PARTE_B_INCENTIVO_FISCAL_HISTORICO_VALOR_APROVEITADO | varchar(250) |  |  | Parte B - Incentivo fiscal - histórico valor aproveitado |
| PARTE_B_INCENTIVO_FISCAL_HISTORICO_BAIXA_VALOR_NAO_APROVEITADO | varchar(250) |  |  | Parte B - Incentivo fiscal - histórico valor não aproveitado |
| COMPENSACAO_PREJUIZO | char(1) |  |  | Compensação de prejuízos (T-Registrar todos os meses / D-Registrar somente no mês de dezembro) |
| DEDUCAO_CSLL_ORGAO_PUBLICO_FEDERAL_CONTA_CREDITO | integer(4) |  |  | Dedução Contribuição Social retida por órgãos públicos federais - conta crédito |
| DEDUCAO_CSLL_ORGAO_PUBLICO_FEDERAL_CONTA_DEBITO | integer(4) |  |  | Dedução Contribuição Social retida por órgãos públicos federais - conta débito |
| DEDUCAO_CSLL_ORGAO_PUBLICO_FEDERAL_HISTORICO | integer(4) |  |  | Dedução Contribuição Social retida por órgãos públicos federais - histórico |
| DEDUCAO_CSLL_PESSOA_JURIDICA_CONTA_CREDITO | integer(4) |  |  | Dedução Contribuição Social retida por outras pessoas jurídicas - conta crédito |
| DEDUCAO_CSLL_PESSOA_JURIDICA_CONTA_DEBITO | integer(4) |  |  | Dedução Contribuição Social retida por outras pessoas jurídicas - conta débito |
| DEDUCAO_CSLL_PESSOA_JURIDICA_HISTORICO | integer(4) |  |  | Dedução Contribuição Social retida por outras pessoas jurídicas - histórico |
| DEDUCAO_CSLL_MES_ANTERIOR_CONTA_CREDITO | integer(4) |  |  | Dedução Contribuição Social pago em meses anteriores - conta crédito |
| DEDUCAO_CSLL_MES_ANTERIOR_CONTA_DEBITO | integer(4) |  |  | Dedução Contribuição Social pago em meses anteriores - conta débito |
| DEDUCAO_CSLL_MES_ANTERIOR_HISTORICO | integer(4) |  |  | Dedução Contribuição Social pago em meses anteriores - histórico |
| DEDUCAO_IRPJ_IRRF_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ - conta crédito |
| DEDUCAO_IRPJ_IRRF_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ - conta débito |
| DEDUCAO_IRPJ_IRRF_HISTORICO | integer(4) |  |  | Dedução IRPJ - histórico |
| DEDUCAO_IRPJ_ORGAO_PUBLICO_FEDERAL_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ por órgãos públicos federais - conta crédito |
| DEDUCAO_IRPJ_ORGAO_PUBLICO_FEDERAL_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ por órgãos públicos federais - conta débito |
| DEDUCAO_IRPJ_ORGAO_PUBLICO_FEDERAL_HISTORICO | integer(4) |  |  | Dedução IRPJ por órgãos públicos federais - histórico |
| DEDUCAO_IRPJ_MES_ANTERIOR_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ pago em meses anteriores - conta crédito |
| DEDUCAO_IRPJ_MES_ANTERIOR_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ pago em meses anteriores - conta débito |
| DEDUCAO_IRPJ_MES_ANTERIOR_HISTORICO | integer(4) |  |  | Dedução IRPJ pago em meses anteriores - histórico |
| DEDUCAO_IR_CSLL_PAGO_MES_ANTERIOR | char(1) |  |  | Dedução IR e CSLL pago em meses anteriores (F=Considerar o valor final a recolher / A=Considerar o valor apurado antes das demais deduções) |
| INCENTIVO_ALIMENTACAO_TRABALHADOR_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Programa de alimentação do trabalhador - conta débito |
| INCENTIVO_ALIMENTACAO_TRABALHADOR_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Programa de alimentação do trabalhador - conta crédito |
| INCENTIVO_ALIMENTACAO_TRABALHADOR_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Programa de alimentação do trabalhador - histórico |
| INCENTIVO_CULTURAL_ARTISTICO_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Operações de caráter cultural e artístico - conta débito |
| INCENTIVO_CULTURAL_ARTISTICO_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Operações de caráter cultural e artístico - conta crédito |
| INCENTIVO_CULTURAL_ARTISTICO_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Operações de caráter cultural e artístico - histórico |
| INCENTIVO_VALE_CULTURA_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Operações de aquisição de vale cultura - conta débito |
| INCENTIVO_VALE_CULTURA_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Operações de aquisição de vale cultura - conta crédito |
| INCENTIVO_VALE_CULTURA_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Operações de aquisição de vale cultura - histórico |
| INCENTIVO_INDUSTRIAL_AGROPECUARIO_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Desenvolvimento tecnológico industrial / agropecuário - conta débito |
| INCENTIVO_INDUSTRIAL_AGROPECUARIO_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Desenvolvimento tecnológico industrial / agropecuário - conta crédito |
| INCENTIVO_INDUSTRIAL_AGROPECUARIO_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Desenvolvimento tecnológico industrial / agropecuário - histórico |
| INCENTIVO_AUDIOVISUAL_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Atividade audiovisual - conta débito |
| INCENTIVO_AUDIOVISUAL_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Atividade audiovisual - conta crédito |
| INCENTIVO_AUDIOVISUAL_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Atividade audiovisual - histórico |
| INCENTIVO_CRIANCA_ADOLESCENTE_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Fundos dos direitos da criança e adolescente - conta débito |
| INCENTIVO_CRIANCA_ADOLESCENTE_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Fundos dos direitos da criança e adolescente - conta crédito |
| INCENTIVO_CRIANCA_ADOLESCENTE_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Fundos dos direitos da criança e adolescente - histórico |
| INCENTIVO_CARATER_DISPOSITIVO_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Atividades da caráter desportivo - conta débito |
| INCENTIVO_CARATER_DISPOSITIVO_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Atividades da caráter desportivo - conta crédito |
| INCENTIVO_CARATER_DISPOSITIVO_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Atividades da caráter desportivo - histórico |
| INCENTIVO_IDOSO_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Fundos nacional, estaduais e municipais do idoso - conta débito |
| INCENTIVO_IDOSO_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Fundos nacional, estaduais e municipais do idoso - conta crédito |
| INCENTIVO_IDOSO_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Fundos nacional, estaduais e municipais do idoso - histórico |
| INCENTIVO_ATENCAO_ONCOLOGICA_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção oncológica - conta débito |
| INCENTIVO_ATENCAO_ONCOLOGICA_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção oncológica - conta crédito |
| INCENTIVO_ATENCAO_ONCOLOGICA_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção oncológica - histórico |
| INCENTIVO_ATENCAO_SAUDE_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção da saúde da pessoa com deficiência - conta débito |
| INCENTIVO_ATENCAO_SAUDE_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção da saúde da pessoa com deficiência - conta crédito |
| INCENTIVO_ATENCAO_SAUDE_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Programa nacional de apoio à atenção da saúde da pessoa com deficiência - histórico |
| INCENTIVO_LICENCA_MATERNIDADE_CONTA_DEBITO | integer(4) |  |  | Incentivos Fiscais - Valor da remuneração da prorrogação da licença maternidade - conta débito |
| INCENTIVO_LICENCA_MATERNIDADE_CONTA_CREDITO | integer(4) |  |  | Incentivos Fiscais - Valor da remuneração da prorrogação da licença maternidade - conta crédito |
| INCENTIVO_LICENCA_MATERNIDADE_HISTORICO | integer(4) |  |  | Incentivos Fiscais - Valor da remuneração da prorrogação da licença maternidade - histórico |
| CALCULAR_BONUS_ADIMPLENCIA_FISCAL_SOBRE | char(1) |  |  | Calcular sobre (B - Base de cálculo da CSLL após compensação/N - Receita Bruta) |
| CONSIDERAR_SALDO_DEVOLUCAO_PERIODO_ANTERIOR_IMPORTACAO_RECEITA_BRUTA | char(1) |  |  | Considerar o saldo de devoluções de períodos anteriores na importação da Receita Bruta(S/N) |
| CONSIDERAR_JUROS_MULTAS_OUTRAS_ESCRITA_FISCAL | char(1) |  |  | Considerar como receita financeira os juros, multas e outras das parcelas das notas no módulo Escrita Fiscal |
| COMPENSACAO_IF_CSLL_COMPENSAR_CONTA_DEBITO | integer(4) |  |  | Impostos CSLL - Compensação - Conta Débito |
| COMPENSACAO_IF_CSLL_COMPENSAR_CONTA_CREDITO | integer(4) |  |  | Impostos CSLL - Compensação - Conta Crédito |
| COMPENSACAO_IF_CSLL_COMPENSAR_HISTORICO | integer(4) |  |  | Impostos CSLL - Compensação - Conta Historico |
| COMPENSACAO_IF_IRPJ_COMPENSAR_CONTA_DEBITO | integer(4) |  |  | Impostos IRPJ - Compensação - Conta Débito |
| COMPENSACAO_IF_IRPJ_COMPENSAR_CONTA_CREDITO | integer(4) |  |  | Impostos IRPJ - Compensação - Conta Crédito |
| COMPENSACAO_IF_IRPJ_COMPENSAR_HISTORICO | integer(4) |  |  | Impostos IRPJ - Compensação - Conta Historico |
| INCENTIVOS_FISCAIS_LANCAR | char(1) |  |  | Valor de Pessoa Júridica Sistema Financeiro Presumido |
| COMPLEMENTO_ADICAO_CSLL_PARA_IRPJ | varchar(100) |  | S | Complemento de ContribuiÃ§Ã£o Social como adiÃ§Ã£o para o cÃ¡lculo IRPJ |
| DETALHAR_LANCAMENTOS_ADICOES_EXCLUSOES_CCU | char(1) |  |  | Detalhar os lanÃ§amentos de AdiÃ§Ãµes e ExclusÃµes por centro de custos (S/N) |
| CONTABILIZACAO_CSLL_AN_CONTA_DEBITO | integer(4) |  |  | Impostos CSLL - Ajuste Anual - Conta Débito |
| CONTABILIZACAO_CSLL_AN_CONTA_CREDITO | integer(4) |  |  | Impostos CSLL - Ajuste Anual - Conta Crédito |
| CONTABILIZACAO_CSLL_AN_HISTORICO | integer(4) |  |  | Impostos CSLL - Ajuste Anual - Conta Historico |
| CONTABILIZACAO_IRPJ_AN_CONTA_DEBITO | integer(4) |  |  | Impostos IRPJ - Ajuste Anual - Conta Débito |
| CONTABILIZACAO_IRPJ_AN_CONTA_CREDITO | integer(4) |  |  | Impostos IRPJ - Ajuste Anual - Conta Crédito |
| CONTABILIZACAO_IRPJ_AN_HISTORICO | integer(4) |  |  | Impostos IRPJ - Ajuste Anual - Conta Historico |
| TIPO_CONSIDERA_VALOR_ADICAO | char(1) |  |  | Valor a ser considerado na adição (CSLL devida/CSLL a recolher |
| DEFINIR_TERMINO_FRUICAO_PERSE_CSLL | char(1) |  |  | Definir término de fruição do Perse para o imposto CSLL |
| DEFINIR_TERMINO_FRUICAO_PERSE_IRPJ | char(1) |  |  | Definir término de fruição do Perse para o imposto IRPJ |
| DATA_TERMINO_FRUICAO_PERSE_CSLL | date(4) |  | S | Data término de fruição do Perse para o imposto CSLL |
| DATA_TERMINO_FRUICAO_PERSE_IRPJ | date(4) |  | S | Data término de fruição do Perse para o imposto IRPJ |
| CODIGO_HISTORICO_LUCRO_ECF | integer(4) |  | S | Código do histórico de Lucro do Sped Ecf |
| DESCRICAO_HISTORICO_LUCRO_ECF | varchar(250) |  | S | Descrição do histórico de Lucro do Sped Ecf |
| CODIGO_HISTORICO_PREJUIZO_ECF | integer(4) |  | S | Código do histórico de Prejuizo do Sped Ecf |
| DESCRICAO_HISTORICO_PREJUIZO_ECF | varchar(250) |  | S | Descrição do histórico de Prejuizo do Sped Ecf |
| DEDUCAO_CSLL_RETIDA_ESTADOS_MUNICIPIOS_CONTA_CREDITO | integer(4) |  |  | Dedução Contribuição Social retida por Estados e Municipios - conta crédito |
| DEDUCAO_CSLL_RETIDA_ESTADOS_MUNICIPIOS_CONTA_DEBITO | integer(4) |  |  | Dedução Contribuição Social retida por Estados e Municipios - conta débito |
| DEDUCAO_CSLL_RETIDA_ESTADOS_MUNICIPIOS_HISTORICO | integer(4) |  |  | Dedução Contribuição Social retida por Estados e Municipios - histórico |
| DEDUCAO_CSLL_RETIDA_ADM_PUBLICA_CONTA_CREDITO | integer(4) |  |  | Dedução Contribuição Social retida por administração pública - conta crédito |
| DEDUCAO_CSLL_RETIDA_ADM_PUBLICA_CONTA_DEBITO | integer(4) |  |  | Dedução Contribuição Social retida por administração pública - conta débito |
| DEDUCAO_CSLL_RETIDA_ADM_PUBLICA_HISTORICO | integer(4) |  |  | Dedução Contribuição Social retida por administração pública - histórico |
| DEDUCAO_CSLL_PAGO_EXTERIOR_CONTA_CREDITO | integer(4) |  |  | Dedução Pago no exterior sobre lucros, rendimentos e ganhos de capital - conta crédito |
| DEDUCAO_CSLL_PAGO_EXTERIOR_CONTA_DEBITO | integer(4) |  |  | Dedução Pago no exterior sobre lucros, rendimentos e ganhos de capital - conta débito |
| DEDUCAO_CSLL_PAGO_EXTERIOR_HISTORICO | integer(4) |  |  | Dedução Pago no exterior sobre lucros, rendimentos e ganhos de capital - histórico |
| DEDUCAO_CSLL_PARCELAMENTO_FORMALIZADO_CONTA_CREDITO | integer(4) |  |  | Dedução Parcelamento formalizado de CSLL sobre a base de cálculo estimada - conta crédito |
| DEDUCAO_CSLL_PARCELAMENTO_FORMALIZADO_CONTA_DEBITO | integer(4) |  |  | Dedução Parcelamento formalizado de CSLL sobre a base de cálculo estimada - conta débito |
| DEDUCAO_CSLL_PARCELAMENTO_FORMALIZADO_HISTORICO | integer(4) |  |  | Dedução Parcelamento formalizado de CSLL sobre a base de cálculo estimada - histórico |
| DEDUCAO_CSLL_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_CONTA_CREDITO | integer(4) |  |  | Dedução Compensação de impostos federais de períodos anteriores - conta crédito |
| DEDUCAO_CSLL_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_CONTA_DEBITO | integer(4) |  |  | Dedução Compensação de impostos federais de períodos anteriores - conta débito |
| DEDUCAO_CSLL_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_HISTORICO | integer(4) |  |  | Dedução Compensação de impostos federais de períodos anteriores - histórico |
| DEDUCAO_CSLL_COMPENSACAO_RECUPERACAO_CREDITO_CSLL_CONTA_CREDITO | integer(4) |  |  | Dedução Recuperação de crédito CSLL - conta crédito |
| DEDUCAO_CSLL_COMPENSACAO_RECUPERACAO_CREDITO_CSLL_CONTA_DEBITO | integer(4) |  |  | Dedução Recuperação de crédito CSLL - conta débito |
| DEDUCAO_CSLL_COMPENSACAO_RECUPERACAO_CREDITO_CSLL_HISTORICO | integer(4) |  |  | Dedução Recuperação de crédito CSLL - histórico |
| DEDUCAO_CSLL_COMPENSACAO_CREDITO_DEPRECIACAO_IMOBILIZADO_CONTA_CREDITO | integer(4) |  |  | Dedução Crédito sobre depreciação de imobilizado - conta crédito |
| DEDUCAO_CSLL_COMPENSACAO_CREDITO_DEPRECIACAO_IMOBILIZADO_CONTA_DEBITO | integer(4) |  |  | Dedução Crédito sobre depreciação de imobilizado - conta débito |
| DEDUCAO_CSLL_COMPENSACAO_CREDITO_DEPRECIACAO_IMOBILIZADO_HISTORICO | integer(4) |  |  | Dedução Crédito sobre depreciação de imobilizado - histórico |
| DEDUCAO_IRPJ_IRRF_ADM_PUBLICA_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ IRRF Administracao pública - conta crédito |
| DEDUCAO_IRPJ_IRRF_ADM_PUBLICA_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ  IRRF Administracao pública - conta débito |
| DEDUCAO_IRPJ_IRRF_ADM_PUBLICA_HISTORICO | integer(4) |  |  | Dedução IRPJ IRRF Administracao pública - histórico |
| DEDUCAO_IRPJ_PAGO_EXTERIOR_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ Pago no exterior sobre lucros, rendimentos e ganhos de capital - conta crédito |
| DEDUCAO_IRPJ_PAGO_EXTERIOR_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ Pago no exterior sobre lucros, rendimentos e ganhos de capital - conta débito |
| DEDUCAO_IRPJ_PAGO_EXTERIOR_HISTORICO | integer(4) |  |  | Dedução IRPJ Pago no exterior sobre lucros, rendimentos e ganhos de capital - histórico |
| DEDUCAO_IRPJ_PAGO_INCIDENTE_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ Pago incidente sobre ganhos no mercado de renda variável - conta crédito |
| DEDUCAO_IRPJ_PAGO_INCIDENTE_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ Pago incidente sobre ganhos no mercado de renda variável - conta débito |
| DEDUCAO_IRPJ_PAGO_INCIDENTE_HISTORICO | integer(4) |  |  | Dedução IRPJ Pago incidente sobre ganhos no mercado de renda variável - histórico |
| DEDUCAO_IRPJ_PARCELAMENTO_FORMALIZADO_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ Parcelamento formalizado de IR sobre a base de cálculo estimada - conta crédito |
| DEDUCAO_IRPJ_PARCELAMENTO_FORMALIZADO_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ Parcelamento formalizado de IR sobre a base de cálculo estimada - conta débito |
| DEDUCAO_IRPJ_PARCELAMENTO_FORMALIZADO_HISTORICO | integer(4) |  |  | Dedução IRPJ Parcelamento formalizado de IR sobre a base de cálculo estimada - histórico |
| DEDUCAO_IRPJ_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_CONTA_CREDITO | integer(4) |  |  | Dedução IRPJ Compensação de impostos federais de períodos anteriores - conta crédito |
| DEDUCAO_IRPJ_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_CONTA_DEBITO | integer(4) |  |  | Dedução IRPJ Compensação de impostos federais de períodos anteriores - conta débito |
| DEDUCAO_IRPJ_COMPENSACAO_IMPOSTO_FEDERAL_PERIODO_ANT_HISTORICO | integer(4) |  |  | Dedução IRPJ Compensação de impostos federais de períodos anteriores - histórico |
