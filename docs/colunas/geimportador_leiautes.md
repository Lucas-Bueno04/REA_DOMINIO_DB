# GEIMPORTADOR_LEIAUTES — Leiautes do importador
209 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_LEIAUTE | integer(4) | PK |  | Código do leiaute |
| NOME_LEIAUTE | varchar(64) |  |  | Nome do leiaute |
| DESC_LEIAUTE | varchar(256) |  |  | Descrição do leiaute |
| UTILIZA_SEPARADOR_CAMPOS | char(1) |  |  | Utiliza separador de campos (S/N) |
| SEPARADOR_CAMPOS | char(5) |  | S | Separador campos |
| IGNORAR_PRIMEIRO_SEPARADOR_CAMPOS | char(1) |  |  | Ignorar o primeiro caractere da linha quando iniciar com o separador (S/N)) |
| ESTRUTURA_ARQUIVO | char(1) |  |  | Estrutura do arquivo (H = Hierárquico/A = Agrupado) |
| UTILIZA_SEPARADOR_DECIMAL | char(1) |  |  | Utiliza separador decimal (S/N) |
| SEPARADOR_DECIMAL | char(1) |  | S | Separador decimal |
| UTILIZA_DELIMITADOR_CARACTERES | char(1) |  |  | Utiliza delimitador de caracteres (S/N) |
| DELIMITADOR_CARACTERES | char(1) |  | S | Delimitador de caracteres |
| UTILIZA_AGRUPAMENTO_NOTAS | char(1) |  |  | Utiliza agrupamento de notas (S/N) |
| PADRAO | varchar(20) |  | S | Padrão da Domínio Sistemas |
| TIPO_ARQUIVO | char(1) |  | S | Tipo do arquivo (T = Txt/X = XML) |
| OBSERVACAO | varchar(32000) |  | S | Observação |
