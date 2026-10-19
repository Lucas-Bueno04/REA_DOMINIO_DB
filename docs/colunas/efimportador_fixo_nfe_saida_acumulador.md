# EFIMPORTADOR_FIXO_NFE_SAIDA_ACUMULADOR — Configuração do leiaute NF-e XML do Importador Fixo - Saída - Acumulador
148.407 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| OPERACAO | char(1) |  | S | Operação abrangente |
| SELECAO_CST | char(1) |  |  | Seleção do CST do ICMS |
| SELECAO_CST_PIS | char(1) |  |  | Seleção do CST do PIS |
| SELECAO_PRODUTO | char(1) |  |  | Seleção do produto |
| SELECAO_NCM | char(1) |  |  | Seleção do NCM |
| SELECAO_CLIENTE | char(1) |  |  | Seleção do cliente |
| VERSAO_LEIAUTE | integer(4) |  |  | Versão do leiaute: 31 para leiaute até 3.1 e 40 para leiaute 4.0. |
| SELECAO_FORMA_PAGAMENTO | char(1) |  |  | Seleção da porma de pagamento |
| SELECAO_ORIGEM | char(1) |  |  | Origem do acumulador (T = Todos, S = Selecionados) |
| SELECAO_GRUPO | char(1) |  |  | Seleção do grupo |
| SELECAO_TIPO_INSCRICAO_CLIENTE | char(1) |  |  | Seleção do tipo de inscrição do cliente |
