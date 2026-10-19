# fosaldosimp — Dados de Guias(IRRF,GPS,PIS e etc...)
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_saldos | integer(4) | PK |  | Codigo |
| codi_emp | integer(4) |  |  | Codigo empresa |
| imposto | integer(4) |  |  | Tipo imposto |
| data_ini | date(4) |  |  | Data inicial |
| tipo_proc | integer(4) |  |  | Tipo folha |
| i_servicos | integer(4) |  |  | Servico |
| data_fim | date(4) |  |  | Data final |
| val_devido | numeric(13) |  |  | Valor devido |
| saldo_acumulado | numeric(13) |  |  | Saldo acumulado |
| data_inicio_acum | date(4) |  |  | Data inicio acumulo |
| pago | char(1) |  |  | Pago |
| data_pagto | date(4) |  |  | Data pagamento |
| val_pago | numeric(13) |  |  | Valor pago |
| val_multa | numeric(13) |  |  | Valor multa |
| val_juro | numeric(13) |  |  | Valor juros |
| conta_cre | integer(4) |  |  | Conta credito |
| val_acid_trab | numeric(13) |  |  | Valor acid. trabalho |
| val_segurados | numeric(13) |  |  | Valor segurado |
| val_empresa | numeric(13) |  |  | Valor empresa |
| val_terceiros | numeric(13) |  |  | Valor terceiros |
| val_deducoes | numeric(13) |  |  | Valor deducoes |
| val_retencao | numeric(13) |  |  | Valor retencao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| val_cooperativas | numeric(13) |  |  | Valores pagos a cooperativas de trabalho. |
| val_comp_100 | numeric(13) |  |  | Valor da compensacao 100% na GPS |
| val_comp_30 | numeric(13) |  |  | Valor da compensacao 30% na GPS |
| val_comp_retecao | numeric(13) |  |  | Valor compensado da retenção do mês |
