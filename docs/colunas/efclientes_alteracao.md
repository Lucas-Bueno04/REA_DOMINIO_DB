# EFCLIENTES_ALTERACAO — Clientes - Alteracoes - Cadastro
9.264 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_CLI | integer(4) | PK |  | Cliente |
| DATA_ALTERACAO | date(4) | PK |  | Data da alteracao |
| CAMPO | tinyint(1) | PK |  | CAMPO ALTERADO (1=RAZAO SOCIAL/ 2=ENDERECO/ 3=COMPLEMENTO/ 4=NUMERO/ 5=BAIRRO/ 6=MUNICIPIO/ 7=PAIS/ 8=INSCRICAO ESTADUAL/ 9=INSCRICAO SUFRAMA/ 10=INCRIÇÃO/ 11=PERCENTUAL CARGA MÉDIA/12=ALÍQUOTA ICMS) |
| DE | varchar(150) |  |  | Valor anterior a alteracao |
| PARA | varchar(150) |  |  | Valor posterior a aleracao |
