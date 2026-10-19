# FOCCUSTOS_EXPOSICAO_FATORES_RISCO_I — Tabela de Exposição a Fatores de Riscos I referente ao cargo do empregado
13 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_CCUSTOS | integer(4) | PK |  | Código do centro de custos. |
| CODIGO | integer(4) | PK |  | Código sequencial |
| DESCRICAO | char(40) |  | S | Descrição |
| TIPO | char(1) |  | S | Tipo: (F=Físico/Q=Químico/B=Biológico/E=Ergonômico/M=Mecânico) |
| FATOR_RISCO | varchar(80) |  | S | Fator de risco |
| INTENSIDADE | char(15) |  | S | Intensidade |
| TECNICA_UTILIZADA | char(40) |  | S | Técnica utilizada |
| EPC_EFICAZ | smallint(2) |  |  | EPC eficaz: (0=Não/1=Sim/2=NA) |
| EPI_EFICAZ | smallint(2) |  |  | EPI eficaz: (0=Não/1=Sim/2=NA) |
| CA_EPI | char(5) |  |  | CA EPI |
| DATA_INICIO | date(4) |  | S | Data início. |
| DATA_FIM | date(4) |  | S | Data fim. |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro: (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |
