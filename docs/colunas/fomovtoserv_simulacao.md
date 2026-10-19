# FOMOVTOSERV_SIMULACAO — Movimentação do cálculo de simulação de rescisão/férias
106.705 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo empresa |
| I_EMPREGADOS | integer(4) | PK |  | Empregado |
| DATA | date(4) | PK |  | Competencia |
| TIPO_PROCES | integer(4) | PK |  | Tipo folha |
| I_EVENTOS | integer(4) | PK |  | Evento |
| VALOR_INF | numeric(15) |  |  | Valor informado |
| VALOR_CAL | numeric(15) |  |  | Valor Calculado |
| PROV_DESC | varchar(2) |  |  | Provento/Desconto |
| ORIGEM | char(1) |  |  | Origem Calculo (Origem calculo C = mensal / F = férias / I = convocacao intermitente |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| RATEIO | integer(4) | PK |  | Rateio |
| I_SERVICOS | integer(4) | PK |  | Servico |
| VALOR_INF_COMPL | numeric(15) |  |  | Valor informado da folha complementar |
| I_CALCULOS_OLD | integer(4) |  | S | Código do cálculo - Renomeado |
| SIMULACAO | smallint(2) |  |  | É simulação (0=Não/1=Sim) |
| VALOR_CALCULADO_INTEGRAL | numeric(15) |  |  | Valor calculado integral. |
| VALOR_INFORMADO_REAL | numeric(17) |  |  | Valor informado real utilizado no cálculo da rubrica. |
| CONSIDERAR_REMUNERACAO_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_RETENCAO_PAGAMENTO_ESOCIAL | smallint(2) |  |  | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL | smallint(2) |  |  | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) | PK |  | Código do cálculo |
