# FOFERIAS_GOZO_SIMULACAO — Simulação do gozo de férias
3.643 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CODIGO EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CODIGO |
| I_FERIAS_GOZO | integer(4) | PK |  | SEQUENCIAL DE PERIODOS DE GOZO |
| I_FERIAS_AQUISITIVOS | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| GOZO_INICIO | date(4) |  |  | INICIO DO GOZO |
| GOZO_FIM | date(4) |  |  | FIM DO GOZO |
| ABONO_PAGA | char(1) |  |  | PAGA ABONO (S/N) |
| ABONO_INICIO | date(4) |  |  | INICIO ABONO |
| ABONO_FIM | date(4) |  |  | FIM ABONO |
| DATA_PAGTO | date(4) |  |  | DATA DO PAGAMENTO |
| PAGA_AD13 | char(1) |  |  | PAGA 13O (S/N) |
| MEDIAS_MANUAL | char(1) |  |  | MEDIAS INFORMADAS MANUALMENTE (S/N) |
| DIAS_FALTAS | integer(4) |  |  | NUMERO DE DIAS DE FALTAS NO MOMENTO DO CALCULO DE FERIAS |
| BAIXA_PROV_FERIAS | numeric(13) |  |  | VALOR DE FERIAS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| BAIXA_PROV_ADICFERIAS | numeric(13) |  |  | VALOR DE ADICIONAL DE FERIAS (1/3) BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| BAIXA_PROV_INSS | numeric(13) |  |  | VALOR DE INSS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| BAIXA_PROV_FGTS | numeric(13) |  |  | VALOR DE FGTS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| BAIXA_PROV_PIS | numeric(13) |  |  | VALOR DE PIS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| I_PAGTO | integer(4) |  | S | SEQUENCIA DE PAGAMENTO |
| DESCONTAR_FALTAS | char(1) |  |  | DESCONTAR FALTAS |
| I_FERIAS_COLETIVAS | integer(4) |  | S | SEQUENCIAL DE FERIAS COLETIVAS |
| TRANSFERIDO | smallint(2) |  |  | INDICA SE O EMPREGADO FOI TRANSFERIDO |
| TIPO | smallint(2) |  |  | Tipo de cálculo das férias. (1=Individual/2=Coletiva/3=Rescisão/4=Manual/5=Provisão/6=Acerto/7=Simulação férias/8=Simulação rescisão) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| GOZO_INICIO_DN | numeric(10) |  |  | INICIO DO GOZO NUMERICO |
| GOZO_FIM_DN | numeric(10) |  |  | FIM DO GOZO NUMERICO |
| ABONO_INICIO_DN | numeric(10) |  |  | INICIO ABONO NUMERICO |
| ABONO_FIM_DN | numeric(10) |  |  | FIM ABONO NUMERICO |
| INICIO_AQUISITIVO | date(4) |  |  | Data inicial do período aquisitivo |
| FIM_AQUISITIVO | date(4) |  |  | Data final do período aquisitivo |
| DESCONTAR_FALTAS_NOTURNAS | char(1) |  |  | Descontar faltas noturnas. (S=Sim/N=Não) |
| DESCONTAR_FALTAS_SUSPENSAO | char(1) |  |  | Descontar faltas por suspensão (S=Sim/N=Não) |
| DESCONTAR_FALTAS_PARCIAIS | char(1) |  |  | Descontar faltas parciais. (S=Sim/N=Não) |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| NAO_CALCULAR_ADICIONAL_MP_927 | char(1) |  |  | Não calcular 1/3 férias MP 927 |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| INICIOU_NOVO_PERIODO_AQUISITIVO_FERIAS_COLETIVAS_ANO_ADMISSAO | smallint(2) |  |  | Iniciou novo período aquisitivo por férias coletivas no ano da admissão |
| PARCELAR_UM_TERCO_FERIAS | smallint(2) |  |  | Parcelar o valor do 1/3 das férias (0=Não/1=Sim) |
| PAGA_FERIAS | char(1) |  |  | Indica se as férias foram pagas |
