# GEATENDIMENTOACOES — Ações a serem enviadas para o Domínio Atendimento
4.390.127 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CLAUSULA | varchar(5000) |  |  |  |
| CODIGO_TABELA | integer(4) |  |  |  |
| ACAO | integer(4) |  |  |  |
| STATUS | integer(4) |  |  |  |
| SEQUENCIAL_GRUPO_ENVIO | integer(4) |  | S |  |
| SEQUENCIAL_GRUPO_RECEBIMENTO | integer(4) |  | S |  |
| CODI_EMP | integer(4) |  |  |  |
| ORDEM | integer(4) |  |  |  |
| ORIGEM_ACAO | integer(4) |  | S | 1-Carga Inicial, 2-Aplicacao |
| DATA_INSERCAO | timestamp(8) |  | S | Data e hora da inserção da ação na tabela. |
| ORIGEM_REENVIO_ERRO | integer(4) |  |  | Se o registro é um reenvio de informação proveniente de uma ação que deu erro |
| ORIGEM_REENVIO_ACAO_ERRO | integer(4) |  |  | Número da ação que deu erro que criou esta ação de reenvio |
| I_FILIAL | integer(4) |  |  | Coluna que indica o código referente a filial |
| NUMERO_TENTATIVAS | integer(4) |  |  | Coluna que indica a quantidade de vezes que foi tentado enviar esta ação |
| EMPRESA_USA_DA | tinyint(1) |  |  | Empresa usa o DA quando a ação foi processada. (0=Não usa/1=Usa). |
| INCLUSAO_EMPRESA | integer(4) |  |  | 1-Registro de inclusao da empresa, 0-Alteração ou exclusão/desativação de empresa |
