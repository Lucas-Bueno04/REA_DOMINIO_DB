# EFIMPORTADOR_FIXO_NFSE_SERVICO — Configuração do leiaute NFS-e XML do Importador Fixo - Serviço
1.190 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| GERAR_PARCELA_COM_PAGAMENTO | char(1) |  |  | Gerar parcela com pagamento para notas sem parcelas |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| INFORMAR_DATA_SAIDA | char(1) |  |  | Informar data de saída no momento da importação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas na ordem do número do documento e sem intervalo no código sequencial |
| GERAR_MOVIMENTO_PRODUTOS | char(1) |  |  | Gerar movimento de produtos |
| CODI_PDI_PADRAO | char(14) |  | S | Código produto padrão |
| DEFINIR_CFPS | char(1) |  |  | Definir CPFS |
| CFPS_MUNICIPIO | integer(4) |  | S | CPFS - Clientes do município |
| CFPS_OUTRO_MUNICIPIO | integer(4) |  | S | CPFS - Clientes de outro município |
| CFPS_OUTRO_ESTADO | integer(4) |  | S | CPFS - Clientes de outro estado |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| FORMATO_ALIQUOTA | char(1) |  |  | Formato da alíquota do imposto ISS informado no arquivo XML |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Excluir movimentação de itens |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CANC_EXCLUI_LANCTOS_CONTABEIS | char(1) |  |  | Excluir lançamentos contábeis |
| INFORMAR_CAMPO_DATA | char(1) |  |  | Informar no campo data de saída da NFS-e a data de |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definiÃ§Ãµes do imposto ISS do cadastro do acumulador |
| CODI_CLI_PADRAO | integer(4) |  | S | Cliente padrão |
| UTILIZAR_CLIENTE_PADRAO_QUANDO | integer(4) |  |  | Utilizar o cliente padrão quando |
| IMPORTAR_NOTA_ENTRADA_OUTRA_EMPRESA | char(1) |  |  | Importar nota de entrada em outra empresa |
| CODI_ACU_CANCELADA | integer(4) |  | S | CÃ³digo do acumulador especifico para notas canceladas |
| INFORMAR_ITEM_SERV_ACUMULADOR_PRODUTO | char(1) |  | S | Identificar tabela para relacionar item serviço ao acumulador e produto(I-Tabela Padrão\P-Tabela Personalizável) |
| IMPORTAR_PARCELAS | char(1) |  |  | Importar parcelas |
| NAO_IMPORTAR_VALOR_DESCONTO | char(1) |  |  | Não importar o valor dos descontos |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SERVICOS | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador saída |
| IDENTIFICAR_CLIENTE_POR | char(1) |  |  | Identificar o cliente para relacionar ao acumulador por |
| DEDUZIR_ISS_DA_BASE_PIS_COFINS | char(1) |  |  | Deduzir o valor do ISS da base de cálculo do PIS e COFINS |
| DEDUZIR_ISS_DA_BASE_PIS_COFINS_OPCOES | char(1) |  |  | Opção - Deduzir o valor do ISS da base de cálculo do PIS e COFINS |
| CONSIDERAR_INSS_RETIDO_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto INSS Retido do cadastro do acumulador |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de serviço: Gerar observação na nota conforme informado no(a) - Definição |
| CONSID_DEF_CONTRIB_RET_NA_FONTE_NO_ACU | char(1) |  |  | Considerar as definições das contribuições retidas na fonte (PIS, COFINS e CSLL) do cadastro do acumulador |
