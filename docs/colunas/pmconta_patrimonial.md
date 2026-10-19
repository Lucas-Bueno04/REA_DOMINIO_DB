# PMCONTA_PATRIMONIAL — Contas Patrimoniais
6.528 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CONTA_PATRIMONIAL | integer(4) | PK |  | Código |
| DESCRICAO | varchar(40) |  |  | Descrição |
| TAXA_DEPRECIACAO_FISCAL | numeric(7) |  |  | Taxa ddepreciação fiscal |
| NATUREZA_CONTA | char(1) |  |  | Natureza da conta (D=Devedora/ C=Credora) |
| I_GRUPO_CONTABIL | integer(4) |  | S | Grupo contábil |
| CALCULAR_CORRECAO_MONETARIA_1995 | char(1) |  |  | Calcular correção monetária até 31/12/1995 |
| CONTA_PATRIMONIAL | integer(4) |  | S | Conta contábil - Patrimonial |
| CONTA_AQUISICAO | integer(4) |  |  | Conta contábil - Aquisição |
| HISTORICO_AQUISICAO | integer(4) |  |  | Histórico contábil - Aquisição |
| CONTA_DEBITO_AVALIACAO | integer(4) |  |  | Conta contábil - Avaliação - Valor não recuperável - Débito |
| CONTA_CREDITO_AVALIACAO | integer(4) |  |  | Conta contábil - Avaliação - Valor não recuperável - Crédito |
| HISTORICO_AVALIACAO | integer(4) |  |  | Histórico - Avaliação - Valor não recuperável |
| CONTA_DEPRECIACAO_ACUMULADA | integer(4) |  | S | Conta contábil - Depreciação acumulada |
| HISTORICO_DEPRECIACAO_ACUMULADA | integer(4) |  |  | Histórico contábil - Depreciação acumulada |
| CONTA_DEPRECIACAO_PERIODO | integer(4) |  | S | Conta contábil - Depreciação do período |
| HISTORICO_DEPRECIACAO_PERIODO | integer(4) |  |  | Histórico contábil - Depreciação do período |
| CONTA_BAIXA_CAIXA | integer(4) |  |  | Conta contábil - Baixa - Caixa |
| CONTA_BAIXA_RECEITA_ALIENACAO | integer(4) |  |  | Conta contábil - Baixa - Receita da alienação |
| HISTORICO_BAIXA_RECEITA_ALIENACAO | integer(4) |  |  | Histórico contábil - Baixa - Receita da alienação |
| CONTA_BAIXA_CUSTO_ALIENACAO | integer(4) |  |  | Conta contábil - Baixa - Custo da alienação |
| HISTORICO_BAIXA_CUSTO_ALIENACAO | integer(4) |  |  | Histórico contábil - Baixa - Custo da alienação |
| CONTA_CREDITO_ICMS_RECUPERAR | integer(4) |  |  | Conta contábil - Crédito de ICMS - Provisão - ICMS a recuperar |
| HISTORICO_CREDITO_ICMS_RECUPERAR | integer(4) |  |  | Histórico contábil - Crédito de ICMS - Provisão - ICMS a recuperar |
| CONTA_CREDITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Conta contábil - Crédito de ICMS - Estorno - Custo ou perda |
| HISTORICO_CREDITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Histórico contábil - Crédito de ICMS - Estorno - Custo ou perda |
| CREDITO_ICMS_ATIVO_IMOBILIZADO_CODIGO_AJUSTE | integer(4) |  | S | Crédito ICMS ativo imobilizado - Código do ajuste |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| CONTA_DEBITO_AVALIACAO_AJUSTE | integer(4) |  |  | Conta contábil - Avaliação - Ajuste de avaliação patrimonial - Débito |
| CONTA_CREDITO_AVALIACAO_AJUSTE | integer(4) |  |  | Conta contábil - Avaliação - Ajuste de avaliação patrimonial - Crédito |
| HISTORICO_AVALIACAO_AJUSTE | integer(4) |  |  | Histórico - Avaliação/valor não recuperável |
| CREDITO_ICMS_PERIODO_ANTERIOR_CODIGO_AJUSTE | integer(4) |  | S | Crédito ICMS de períodos anteriores - Código do ajuste |
| CONTA_DEBITO_ICMS_RECUPERAR | integer(4) |  |  | Conta débito da provisão do crédito de ICMS a recuperar |
| CONTA_DEBITO_ICMS_CUSTO_PERDA | integer(4) |  |  | Conta débito do estorno do crédito de ICMS |
| CONTA_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Conta contábil - Crédito de ICMS - Provisão - ICMS a recuperar - Longo Prazo |
| CONTA_DEBITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Conta débito da provisão do crédito de ICMS a recuperar - Longo Prazo |
| HISTORICO_PROVISAO_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Histórico contábil - Crédito de ICMS - Provisão - ICMS a recuperar - Longo Prazo |
| HISTORICO_TRANSFERENCIA_CREDITO_ICMS_RECUPERAR_LONGO_PRAZO | integer(4) |  |  | Histórico contábil - Crédito de ICMS - Transferência - ICMS a recuperar - Longo Prazo |
| SUBCONTA_DEPRECIACAO_ACUMULADA | integer(4) |  |  | Subconta - Depreciação acumulada |
| SUBCONTA_DEBITO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Conta contábil - Avaliação a valor justo - Ganho - Débito |
| CONTA_CREDITO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Conta contábil - Avaliação a valor justo - Ganho - Crédito |
| HISTORICO_AVALIACAO_VALOR_JUSTO_GANHO | integer(4) |  |  | Histórico - Avaliação a valor justo - Ganho |
| CONTA_DEBITO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Conta contábil - Avaliação a valor justo - Perda - Débito |
| SUBCONTA_CREDITO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Conta contábil - Avaliação a valor justo - Perda - Crédito |
| HISTORICO_AVALIACAO_VALOR_JUSTO_PERDA | integer(4) |  |  | Histórico - Avaliação a valor justo - Perda |
| CONTA_BEM_MANTIDO_VENDA | integer(4) |  |  | Conta contábil - Bens mantidos para venda |
| HISTORICO_BEM_MANTIDO_VENDA | integer(4) |  |  | Histórico contábil - Bens mantidos para venda |
