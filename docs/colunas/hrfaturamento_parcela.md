# HRFATURAMENTO_PARCELA — Faturamento - Parcelas
43.224 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_FATURAMENTO | integer(4) | PK |  | Faturamento |
| I_PARCELA | integer(4) | PK |  | Parcela |
| VENCIMENTO | date(4) |  |  | Data de vencimento |
| VENCIMENTO_ORIGINAL | date(4) |  |  | Data de vencimento original |
| IMPRIMIU_BOLETO | char(1) |  |  | Imprimiu boleto S N |
| SEQUENCIAL_BOLETO | numeric(30) |  | S | Sequencial usado para gerar o campo nosso numero |
| NOSSO_NUMERO_BOLETO | varchar(128) |  | S | Nosso numero do boleto |
| EMISSAO_BOLETO | date(4) |  | S | Data de emisao do boleto |
| I_CONTA_FINANCEIRA_BOLETO | integer(4) |  | S | Conta financeira usada na emissao do boleto |
| MODALIDADE_BOLETO | integer(4) |  | S | Modalidade usada na emissao do boleto |
| AGENCIA_CEDENTE_BOLETO | integer(4) |  | S | Agencia cedente usada na emissao do boleto |
| POSTO_AG_CEDENTE_BOLETO | integer(4) |  | S | Posto da agencia cedente usada na emissao do boleto |
| OPERACAO_COD_CEDENTE_BOLETO | integer(4) |  | S | Operacao codigo cedente usada na emissao do boleto |
| CARTEIRA_BOLETO | integer(4) |  | S | Carteira usada na emissao do boleto |
| CONVENIO_BOLETO | varchar(7) |  | S | Convenio usado na emissao do boleto |
| ESPECIE_BOLETO | char(10) |  | S | Especie usada na emissao do boleto |
| OBSERVACAO_BOLETO | varchar(512) |  | S | Observacao do boleto |
| TIPO_BOLETO | tinyint(1) |  | S | Tipo do boleto 1 Completo 2 Detalhado 3 Pre Impresso 4 Carnê |
| MODELO_BOLETO | varchar(80) |  | S | Titulo do boleto emitido |
| GERAR_COD_BARRA_BOLETO | char(1) |  | S | Gerar codigo de barras S N |
| IMPRIMIU_COBRANCA | char(1) |  |  | Imprimiu documento de cobranca S N |
| NUMERO_COBRANCA | integer(4) |  | S | Numero do documento de cobranca |
| EMISSAO_COBRANCA | date(4) |  | S | Data de emissao do documento de cobranca |
| OBSERVACAO_COBRANCA | varchar(512) |  | S | Observacao do documento |
| MODELO_COBRANCA | varchar(80) |  | S | Titulo do documento emitido |
| VALOR | numeric(13) |  |  | Valor da parcela |
| VALOR_DESCONTO | numeric(13) |  |  | Valor de desconto |
| VALOR_DESCONTO_ADIMPLENTE | numeric(13) |  |  | Valor de desconto concedido por adimplente |
| VALOR_ORIGINAL | numeric(13) |  |  | Valor original |
| VALOR_IRRF | numeric(13) |  |  | Valor IRRF |
| VALOR_ISS | numeric(13) |  |  | Valor de ISS |
| VALOR_ISS_RETIDO | numeric(13) |  |  | Valor de ISS Retido |
| VALOR_INSS_RETIDO | numeric(13) |  |  | Valor de INSS Retido |
| VALOR_CRF | numeric(13) |  |  | Valor de CRF |
| VALOR_CRF_PIS | numeric(13) |  |  | Valor de CRF PIS |
| VALOR_CRF_COFINS | numeric(13) |  |  | Valor de CRF COFINS |
| VALOR_CRF_CSLL | numeric(13) |  |  | Valor de CRF CSLL |
| NOTA_FISCAL_BOLETO | integer(4) |  | S | Especie do titulo notas fiscais usada na emissao do boleto |
| DOCUMENTO_COBRANCA_BOLETO | integer(4) |  | S | Especie do titulo documento de cobranca usada na emissao do boleto |
| SOMENTE_BOLETO_BOLETO | integer(4) |  | S | Especie do titulo somente boleto usada na emissao do boleto |
| VALOR_PIS | numeric(13) |  |  | Valor de PIS (Usado somente para DF) |
| VALOR_COFINS | numeric(13) |  |  | Valor de COFINS (Usado somente para DF) |
| VARIACAO_CARTEIRA_BOLETO | varchar(3) |  |  | Variação da carteira |
| PARCELA | integer(4) |  | S | Parcela do Boleto(Carnê) |
| PARCELA_TOTAL | integer(4) |  | S | Total Parcela do Boleto(Carnê) |
| EMITIU_REMESSA | char(1) |  |  | Emitiu remessa |
| BOLETO_ICEBERG_ID | varchar(128) |  | S | Id do boleto Iceberg retornado pela API |
| BOLETO_ICEBERG_CODIGO_BARRAS | char(128) |  | S | Código de barras do boleto iceberg retornado pela API |
| BOLETO_ICEBERG_LINHA_DIGITAVEL | char(128) |  | S | Linha digitável do boleto iceberg retornado pela API |
| DOCUMENTO_COBRANCA_ICEBERG_ID | char(128) |  | S | Id Documento Cobranca |
| CONTA_CORRENTE_DIGITAL_BANKING | varchar(150) |  | S | Número/digito verificador da conta corrente do digital banking |
| CODIGO_AGENCIA_DIGITAL_BANKING | integer(4) |  | S | Número/digito verificador da agencia do digital banking |
| ATUALIZOU_NOSSO_NUMERO | char(1) |  | S | Atualizou o nosso numero (S/N) |
| CODIGO_BANCO_DIGITAL_BANKING | integer(4) |  | S | Código do banco Dominio Conta PJ vinculado ao boleto |
| VALOR_IBS | numeric(13) |  | S | Valor IBS calculado |
| BASE_CALCULO_IBS | numeric(13) |  | S | Base de cálculo IBS |
| VALOR_CBS | numeric(13) |  | S | Valor CBS calculado |
| BASE_CALCULO_CBS | numeric(13) |  | S | Base de cálculo CBS |
| TIPO_RETENCAO_PIS_COFINS_CSLL | integer(4) |  |  | Tipo de retenção de pis/cofins/csll para tag xml tpRetPisCofins |
