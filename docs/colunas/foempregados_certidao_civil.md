# FOEMPREGADOS_CERTIDAO_CIVIL — Cadastro de certidão civil do empregado
140 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| TIPO | smallint(2) | PK |  | Tipo da certidão. (1=Certidão de nascimento/2=Certidão de casamento/3=Certidão nascimento indígena4=Certidão de óbito/5=Certidão de emancipação) |
| DATA_EMISSAO | date(4) | PK |  | Data de emissão da certidão. |
| TERMO_MATRICULA | varchar(60) |  | S | Termo/Matrícula da certidão. |
| LIVRO | varchar(10) |  | S | Livro de registro da certidão. |
| FOLHA | varchar(20) |  | S | Folha de registro da certidão. |
| CARTORIO | varchar(40) |  | S | Cartório de registro da certidão. |
| CODIGO_MUNICIPIO | integer(4) |  |  | Código do município do cartório. |
| EMITIR_DOCUMENTOS | smallint(2) |  |  | Emitir documentos. (0=Não/1=Sim) |
| ORIGEM_REG | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
