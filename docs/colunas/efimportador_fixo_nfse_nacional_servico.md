# EFIMPORTADOR_FIXO_NFSE_NACIONAL_SERVICO — Configuração do leiaute NFS-e XML Nacional do Importador Fixo - Serviço
191 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| GERAR_PARCELA_COM_PAGAMENTO | char(1) |  |  | Gerar parcela com pagamento para notas sem parcelas |
| GERAR_OBSERVACAO_ACUMULADOR | char(1) |  |  | Gerar observação informada no cadastro do acumulador |
| INFORMAR_DATA_SAIDA | char(1) |  |  | Informar data de saída no momento da importação |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  | Gerar lançamentos contábeis |
| REORDENAR_CODIGO_NOTAS | char(1) |  |  | Gravar as notas importadas na ordem do número do documento e sem intervalo no código sequencial |
| CONSIDERAR_ISS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| IMPORTAR_NOTA_ENTRADA_OUTRA_EMPRESA | char(1) |  |  | Importar nota de entrada em outra empresa |
| INFORMAR_CAMPO_DATA | char(1) |  |  | Informar no campo data de saída da NFS-e a data de |
| CODI_CLI_PADRAO | integer(4) |  | S | Cliente padrão |
| UTILIZAR_CLIENTE_PADRAO_QUANDO | integer(4) |  |  | Utilizar o cliente padrão |
| CFPS_MUNICIPIO | integer(4) |  | S | CPFS - Clientes de outro município |
| CFPS_OUTRO_MUNICIPIO | integer(4) |  | S | CPFS - Clientes de outro município |
| CFPS_OUTRO_ESTADO | integer(4) |  | S | CPFS - Clientes de outro estado |
| DEFINIR_CFPS | char(1) |  |  | Definir CPFS |
| ACUMULADOR_EXCECAO | char(1) |  |  | Definir acumulador para exceção |
| CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção |
| CANC_EXCLUI_MOV_PRODUTOS | char(1) |  |  | Excluir movimentação de produtos |
| CANC_EXCLUI_PARCELAS | char(1) |  |  | Excluir parcelas |
| CODI_ACU_CANCELADA | integer(4) |  | S | Acumulador para notas canceladas |
| CODI_PDI_PADRAO | char(14) |  | S | Código produto padrão |
| GERAR_MOVIMENTO_PRODUTOS | char(1) |  |  | Gerar movimento de produtos |
| CONSIDERAR_TODOS_COMO_EXCECAO_ACU_SERVICOS | char(1) |  | S | Considerar como exceção a opção "Todos" das colunas para relacionamento do acumulador saída |
| IDENTIFICAR_CLIENTE_POR | char(1) |  |  | Identificar o cliente para relacionar ao acumulador por |
| DEDUZIR_ISS_DA_BASE_PIS_COFINS | char(1) |  |  | Deduzir o valor do ISS da base de cálculo do PIS e COFINS |
| DEDUZIR_ISS_DA_BASE_PIS_COFINS_OPCOES | char(1) |  |  | Opção - Deduzir o valor do ISS da base de cálculo do PIS e COFINS |
| GERAR_OBSERVACAO_DEFINICAO | integer(4) |  | S | Notas de serviço: Gerar observação na nota conforme informado no(a) - Definição |
| CONSID_DEF_CONTRIB_RET_NA_FONTE_NO_ACU | char(1) |  |  | Considerar as definições das contribuições retidas na fonte (PIS, COFINS e CSLL) do cadastro do acumulador |
| CONSIDERAR_INSS_RETIDO_ACUMULADOR | char(1) |  |  | Considerar definições do acumulador para cálculo de INSS retido (NFS-e Nacional - serviços) |
| NAO_IMPORTAR_DESCONTO_SER | char(1) |  | S | Não importar o valor dos descontos para serviços prestados |
