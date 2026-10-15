# fomovtoserv — Movimentacao - Calculo
2.927.129 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| data | date(4) | PK |  | Competencia |
| tipo_proces | integer(4) | PK |  | Tipo folha |
| i_eventos | integer(4) | PK |  | Evento |
| valor_inf | numeric(15) |  |  | Valor informado |
| valor_cal | numeric(15) |  |  | Valor Calculado |
| prov_desc | varchar(2) |  |  | Provento/Desconto |
| origem | char(1) |  |  | Origem Calculo (Origem calculo C = mensal / F = férias / I = convocacao intermitente |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| rateio | integer(4) | PK |  | Rateio |
| i_servicos | integer(4) | PK |  | Servico |
| valor_inf_compl | numeric(15) |  |  | Valor informado da folha complementar |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| SIMULACAO | smallint(2) |  |  | Simulação de cálculo. (0=Não/1=Sim) |
| VALOR_CALCULADO_INTEGRAL | numeric(15) |  |  | Valor calculado integral. |
| VALOR_INFORMADO_REAL | numeric(17) |  |  | Valor informado real utilizado no cálculo da rubrica. |
| CONSIDERAR_REMUNERACAO_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_RETENCAO_PAGAMENTO_ESOCIAL | smallint(2) |  |  | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
