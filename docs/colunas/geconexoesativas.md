# geconexoesativas — Conexoes concorrentes e ativas
43 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_conexoesativas | integer(4) | PK |  |  |
| i_conexao_id | integer(4) |  |  | Identificador da conexao |
| i_produto | integer(4) |  |  | Codigo do produto dominio |
| mac_address | varchar(512) |  |  | Endereco MAC da placa de rede |
| session_id | integer(4) |  |  | Id da sessao do usuario(WTS) |
| usuario | char(64) |  |  | Nome do usuario do banco conectado |
| inicio_conexao | timestamp(8) |  |  | inicio_conexao |
| ip | varchar(48) |  |  | Numero do IP da estação conectada ao banco |
| sistema | tinyint(1) |  | S | Codigo do sistema |
| empresa | integer(4) |  | S | Codigo da empresa |
| estacao | char(40) |  | S | Nome da maquina. |
| usuario_rede | char(40) |  | S | Usuario da rede. |
| ocioso_inicial | timestamp(8) |  | S | Tempo ocioso inicial. |
| ocioso_acumulado | timestamp(8) |  | S | Tempo ocioso acumulado. |
| ocioso_acum_seg | integer(4) |  | S | Segundos ocioso acumulado. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
