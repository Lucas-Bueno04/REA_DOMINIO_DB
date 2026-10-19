# EFFORNECE_DEPENDENTES — Fornecedores - Cadastro - Dependentes
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_FOR | integer(4) | PK |  | Código do fornecedor |
| I_DEPENDENTE | integer(4) | PK |  | Sequencial |
| NOME | char(60) |  |  | Nome |
| DATA_NASCIMENTO | date(4) |  |  | Data de nascimento |
| DEPENDENTE_ATE | integer(4) |  |  | Dependente até |
| CPF_DEPENDENTE | varchar(14) |  | S | CPF do dependente |
| RELACAO_DEPENDENCIA | integer(4) |  | S | Relação de dependencia |
| DESCRICAO_DEPENDENCIA | varchar(50) |  | S | Descrição da dependencia |
