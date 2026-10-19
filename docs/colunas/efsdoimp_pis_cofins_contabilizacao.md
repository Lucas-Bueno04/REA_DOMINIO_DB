# EFSDOIMP_PIS_COFINS_CONTABILIZACAO — Saldo do Impostos - ContabilizaÃ§Ã£o do PIS/COFINS
169.720 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| I_SCP | integer(4) | PK |  | SCP |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
| CONSOLIDADO | char(1) | PK |  | Consolidado |
| SALDO_DEVEDOR | numeric(13) |  |  | Saldo devedor |
| SALDO_CREDOR | numeric(13) |  |  | Saldo credor |
| VALOR_TOTAL_DEBITOS | numeric(13) |  |  | Total dÃ©bitos |
| VALOR_TOTAL_CREDITOS | numeric(13) |  |  | Total crÃ©ditos |
| VALOR_DEVOLUCAO | numeric(13) |  |  | DevoluÃ§Ã£o |
| ESTORNO_DEBITO_DIFERIDO_NO_PERIODO | numeric(13) |  |  | Estorno de dÃ©bito diferido no perÃ­odo |
| DEBITO_DIFERIDO_A_PAGAR_NO_PERIODO | numeric(13) |  |  | DÃ©bito diferido a pagar no perÃ­odo |
| VALOR_RETENCOES_UTILIZADAS_PERIODO | numeric(13) |  |  | Valor das retenÃ§Ãµes a serem utilizadas no perÃ­odo |
| VALOR_CREDITO_PRESUMIDO_BEBIDA_FRIA_13097 | numeric(13) |  |  | CrÃ©dito presumido na aquisiÃ§Ã£o de bebidas frias |
| AJUSTE_REDUCAO_DEV_CRE_EMPRE_IMOBILIARIO | numeric(13) |  |  | Ajuste de reduÃ§Ã£o - DevoluÃ§Ãµes de crÃ©ditos empreendimentos imobiliÃ¡rio utilizado no perÃ­odo |
| AJUSTE_REDUCAO_DEVOLUCAO_VENDA | numeric(13) |  |  | Ajuste de reduÃ§Ã£o - DevoluÃ§Ãµes de vendas utilizado no perÃ­odo |
| VALOR_ESTORNO_CREDITO_DIFERIDO | numeric(13) |  |  | Valor de estorno de crÃ©dito diferido no perÃ­odo |
| VALOR_CREDITO_DIFERIDO_UTILIZADO_NO_PERIODO | numeric(13) |  |  | Valor de crÃ©dito diferido utilizado no perÃ­odo |
| VALOR_DIFERIDO_UTILIZADO_NO_PERIODO | numeric(13) |  |  | Valor de crÃ©dito e dÃ©bito diferido utilizado no perÃ­odo |
| CREDITO_PRESUMIDO_ALCOOL_12859 | numeric(13) |  |  | CrÃ©dito presumido importador ou produtor de Ã¡lcool - Lei 12.859/2013 |
| VALOR_DEV_CRE_PRESUMIDO_ALCOOL_12859 | numeric(13) |  |  | Ajuste de AcrÃ©scimo - CrÃ©dito presumido importador ou produtor de Ã¡lcool - Lei 12.859/2013 |
| CREDITO_SOBRE_ESTOQUE | numeric(13) |  |  | CrÃ©dito sobre estoque |
| TOTAL_DEBITOS_CONTRIBUICAO | numeric(13) |  |  | Total de dÃ©bitos: Soma do campos "01 - AlÃ­quota bÃ¡sica", "02 - AlÃ­quotas diferenciadas", "03 - AlÃ­quota por unidade de medida de produto" e "04 - Atividade imobiliÃ¡ria" |
| ESTORNO_DEBITO_DIFERIDO | numeric(13) |  |  | Estorno de dÃ©bito diferido no perÃ­odo |
| DEVOLUCAO_VENDA | numeric(13) |  |  | DevoluÃ§Ã£o de venda |
| VALOR_RETENCAO_APROVEITADA | numeric(13) |  |  | RetenÃ§Ãµes |
| CREDITO_PRESCRITO_PRAZO_DECADENCIAL | numeric(13) |  |  | Credito prescrito prazo decadencial |
| VALOR_SAIDA | numeric(13) |  |  | DÃ©bito |
| DEVOLUCAO_VENDA_REALIZADA_NO_PERIODO | numeric(13) |  |  | Devoluções de vendas realizadas no período |
| CREDITO_PRESUMIDO_SOBRE_RECEITA | numeric(13) |  |  | Crédito presumido sobre as receitas - Art. 31, Lei 12.865/2013 |
| RECEITA_FINANCEIRA_DOCUMENTO_NAO_FISCAL | numeric(13) |  |  | Receita financeira documento não fiscal |
| ACRESCIMO_REDUCAO_LINEAR_ISENCAO_ALIQUOTA_ZERO | numeric(13) |  |  | Acrescimo Reducao Linear da LC 224-2025 |
| REDUCAO_REDUCAO_LINEAR_ISENCAO_ALIQUOTA_ZERO | numeric(13) |  |  | Reducao Reducao Linear da LC 224-2025 - Devolucao |
| CREDITO_PRESUMIDO_SOBRE_RECEITA_REDUCAO_LINEAR | numeric(13) |  |  | Credito Presumido sobre as receitas Reducao Linear da LC 224-2025 |
