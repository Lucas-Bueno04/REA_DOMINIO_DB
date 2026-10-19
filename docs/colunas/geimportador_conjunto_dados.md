# GEIMPORTADOR_CONJUNTO_DADOS — Conjunto de dados
163 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_CONJUNTO | integer(4) | PK |  | Código do conjunto |
| NOME_CONJUNTO | varchar(64) |  |  | Nome do conjunto |
| CODI_LEIAUTE | integer(4) |  |  | Código do leiaute do conjunto |
| IDENTIFICAR_EMPRESA | char(1) |  |  | Identificar a empresa no arquivo (S=Sim/N=Não) |
| CODI_REGISTRO | integer(4) |  | S | Registro usado para identificar a empresa |
| CODI_TABELA_ESTRANGEIRA | integer(4) |  | S | Tabela estrangeira que identifica a empresa |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
