# EFIMPORTADOR_FIXO_NF3E_SAIDA — Configuração do leiaute NF3-e XML do Importador Fixo - Saída
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| GERAR_INFORMACOES_COMPLEMENTARES | char(1) |  |  | Gerar informações complementares na nota conforme informado no(a) |
| GERAR_INFORMACOES_COMPLEMENTARES_DEFINICAO | integer(4) |  | S | Gerar informações complementares na nota conforme informado no(a) - definição |
| DETERMINAR_TIPO_TITULO_PADRAO | char(1) |  |  | Determinar tipo do título padrão para notas a prazo |
| TITULO_PADRAO | integer(4) |  | S | Título padrão para notas a prazo |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| IMPORTAR_PROD | char(1) |  |  | Importar produto e movimentação de produtos |
| PROCURA_PROD | char(1) |  |  |  |
| PROD_NOVO | char(1) |  |  | Quando o produto a ser importado não estiver cadastrado |
| PRODUTO_EM_DUPLICIDADE | char(1) |  | S | Qaundo o produto a ser importado estiver cadastrado em duplicidade |
| CODI_GRU | integer(4) |  | S | Grupo para cadastro de produtos |
| TABELA_ICMS_PROD | integer(4) |  | S | Tabela de alíquota interestadual de ICMS |
| COMPLEMENTO_CFOP_CAT_17_99 | integer(4) |  | S | Complemento padrão do ICMS-CAT 17/99 |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Exclui movimentação de produtos |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Exclui parcelas |
| CANC_EXCLUI_LANCTOS_CONTABEIS | char(1) |  |  | Excluir lançamentos contáveis |
| CFOP_ESTADUAL_EXCECAO | integer(4) |  | S | CFOP Estadual Exceção |
| VERSAO_CFOP_ESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção em operação estadual |
| CFOP_INTERESTADUAL_EXCECAO | integer(4) |  | S | CFOP Interestadual Exceção |
| VERSAO_CFOP_INTERESTADUAL_EXCECAO | smallint(2) |  | S | Versão do CFOP para exceção em operação interestadual |
| CFOP_EXCECAO | char(1) |  |  | Definir CFOPs para exceção |
