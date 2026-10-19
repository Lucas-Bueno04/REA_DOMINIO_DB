# CTSPED_CONTABIL_OD_SIGNATARIO — SPED Contábil - Outros Dados - Signatários
329 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial dos outros dados |
| I_SIGNATARIO | integer(4) | PK |  | Sequencial do signatário |
| NOME_SIGNATARIO | varchar(200) |  |  | Nome do signatário |
| CPF | varchar(11) |  |  | CPF |
| QUALIFICACAO | integer(4) |  |  | Qualificação |
| TELEFONE | varchar(14) |  |  | Telefone |
| EMAIL | varchar(60) |  |  | E-mail |
| CRC | varchar(15) |  |  | CRC |
| SEQUENCIAL_CRC | varchar(20) |  |  | Sequencial do CRC |
| DATA_VALIDADE_CRC | date(4) |  | S | Data de validade do CRC |
| UF_CRC | varchar(2) |  |  | UF CRC |
