# GECHECKPOINT_COMPARATIVO_REGIME_TRIBUTACAO — Checkpoint - Comparativo de Regime de Tributação
168 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| ANO_CALENDARIO | integer(4) | PK |  | Ano calendário |
| MES | integer(4) | PK |  | Mês |
| FOLHA_SALARIO_12_MESES | numeric(13) |  |  | Folha salários em 12 meses |
| SALDO_IPI | numeric(13) |  |  | Saldo IPI |
| SALDO_ICMS | numeric(13) |  |  | Saldo ICMS |
| FOLHA_SALARIO | numeric(13) |  |  | Folha Salários |
| FOLHA_CONTRIBUINTE | numeric(13) |  |  | Folha Contribuintes |
| OUTRAS_DESPESAS | numeric(13) |  |  | Outras despesas |
| BASE_CALCULO_CREDITO_PIS | numeric(13) |  |  | Base de cálculo crédito de PIS |
| BASE_CALCULO_CREDITO_COFINS | numeric(13) |  |  | Base de cálculo crédito de COFINS |
| ADICAO_LALUR | numeric(13) |  |  | Adições do LALUR (exceto CSLL) |
| EXCLUSAO_LALUR | numeric(13) |  |  | Exclusões do LALUR |
| RB_COMERCIO_EXPORTACAO | numeric(13) |  | S | Coluna receita bruta comercio exportacao |
| RB_COMERCIO_EXPORTACAO_IND | numeric(13) |  | S | Coluna receita bruta comercio exportacao indireta |
| RB_COMERCIO_N_TRIB_PISCOFINS | numeric(13) |  | S | Coluna receita bruta comercio não tributada por piscofins |
| RB_COMERCIO_DEMAIS_ATIV | numeric(13) |  | S | Coluna receita bruta comercio demais atividades |
| RB_SERVICO_EXPORTACAO | numeric(13) |  | S | Coluna receita bruta servico exportacao |
| RB_SERVICO_N_TRIB_PISCOFINS | numeric(13) |  | S | Coluna receita bruta servico nao tributada por pis/cofins |
| RB_SERVICO_DEMAIS_ATIV | numeric(13) |  | S | Coluna receita bruta servico demais atividades |
| RB_INDUSTRIA_EXPORTACAO | numeric(13) |  | S | Coluna receita bruta industria exportacao |
| RB_INDUSTRIA_EXPORTACAO_IND | numeric(13) |  | S | Coluna receita bruta industria exportacao indireta |
| RB_INDUSTRIA_N_TRIB_PISCOFINS | numeric(13) |  | S | Coluna receita bruta industria nao tributada por pis/cofins |
| RB_INDUSTRIA_PISCOFINS_MONO | numeric(13) |  | S | Coluna receita bruta industria pis/cofins monofasico |
| RB_INDUSTRIA_PISCOFINS_ST | numeric(13) |  | S | Coluna receita bruta industria pis/cofins st |
| RB_INDUSTRIA_DEMAIS_ATIV | numeric(13) |  | S | Coluna receita bruta industria demais atividades |
| RB_MERCADO_INTERNO_12_MESES | numeric(13) |  | S | Coluna receita bruta mercado interno em 12 meses |
| RB_MERCADO_EXTERNO_12_MESES | numeric(13) |  | S | Coluna receita bruta mercado externo em 12 meses |
| RF_JCP | numeric(13) |  | S | Coluna receita financeiras de jcp |
| RF_EXCETO_JCP | numeric(13) |  | S | Coluna receita financeira exceto jcp |
| PIS_MONO_E_ST | numeric(13) |  | S | Coluna pis monofasico e st |
| COFINS_MONO_E_ST | numeric(13) |  | S | Coluna cofins monofasico e st |
