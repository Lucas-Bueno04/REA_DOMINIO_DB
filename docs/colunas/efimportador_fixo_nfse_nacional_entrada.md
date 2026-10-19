# EFIMPORTADOR_FIXO_NFSE_NACIONAL_ENTRADA — Configuração do leiaute NFS-e XML Nacional do Importador Fixo - Entrada
191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar o percentual de base de cálculo e alíquota do ISS do cadastro do acumulador |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| INFORMAR_DATA_ENTRADA | char(1) |  |  | Informar a data de entrada no momento da importação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| CODI_PDI_PADRAO | char(14) |  | S | Produto padrão |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador exceção |
| CFOP_ESTADO | integer(4) |  | S | CFOP - Fornecedor do estado |
| CFOP_OUTRO_ESTADO | integer(4) |  | S | CFOP - Fornecedor fora do estado |
| INFORMAR_CAMPO_DATA | char(1) |  |  | informar no campo data de entrada da NFS-e data de |
| GERAR_MOVIMENTO_PRODUTOS | char(1) |  |  | Gerar movimento de produtos |
| ACUMULADOR_EXCECAO | char(1) |  |  | Acumulador exceção |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_ENT | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador entrada |
| IDENTIFICAR_FORNECEDOR_POR | char(1) |  |  | Identificar o fornecedor para relacionar ao acumulador por |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de entrada: Gerar observação na nota conforme informado no(a) - Definição |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Excluir movimentação de produtos |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CODI_ACU_CANCELADA | integer(4) |  | S | Acumulador para notas canceladas |
| CONSID_DEF_CONTRIB_RET_NA_FONTE_NO_ACU | char(1) |  |  | Considerar as definições das contribuições retidas na fonte (PIS, COFINS e CSLL) do cadastro do acumulador |
| CONSIDERAR_INSS_RETIDO_ACUMULADOR | char(1) |  |  | Considerar definições do acumulador para cálculo de INSS retido (NFS-e Nacional - entradas) |
| NAO_IMPORTAR_DESCONTO_ENT | char(1) |  | S | Não importar o valor dos descontos para serviços tomados |
