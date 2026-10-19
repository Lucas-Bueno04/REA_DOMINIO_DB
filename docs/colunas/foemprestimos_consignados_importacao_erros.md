# FOEMPRESTIMOS_CONSIGNADOS_IMPORTACAO_ERROS — Empréstimos consignados realizados pela importação de arquivos com erros
3.574 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo da empresa que foi realizada a importação |
| COMPETENCIA | date(4) | PK |  | Competência de desconto |
| SEQUENCIAL | uniqueidentifier(16) | PK |  | Código sequencial da tabela |
| CPF_COLABORADOR | varchar(11) |  | S | CPF do colaborador |
| MATRICULA | varchar(30) |  | S | Matrícula |
| CATEGORIA_ESOCIAL | integer(4) |  | S | Tipo da folha |
| CODI_EMP_IMPORTADA | integer(4) |  | S | Código da empresa importada |
| INSCRICAO_EMPRESA_IMPORTADA | varchar(14) |  | S | Inscrição da empresa importada |
| TIPO_INSCRICAO_EMPRESA_IMPORTADA | integer(4) |  | S | Tipo inscrição da empresa importada (1-CNPJ/2-CPF/3-CEI) |
| MENSAGEM | varchar(500) |  | S | Mensagem do erro |
| I_USUARIO | integer(4) |  | S | Usuário que realizou o processo de importação |
| DATA_IMPORTACAO | timestamp(8) |  | S | data que o arquivo foi importado |
| NOME_ARQUIVO | varchar(255) |  | S | Arquivo que foi processado as informações |
