# eftabaju — Outros Movimentos - Impostos Lancados - Detalhamento de Ajustes - RS
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_aju | integer(4) | PK |  | Ajuste |
| codi_taj | integer(4) | PK |  | Codigo |
| cgce_taj | char(20) | PK |  | CNPJ |
| peri_taj | date(4) |  | S | Periodo de referencia |
| diaf_taj | integer(4) |  | S | Dia final |
| dvct_taj | date(4) |  | S | Data de vencimento |
| vdev_taj | numeric(13) |  | S | Valor devido |
| vpag_taj | numeric(13) |  | S | Valor pago |
| data_maj | date(4) | PK |  | Data |
| iest_taj | char(14) |  | S | Inscricao estadual |
| disp_taj | varchar(100) |  | S | Dispositivo Legal Regulamentador da transferencia - AL |
| modelo_taj | integer(4) |  | S | Modelo da nota de transferencia - SE |
| serie_taj | char(3) |  | S | Serie da nota de transferencia - SE |
| numero_taj | integer(4) |  | S | Numero da nota de transferencia - SE |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
