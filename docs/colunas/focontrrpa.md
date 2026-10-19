# focontrrpa — RPA Emitidas
1.994 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo empresa |
| i_empregados | integer(4) | PK |  | Empregado |
| numero | numeric(10) | PK |  | Numero |
| competencia | date(4) |  |  | Competencia |
| i_tab_desc_servico | char(255) |  |  | Descricao do servico |
| rendimento | numeric(13) |  |  | Rendimento |
| base_inss | numeric(13) |  | S | Base INSS |
| perc_inss | numeric(5) |  | S | Percentual INSS |
| base_irrf | numeric(13) |  |  | Base IRRF |
| no_depend | integer(4) |  |  | No. Dependente |
| deducao_inss | numeric(13) |  |  | Deducao INSS |
| valor_irrf | numeric(13) |  |  | Valor INSS |
| cod_receita | integer(4) |  |  | Cod. Receita |
| data_pag_irrf | date(4) |  |  | Data pag IRRF |
| valor_iss | numeric(13) |  |  | Valor ISS |
| outros_desc | numeric(13) |  |  | Outros descontos |
| taxa_irrf | numeric(13) |  |  | Taxa IRRF |
| desc_irrf | numeric(13) |  |  | Desconto IRRF |
| desc_depend | numeric(13) |  |  | Desconto dependente |
| inss_frete | numeric(13) |  | S | INSS frete |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_CALCULOS_OLD | integer(4) |  | S | Código sequencial de calculos - Renomeado |
| pensao_alimenticia | numeric(13) |  |  | Pensao alimenticia |
| PERCENTUAL_ISS | numeric(5) |  |  | Percentual ISS |
| DATA_VENCIMENTO_ISS | date(4) |  | S | Data de vencimento |
| OUTROS_PROVENTOS | numeric(13) |  |  | Outros proventos |
| INSS_FRETE_SENAT | numeric(13) |  | S | INSS frete SENAT |
| I_DADOS_EVENTOS_ESOCIAL | integer(4) |  | S | **SEM USO** |
| I_LOTE_ESOCIAL | integer(4) |  | S | **SEM USO** |
| STATUS_ESOCIAL | smallint(2) |  | S | **SEM USO** |
| ENVIAR_ESOCIAL | smallint(2) |  |  | Enviar para o eSocial. (0=Não/1=Sim) |
| INCLUSAO_VALIDADA_ESOCIAL | smallint(2) |  |  | **SEM USO** |
| GERAR_RETIFICACAO_ESOCIAL | smallint(2) |  |  | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| PROCESSAR_EXCLUSAO_ESOCIAL | smallint(2) |  |  | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_CALCULOS | uniqueidentifier(16) |  |  | Código sequencial de calculos |
| VALOR_LIQUIDO | numeric(13) |  | S | Valor liquido |
