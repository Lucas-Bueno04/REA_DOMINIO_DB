# EFDAS_API_ENVIO_ARQUIVOS — DAS Api - Envio dos Arquivos
13.225 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| COMPETENCIA | date(4) |  |  | Competência |
| TIPO_ENVIO | integer(4) |  |  | Tipo de envio |
| SITUACAO | integer(4) |  |  | Situação processo |
| NOME_ARQUIVO | varchar(100) |  | S | Nome do arquivo |
| TIPO_DECLARACAO | integer(4) |  |  | Tipo de declaração |
| DATA_ENVIO | date(4) |  |  | Data de envio |
| HORARIO_ENVIO | time(8) |  |  | Hora de envio |
| NUMERO_DAS | char(20) |  | S | Numero da guia DAS |
| VALOR_DIFERENTE_SISTEMA | char(1) |  | S | Valor diferente do enviado pelo sistema |
