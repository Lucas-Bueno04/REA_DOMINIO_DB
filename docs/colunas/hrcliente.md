# HRCLIENTE — Clientes Fixos e Eventuais
2.918 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CLIENTE | integer(4) | PK |  | Codigo |
| APELIDO | varchar(20) |  |  | Apelido |
| NOME | varchar(40) |  |  | Nome |
| TIPO | char(1) |  |  | Tipo F Fixo E Eventual |
| I_CLIENTE_FIXO | integer(4) |  | S | Codigo do cliente fixo |
| DATA_CADASTRO | date(4) |  |  | Data de cadastro |
| TIPO_INSCRICAO | tinyint(1) |  |  | Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| INSCRICAO | varchar(14) |  | S | Inscricao |
| TIPO_ENDERECO | tinyint(1) |  |  | Tipo endecero |
| ENDERECO | varchar(40) |  | S | Endereco |
| NUMERO | integer(4) |  | S | Numero do endereco |
| BAIRRO | varchar(60) |  | S | Bairro |
| COMPLEMENTO | varchar(30) |  | S | Complemento |
| CODIGO_MUNICIPIO | integer(4) |  | S | Municipio |
| UF | char(2) |  | S | UF |
| CEP | char(8) |  | S | CEP |
| CAIXA_POSTAL | char(6) |  | S | Caixa postal |
| CODIGO_PAIS | integer(4) |  | S | Pais |
| EMAIL | varchar(255) |  | S | eMail |
| SITE | varchar(255) |  | S | Site |
| DDD_FONE | integer(4) |  | S | DD do telefone |
| FONE | varchar(14) |  | S | Telefone |
| DDD_FAX | integer(4) |  | S | DD do fax |
| FAX | varchar(14) |  | S | Fax |
| DDD_CELULAR | integer(4) |  | S | DD do celular |
| CELULAR | varchar(14) |  | S | celular |
| REGIME_FEDERAL | tinyint(1) |  | S | Regime federal 1 Normal 2 Microempresa 3 Empresa de Pequeno Porte |
| I_CLASSIFICACAO | integer(4) |  | S | Codigo da classificacao |
| OBSERVACAO | varchar(32000) |  | S | Observacoes |
| CONTA_CONTABIL | integer(4) |  |  | Conta contabil |
| GERA_CONTABILIZACAO | char(1) |  |  | Gera lancamentos contabeis na contabilidade S N |
| CONTA_HONORARIO | integer(4) |  |  | Conta honorarios a pagar |
| PAGAMENTO_CONTA_CREDITO | integer(4) |  |  | Conta credito de pagamento |
| PAGAMENTO_HISTORICO | integer(4) |  |  | Historico de pagamento |
| ADIANTAMENTO_DEBITO | integer(4) |  |  | Conta debito de adiantamento |
| ADIANTAMENTO_CREDITO | integer(4) |  |  | Conta credito de adiantamento |
| ADIANTAMENTO_HISTORICO | integer(4) |  |  | Historico de adiantamento |
| JUROS_CONTA | integer(4) |  |  | Conta juros |
| JUROS_HISTORICO | integer(4) |  |  | Historico juros |
| MULTA_CONTA | integer(4) |  |  | Conta multa |
| MULTA_HISTORICO | integer(4) |  |  | Historico multa |
| DESCONTO_CONTA | integer(4) |  |  | Conta desconto |
| DESCONTO_HISTORICO | integer(4) |  |  | Historico desconto |
| MOSTRAR_BAIXA_RECEBER | char(1) |  |  | Mostar lancamento contabil na baixa de contas a receber individual S N |
| MOSTRAR_ADIANTAMENTO | char(1) |  |  | Mostar lancamento contabil no adiantamento S N |
| POSSIVEL_CONTA_RECEBIMENTO | integer(4) |  | S | Possivel conta para recebimento |
| TIPO_COBRANCA | char(1) |  |  | Tipo de cobranca D Documento de cobranca B Boleto C Cobranca registrada |
| ENDERECO_COBRANCA | char(1) |  |  | Endereco para cobranca M Mesmo do cliente D Definir outro |
| COBRANCA_ENDERECO | varchar(40) |  | S | Endereco para cobranca Endereco |
| COBRANCA_NUMERO | integer(4) |  | S | Endereco para cobranca Numero |
| COBRANCA_BAIRRO | varchar(40) |  | S | Endereco para cobranca Bairro |
| COBRANCA_COMPLEMENTO | varchar(30) |  | S | Endereco para cobranca Complemento |
| COBRANCA_CODIGO_MUNICIPIO | integer(4) |  | S | Endereco para cobranca Municipio |
| COBRANCA_UF | char(2) |  | S | Endereco para cobranca UF |
| COBRANCA_CEP | char(8) |  | S | Endereco para cobranca CEP |
| COBRANCA_CAIXA_POSTAL | char(6) |  | S | Endereco para cobranca Caixa postal |
| COBRANCA_CODIGO_PAIS | integer(4) |  | S | Endereco para cobranca Pais |
| COBRANCA_TIPO_ENDERECO | tinyint(1) |  | S | Endereco para cobranca Tipo endecero |
| CRF_CONTA | integer(4) |  |  | Conta CRF |
| CRF_HISTORICO | integer(4) |  |  | Historico CRF |
| IRRF_CONTA | integer(4) |  |  | Conta IRRF |
| IRRF_HISTORICO | integer(4) |  |  | Historico IRRF |
| INSS_RET_CONTA | integer(4) |  |  | Conta INSS Retido |
| INSS_RET_HISTORICO | integer(4) |  |  | Historico INSS Retido |
| ISS_RET_CONTA | integer(4) |  |  | Conta ISS Retido |
| ISS_RET_HISTORICO | integer(4) |  |  | Historico ISS Retido |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| COBRANCA_AUTORIZA_DEBITO_CONTA | char(1) |  |  | Autoriza débido em conta (S/N) |
| DESCONSIDERAR_VALOR_MINIMO_CRF | char(1) |  |  | Desconsiderar valor mínimo da parcela para cálculo CRF |
| INSCRICAO_ESTADUAL | char(22) |  | S | Inscrição estadual |
| INSCRICAO_MUNICIPAL | char(20) |  | S | Inscrição municipal |
| SISTEMA_GESTAO | varchar(40) |  | S | Sistema de gestÃ£o usado pelo cliente |
| MODELO_CARTA_RESPONSABILIDADE | varchar(80) |  | S | Modelo de relatório de carta de responsabilidade de administração |
| I_OLE_CARTA_RESPONSABILIDADE | integer(4) |  | S | Código do modelo ole para carta de responsabilidade de administração |
| RAZAO_SOCIAL | varchar(255) |  |  | Razão Social |
| GERAR_NOTA_ENTRADA_ESCRITA | char(1) |  |  | Gerar notas de entrada no módulo Escrita Fiscal (S/N) |
| ESPECIE_NOTA_FISCAL | integer(4) |  | S | Espécie |
| ACUMULADOR_NOTA_FISCAL | integer(4) |  | S | Acumulador |
| CFOP_ESTADO | integer(4) |  | S | CFOP fornecedor do estado |
| CFOP_ESTADO_VERSAO | smallint(2) |  | S | CFOP fornecedor do estado versão |
| CFOP_OUTRO_ESTADO | integer(4) |  | S | CFOP fornecedor de outro estado |
| CFOP_OUTRO_ESTADO_VERSAO | smallint(2) |  | S | CFOP fornecedor de outro estado versão |
| CFPS_MUNICIPIO | integer(4) |  | S | CFPS fornecedor do município |
| CFPS_OUTRO_MUNICIPIO | integer(4) |  | S | CFPS fornecedor de outro município |
| CFPS_OUTRO_ESTADO | integer(4) |  | S | CFPS fornecedor de outro estado |
| GERAR_MOVIMENTO_PRODUTO | char(1) |  |  | Gerar movimento de produtos no módulo Escrita Fiscal (S/N) |
| INFORMAR_PRODUTO | char(1) |  |  | Informar produto (P=Padrão/ E=Para cada evento da nota fiscal) |
| PRODUTO_PADRAO | char(14) |  | S | Código do produto padrão |
| POSSUI_AVALISTA | char(1) |  |  | Possui Avalista |
| NOME_AVALISTA | varchar(40) |  | S | Nome do Avalista |
| TIPO_INSCRICAO_AVALISTA | integer(4) |  | S | Tipo de inscrição do Avalista |
| INSCRICAO_AVALISTA | varchar(14) |  | S | Inscrição do Avalista |
| ENDERECO_AVALISTA | varchar(40) |  | S | Endereço do Avalista |
| NUMERO_AVALISTA | integer(4) |  | S | Número do Avalista |
| BAIRRO_AVALISTA | varchar(60) |  | S | Bairro do Avalista |
| COMPLEMENTO_AVALISTA | varchar(30) |  | S | Complemento do Avalista |
| CODIGO_MUNICIPIO_AVALISTA | integer(4) |  | S | Município do Avalista |
| UF_AVALISTA | char(2) |  | S | UF do Avalista |
| CEP_AVALISTA | char(8) |  | S | CEP do Avalista |
| EMAIL_AVALISTA | varchar(255) |  | S | Email do Avalista |
| RENEGOCIACAO_CONTA_QUITAR_SEM_RECEBIMENTO | integer(4) |  |  | Renegociação - Conta quitar sem recebimento |
| RENEGOCIACAO_HISTORICO_QUITAR_SEM_RECEBIMENTO | integer(4) |  |  | Renegociação - Histórico quitar sem recebimento |
| NFSE_CLIENTE_ENQUADRADO_SUBTRI_ISS | char(1) |  |  | Cliente enquadrado na substituição tributária de ISS(S/N) |
| CONTATO | varchar(100) |  |  | Contato |
| DESCONTO_COBRANCA | char(1) |  |  | Desconto na cobrança(S/N) |
| DESCONTO_COBRANCA_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira do desconto de cobrança |
| DESCONTO_TIPO | tinyint(1) |  |  | Tipo de desconto(0 - Não conceder descontos/ 1 - Valor Fixo Até a Data Informada/ 2 - Percentual Até a Data Informada) |
| DESCONTO_DATA | char(1) |  |  | Desconto data(A - Antes do vencimento/ V - Vencimento) |
| DESCONTO_DIAS | integer(4) |  |  | Quantidade de dias do desconto |
| DESCONTO_VALOR_PERCENTUAL | numeric(13) |  |  | Valor ou percentual do desconto(Depende do tipo de desconto informado) |
| DESCONTOII_TIPO | tinyint(1) |  |  | Tipo de desconto(0 - Não conceder descontos/ 1 - Valor Fixo Até a Data Informada/ 2 - Percentual Até a Data Informada) |
| DESCONTOII_DATA | char(1) |  |  | Desconto data(A - Antes do vencimento/ V - Vencimento) |
| DESCONTOII_DIAS | integer(4) |  |  | Quantidade de dias do desconto |
| DESCONTOII_VALOR_PERCENTUAL | numeric(13) |  |  | Valor ou percentual do desconto(Depende do tipo de desconto informado) |
| DESCONTOIII_TIPO | tinyint(1) |  |  | Tipo de desconto(0 - Não conceder descontos/ 1 - Valor Fixo Até a Data Informada/ 2 - Percentual Até a Data Informada) |
| DESCONTOIII_DATA | char(1) |  |  | Desconto data(A - Antes do vencimento/ V - Vencimento) |
| DESCONTOIII_DIAS | integer(4) |  |  | Quantidade de dias do desconto |
| DESCONTOIII_VALOR_PERCENTUAL | numeric(13) |  |  | Valor ou percentual do desconto(Depende do tipo de desconto informado) |
| SELECIONAR_EVENTOS_CALCULO_DESCONTO_CLIENTE | varchar(1) |  |  | Selecionar eventos para cálculo de desconto ao cliente |
| EMAIL_EXCLUSIVO_FINANCEIRO | char(1) |  |  | Email exclusivo financeiro |
| EMAIL_EXCLUSIVO_FINANCEIRO_EMAIL | varchar(255) |  | S | Email exclusivo financeiro - Email |
| RENEGOCIACAO_CONTA_JUROS | integer(4) |  | S | Código da conta juros |
| RENEGOCIACAO_HISTORICO_JUROS | integer(4) |  | S | Código do historico da conta juros |
| RENEGOCIACAO_CONTA_MULTA | integer(4) |  | S | Código da conta multa |
| RENEGOCIACAO_HISTORICO_MULTA | integer(4) |  | S | Código do historico da conta multa |
| MOSTRAR_DESCONTO_MENSAL | char(1) |  |  | Mostrar desconto mensal |
| ORIGEM_EMP | integer(4) |  |  | Origem da empresa 1 - BRClient 0 - Dominio |
| MODELO_TERMO_CONFISSAO_DIVIDA | varchar(80) |  |  | Modelo de termo de confissão de dívida no momento da renegociação |
| I_OLE_TERMO_CONFISSAO_DIVIDA | integer(4) |  | S | Código do modelo ole para termo de confissão de dívida |
| NFSE_DESCONSIDERAR_INSCRICAO_MUNICIPAL | char(1) |  |  | Desconsiderar a inscricao municipal do tomador na emissao de NFS-e |
