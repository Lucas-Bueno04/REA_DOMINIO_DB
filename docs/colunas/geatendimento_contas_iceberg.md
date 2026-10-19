# GEATENDIMENTO_CONTAS_ICEBERG — Contas financeiras Iceberg
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| CONTA_CORRENTE | varchar(20) |  | S | Conta corrente |
| DV_CONTA_CORRENTE | char(2) |  | S | Digito verificador da conta corrente |
| CODI_AGE | varchar(10) |  | S | Agencia bancaria |
| AGENCIA_DV | char(2) |  | S | Digito verificador da Agencia bancaria |
| DATA_CRIACAO | date(4) |  | S | Data de criacao da conta |
| STATUS | integer(4) |  |  | 0=Bloqueada / 1=Ativa / 2=Aguardando Confirm. Adicional / 3=Credencial Invalida / 4=Conexao Encerrada / 5=Refazer Consentimento |
| I_BANCO | integer(4) | PK |  | Codigo de identificacão do banco |
| NOME_BANCO | varchar(100) |  | S | Nome da instituição/banco |
| DESCRICAO_BANCO | varchar(100) |  | S | Nome da instituição/banco formatado |
| LINK | varchar(256) |  | S | Link de consentimento gerado via Open Finance |
| ACCOUNT_ID | varchar(256) |  | S | Id gerado via Open Finance |
| OPEN_FINANCE | integer(4) |  |  | Origem do banco 0 - não/ 1 - sim |
| DATA_REQUISICAO | timestamp(8) |  |  | Data do Consentimento (requestDate) |
| CODIGO_BANCO | integer(4) |  | S | Código da Instituição Financeira |
| CONTA_CORRENTE_FORMATADA | varchar(20) |  | S | Conta corrente formatada para uso visual |
| PARTNER | varchar(100) |  | S | Parceiro de conexão Open Banking |
| CONSENT_ID | varchar(50) |  | S | Identificador do consentimento Open Banking |
| CONTA_PROCESSADA | integer(4) |  |  | 0-Aguardando processamento da conta após receber consentimento / 1-Conta cadastrada |
| DATA_ULTIMA_TRANSACAO | timestamp(8) |  | S | Data da última transação recebida antes da troca do id do consentimento |
