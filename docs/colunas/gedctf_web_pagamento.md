# GEDCTF_WEB_PAGAMENTO — DCTF Web - Pagamentos
82 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competência |
| TIPO_GUIA | smallint(2) | PK |  | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| CODI_IMP | integer(4) |  |  | Imposto |
| I_PAGAMENTO | integer(4) | PK |  | Sequencial do pagamento |
| DATA_PAGAMENTO | date(4) |  |  | Data do pagamento |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| VALOR_MULTA | numeric(13) |  |  | Valor da multa |
| VALOR_JUROS | numeric(13) |  |  | Valor dos juros |
| VALOR_PAGO_A_MAIOR | numeric(13) |  |  | Valor pago a maior |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout/3=Importação tabelas concorrentes/4=Importação de baixas Conta Azul/5=Digital Bank) |
| I_MOVIMENTO_ESCRITORIO | integer(4) |  | S | Conta corrente escritório Honorários |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_PAGAMENTO_CONTA_AZUL | integer(4) |  | S | Sequencial Baixa parcial Conta Azul |
| GUID_CONTABIL | varchar(36) |  | S | Identificador integração Conta Azul |
