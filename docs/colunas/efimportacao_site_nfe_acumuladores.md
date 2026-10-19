# EFIMPORTACAO_SITE_NFE_ACUMULADORES — Configuração da importação da NFe - Tabela de acumuladores
271.192 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| TIPO_NOTA | char(1) | PK |  | Tipo da nota |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| OPERACAO | char(1) |  |  | Operação abrangente |
| SELECAO_CST | char(1) |  |  | Seleção do CST |
| SELECAO_FORNECEDOR | char(1) |  |  | Seleção do fornecedor |
| SELECAO_PRODUTO | char(1) |  |  | Seleção do produto |
| SELECAO_NCM | char(1) |  |  | Seleção do NCM |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
| VERSAO_LEIAUTE | integer(4) |  |  | Versão do leiaute: 31 para leiaute até 3.1 e 40 para leiaute 4.0. |
| SELECAO_FORMA_PAGAMENTO | char(1) |  |  | Seleção da Forma de Pagamento |
| SELECAO_ORIGEM | char(1) |  |  | Origem do acumulador (T = Todos, S = Selecionados) |
| SELECAO_GRUPO | char(1) |  |  | Seleção do grupo |
