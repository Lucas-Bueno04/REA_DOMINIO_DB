# HRNUMERO_UTILIZADO_RECEBIMENTO — Tabela para ser usada na geração de números e verificar se os números estão sendo utilizados
872 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_NUMERO_UTILIZADO | numeric(30) | PK |  | Número |
| I_CONTA_FINANCEIRA | integer(4) |  | S | Conta financeira |
| USUARIO | varchar(128) |  |  | Usuário |
| TIPO_RECEBIMENTO | integer(4) |  |  | Tipo de recebimento |
| CONNECTION_ID | integer(4) |  | S | Identificador de conexão |
