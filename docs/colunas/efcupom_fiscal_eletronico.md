# EFCUPOM_FISCAL_ELETRONICO — Cupom Fiscal Eletrônico - CF-e
7.235.124 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CFE | integer(4) | PK |  | Código do CF-e |
| CHAVE_CFE | varchar(44) |  |  | Chave CF-e |
| DATA_CFE | date(4) |  |  | Data do CF-e |
| EXTRATO | integer(4) |  |  | Extrato |
| SAT | integer(4) |  |  | Código do SAT CF-e |
| CODI_CLI | integer(4) |  | S | Código do cliente |
| TIPO_TITULO | tinyint(1) |  |  | Tipo do título (0=Duplicata/1=Cheque/2=Promissória/3=Recibo/4=Clientes/5=Documento Fiscal/99=Outros) |
| IDENTIFICACAO | varchar(255) |  | S | Identificação |
| SITUACAO | integer(4) |  |  | Situação (0/1/2/4) |
| VALOR_TOTAL_CFE | numeric(13) |  |  | Valor Total do CF-e |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| EXTRATO_CANCELAMENTO | integer(4) |  | S | Número CF-e Cancelamento |
| CHAVE_NFE_CANCELAMENTO | varchar(44) |  |  | Chave CF-e Cancelamento |
| CODI_USU | char(30) |  | S | Usuário |
| CONFERIDO | char(1) |  |  | Conferido (S/N) |
