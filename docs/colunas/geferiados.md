# geferiados — Feriados
106 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_feriados | integer(4) | PK |  | Codigo sequencial |
| descricao | char(40) |  |  | Descrição |
| abrangencia | tinyint(1) |  |  | Abrangência: (1=Federal/2=Estadual/3=Municipal/4=Sindical) |
| codigo_municipio | integer(4) |  | S | Codigo sequencial do municipio para feriados municipais |
| codigo_uf | integer(4) |  | S | Codigo do estado para feriado estadal |
| tipo | tinyint(1) |  |  | Tipo do feriado(1-Movel/2-Fixo) |
| dia | tinyint(1) |  |  | dia |
| mes | tinyint(1) |  |  | mes |
| ano | integer(4) |  | S | ano |
| I_SINDICATOS | integer(4) |  | S | Código do sindicato (Abrangência Sindical) |
| TIPO_CONSIDERAR_FEDERAL | smallint(2) |  | S | Tipo de consideração para feriados de nível federal.(0-Cálculos e vencimentos/1-Somente cálculos/2-Somente vencimentos) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
