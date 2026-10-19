# EFIMPORTACAO_SITE_NFE_ACUMULADORES_NCM — Configuração da importação da NFe - Tabela de acumuladores e seus NCMs
18 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| TIPO_NOTA | char(1) | PK |  | Tipo da nota |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| OPERACAO | char(1) |  |  | Operação abrangente |
| I_NCM | integer(4) | PK |  | Sequencial do NCM |
| NCM | char(8) |  |  | NCM |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
