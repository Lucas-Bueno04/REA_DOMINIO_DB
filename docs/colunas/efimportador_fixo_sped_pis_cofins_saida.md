# EFIMPORTADOR_FIXO_SPED_PIS_COFINS_SAIDA — Configuração do leiaute SPED PIS/COFINS do Importador Fixo - Saída
19 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ICMS do cadastro do acumulador |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CFOP_CANCELADA | integer(4) |  | S | CFOP das notas canceladas |
| VERSAO_CFOP_CANCELADA | smallint(2) |  | S | Versão do CFOP das notas canceladas |
| CODI_ACU_CANCELADA | integer(4) |  | S | Código do acumulador para nota cancelada |
| CODI_CLI_CANCELADA | integer(4) |  | S | Cliente das notas canceladas |
| DATA_CANCELADA | char(1) |  |  | Data das notas canceladas |
| DIFERENCA_BC_ICMS_EXCECAO | char(1) |  |  | Diferença base de cálculo para exceção |
| DEFINICAO_BC_ICMS_EXCECAO | char(1) |  | S | Definição da diferença base de cálculo para exceção |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas em ordem de número e sem intervalo no código sequencial |
| UTILIZAR_CHAVE_PARA_IDENTIFICAR_NOTAS | char(1) |  | S | Utilizar somente a chave da NF-e, NFC-e e CT-e para identificar as notas já lançadas |
| F100_IGNORAR_IMPOSTOS_NAO_DEF_ACU | char(1) |  | S | F100: Ignorar impostos não definidos no acumulador |
| F100_GERAR_LANCAMENTOS_CONTABEIS | char(1) |  | S | F100: Gerar lançamentos contábeis |
| F100_GERAR_MOVIMENTO_PRODUTO | char(1) |  | S | F100: Gerar movimento de produto para documento sem item |
| F100_CODI_PDI_PADRAO | char(14) |  | S | F100: Produto padrão |
| F100_DADOS_DOCUMENTO_SERIE | char(7) |  | S | F100: Dados do documento - Série |
| F100_DADOS_DOCUMENTO_CLIENTE_PADRAO | integer(4) |  | S | F100: Dados do documento - Cliente padrão |
| F100_CFOP_ESTADUAL | integer(4) |  | S | F100: CFOPs - CFOP estadual |
| F100_VERSAO_CFOP_ESTADUAL | smallint(2) |  | S | F100: CFOPs - Versão do CFOP estadual |
| F100_CFOP_INTERESTADUAL | integer(4) |  | S | F100: CFOPs - CFOP interestadual |
| F100_VERSAO_CFOP_INTERESTADUAL | smallint(2) |  | S | F100: CFOPs - Versão do CFOP interestadual |
| F100_CFOP_EXTERIOR | integer(4) |  | S | F100: CFOPs - CFOP exterior |
| F100_VERSAO_CFOP_EXTERIOR | smallint(2) |  | S | F100: CFOPs - Versão do CFOP exterior |
| F100_CODI_ESP | integer(4) |  | S | F100: Código da espécie do serviço |
| F100_CODI_ACU_TRIBUTADA | integer(4) |  | S | F100: Código acumulador operação tributada |
| F100_CODI_ACU_NAO_TRIBUTADA | integer(4) |  | S | F100: Código acumulador operação não tributada |
| CODI_CLI_C175 | integer(4) |  |  | Cliente padrão das notas modelo 65 |
| UTILIZAR_CLIENTE_PADRAO_C175_QUANDO | integer(4) |  |  | Utilizar cliente padrão das notas modelo 65 quando |
| NAO_CONSIDERAR_DIFERENCA_BC_IPI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de IPI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_IPI_EXCECAO | char(1) |  | S | Lançar IPI em |
| NAO_CONSIDERAR_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  |  | Não considerar as definições para os valores de SUBTRI e lança-los em: |
| DEFINICAO_DIFERENCA_BC_SUBTRI_EXCECAO | char(1) |  | S | IPI - Lançar SUBTRI em |
