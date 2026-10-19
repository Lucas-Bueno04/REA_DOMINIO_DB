# paparmto — Parametros
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| dini_par | date(4) |  |  | Data do proximo periodo depois do fechamento |
| masc_bem_par | char(16) |  |  | Mascara do bem |
| masc_aje_par | char(1) |  | S | Coluna nao utilizada |
| calmes01 | tinyint(1) |  | S | Calculado mes 01 (1 - Sim/2 - Nao) |
| calmes02 | tinyint(1) |  | S | Calculado mes 02 (1 - Sim/2 - Nao) |
| calmes03 | tinyint(1) |  | S | Calculado mes 03 (1 - Sim/2 - Nao) |
| calmes04 | tinyint(1) |  | S | Calculado mes 04 (1 - Sim/2 - Nao) |
| calmes05 | tinyint(1) |  | S | Calculado mes 05 (1 - Sim/2 - Nao) |
| calmes06 | tinyint(1) |  | S | Calculado mes 06 (1 - Sim/2 - Nao) |
| calmes07 | tinyint(1) |  | S | Calculado mes 07 (1 - Sim/2 - Nao) |
| calmes08 | tinyint(1) |  | S | Calculado mes 08 (1 - Sim/2 - Nao) |
| calmes09 | tinyint(1) |  | S | Calculado mes 09 (1 - Sim/2 - Nao) |
| calmes10 | tinyint(1) |  | S | Calculado mes 10 (1 - Sim/2 - Nao) |
| calmes11 | tinyint(1) |  | S | Calculado mes 11 (1 - Sim/2 - Nao) |
| calmes12 | tinyint(1) |  | S | Calculado mes 12 (1 - Sim/2 - Nao) |
| demp_par | date(4) |  | S | Data do inicio do calcula da empresa |
| codmat_par | integer(4) |  | S | Empresa para gerar lancamentos contabeis |
| index_par | char(8) |  | S | Indexador para credito do ICMS |
| dcor_par | date(4) |  | S | Data inicio da correcao pelo Indexador do credito de ICMS |
| icms_par | tinyint(1) |  | S | Credito de ICMS a partir de (1 - 08/2000 / 2 -  01/2001) |
| pro_rata_die_par | char(1) |  | S | Calcula ICMS conforme POR RATA DIE |
| calcula_piscofins | char(1) |  |  | Calcula credito de PIS/COFINS (S/N) |
| ajuste_pis | integer(4) |  | S | Codigo do ajuste para credito do PIS |
| ajuste_cofins | integer(4) |  | S | Codigo do ajuste para credito do COFINS |
| deduzir_valor_original_par | char(1) |  | S | Deduzir valor do ICMS do valor original(S/N) |
| gera_lancamentos_ccu_par | char(1) |  |  | Gera lancamentos contabeis por centro de custos(S/N) |
| atualizar_valores_par | char(1) |  |  | Atualiza valores para data anterior(S/N) |
| calcula_piscofins_a | char(1) |  |  | Calcula credito de PIS/COFINS sobre o valor da aquisicao (S/N) |
| ajuste_pis_a | integer(4) |  | S | Codigo do ajuste para credito do PIS sobre aquisicao |
| ajuste_cofins_a | integer(4) |  | S | Codigo do ajuste para credito do COFINS sobre aquisicao |
| ACUMULADOR_PIS_D | integer(4) |  | S | Código do acumulador para crédito do PIS sobre depreciação |
| ACUMULADOR_COFINS_D | integer(4) |  | S | Código do acumulador para crédito do COFINS sobre depreciação |
| ACUMULADOR_PIS_A | integer(4) |  | S | Código do acumulador para crédito do PIS sobre aquisição |
| ACUMULADOR_COFINS_A | integer(4) |  | S | Código do acumulador para crédito do COFINS sobre aquisição |
| GERA_CREDITO_ICMS_PAR | char(1) |  |  | Gerar informacoes de credito de ICMS (S/N) |
| INICIO_OBRIGATORIEDADE_PAR | date(4) |  | S | Competencia inicial da obrigatoriedade |
| CALCULAR_CREDITO_DEPRECIACAO_PAR | char(1) |  |  | Calcular credito sobre depreciacao (S/N) |
| CALCULAR_CREDITO_AQUISICAO_PAR | char(1) |  |  | Calcular credito sobre valor de aquisicao (S/N) |
| CONTA_PIS_RECUPERAR_PAR | integer(4) |  |  | Conta PIS a recuperar |
| HISTORICO_PIS_RECUPERAR_PAR | integer(4) |  |  | Historico PIS a recuperar |
| CONTA_COFINS_RECUPERAR_PAR | integer(4) |  |  | Conta COFINS a recuperar |
| HISTORICO_COFINS_RECUPERAR_PAR | integer(4) |  |  | Historico COFINS a recuperar |
| DCOR_FINAL_PAR | date(4) |  | S | Data final da correcao pelo Indexador do credito de ICMS |
| ACUMULADOR_IRPJ_GANHO_CAPITAL | integer(4) |  | S | Código do acumulador para cobrança do IRPJ sobre ganho de capital |
| CALCULA_CREDITO_AQUISICAO_MP_540 | char(1) |  |  | Calcula crédito sobre valor de aquisição conforme MP 540/11 |
| DEBITO_ICMS_CODIGO_AJUSTE_PAR | integer(4) |  | S | Débito ICMS - Importação - Código do ajuste na Escrita Fiscal |
