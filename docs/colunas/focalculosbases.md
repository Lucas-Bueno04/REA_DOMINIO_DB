# focalculosbases — Calculos - Bases de calculos
8.459.388 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CALCULOSBASES_OLD | integer(4) |  | S | i_calculosbases |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| i_cadbases | integer(4) |  |  | Base de Calculo |
| base | numeric(17) |  |  | Valor da base de calculo |
| taxa | numeric(11) |  |  | Taxa |
| valor | numeric(20) |  |  | Valor |
| DESCRICAO_CALCULO | varchar(250) |  | S | Descrição do cálculo efetuado para a base. |
| I_CALCULOSBASES_EXPIMP_OLD | integer(4) |  | S | Identificador único Exporta importa - Antigo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOSBASES | uniqueidentifier(16) | PK |  | CÓDIGO DA BASE DE CÁLCULO. |
| I_CALCULOSBASES_EXPIMP | uniqueidentifier(16) |  | S | Identificador único Exporta importa |
| I_CALCULOS | uniqueidentifier(16) |  |  | Código do cálculo |
