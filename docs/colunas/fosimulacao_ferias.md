# FOSIMULACAO_FERIAS — Simulação do cálculo de férias
462 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_SIMULACAO_FERIAS | integer(4) | PK |  | Sequencial de simulação de férias. |
| DESCRICAO | varchar(100) |  |  | Descrição. |
| ADIANTAR_PRIMEIRA_PARCELA_13_SALARIO | smallint(2) |  |  | Adiantar 1ª parcela do 13º salário. (0=Não/1=Sim) |
| DESCONTAR_FALTAS | smallint(2) |  |  | Descontar faltas. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_NOTURNAS | smallint(2) |  |  | Descontar faltas noturnas. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_SUSPENSAS | smallint(2) |  |  | Descontar faltas suspensas. (0=Não/1=Sim) |
| DESCONTAR_FALTAS_PARCIAIS | smallint(2) |  |  | Descontar faltas parciais. (0=Não/1=Sim) |
| GOZO_INICIO | date(4) |  |  | Data de início do período de gozo. |
| GOZO_FIM | date(4) |  |  | Data do fim do período de gozo. |
| PAGA_ABONO | smallint(2) |  |  | Pagar abono pecuniário. (0=Não/1=Sim) |
| ABONO_INICIO | date(4) |  |  | Data de início do período de abono. |
| ABONO_FIM | date(4) |  |  | Data do fim do período de abono. |
| GOZO_INICIO_DN | numeric(13) |  |  | Início do período de gozo numérico. |
| GOZO_FIM_DN | numeric(13) |  |  | Fim do período de gozo numérico. |
| ABONO_INICIO_DN | numeric(13) |  |  | Início do período de abono numérico. |
| ABONO_FIM_DN | numeric(13) |  |  | Fim do período de abono numérico. |
| DATA_PAGTO | date(4) |  |  | Data de pagamento |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1-Importação de tabelas/2=Importação de layout) |
| NAO_CALCULAR_ADICIONAL_MP_927 | smallint(2) |  |  | Não calcular 1/3 férias MP 927 |
| PAGA_FERIAS | smallint(2) |  |  | Indica se as férias foram pagas |
