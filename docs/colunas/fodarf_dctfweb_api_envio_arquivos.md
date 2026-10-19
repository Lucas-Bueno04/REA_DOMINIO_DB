# FODARF_DCTFWEB_API_ENVIO_ARQUIVOS — DARF DCTFWeb Api - Envio dos Arquivos
38.378 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| COMPETENCIA | date(4) |  |  | Competência |
| TIPO_ENVIO | integer(4) |  |  | Tipo de envio (1=Transmissão Mensal/2=Gerar DCTFWeb/3=Relatório DCTFWeb/4=Consulta XML declaração/5=Gerar DCTFWeb Parcial) |
| SITUACAO | integer(4) |  |  | Situação processo (0=Processando/1=Sucesso/2=Insucesso/3=Falha/4=Não autenticado) |
| TIPO_PROCESSO | integer(4) |  |  | Tipo do processo (1=Mensal/2=13º Salário/3=Reclamatória trabalhista) |
| NOME_ARQUIVO | varchar(100) |  | S | Nome do arquivo |
| DATA_ENVIO | date(4) |  |  | Data de envio |
| HORARIO_ENVIO | time(8) |  |  | Hora de envio |
| NUMERO_PROCESSO | char(20) |  | S | Número do processo |
| XMLASSINADOBASE64 | long varchar(32767) |  | S | Informações do arquivo XML de retorno assinado. |
| ORIGEM_IMPOSTO | char(20) |  |  | Envio de Guia Parcial - Origem dos impostos |
