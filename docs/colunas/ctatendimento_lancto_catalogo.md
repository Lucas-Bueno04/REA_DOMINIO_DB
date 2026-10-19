# CTATENDIMENTO_LANCTO_CATALOGO — Catálogo de lancamentos - Domínio Atendimento
80.534 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_CATALOGO | integer(4) | PK |  | Código do catálogo |
| CODI_EMP | integer(4) |  |  | Empresa |
| GUID_LOTE | uniqueidentifier(16) |  | S | Identificador único para o lote |
| SEQUENCIAL | integer(4) | PK |  | Código sequencial do site |
| DATA_LANCAMENTO | date(4) |  |  | Data de lançamentos |
| CONTA_DEBITO | integer(4) |  |  | Conta debito |
| CONTA_CREDITO | integer(4) |  |  | Conta credito |
| VALOR | numeric(14) |  |  | Valor lançamento |
| HISTORICO | varchar(1000) |  |  | Historico |
| FILIAL | integer(4) |  |  | Filial |
| BAIXADO | smallint(2) |  |  | Baixa do arquivo (0=Download do XML ainda não realizado/1=Download do XML já realizado) |
| IMPORTADO | smallint(2) |  |  | Importação do arquivo (0=Lancamento ainda não importado/1=Lancamento já importado) |
| NOTIFICADO | smallint(2) |  |  | Importação do arquivo (0=Arquivo não notificado para o usuário da Contabilidade/1=Arquivo já notificado para o usuário da Contabilidade) |
| DATA_BAIXADO | date(4) |  | S | Data que o xml foi baixado |
| ORIGEM_XML | smallint(2) |  | S | Origem do XML (1=Baixado automaticamente/2=Baixado pelo utilitários) |
| XML_EXCLUIDO | smallint(2) |  |  | Exclusão do XML (0=Não excluído/1=Excluído) |
| XML_EXCLUIDO_MANUALMENTE | smallint(2) |  |  | Exclusão manual (0=Não/1=Sim) |
| CODIGO_HISTORICO | integer(4) |  | S | Código Historico |
