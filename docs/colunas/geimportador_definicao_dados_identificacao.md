# GEIMPORTADOR_DEFINICAO_DADOS_IDENTIFICACAO — Identificação da definição de dados
2.402 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_DEFINICAO | integer(4) | PK |  | Código da definição |
| CODI_IDENTIFICACAO | integer(4) | PK |  | Código da identificação |
| CODI_LEIAUTE | integer(4) |  |  | Código do leiaute referente |
| CODI_REGISTRO | integer(4) |  |  | Código do registro do leiaute referente |
| CODI_CAMPO | integer(4) |  |  | Código do campo do registro |
| CONDICAO | varchar(2) |  |  | Condição do campo (=/</>/<=/>=/<>/BW/VV/VI/LI/LD) |
| VALOR1 | varchar(32) |  | S | Valor da condição |
| VALOR2 | varchar(32) |  | S | Valor2 da condição entre(BW) |
| OPERADOR | char(1) |  |  | Operador lógico (E/O = Ou) |
