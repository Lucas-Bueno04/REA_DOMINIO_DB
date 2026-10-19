# CTEXTRATO_BANCARIO_CONFIGURACAO_ICEBERG_DETALHE — Configuração para Contabilizar Extrato Bancário Contabilidade Digital - Detalhe
486 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_TRANSACAO | decimal(20) | PK |  | Código da transação |
| I_DETALHE | integer(4) | PK |  | Sequencial do detalhe |
| TIPO_INSCRICAO | tinyint(1) |  |  | Tipo de inscrição (1=CNPJ/2=CPF) |
| INSCRICAO | varchar(14) |  | S | Número da inscrição |
| NOME | varchar(150) |  | S | Nome do participante |
| CODI_CTA | integer(4) |  | S | Código da conta contábil |
| CODI_HIS | integer(4) |  | S | Código do histórico |
| HISTORICO | varchar(300) |  | S | Descrição do histórico |
