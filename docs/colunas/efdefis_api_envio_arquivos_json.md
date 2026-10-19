# EFDEFIS_API_ENVIO_ARQUIVOS_JSON — DEFIS Api - Envio dos Arquivos - JSON
680 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| TIPO_ARQUIVO | char(1) | PK |  | Tipo do arquivo |
| ARQUIVO_JSON | long binary(32767) |  | S | Arquivo JSON |
