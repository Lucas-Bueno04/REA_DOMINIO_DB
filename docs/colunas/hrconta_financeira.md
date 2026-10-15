# HRCONTA_FINANCEIRA — Contas financeiras
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_CONTA_FINANCEIRA | integer(4) | PK |  | Codigo |
| DESCRICAO | char(60) |  |  | Descricao |
| TIPO | char(1) |  |  | TIPO (B=BANCARIA/C=CAIXA/H=CHEQUE) |
| I_BANCO | integer(4) |  | S | Codigo banco |
| I_AGENCIA | integer(4) |  | S | Codigo agencia |
| CONTA_CORRENTE | char(10) |  | S | Conta corrente |
| DV_CONTA_CORRENTE | char(2) |  | S | Digito verificador da conta corrente |
| CONTA_CONTABIL | integer(4) |  |  | Conta contabil |
| CARTEIRA | tinyint(1) |  | S | CARTEIRA (1=COBRANCA COM REGISTRO (SIGCB)/ 2=COBRANCA SEM REGISTRO (SIGCB)/ 4=COBRANÇA DESCONTADA/ 5=COBRANÇA RÁPIDA COM REGISTRO/ 6=COBRANÇA SIMPLES/ 82=COBRANCA SEM REGISTRO/ 90=CABRANCA RAPIDA/ 201=PENHOR) |
| CEDENTE | char(20) |  | S | Cedente |
| DV_CEDENTE | char(2) |  | S | Digito verificador cedente |
| TIPO_NOSSO_NRO | tinyint(1) |  |  | Tipo nosso numero (11=Posições/17=Posições-SINCO/172=Posições-SIGCB/ 16=Posições) |
| INTERVALO_NUMERACAO | char(1) |  |  | Informar intervalo da numeracao S N |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CODIGO_CONVENIO | varchar(20) |  | S | Codigo do convenio |
| NUMERO_CONTRATO | varchar(10) |  | S | Numero do contrato |
| NOTA_FISCAL | integer(4) |  | S | Especie do titulo notas fiscais |
| DOCUMENTO_COBRANCA | integer(4) |  | S | Especie do titulo documento de cobranca |
| SOMENTE_BOLETO | integer(4) |  | S | Especie do titulo somente boleto |
| ENVIA_COBRANCA_REGISTRADA | char(1) |  |  | Envia cobranca registrada S N |
| MODALIDADE_BOLETO | integer(4) |  | S | Modalidade usada na emissao do boleto |
| AGENCIA_CEDENTE_BOLETO | integer(4) |  | S | Agencia cedente usada na emissao do boleto |
| POSTO_AG_CEDENTE_BOLETO | integer(4) |  | S | Posto da agencia cedente usada na emissao do boleto |
| OPERACAO_CODIGO_CEDENTE_BOLETO | integer(4) |  | S | Operacao codigo cedente |
| CARTEIRA_BOLETO | integer(4) |  | S | Carteira usada na emissao do boleto |
| CONVENIO_BOLETO | varchar(7) |  | S | Convenio usado na emissao do boleto |
| ESPECIE_BOLETO | char(10) |  | S | Especie usada na emissao do boleto |
| TIPO_DOCUMENTO | tinyint(1) |  |  | Tipo de documento (1=Tradicional ou Direto/ 2=Escritural) |
| ESPECIE_DOCUMENTO_BOLETO | varchar(10) |  | S | Especie do documento usada na emissao do boleto |
| ACEITE | char(1) |  |  | Aceite usada na emissao do boleto |
| TIPO_COBRANCA | integer(4) |  |  | Tipo de cobrança |
| IMPRESSAO_BOLETO_PELO_BANCO | char(1) |  |  | Impressão do boleto pelo banco (S/N) |
| TIPO_REMESSA | tinyint(1) |  |  | Tipo de remessa (1=CNAB 240/ 2=CNAB 400) |
| TIPO_CONTA | tinyint(1) |  | S | Tipo da conta |
| BANCO_REMESSA | tinyint(1) |  |  | BANCO PARA REMESSA (1=TRANSPOCRED OU CREDIP/ 2=VIACREDI OU OUTROS/ 3=CREDCREA OU ECOCREDI/ 4=UNICRED) |
| CODIGO_COBRANCA | integer(4) |  |  | Código de cobrança |
| VERSAO_ARQUIVO | integer(4) |  |  | Versão do arquivo |
| GERAR_VARIACAO_CARTEIRA_BOLETO_BANCARIO | char(1) |  |  | Gerar variação da carteira no boleto bancário |
| VARIACAO_CARTEIRA | varchar(3) |  |  | Variação da carteira |
| TIPO_CONVENIO | char(1) |  | S | Tipo do convênio |
| PARAMETRO_MOVIMENTO | integer(4) |  | S | Parâmetro de movimento |
| GERAR_INSCRICAO_DIFERENTE_ESCRITORIO | char(1) |  |  | Gera a inscrição (CNPJ/CPF) no cadastro de conta financeira diferente do cadastro da empresa. |
| TIPO_INSCRICAO_DIFERENTE_ESCRITORIO | integer(4) |  |  | 1 - CNPJ/2 - CPF |
| INSCRICAO_DIFERENTE_ESCRITORIO | char(14) |  | S | Inscrição diferente do escritório |
| SALVAR_ENVIAR_BOLETO_SOMENTE_APOS_GRAVADO | char(1) |  |  | Salvar boleto somente após gravado |
| CONTA_INTEGRADA_DIGITAL_BANKING | char(1) |  | S | Verifica se a conta estÃ¡ integrada com o digital banking |
| CONTA_CORRENTE_DIGITAL_BANKING | char(150) |  | S | NUMERO DA CONTA CORRENTE DO DIGITAL BANKING |
| CONTA_CORRENTE_DV_DIGITAL_BANKING | char(10) |  | S | DIGITO VERIFICADOR DA CONTA CORRENTE DO DIGITAL BANKING |
| CODIGO_AGENCIA_DIGITAL_BANKING | integer(4) |  | S | NUMERO DA AGENCIA DO DIGITAL BANKING |
| AGENCIA_DV_DIGITAL_BANKING | integer(4) |  | S | DIGITO VERIFICADOR DA AGENCIA DO DIGITAL BANKING |
| CODIGO_BANCO_DIGITAL | integer(4) |  | S | Campo para guardar código do Digital Banking |
