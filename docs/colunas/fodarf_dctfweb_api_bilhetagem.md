# FODARF_DCTFWEB_API_BILHETAGEM — DARF DCTFWeb Api - Envio dos Arquivos - Bilhetagem de custos
38.378 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| CODI_CON | integer(4) | PK |  | Código do contador |
| SEQUENCIAL_BILHETAGEM | integer(4) | PK |  | Código sequencial |
| DATA_HORA_REQUISICAO | timestamp(8) |  |  | Data/Hora da requisição |
| TIPO_ENVIO | integer(4) |  |  | Tipo de serviço realizado (1=Transmissão Mensal/2=Gerar DCTFWeb/3=Relatório DCTFWeb/4=Consulta XML declaração/5=Gerar DCTFWeb Parcial) |
| GEROU_CUSTO | char(1) |  |  | Operação gerou custo (S=Sim/N=Não) |
