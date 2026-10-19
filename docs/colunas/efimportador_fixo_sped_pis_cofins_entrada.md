# EFIMPORTADOR_FIXO_SPED_PIS_COFINS_ENTRADA — Configuração do leiaute SPED PIS/COFINS do Importador Fixo - Entrada
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| C100_IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | C100 - Ignorar impostos não definidos no acumulador |
| C100_CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | C100 - Considerar as definições do imposto ICMS do cadastro do acumulador |
| C100_ACUMULADOR_EXCECAO | char(1) |  |  | C100 - Definir acumulador para exceção |
| C100_CODI_ACU_EXCECAO | integer(4) |  | S | C100 - Código do acumulador para exceção |
| A100_IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  |  | A100 - Ignorar impostos não definidos no acumulador |
| A100_CFOP_ESTADUAL | integer(4) |  |  | A100 - CFOP estadual |
| A100_CFOP_VERSAO_ESTADUAL | smallint(2) |  |  | A100 - Versão do CFOP estadual |
| A100_CFOP_INTERESTADUAL | integer(4) |  |  | A100 - CFOP interestadual |
| A100_CFOP_VERSAO_INTERESTADUAL | smallint(2) |  |  | A100 - Versão do CFOP interestadual |
| A100_CFOP_EXTERIOR | integer(4) |  |  | A100 - CFOP exterior |
| A100_CFOP_VERSAO_EXTERIOR | smallint(2) |  |  | A100 - Versão do CFOP exterior |
| A100_CODI_ACU_A_VISTA | integer(4) |  |  | A100 - Código do acumulador para pagamento à vista |
| A100_CODI_ACU_A_PRAZO | integer(4) |  |  | A100 - Código do acumulador para pagamento à prazo |
| A100_CODI_ACU_OUTROS | integer(4) |  |  | A100 - Código do acumulador para outros tipos de pagamento |
| A100_CODI_ESP | integer(4) |  |  | A100 - Código da espécie do serviço |
| C100_CFOP_CANCELADA | integer(4) |  | S | C100 - CFOP das notas canceladas |
| C100_VERSAO_CFOP_CANCELADA | smallint(2) |  | S | C100 - Versão do CFOP das notas canceladas |
| C100_CODI_ACU_CANCELADA | integer(4) |  | S | C100 - Código do acumulador para nota cancelada |
| C100_CODI_FOR_CANCELADA | integer(4) |  | S | C100 - Fornecedor das notas canceladas |
| C100_DATA_CANCELADA | char(1) |  |  | C100 - Data das notas canceladas |
| C100_DATA_DOCUMENTO_EXTEMPORANEO | char(1) |  |  | Data de escrituração dos documentos extemporâneos |
| C100_DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| C100_DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| C100_NAO_CONSIDERA_DEFINICAO_VALORES | char(1) |  |  | Não considerar as definições para os valores de IPI e SUBTRI da linha do ICMS |
| C100_GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| A100_GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| C100_CONSIDERAR_IPI_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto IPI do cadastro do acumulador |
| C100_UTILIZAR_CHAVE_PARA_IDENTIFICAR_NOTAS | char(1) |  | S | C100 - Utilizar somente a chave da NF-e, NFC-e e CT-e para identificar as notas já lançadas |
| F100_IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  | S | F100: Ignorar impostos não definidos no acumulador |
| F100_GERAR_LANCAMENTOS_CONTABEIS | char(1) |  | S | F100: Gerar lançamentos contábeis |
| F100_GERAR_MOVIMENTO_PRODUTO | char(1) |  | S | F100: Gerar movimento de produto para documento sem item |
| F100_CODI_PDI_PADRAO | char(14) |  | S | F100: Produto padrão |
| F100_DADOS_DOCUMENTO_SERIE | char(7) |  | S | F100: Dados do documento - Série |
| F100_DADOS_DOCUMENTO_ACUMULADOR | integer(4) |  | S | F100: Dados do documento - Acumulador |
| F100_CFOP_ESTADUAL | integer(4) |  | S | F100: CFOPs - CFOP estadual |
| F100_VERSAO_CFOP_ESTADUAL | smallint(2) |  | S | F100: CFOPs - Versão do CFOP estadual |
| F100_CFOP_INTERESTADUAL | integer(4) |  | S | F100: CFOPs - CFOP interestadual |
| F100_VERSAO_CFOP_INTERESTADUAL | smallint(2) |  | S | F100: CFOPs - Versão do CFOP interestadual |
| F100_CFOP_EXTERIOR | integer(4) |  | S | F100: CFOPs - CFOP exterior |
| F100_VERSAO_CFOP_EXTERIOR | smallint(2) |  | S | F100: CFOPs - Versão do CFOP exterior |
| F100_CODI_ESP | integer(4) |  | S | F100: Código da espécie do serviço |
| C100_NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de IPI e lança-los em: |
| C100_DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| C100_NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de SUBTRI e lança-los em: |
| C100_DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | IPI - Lançar SUBTRI em |
