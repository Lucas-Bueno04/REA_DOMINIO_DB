# EFIMPORTADOR_FIXO_NFSE_ENTRADA — Configuração do leiaute NFS-e XML do Importador Fixo - Entrada
84 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ISS do cadastro do acumulador |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar a data de entrada no momento da importação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| GERAR_MOVIMENTO_PRODUTOS | char(1) |  |  | Gerar movimento de produtos |
| CODI_PDI_PADRAO | char(14) |  | S | Produto padrão |
| ACUMULADOR_EXCECAO | char(1) |  |  | Acumulador exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador exceção |
| CFOP_ESTADO | integer(4) |  | S | CFOP - Fornecedor do estado |
| CFOP_OUTRO_ESTADO | integer(4) |  | S | CFOP - Fornecedor fora do estado |
| INFORMAR_ITEM_SERV_ACUMULADOR_PRODUTO | char(1) |  | S | Identificar tabela para relacionar item serviço ao acumulador e produto(I-Tabela Padrão\P-Tabela Personalizável) |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| INFORMAR_CAMPO_DATA | char(1) |  |  | Informar no campo data de entrada da NFS-e a data de |
| NAO_IMPORTAR_VALOR_DESCONTO | char(1) |  |  | Não importar o valor dos descontos |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador entrada |
| IDENTIFICAR_FORNECEDOR_POR | char(1) |  |  | Identificar o fornecedor para relacionar ao acumulador por |
| CONSIDERAR_INSS_RETIDO_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto INSS Retido do cadastro do acumulador |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de entrada: Gerar observação na nota conforme informado no(a) - Definição |
| CONSID_DEF_CONTRIB_RET_NA_FONTE_NO_ACU | char(1) |  |  | Considerar as definições das contribuições retidas na fonte (PIS, COFINS e CSLL) do cadastro do acumulador |
