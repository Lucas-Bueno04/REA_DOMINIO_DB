# FOTABELA_CALCULO_IRRF_PARTICIPACAO_LUCROS — Tabela de cálculo do IRRF sobre participação nos lucros.
68 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| COMPETENCIA | date(4) | PK |  | Competência. |
| VALOR_DESCONTO_DEPENDENTE | numeric(13) |  |  | Valor do desconto por dependente. |
| VALOR_MINIMO_RETENCAO | numeric(13) |  |  | Valor mínimo para retenção. |
| ORIGEM_SGD | smallint(2) |  |  | Tabela incluída através do processo de atualização automática do SGD. (0=Não/1=Sim) |
| VERSAO_TABELA_SGD | smallint(2) |  | S | Versão da tabela atualizada pelo SGD |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
