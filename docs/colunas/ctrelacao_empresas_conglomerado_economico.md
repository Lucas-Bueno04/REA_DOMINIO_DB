# CTRELACAO_EMPRESAS_CONGLOMERADO_ECONOMICO — Empresas do Conglomerado Econômico
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EMPRESA_CONGLOMERADO_ECONOMICO | integer(4) | PK |  | Sequencial conglomerado economico |
| IDENTIFICADOR_ECD | integer(4) |  |  | Identificador ECD |
| CNPJ | varchar(14) |  | S | CNPJ Empresa |
| NOME_EMPRESARIAL | varchar(255) |  |  | Nome empresarial conglomerado economico |
| CODIGO_MUNICIPIO | integer(4) |  | S | Municipio |
| UF | char(2) |  | S | UF |
| CODIGO_PAIS | integer(4) |  |  | Pais |
| CODI_EMP_CONSOLIDADA | integer(4) |  | S | Código de empresa consolidada |
