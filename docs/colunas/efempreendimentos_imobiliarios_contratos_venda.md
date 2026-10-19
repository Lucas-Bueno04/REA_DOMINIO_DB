# EFEMPREENDIMENTOS_IMOBILIARIOS_CONTRATOS_VENDA — Empreendimentos imobiliários - Contratos de venda
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONTRATO | integer(4) | PK |  | Código do contrato |
| I_EMPREENDIMENTO | integer(4) |  |  | Código do empreendimento |
| CODI_CLI | integer(4) |  |  | Código do cliente |
| NUMERO | char(90) |  |  | Número do contrato |
| DATA_OPERACAO | date(4) |  |  | Data da operação |
| VALOR_VENDA | numeric(13) |  |  | Valor de venda |
| TIPO_OPERACAO | char(2) |  |  | Tipo da operação |
| INFORMACOES_COMPLEMENTARES | char(90) |  |  | Informações complementares |
| CALCULAR_CORRECAO_MONETARIA | char(1) |  |  | Calcular correção monetária (S/N) |
| INDICE_CORRECAO_MONETARIA | char(8) |  | S | Indice de cálculo da correção monetária |
| VALOR_CONTRATO_EM_INDICE | numeric(17) |  |  | Valor do contrato em índice |
| CALCULAR_JUROS | char(1) |  |  | Calcular juros (S/N) |
| FORMA_CALCULO_JUROS | char(1) |  |  | Forma de cálculo dos juros |
| INDICE_JUROS | char(8) |  | S | Índice de cálculo dos juros |
| TAXA_JUROS | numeric(5) |  |  | Taxa de juros |
| ENCERRADO | char(1) |  |  | Contrato já encerrado (S/N) |
| DATA_ENCERRAMENTO | date(4) |  | S | Data de encerramento do contrato |
| I_INDICE_CORRECAO_MONETARIA | integer(4) |  | S | Código do Índice da Correção Monetária |
| I_INDICE_JUROS | integer(4) |  | S | Código do Índice do Juros |
| I_CONTRATO_ORIGEM | integer(4) |  | S | Sequencial do contrato origem |
| CONTRATO_RENEGOCIADO | char(1) |  |  | Contrato renegociado (S/N) |
| DATA_RENEGOCIACAO | date(4) |  | S | Data da renegociação |
| CONTRATO_TRANSFERIDO | char(1) |  |  | Contrato Transferido |
| DATA_TRANSFERENCIA | date(4) |  | S | Data transferência |
| ORIGEM_TRANSFERENCIA | char(1) |  |  | Origem da transferência |
| APLICAR_RET_1_PORCENTO_FAIXA_URBANA_1 | char(1) |  |  | Aplicar RET 1% - Faixa Urbana 1 |
| REDUTOR_AJUSTE | numeric(13) |  |  | Redutor de Ajuste |
| REDUTOR_SOCIAL | numeric(13) |  |  | Redutor Social |
