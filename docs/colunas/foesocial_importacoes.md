# FOESOCIAL_IMPORTACOES — Importação de dados do site do eSocial.
97 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| COMPETENCIA | date(4) |  |  | Competência de início de utilização. |
| TIPO_ACESSO | smallint(2) |  |  | Tipo de acesso. (2=Certificado própria empresa/3=Certificado procuração) |
| IMPORTAR_TODAS_ALTERACOES_CADASTRO_COLABORADOR | smallint(2) |  |  | Importar todas as alterações do cadastro do colaborador. (0=Não/1=Sim) |
| VERSAO_SISTEMA_IMPORTACAO | varchar(50) |  | S | Versão do sistema no momento da realização da importação. |
| DATA_PROCESSAMENTO | timestamp(8) |  |  | Data em que a importação foi processada. |
| TIPO_IMPORTACAO | smallint(2) |  |  | Tipo de importação. (1=Somente serviços e filiais/2=Somente colaboradores) |
| IMPORTAR_RECIBO | smallint(2) |  |  | 0 - IMPORTAR SEM RECIBO, 1 - IMPORTAR COM RECIBO |
| AGENDAMENTO | smallint(2) |  |  | Importação agendada. (0=Não agendada/1=Agendada) |
| AGENDAMENTO_DATA | date(4) |  | S | Data da importação agendada |
| AGENDAMENTO_HORA | time(8) |  | S | Hora da importação agendada |
