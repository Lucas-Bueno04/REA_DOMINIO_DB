# GEIMPORTADOR_DEFINICAO_DADOS — Definição de dados
2.608 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_DEFINICAO | integer(4) | PK |  | Código da definição |
| NOME | varchar(64) |  |  | Nome da definição |
| DESCRICAO | varchar(256) |  |  | Descrição da definição |
| CODI_LEIAUTE | integer(4) |  |  | Código do leiaute referente |
| CODI_REGISTRO | integer(4) |  |  | Código do registro do leiaute referente |
| DEPENDENTE | char(1) |  |  | Dependente de outra definição (S/N) |
| DEPENDENTE_CODI_DEFINICAO | integer(4) |  | S | Definição de dados da qual depende |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
| DIFERENCIAR_MAIUSCULO_MINUSCULO | char(1) |  |  | Diferenciar maiúsculo de minúsculo |
