# FOFERIAS_COLETIVAS — CALCULOS DE FERIAS COLETIVAS
345 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO |
| I_FERIAS_COLETIVAS | integer(4) | PK |  | SEQUENCIAL DE FERIAS COLETIVAS |
| GOZO_INICIO | date(4) |  |  | INICIO DO GOZO |
| GOZO_FIM | date(4) |  |  | FIM DO GOZO |
| ABONO_PAGA | char(1) |  |  | PAGA ABONO |
| ABONO_INICIO | date(4) |  |  | INICIO DO ABONO |
| ABONO_FIM | date(4) |  |  | FIM DO ABONO |
| DATA_PAGTO | date(4) |  |  | DATA DO PAGAMENTO |
| PAGA_AD13 | char(1) |  |  | PAGAR ADIANTAMENTO DE DECIMO TERCEIRO |
| DESCONTAR_FALTAS | char(1) |  |  | DESCONTAR FALTAS |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| DESCONTAR_FALTAS_NOTURNAS | char(1) |  |  | Descontar faltas noturnas. (S=Sim/N=Não) |
| DESCONTAR_FALTAS_SUSPENSAO | char(1) |  |  | Descontar faltas por suspensão (S=Sim/N=Não) |
| DESCONTAR_FALTAS_PARCIAIS | char(1) |  |  | Descontar faltas parciais. (S=Sim/N=Não) |
| NAO_CALCULAR_ADICIONAL_MP_927 | char(1) |  |  | Não calcular 1/3 férias MP 927 |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| PARCELAR_UM_TERCO_FERIAS | smallint(2) |  |  | Parcelar o valor do 1/3 das férias (0=Não/1=Sim) |
