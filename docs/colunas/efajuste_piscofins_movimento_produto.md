# EFAJUSTE_PISCOFINS_MOVIMENTO_PRODUTO — Ajuste no calculo do PIS/COFINS por movimento de produtos
24 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_AJUSTE | integer(4) | PK |  | Codigo |
| DATA_AJUSTE | date(4) |  |  | Data |
| DATA_REFERENCIA | date(4) |  |  | Data de referencia |
| CODI_IMP | integer(4) |  |  | Imposto |
| OPERACAO | tinyint(1) |  |  | OPERACAO (1=AJUSTE DE CREDITO/ 2=AJUSTE DE DEBITO/ 3=OUTRAS DEDUCOES/ 4=AJUSTE DE DÉBITO - SALDO DIFERIDO ANTERIOR) |
| TIPO_AJUSTE | char(1) |  |  | Tipo de ajuste (A=Acrescimo/ R=Reducao) |
| ORIGEM_CREDITO | char(1) |  |  | Origem do credito (M=Mercado Interno/ I=Importacao) |
| TIPO_CREDITO | integer(4) |  | S | Tipo de credito |
| TIPO_CONTRIBUICAO | integer(4) |  | S | Tipo de contribuicao |
| ORIGEM_AJUSTE | tinyint(1) |  |  | Origem do ajuste |
| ORIGEM_DEDUCAO | tinyint(1) |  | S | Origem da deducao (1=Credito presumido-Medicamentos/ 2=Creditos admitidos no regime cumulativo-Bebidas frias/ 3=Contribuicao para pelo substituto tributario-ZFM/ 4=Substituicao tributaria-Nao ocorrencia do fato gerador presumido/ 99=Outras Deducoes) |
| NUMERO_DOCUMENTO | varchar(255) |  |  | Numero do documento |
| BASE_CALCULO | numeric(13) |  |  | Base de calculo |
| ALIQUOTA | numeric(13) |  |  | Aliquota |
| VALOR | numeric(13) |  |  | Valor |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| DESCRICAO_AJUSTE | varchar(250) |  |  | Descrição do ajuste |
| I_RECOLHIMENTO | integer(4) |  | S | Código Sequencial do Recolhimento |
| CODIGO_RECOLHIMENTO | char(6) |  |  | Código do Recolhimento |
| DETALHAR_AJUSTE_PIS_COFINS | char(1) |  |  | Detalhar ajustes do PIS e COFINS (S/N) |
| POSSUI_PROCESSO_REFERENCIADO | char(1) |  |  | Possui processo referenciado (S/N) |
| IDENTIFICACAO | char(20) |  | S | Identificação |
| SECAO_JUDICIARIA | varchar(255) |  | S | Seção judiciária |
| VARA | char(2) |  | S | Vara |
| NATUREZA_ACAO | integer(4) |  | S | Natureza da ação |
| DATA_SENTENCA_DESPACHO | date(4) |  | S | Data da sentença ou despacho |
| DESCRICAO_PROCESSO | varchar(100) |  | S | Descrição do processo |
| AJUSTE_NO | char(1) |  |  | Ajuste no(a) |
