# FOEMPRESTIMOS_CRED_TRAB_RESCISAO — Dados do ultimo calculo da rescisao para o Credito do Trabalhador
57 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Codigo da empresa |
| I_EMPREGADOS | integer(4) | PK |  | Codigo do empregado |
| COMPETENCIA_RESCISAO | date(4) | PK |  | Competencia da rescisao |
| NUMERO_CONTRATO | varchar(15) | PK |  | Numero do contrato |
| DATA_INICIO_CONTRATO | date(4) |  | S | Data de inicio do contrato |
| DATA_FIM_CONTRATO | date(4) |  | S | Data de termino do contrato |
| VALOR_SALDO_DEVEDOR | numeric(13) |  | S | Valor do saldo devedor |
| PERCENTUAL_GARANTIA | numeric(5) |  | S | Percentual da garantia ofertada para desconto na rescisao |
| COMPETENCIA_INICIO_DESCONTO | date(4) |  | S | Competencia de inicio do desconto |
| I_BANCOS | integer(4) |  | S | Codigo do banco |
| CONCESSORA_CODIGO | integer(4) |  | S | Código da instituição financeira concessionária |
| CONCESSORA_DESCRICAO | varchar(40) |  | S | Descrição da instituição financeira concessionária |
| NUMERO_PARCELAS | smallint(2) |  | S | Numero de parcelas |
| VALOR_TOTAL_EMPRESTIMO | numeric(13) |  | S | Valor total do emprestimo |
| DATA_CONSULTA_API | timestamp(8) |  | S | Data da consulta a API do Credito do Trabalhador |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| EXISTIA_PARCELA_COMPETENCIA | smallint(2) |  |  | Indica se ja existia parcela na competencia da rescisao antes do calculo (0=Nao, 1=Sim) |
| VALOR_PARCELA_ORIGINAL | numeric(13) |  | S | Valor original da parcela na competencia antes do calculo da rescisao |
| I_EMPRESTIMO | integer(4) |  | S | Codigo do emprestimo consignado vinculado a parcela da competencia |
| PARCELA | integer(4) |  | S | Numero da parcela na competencia antes do calculo da rescisao |
