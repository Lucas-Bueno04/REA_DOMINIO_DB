# EFOUTROSDADOS_EFD_REINF_SERVICOS_TOMADOS — EFD-Reinf - Outros Dados - Serviçoes Tomados
79 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| CODI_EMP_TOMADOR | integer(4) | PK |  | Empresa Tomador |
| TIPO_INSCRICAO_TOMADOR | integer(4) | PK |  | Tipo inscrição tomador |
| INSCRICAO_TOMADOR | varchar(14) | PK |  | Inscrição tomador |
| CODIGO_RECOLHIMENTO_VALOR_APURADO | varchar(6) | PK |  | Código de recolhimento |
| TIPO_INSCRICAO_VALOR_APURADO | integer(4) | PK |  | Tipo inscrição valor apurado |
| INSCRICAO_VALOR_APURADO | varchar(14) | PK |  | Inscrição valor apurado |
| VALOR_DEBITO | numeric(13) |  |  | Valor débito |
| NUMERO_CNO | varchar(14) |  |  | Número CNO |
| NUMERO_DOCUMENTO | numeric(15) | PK |  | Número do documento |
| INDICATIVO_PRESTACAO_SERVICOS | integer(4) | PK |  | Indicativo de Prestação de Serviços |
