# focalcinss_movto — Movimento do valor a ser compensado
553 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) |  |  | Empresa |
| i_servicos | integer(4) |  | S | Servico |
| competencia | date(4) |  |  | Competencia |
| I_SEQUENCIA_OLD | integer(4) |  | S | Sequencia - Renomeado |
| tipo_lanc | tinyint(1) |  |  | is Tipo lancamento |
| descricao | varchar(128) |  |  | Descricao |
| valor | numeric(13) |  |  | Valor lancamento |
| origem | tinyint(1) |  |  | is Origem |
| mes_lancto | date(4) |  |  | Mes lancamento |
| tipo_process | integer(4) |  |  | is Tipo da folha |
| tipo_process_lancto | integer(4) |  |  | is Tipo de processamento |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| i_filiais | integer(4) |  |  | Código da filial referente a FOFILIAIS |
| I_CALCINSS_MOVTO_OLD | integer(4) |  | S | Renomeado |
| I_GUIAINSS_OLD | integer(4) |  | S | Renomeado |
| tipo_servico | integer(4) |  |  | Tipo do servico |
| tipo_servico_lanc | integer(4) |  | S | Tipo do Serviço (1=Único/2=Separado/3=Cooperados/4=Tomador Serviço/5=Empreitada Parcial/6=Empreitada Total) |
| TIPO_INSS_LANCTO | smallint(2) |  |  | Tipo INSS: 1=Normal/2=CCT |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCINSS_MOVTO | uniqueidentifier(16) | PK |  | Identificador único |
| I_GUIAINSS | uniqueidentifier(16) |  | S | Identificador único da guia de INSS referente a FOGUIAINSS |
| I_SEQUENCIA | uniqueidentifier(16) |  | S | Sequencia |
