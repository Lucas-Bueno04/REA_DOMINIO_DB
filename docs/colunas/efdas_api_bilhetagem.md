# EFDAS_API_BILHETAGEM — DAS Api - Envio dos Arquivos - Bilhetagem de custos
13.225 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| CODI_CON | integer(4) | PK |  | Código do contador |
| SEQUENCIAL_BILHETAGEM | integer(4) | PK |  |  |
| DATA_HORA_REQUISICAO | timestamp(8) |  |  | Data/Hora da requisição |
| TIPO_ENVIO | integer(4) |  |  | Tipo de serviço realizado |
| GEROU_CUSTO | char(1) |  |  | Operação gerou custo |
