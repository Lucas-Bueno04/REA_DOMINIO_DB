# EFFORNECE_ALTERACAO — Fornecedores - Alteracoes - Cadastro
4.362 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_FOR | integer(4) | PK |  | Fornecedor |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteracao |
| CAMPO | tinyint(1) | PK |  | CAMPO ALTERADO (1=RAZAO SOCIAL/ 2=ENDERECO/ 3=COMPLEMENTO/ 4=NUMERO/ 5=BAIRRO/ 6=MUNICIPIO/ 7=PAIS/ 8=INSCRICAO ESTADUAL/ 9=INSCRICAO SUFRAMA/ 10=INSCRIÇÃO/ 11=POSSUI TRIBUTAÇÃO SOBRE A FOLHA DE PAGAMENTO/ 12=DATA NASCIMENTO) |
| DE | varchar(150) |  |  | Valor anterior a alteracao |
| PARA | varchar(150) |  |  | Valor posterior a aleracao |
