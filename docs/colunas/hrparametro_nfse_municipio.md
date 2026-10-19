# HRPARAMETRO_NFSE_MUNICIPIO — Parametro Honorarios - Municípios que usam a NFS-e
1.735 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_MUNICIPIO | integer(4) | PK |  | Sequencial |
| CODIGO_MUNICIPIO | integer(4) |  |  | Codigo do município |
| FORNECEDOR_SOFTWARE | varchar(128) |  |  | Nome do fornecedor do software |
| VERSAO_ESTRUTURA_XML | tinyint(1) |  |  | Versão da estrutura do arquivo XML que é enviado para a prefeitura |
| NOME_CLASSE_XML | varchar(100) |  | S | Nome da classe xml a ser utilizada para o envio de notas |
| CONTROLE_SEQUENCIAL_TROCA_FORNECEDOR | char(1) |  |  | Controla sequencial quando troca de fornecedor. |
| VIGENCIA | date(4) |  |  | Vigencia do fornecedor |
