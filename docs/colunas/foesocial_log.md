# FOESOCIAL_LOG — Tabela de LOG do esocial
265.588 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| SEQUENCIAL | integer(4) |  | S | Código sequencial |
| HORARIO | timestamp(8) |  |  | Horário |
| TIPO | integer(4) |  |  | Tipo do log (1=Lote/2=Evento/3=Geral) |
| CODI_EMP | integer(4) |  | S | Código da empresa |
| I_LOTE | integer(4) |  | S | Código do lote |
| I_DADOS_EVENTO | integer(4) |  | S | Código do evento |
| DESCRICAO | varchar(1000) |  |  | Descrição |
| CICLO | integer(4) |  | S | Ciclo |
| GUID_LOG | uniqueidentifier(16) | PK |  | Identificador único do LOG. |
