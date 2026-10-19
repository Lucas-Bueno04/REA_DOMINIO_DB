# FOFERIAS_PROGRAMACAO — PROGRAMAÇÃO E AVISO DE FERIAS
17.449 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_PROGRAMACAO | integer(4) | PK |  | Código da programação de férias |
| TIPO | integer(4) | PK |  | 1=PROGRAMACAO, 2=AVISO |
| I_FERIAS_AQUISITIVOS | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| I_FERIAS_GOZO | integer(4) |  | S | SEQUENCIAL DE PERIODOS DE GOZO |
| GOZO_INICIO | date(4) |  | S | Data de início do gozo de férias |
| DIAS_GOZO | numeric(10) |  |  | Data numérica para a quantidade de dias de gozo de férias |
| DIAS_ABONO | numeric(10) |  |  | Data numérica para a quantidade de dias de abono |
| DATA_AVISO | date(4) |  |  | Data do aviso de férias |
| DATA_PAGTO | date(4) |  |  | Data do pagamento das férias |
| PAGA_ABONO | char(1) |  |  | Indica se o abono foi pago |
| PAGA_AD13 | char(1) |  |  | Indica se a antecipação do 13º salário foi paga |
| DIAS_DIREITO | numeric(10) |  |  | Data numérica para a quantidade de dias de direito às férias |
| DIAS_GOZADOS | numeric(10) |  |  | Data numérica para a quantidade de dias de férias já gozados |
| LIMITE_INICIO_GOZO | date(4) |  |  | Data limite para início do gozo de férias |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| ABONO_INICIO | date(4) |  | S | Início do abono |
| ABONO_FIM | date(4) |  | S | Final do abono |
| DATA_SOLICITACAO_ABONO | date(4) |  | S | Data da solicitação do abono pecuniário. |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| PAGA_FERIAS | char(1) |  |  | Indica se as férias foram pagas |
