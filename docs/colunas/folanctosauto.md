# folanctosauto — Lançamentos automaticos
848 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_lanctosauto | integer(4) | PK |  | Sequencial |
| tipo_process | integer(4) |  |  | Tipo do processamento |
| tipo | integer(4) |  |  | Tipo(Serv, Cargos, Filiais etc...) |
| codigo_tipo | integer(4) |  |  | Codigo conforme tipo |
| i_eventos | integer(4) |  |  | Código do evento |
| valor | numeric(13) |  |  | Valor informado. |
| mes_inicio | date(4) |  |  | Data do inicio do lançamento |
| mes_fim | date(4) |  | S | Data do fim do lançamento |
| mes01 | tinyint(1) |  |  | Se o lancamento deve ser feito em janeiro |
| mes02 | tinyint(1) |  |  | Se o lancamento deve ser feito em fevereiro |
| mes03 | tinyint(1) |  |  | Se o lancamento deve ser feito em março |
| mes04 | tinyint(1) |  |  | Se o lancamento deve ser feito em abril |
| mes05 | tinyint(1) |  |  | Se o lancamento deve ser feito em maio |
| mes06 | tinyint(1) |  |  | Se o lancamento deve ser feito em junho |
| mes07 | tinyint(1) |  |  | Se o lancamento deve ser feito em julho |
| mes08 | tinyint(1) |  |  | Se o lancamento deve ser feito em agosto |
| mes09 | tinyint(1) |  |  | Se o lancamento deve ser feito em setembro |
| mes10 | tinyint(1) |  |  | Se o lancamento deve ser feito em outubro |
| mes11 | tinyint(1) |  |  | Se o lancamento deve ser feito em novembro |
| mes12 | tinyint(1) |  |  | Se o lancamento deve ser feito em dezembro |
| I_SINDICATOS_EXPORTA_IMPORTA | integer(4) |  | S | Coluna utilizada para vinculo com o sindicato durante o exporta/importa |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
