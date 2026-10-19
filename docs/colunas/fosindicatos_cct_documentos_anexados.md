# FOSINDICATOS_CCT_DOCUMENTOS_ANEXADOS — Documentos anexados na coleção coletiva.
33 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato. |
| DATA_REGISTRO | date(4) | PK |  | Data de registro da convenção coletiva. |
| SEQUENCIAL | smallint(2) | PK |  | Número sequencial do cadastro do arquivo. |
| NOME_ARQUIVO | varchar(128) |  |  | Nome do arquivo. |
| VIGENCIA_INICIAL | date(4) |  | S | Vigência inicial. |
| VIGENCIA_FINAL | date(4) |  | S | Vigência final. |
| DOCUMENTO | long binary(32767) |  | S | Documento anexado. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabela/2=Importação de layout) |
