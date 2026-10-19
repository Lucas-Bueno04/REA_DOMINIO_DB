# EFDARJ_ENVIO_ARQUIVOS — DARJ - Envio dos Arquivos
11 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_ENVIO | integer(4) | PK |  | Código sequencial de envio dos arquivos |
| CODI_IMP | integer(4) |  |  | Código do imposto |
| PDIC_SIM | integer(4) |  |  | Periodicidade |
| COMPETENCIA | date(4) |  |  | Competência |
| DATA_ENVIO | date(4) |  |  | Data de envio |
| HORARIO_ENVIO | time(8) |  |  | Hora de envio |
| SITUACAO | integer(4) |  |  | Situação processo (0-Não Emitida/1-Em processamento/2-Não processada/3-Processada) |
| ID_SESSAO | integer(4) |  | S | Id da Sessao |
| DATA_PAGAMENTO | date(4) |  | S | Data de pagamento |
| CODIGO_BARRAS | varchar(44) |  | S | Código de barras |
| NOSSO_NUMERO | varchar(25) |  | S | Nosso número |
| VALOR_PRINCIPAL | decimal(12) |  | S | Valor principal |
| VALOR_MULTA | decimal(12) |  | S | Valor da Multa |
| VALOR_JUROS | decimal(12) |  | S | Valor dos Juros |
| VALOR_TOTAL | decimal(12) |  | S | Valor total |
