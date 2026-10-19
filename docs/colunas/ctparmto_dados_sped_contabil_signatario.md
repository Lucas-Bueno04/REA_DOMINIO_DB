# CTPARMTO_DADOS_SPED_CONTABIL_SIGNATARIO — Dados da Assinaturas do registro J930 do SPED CONTABIL
1.203 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SIGNATARIO | integer(4) | PK |  | Sequencial |
| CPF_CNPJ | varchar(14) |  |  | CPF ou CNPJ do Signatário |
| NOME_SIGNATARIO | varchar(255) |  |  | Nome do signatário |
| I_QUALIFICACAO | integer(4) |  |  | Código FK para a tabela CTSPED_SIGNATARIO_QUALIFICACAO |
| CRC_CONTABILISTA | varchar(120) |  | S | CRC do signatário |
| DATA_VALIDADE_CPRC | date(4) |  | S | Data de validade do CRC |
| CRC_EXPEDIDOR | varchar(120) |  | S | CRC do expedidor |
| SEQUENCIAL_CRC | varchar(120) |  | S | Sequencial do CRC |
| TELEFONE_SIGNATARIO | varchar(14) |  | S | Telefone do signatário |
| EMAIL_SIGNATARIO | varchar(150) |  | S | Email signatário |
| RESPONSAVEL_ASSINATURA | char(1) |  | S | Responsável pela assinatura (S - Sim / N - Não) |
