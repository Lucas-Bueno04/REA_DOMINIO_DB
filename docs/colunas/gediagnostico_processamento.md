# GEDIAGNOSTICO_PROCESSAMENTO — Tempos de processamento de funcionalidades
3.954 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| COMPETENCIA | date(4) | PK |  | Competência (data) |
| FUNCIONALIDADE | varchar(50) | PK |  | Funcionalidade: Apuracao, FolhaPagamento |
| USUARIO | varchar(128) |  |  | Usuário do sistema |
| VERSAO | varchar(50) |  |  | Versão do sistema |
| DT_INICIO | timestamp(8) |  |  | Início do processamento |
| DT_FIM | timestamp(8) |  |  | Fim do processamento |
| DOMINIO_WEB | smallint(2) |  |  | Dominio Web(1 - Sim/0 - Nao) |
