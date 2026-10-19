# EFIMPORTADOR_FIXO_NFE_ENTRADA_ACUMULADOR — Configuração do leiaute NF-e XML do Importador Fixo - Entrada - Acumulador
119.292 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| OPERACAO | char(1) |  | S | Operação abrangente |
| SELECAO_CST | char(1) |  |  | Seleção do CST |
| SELECAO_FORNECEDOR | char(1) |  |  | Seleção do fornecedor |
| SELECAO_PRODUTO | char(1) |  |  | Seleção do produto |
| SELECAO_NCM | char(1) |  |  | Seleção do NCM |
| VERSAO_LEIAUTE | integer(4) |  |  | Versão do leiaute: 31 para leiaute até 3.1 e 40 para leiaute 4.0. |
| SELECAO_FORMA_PAGAMENTO | char(1) |  |  | Seleção da porma de pagamento |
| SELECAO_GRUPO | char(1) |  |  | Seleção do grupo |
| SELECAO_ORIGEM | char(1) |  |  | Origem do acumulador (T = Todos, S = Selecionados) |
| SELECAO_TIPO_INSCRICAO_FORNECEDOR | char(1) |  |  | Seleção do tipo de inscrição do fornecedor |
| REGIME_APURACAO_FORNECEDOR | char(1) |  |  | Regime de Apuração (T - Todos, N - Normal, M - Microempresa, E - EPP, O - Outros, S - ME Simples Nacional, P - EPP Simples Nacional, I - Imune do IRPJ, R - Isenta do IRPJ) |
