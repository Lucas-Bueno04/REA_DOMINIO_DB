# GEIMPORTADOR_ARGUMENTOS — Argumentos
829 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_ARG | integer(4) | PK |  | Código do argumento |
| NOME_ARG | varchar(64) |  |  | Nome do argumento |
| TIPO_ARG | char(1) |  |  | Tipo de dado do argumento (C = Caractere/R = Decimal/N = Numérico/D = Data/H = Hora) |
| ORIGEM_ARG | char(1) |  |  | Origem do valor padrão (N = Nenhum/F = Fixo/V = Variável automática) |
| VALOR_FIXO | varchar(128) |  | S | Valor padrão fixo (ORIGEM_ARG = F) |
| VALOR_AUTOMATICO | char(1) |  | S | Valor padrão automática (D = Data atual/E = Empresa atual/U = Usuario atual) (ORIGEM_ARG = V) |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
