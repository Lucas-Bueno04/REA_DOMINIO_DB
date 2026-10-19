# GEATENDIMENTO_PLANO_CONTAS_CONTABILIDADE — Envio do plano de contas para a Conta Azul
3.948 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  |  |
| CODI_EMP | integer(4) |  |  |  |
| GUID_CONTABIL | uniqueidentifier(16) |  |  |  |
| DATA_EMISSAO | timestamp(8) |  | S |  |
| DATA_EXCLUSAO | timestamp(8) |  | S |  |
| PERMITE_INSERIR_UNICA_ACAO_ONVIO | smallint(2) |  |  |  |
| INTEGRATION_KEY | varchar(200) |  | S |  |
| SITUACAO_ENVIO | smallint(2) |  |  | -1 - Não é para fazer o envio/ 0 - Não Enviado; 1 - Enviado; 2 - Envio Pendente; 3 - Excluído; 4 - Exclusão Pendente; |
| CNPJ | varchar(14) |  | S |  |
| CPF | varchar(11) |  | S |  |
| RAZAO_SOCIAL | varchar(200) |  | S |  |
| TIPO_ALTERACAO | char(1) |  |  | C - Envia Cadastro de Conta / E - Envia Alteração de Conta / D - Envia a Exclusão da conta / I - Insere Plano de Contas Completo |
| CODIGO_CONTA | integer(4) |  | S |  |
| CLASSIFICACAO_CONTA | varchar(100) |  | S |  |
| TIPO_CONTA | char(1) |  | S |  |
| DESCRICAO_CONTA | varchar(100) |  | S |  |
| DATA_CADASTRO | date(4) |  | S |  |
| SITUACAO_CONTA | char(1) |  | S |  |
| DATA_INATIVACAO | date(4) |  | S |  |
| COMPANY_ID | uniqueidentifier(16) |  | S |  |
| CONTACT_ID | uniqueidentifier(16) |  | S |  |
| CODI_EMP_PLANO | integer(4) |  | S |  |
| GUID_CONTABIL_JSON | uniqueidentifier(16) |  | S |  |
| CODI_EMP_FILIAL | integer(4) |  | S |  |
| REPLICOU_FILIAL | integer(4) |  |  | 0 - Não Replicou / 1 - Replicou |
