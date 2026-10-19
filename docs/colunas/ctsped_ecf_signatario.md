# CTSPED_ECF_SIGNATARIO — Tabela de Origem da Importação Registros Signatários.
1.051 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SIGNATARIO | integer(4) | PK |  | Código Signatário. |
| CODI_EMP | integer(4) | PK |  | Código Empresa. |
| TIPO_INSCRICAO | tinyint(1) |  |  | 1 - CNPJ/2 - CPF |
| INSCRICAO | varchar(14) |  | S | Inscricao do CNPJ ou CPF. |
| RAZAO | varchar(255) |  | S | Nome da Entidade. |
| I_QUALIFICACAO | integer(4) |  |  | Qualificação da Entidade. |
| CRC | varchar(15) |  | S | Inscrição do Contabilista. |
| EMAIL | varchar(150) |  | S | Email do Signatário. |
| TELEFONE | varchar(14) |  | S | Telefone do Signatário. |
