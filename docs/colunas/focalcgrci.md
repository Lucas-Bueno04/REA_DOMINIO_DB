# focalcgrci — Calculo da GRCI
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| competencia | date(4) | PK |  | Competencia |
| trimestral | tinyint(1) |  |  | Calculo trimestral |
| multa | numeric(13) |  |  | Multa |
| valor | numeric(13) |  |  | Valor |
| deducao | tinyint(1) |  |  | Deducao da GPS |
| dt_emissao | date(4) |  | S | Data emissao |
| tipo_process | integer(4) | PK |  | Tipo folha |
| valor_emitido | numeric(13) |  |  | Valor emitido |
| tipo_process_emissao | integer(4) |  | S | Tipo folha emissao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| calc_sobre_sal_min | tinyint(1) |  |  | Calculou sobre salario minimo |
| TIPO_GPS | smallint(2) | PK |  | Tipo da GPS individual: (1=GPS Normal/2=GPS CCT/3=GPS Patronal Maternidade) |
| TIPO_GPS_EMISSAO | smallint(2) |  | S | Tipo da GPS individual emitida: (1=GPS Normal/2=GPS CCT/3=GPS Patronal Maternidade) |
| GPS_CONJUNTA_NOVEMBRO_13_INTEGRAL | smallint(2) |  |  | Recolheu a competência de novembro e o 13º integral em uma única GPS.(0-Não/1-Sim) |
| I_PAGTO | integer(4) |  | S | Código do pagamento |
| EFETUAR_PAGAMENTO | smallint(2) |  | S | Indica se deve aparecer na tela de Pagamentos. (0=Não/1=Sim) |
| VENCIMENTO | date(4) |  | S | Data de vencimento |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
