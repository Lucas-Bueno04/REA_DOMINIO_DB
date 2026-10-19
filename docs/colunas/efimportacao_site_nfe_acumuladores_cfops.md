# EFIMPORTACAO_SITE_NFE_ACUMULADORES_CFOPS — Configuração da importação da NFe - Tabela de acumuladores e seus CFOPs
504.015 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| TIPO_NOTA | char(1) | PK |  | Tipo da nota |
| CODI_ACU | integer(4) |  |  | Código do acumulador |
| OPERACAO | char(1) |  |  | Operação abrangente |
| CFOP | integer(4) | PK |  | CFOP |
| VERSAO_CFOP | smallint(2) | PK |  | Versão CFOP |
| I_ACUMULADOR | integer(4) | PK |  | Sequencial do acumulador |
