# CTPARMTO_FILIAL_API_CONTA_AZUL — Seleção de empresas filiais para o envio api conta azul
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Prima key com autoincrement |
| HABILITAR | char(1) |  |  | Verifica se a empresa é habilitada |
| CODIGO_EMPRESA_FILIAL | integer(4) |  |  | Verifica se a empresa é habilitada |
| CODI_EMP | integer(4) | PK |  | Empresa principal de parametro |
| GUID_CONTABIL | uniqueidentifier(16) |  | S | Identificador único do contábil |
