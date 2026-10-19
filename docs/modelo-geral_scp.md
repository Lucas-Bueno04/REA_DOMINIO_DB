# Modelo — Geral - scp (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_scp.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [gescp_vigencia_informativos](#gescp_vigencia_informativos) | `GESCP_VIGENCIA_INFORMATIVOS` | 57 | pequeno | empresa |
| [gescp_saldo_inicial](#gescp_saldo_inicial) | `GESCP_SALDO_INICIAL` | 52 | pequeno | empresa |
| [gescp_quadro_societario_socio](#gescp_quadro_societario_socio) | `GESCP_QUADRO_SOCIETARIO_SOCIO` | 36 | pequeno | empresa |
| [gescp_zeramento](#gescp_zeramento) | `GESCP_ZERAMENTO` | 31 | pequeno | empresa |
| [gescp_vigencia](#gescp_vigencia) | `GESCP_VIGENCIA` | 17 | pequeno | empresa |
| [gescp_vigencia_lalur](#gescp_vigencia_lalur) | `GESCP_VIGENCIA_LALUR` | 17 | pequeno | empresa |
| [gescp_quadro_societario](#gescp_quadro_societario) | `GESCP_QUADRO_SOCIETARIO` | 16 | pequeno | empresa |

## gescp_vigencia_informativos

**Sociedade em Conta de Participação - SCP - Vigência Informativos** — tabela `GESCP_VIGENCIA_INFORMATIVOS` (57 linhas)

Sociedade em Conta de Participação - SCP - Vigência Informativos. 57 linhas no catálogo; chave: CODI_EMP, I_SCP, VIGENCIA.

- **Chave:** `CODI_EMP, I_SCP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 57 linhas, 6 empresa(s), VIGENCIA de 2018-01-01 a 2025-01-01.
- forma_de_tributacao_do_lucro_1_lucro_rea: todos os valores reais estão no comentário do banco (5=57).
- periodo_de_apuracao_do_irpj_e_csll_t_tri: todos os valores reais estão no comentário do banco (T=57).
- forma_de_tributacao_do_trimestre_1_1_luc: todos os valores reais estão no comentário do banco (1=57).
- forma_tributacao_trimestre_2: todos os valores reais estão no comentário do banco (1=57).
- forma_tributacao_trimestre_3: todos os valores reais estão no comentário do banco (1=57).
- forma_tributacao_trimestre_4: todos os valores reais estão no comentário do banco (1=57).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(100) |  |  | Descrição |
| forma_de_tributacao_do_lucro_1_lucro_rea | `forma_tributacao` | integer(4) |  | gescp_vigencia_informativos_forma_de_tr | FORMA DE TRIBUTAÇÃO DO LUCRO (1 - LUCRO REAL / 2 - LUCRO REAL/ARBITRADO / 3 - LUCRO PRESUMIDO/REAL / 5 - LUCRO PRESUMIDO / 6 - LUCRO ARBITRADO / 7 - LUCRO PRESUMIDO/ARBITRADO / 8 - IMUNE DE IRPJ / 9 - ISENTO DO IRPJ) |
| periodo_de_apuracao_do_irpj_e_csll_t_tri | `periodo_apuracao_irpj_csll` | char(1) |  | gescp_vigencia_informativos_periodo_de_ | Período de apuração do IRPJ e CSLL (T - Trimestral / A - Anual) |
| forma_de_tributacao_do_trimestre_1_1_luc | `forma_tributacao_trimestre_1` | integer(4) |  | gescp_vigencia_informativos_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_2 | `forma_tributacao_trimestre_2` | integer(4) |  | gescp_vigencia_informativos_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_3 | `forma_tributacao_trimestre_3` | integer(4) |  | gescp_vigencia_informativos_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_4 | `forma_tributacao_trimestre_4` | integer(4) |  | gescp_vigencia_informativos_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |

**Filtros:** `sequencial_do_scp` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo), `periodo_de_apuracao_do_irpj_e_csll_t_tri` (eq/in)

## gescp_saldo_inicial

**Sociedade em Conta de Participação - SCP - Saldo Inicial** — tabela `GESCP_SALDO_INICIAL` (52 linhas)

Sociedade em Conta de Participação - SCP - Saldo Inicial. 52 linhas no catálogo; chave: CODI_EMP, I_SCP, CODI_IMP.

- **Chave:** `CODI_EMP, I_SCP, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_SCP asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 52 linhas, 3 empresa(s).
- Vínculo gescp (GESCP): 0 de 8 linhas sem registro relacionado (empresa 763).
- Vínculo geimposto (geimposto): 0 de 8 linhas sem registro relacionado (empresa 763).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| valor_credor | `valor_credor` | numeric(13) |  |  | Valor Credor |
| valor_devedor | `valor_devedor` | numeric(13) |  |  | Valor Devedor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gescp` → `GESCP` por `codi_emp` = `codi_emp` e `i_scp` = `i_scp`; colunas: `gescp_nome`
- `geimposto` → `geimposto` por `codi_emp` = `codi_emp` e `codi_imp` = `codi_imp`; colunas: `geimposto_nome`

**Filtros:** `sequencial_do_scp` (eq/in), `imposto` (eq/in)

## gescp_quadro_societario_socio

**SCP - Quadro Societário - Sócios** — tabela `GESCP_QUADRO_SOCIETARIO_SOCIO` (36 linhas)

SCP - Quadro Societário - Sócios. 36 linhas no catálogo; chave: CODI_EMP, I_SCP, DATA, I_SOCIO, TIPO.

- **Chave:** `CODI_EMP, I_SCP, DATA, I_SOCIO, TIPO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_INGRESSO`
- **Ordem padrão:** `DATA_INGRESSO desc`, `I_SCP asc`, `DATA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 36 linhas, 5 empresa(s), DATA_INGRESSO de 2018-01-01 a 2025-01-10.
- Colunas expostas nulas em 100% das linhas (1): data_de_saida.
- tipo_s_socio_a_administrador_r_represent: todos os valores reais estão no comentário do banco (S=36).
- exerce_atividade_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=36).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| data | `data` | date(4) |  |  | Data |
| socio | `i_socio` | integer(4) |  |  | Sócio |
| tipo_s_socio_a_administrador_r_represent | `tipo` | char(1) |  | gescp_quadro_societario_socio_tipo_s_socio_a_admini | Tipo (S - Socio/A - Administrador/R - Representante Legal/E - Empresário) |
| ordem | `ordem` | integer(4) |  |  | Ordem |
| participacao | `participacao` | numeric(5) |  |  | Participação % |
| quotas_integralizadas | `valor_quota_integralizada` | numeric(13) |  |  | Quotas integralizadas |
| quotas_a_integralizar | `valor_quota_integralizar` | numeric(13) |  |  | Quotas a integralizar |
| quantidade_de_quotas | `quantidade_quotas` | numeric(13) |  |  | Quantidade de quotas |
| valor_da_quota | `valor_quota` | numeric(13) |  |  | Valor da quota |
| capital_integralizado | `valor_capital_integralizado` | numeric(13) |  |  | Capital integralizado |
| capital_a_integralizar | `valor_capital_integralizar` | numeric(13) |  |  | Capital a integralizar |
| meses_para_integralizacao | `meses_para_integralizacao` | integer(4) |  |  | Meses para integralização |
| condicao | `condicao` | integer(4) |  |  | Condição |
| exerce_atividade_1_sim_0_nao | `exerce_atividade` | integer(4) |  | gescp_quadro_societario_socio_exerce_atividade_1_si | Exerce atividade (1 - Sim/0 - Não) |
| cargo | `cargo` | varchar(30) |  |  | Cargo |
| possui_responsavel_legal_s_n | `possui_responsavel_legal` | char(1) |  |  | Possui responsável legal (S/N) |
| data_de_ingresso | `data_ingresso` | date(4) |  |  | Data de  ingresso |
| data_de_saida | `data_saida` | date(4) |  |  | Data de saída |

**Filtros:** `sequencial_do_scp` (eq/in), `data` (eq/in), `socio` (eq/in), `tipo_s_socio_a_administrador_r_represent` (eq/in), `data_de_ingresso` (entre/gte/lte), `data_de_saida` (entre/gte/lte), `cargo` (contem/prefixo), `possui_responsavel_legal_s_n` (eq/in)

## gescp_zeramento

**Sociedade em Conta de Participação - SCP - Zeramento** — tabela `GESCP_ZERAMENTO` (31 linhas)

Sociedade em Conta de Participação - SCP - Zeramento. 31 linhas no catálogo; chave: CODI_EMP, I_SCP, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_SCP, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_SCP asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 31 linhas, 6 empresa(s).
- Vínculo gescp (GESCP): 0 de 2 linhas sem registro relacionado (empresa 749).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| conta_contabil | `codigo_conta` | integer(4) |  |  | Conta contábil |
| classificacao_da_conta_contabil | `classificacao_conta` | varchar(20) |  |  | Classificação da conta contábil |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gescp` → `GESCP` por `codi_emp` = `codi_emp` e `i_scp` = `i_scp`; colunas: `gescp_nome`

**Filtros:** `sequencial_do_scp` (eq/in), `sequencial` (eq/in), `conta_contabil` (eq/in), `classificacao_da_conta_contabil` (eq/in)

## gescp_vigencia

**Sociedade em Conta de Participação - SCP - Vigência** — tabela `GESCP_VIGENCIA` (17 linhas)

Sociedade em Conta de Participação - SCP - Vigência. 17 linhas no catálogo; chave: CODI_EMP, I_SCP, VIGENCIA.

- **Chave:** `CODI_EMP, I_SCP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17 linhas, 6 empresa(s), VIGENCIA de 2015-01-01 a 2025-01-01.
- Colunas expostas nulas em 100% das linhas (5): codigo_de_atividade_inss_receita_bruta, aliquota_nao_relacionada_inferior_5_inss, forma_de_lancamento_inss_receita_bruta, codigo_recolhimento_pis, codigo_recolhimento_cofins.
- regime_federal_5_lucro_presumido_1_lucro: todos os valores reais estão no comentário do banco (5=17).
- regime_apuracao_c_regime_de_competencia: todos os valores reais estão no comentário do banco (C=9, X=8).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| regime_federal_5_lucro_presumido_1_lucro | `regime_federal` | integer(4) |  | gescp_vigencia_regime_fede | REGIME FEDERAL (5-LUCRO PRESUMIDO / 1-LUCRO REAL / 6-RET - REGIME ESPECIAL TRIB.) |
| regime_apuracao_c_regime_de_competencia | `regime_competencia` | char(1) |  | gescp_vigencia_regime_apur | Regime apuração (C-Regime de Competência / X-Regime de Caixa) |
| codigo_de_recolhimento_irpj | `cod_rec_irpj` | char(6) |  |  | Código de recolhimento IRPJ |
| codigo_de_recolhimento_csll | `cod_rec_csll` | char(6) |  |  | Código de recolhimento CSLL |
| forma_de_calculo_s_c | `lucro_presumido_forma_calculo` | char(1) |  |  | Forma de cálculo (S/C) |
| lancamento_n_p | `lucro_presumido_lancamento` | char(1) |  |  | Lançamento (N/P) |
| descricao | `descricao` | varchar(80) |  |  | Descrição |
| regime_inss_receita_bruta | `regime_apuracao_inss_rb` | integer(4) |  |  | Regime INSS Receita Bruta |
| forma_de_calculo_inss_receita_bruta | `forma_calculo_inss_rb` | integer(4) |  |  | Forma de Cálculo INSS Receita Bruta |
| cnae_principal_inss_receita_bruta | `i_cnae_inss_rb` | char(15) |  |  | CNAE Principal INSS Receita Bruta |
| codigo_de_atividade_inss_receita_bruta | `i_atividade_inss_rb` | char(8) |  |  | Código de atividade INSS Receita Bruta |
| aliquota_inss_receita_bruta | `aliquota_inss_rb` | numeric(7) |  |  | Alíquota INSS Receita Bruta |
| atividade_industria_inss_receita_bruta | `atividade_industria_inss_rb` | char(1) |  |  | Atividade Indústria INSS Receita Bruta |
| atividade_comercio_inss_receita_bruta | `atividade_comercio_inss_rb` | char(1) |  |  | Atividade Comércio INSS Receita Bruta |
| atividade_servico_de_transporte_inss_rec | `atividade_servico_transporte_inss_rb` | char(1) |  |  | Atividade Serviço de Transporte INSS Receita Bruta |
| atividade_demais_servicos_inss_receita_b | `atividade_demais_servicos_inss_rb` | char(1) |  |  | Atividade Demais Serviços INSS Receita Bruta |
| aliquota_nao_relacionada_inferior_5_inss | `aliquota_receitas_nao_rel_inferior_5_inss_rb` | numeric(5) |  |  | Alíquota Não Relacionada Inferior 5% INSS Receita Bruta |
| forma_de_lancamento_inss_receita_bruta | `forma_lancamento_inss_rb` | integer(4) |  |  | Forma de lançamento INSS Receita Bruta |
| considerar_receita_frete_inss_receita_br | `considerar_frete_seguro_despesa_tipo` | integer(4) |  |  | Considerar receita Frete INSS Receita Bruta |
| nao_utilizar_o_credito_da_devolucao_quan | `utilizar_credito_per_sem_rec_desonerada_inss_rb` | char(1) |  |  | Não utilizar o crédito da devolução quando no período de ocorrência não ter receita desonerada |
| calcular_credito_pis_e_cofins_sobre_depr | `calcular_credito_piscofins_depreciacao` | char(1) |  |  | Calcular credito PIS e COFINS sobre depreciação |
| calcular_credito_pis_e_cofins_sobre_aqui | `calcular_credito_piscofins_aquisicao` | char(1) |  |  | Calcular credito PIS e COFINS sobre aquisição |
| calcular_credito_piscofins_aquisicao_mp | `calcular_credito_piscofins_aquisicao_mp` | char(1) |  |  | Calcular credito PIS e COFINS sobre aquisição conforme MP 540/1 |
| deduzir_o_valor_total_do_credito_de_icms | `deduzir_valor_credito_icms_do_pis_cofins` | char(1) |  |  | Deduzir o valor total do crédito de ICMS da base de cálculo de PIS e COFINS |
| possui_mais_de_um_codigo_de_recolhimento | `possui_codigo_recolhimento_pis_cofins` | char(1) |  |  | Possui mais de um código de recolhimento do crédito de PIS e COFINS |
| informar_codigo_recolhimento_pis_cofins | `informar_codigo_recolhimento_pis_cofins` | char(1) |  |  | Possui mais de um código de recolhimento do crédito de PIS e COFINS |
| codigo_recolhimento_pis | `codigo_recolhimento_pis` | varchar(6) |  |  | Código recolhimento PIS |
| codigo_recolhimento_cofins | `codigo_recolhimento_cofins` | varchar(6) |  |  | Código recolhimento COFINS |
| calcular_cradito_de_pis_cofins_sobre_val | `calcular_credito_piscofins_aquisicao_baixa_parcial` | char(1) |  |  | Calcular crÃ©dito de PIS/COFINS sobre valor de aquisiÃ§Ã£o com baixa parcial(S/N) |

**Filtros:** `sequencial_do_scp` (eq/in), `vigencia` (eq/in), `regime_apuracao_c_regime_de_competencia` (eq/in), `codigo_de_recolhimento_irpj` (eq/in), `codigo_de_recolhimento_csll` (eq/in), `forma_de_calculo_s_c` (eq/in), `lancamento_n_p` (eq/in), `descricao` (contem/prefixo), `cnae_principal_inss_receita_bruta` (eq/in), `codigo_de_atividade_inss_receita_bruta` (eq/in), `atividade_industria_inss_receita_bruta` (eq/in), `atividade_comercio_inss_receita_bruta` (eq/in), `atividade_servico_de_transporte_inss_rec` (eq/in), `atividade_demais_servicos_inss_receita_b` (eq/in)

## gescp_vigencia_lalur

**Sociedade em Conta de Participação - SCP - Vigência - Lalur** — tabela `GESCP_VIGENCIA_LALUR` (17 linhas)

Sociedade em Conta de Participação - SCP - Vigência - Lalur. 17 linhas no catálogo; chave: CODI_EMP, I_SCP, VIGENCIA.

- **Chave:** `CODI_EMP, I_SCP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TERMINO_FRUICAO_PERSE_CSLL`
- **Ordem padrão:** `DATA_TERMINO_FRUICAO_PERSE_CSLL desc`, `I_SCP asc`, `VIGENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17 linhas, 6 empresa(s).
- Colunas expostas nulas em 100% das linhas (6): codigo_de_recolhimento_csll, codigo_de_recolhimento_irpj, adicao_contribuicao_social_como_adicao_p, complemento_de_contribuiaao_social_como, data_termino_de_fruicao_do_perse_para_o, data_termino_fruicao_perse_irpj.
- tipo_de_atividade_g_atividade_geral_r_at: todos os valores reais estão no comentário do banco (G=17).
- calcular_sobre_b_base_de_calculo_da_csll: todos os valores reais estão no comentário do banco (B=17).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(100) |  |  | Descrição |
| tipo_de_calculo_1_anual_balanco_de_reduc | `tipo_calculo` | tinyint(1) |  |  | Tipo de cálculo (1=Anual/Balanço de Redução e Suspensão/ 2=Trimestral/ 3=Anual/Recolhimento por estimativa/ 4=Não enquadrada) |
| calcular_lucro_estimado_s_n | `calcular_lucro_estimado` | char(1) |  |  | Calcular lucro Estimado (S/N) |
| optar_sempre_pelo_menor_valor_a_recolher | `optar_menor_calculo_real_estimado` | char(1) |  |  | Optar sempre pelo menor valor a recolher entre os cálculos Real e Estimado (S/N) |
| tipo_de_atividade_g_atividade_geral_r_at | `tipo_atividade` | char(1) |  | gescp_vigencia_lalur_tipo_de_ati | Tipo de atividade (G=Atividade geral/ R=Atividade rural/ A=Ambos) |
| codigo_de_recolhimento_csll | `codigo_recolhimento_csll` | varchar(6) |  |  | Código de recolhimento CSLL |
| codigo_de_recolhimento_irpj | `codigo_recolhimento_irpj` | varchar(6) |  |  | Código de recolhimento IRPJ |
| conta_lucro_operacional_gera | `conta_lucro_operacional_geral` | integer(4) |  |  | Conta - Lucro operacional gera |
| conta_prejuizo_operacional_geral | `conta_prejuizo_operacional_geral` | integer(4) |  |  | Conta - Prejuízo operacional geral |
| conta_lucro_nao_operacional_geral | `conta_lucro_nao_operacional_geral` | integer(4) |  |  | Conta - Lucro não operacional geral |
| conta_prejuizo_nao_operacional_geral | `conta_prejuizo_nao_operacional_geral` | integer(4) |  |  | Conta - Prejuízo não operacional geral |
| conta_lucro_operacional_rural | `conta_lucro_operacional_rural` | integer(4) |  |  | Conta - Lucro operacional rural |
| conta_lucro_nao_operacional_rural | `conta_prejuizo_operacional_rural` | integer(4) |  |  | Conta - Lucro não operacional rural |
| calcular_lucro_da_exploracao_s_n | `calcular_lucro_exploracao` | char(1) |  |  | Calcular Lucro da Exploração (S/N) |
| calcular_bonus_da_adimplencia_fiscal_s_n | `calcular_bonus_adimplencia_fiscal` | char(1) |  |  | Calcular Bônus da Adimplência Fiscal (S/N) |
| adicao_contribuicao_social_como_adicao_p | `i_adicao_csll_para_irpj` | integer(4) |  |  | Adição - Contribuição Social como adição para o cálculo do IRPJ |
| calcular_sobre_b_base_de_calculo_da_csll | `calcular_bonus_adimplencia_fiscal_sobre` | char(1) |  | gescp_vigencia_lalur_calcular_so | Calcular sobre (B - Base de cálculo da CSLL após compensação/N - Receita Bruta) |
| complemento_de_contribuiaao_social_como | `complemento_adicao_csll_para_irpj` | varchar(100) |  |  | Complemento de ContribuiÃ§Ã£o Social como adiÃ§Ã£o para o cÃ¡lculo IRPJ |
| valor_a_ser_considerado_na_adicao_csll_d | `tipo_considera_valor_adicao` | char(1) |  |  | Valor a ser considerado na adição (CSLL devida/CSLL a recolher |
| definir_termino_de_fruicao_do_perse_para | `definir_termino_fruicao_perse_csll` | char(1) |  |  | Definir término de fruição do Perse para o imposto CSLL |
| definir_termino_fruicao_perse_irpj | `definir_termino_fruicao_perse_irpj` | char(1) |  |  | Definir término de fruição do Perse para o imposto IRPJ |
| data_termino_de_fruicao_do_perse_para_o | `data_termino_fruicao_perse_csll` | date(4) |  |  | Data término de fruição do Perse para o imposto CSLL |
| data_termino_fruicao_perse_irpj | `data_termino_fruicao_perse_irpj` | date(4) |  |  | Data término de fruição do Perse para o imposto IRPJ |

**Filtros:** `sequencial_do_scp` (eq/in), `vigencia` (eq/in), `data_termino_de_fruicao_do_perse_para_o` (entre/gte/lte), `data_termino_fruicao_perse_irpj` (entre/gte/lte), `descricao` (contem/prefixo), `tipo_de_calculo_1_anual_balanco_de_reduc` (eq/in), `calcular_lucro_estimado_s_n` (eq/in), `optar_sempre_pelo_menor_valor_a_recolher` (eq/in), `tipo_de_atividade_g_atividade_geral_r_at` (eq/in), `codigo_de_recolhimento_csll` (eq/in), `codigo_de_recolhimento_irpj` (eq/in), `calcular_lucro_da_exploracao_s_n` (eq/in), `calcular_bonus_da_adimplencia_fiscal_s_n` (eq/in), `adicao_contribuicao_social_como_adicao_p` (eq/in)

## gescp_quadro_societario

**SCP - Quadro Societário** — tabela `GESCP_QUADRO_SOCIETARIO` (16 linhas)

SCP - Quadro Societário. 16 linhas no catálogo; chave: CODI_EMP, I_SCP, DATA.

- **Chave:** `CODI_EMP, I_SCP, DATA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 16 linhas, 6 empresa(s), DATA de 2014-10-16 a 2025-01-10.
- Vínculo gescp (GESCP): 0 de 1 linhas sem registro relacionado (empresa 749).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |
| data | `data` | date(4) |  |  | Data |
| capital_social_total | `valor_capital_social_total` | numeric(13) |  |  | Capital social total |
| capital_integralizado | `valor_capital_integralizado` | numeric(13) |  |  | Capital integralizado |
| capital_a_integralizar | `valor_capital_integralizar` | numeric(13) |  |  | Capital a integralizar |
| total_do_capital | `valor_total_capital` | numeric(13) |  |  | Total do capital |
| quotas_integralizadas | `valor_quota_integralizada` | numeric(13) |  |  | Quotas integralizadas |
| quotas_a_integralizar | `valor_quota_integralizar` | numeric(13) |  |  | Quotas a integralizar |
| total_de_quotas | `valor_total_quota` | numeric(13) |  |  | Total de quotas |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `gescp` → `GESCP` por `codi_emp` = `codi_emp` e `i_scp` = `i_scp`; colunas: `gescp_nome`

**Filtros:** `sequencial_do_scp` (eq/in), `data` (eq/in)

## Domínios (significado dos códigos)

`confirmado`: **sim** = vem do comentário do banco e/ou foi conferido nos dados; **parcial** = parte dos valores; **não** = hipótese, não use como regra.

### status_empresa

Situação da empresa no cadastro (geempre.stat_emp)

Confirmado: sim

| Código | Significado |
|---|---|
| A | Ativa |
| I | Inativa |
| C | Em constituição |
| M | Ativo sem movimento |
| B | Em processo de baixa |
| E | Excluindo |

### motivo_inatividade

Motivo da inatividade (geempre.tipoi_emp). Só aparece em empresas inativas.

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Outros |
| 2 | Baixada |
| 3 | Transferida |
| 4 | Inadimplente |

### tipo_inscricao

Tipo da inscrição (CNPJ/CPF/CEI/CAEPF)

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |
| 3 | CEI |
| 6 | CAEPF |

### regime_federal_empresa

Regime federal da folha (geempre.rfed_emp)

Confirmado: parcial

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Microempresa |
| 3 | Empresa de pequeno porte |

### tipo_honorario_empresa

Como a empresa usa o módulo Honorários (geempre.honorario_tipo)

Confirmado: sim

| Código | Significado |
|---|---|
| E | Escritório (quem fatura) |
| C | Cliente |

### sim_nao_texto

Confirmado: sim

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### sim_nao_numerico

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Não |

### gescp_vigencia_informativos_forma_de_tr

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA_INFORMATIVOS.FORMA_TRIBUTACAO_TRIMESTRE_4 estão no comentário do banco (2026-10-18). Distribuição: 1=57.

| Código | Significado |
|---|---|
| 1 | LUCRO REAL |
| 5 | LUCRO PRESUMIDO |
| 6 | ARBITRADO |

### gescp_vigencia_informativos_periodo_de_

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA_INFORMATIVOS.PERIODO_APURACAO_IRPJ_CSLL estão no comentário do banco (2026-10-18). Distribuição: T=57.

| Código | Significado |
|---|---|
| T | Trimestral |
| A | Anual |

### gescp_quadro_societario_socio_tipo_s_socio_a_admini

Confirmado: sim

> Todos os valores observados em GESCP_QUADRO_SOCIETARIO_SOCIO.TIPO estão no comentário do banco (2026-10-18). Distribuição: S=36.

| Código | Significado |
|---|---|
| S | Socio |
| A | Administrador |
| R | Representante Legal |
| E | Empresário |

### gescp_quadro_societario_socio_exerce_atividade_1_si

Confirmado: sim

> Todos os valores observados em GESCP_QUADRO_SOCIETARIO_SOCIO.EXERCE_ATIVIDADE estão no comentário do banco (2026-10-18). Distribuição: 1=36.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Não |

### gescp_vigencia_regime_fede

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA.REGIME_FEDERAL estão no comentário do banco (2026-10-18). Distribuição: 5=17.

| Código | Significado |
|---|---|
| 5 | LUCRO PRESUMIDO |
| 1 | LUCRO REAL |
| 6 | RET - REGIME ESPECIAL TRIB. |

### gescp_vigencia_regime_apur

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA.REGIME_COMPETENCIA estão no comentário do banco (2026-10-18). Distribuição: C=9, X=8.

| Código | Significado |
|---|---|
| C | Regime de Competência |
| X | Regime de Caixa |

### gescp_vigencia_lalur_tipo_de_ati

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA_LALUR.TIPO_ATIVIDADE estão no comentário do banco (2026-10-18). Distribuição: G=17.

| Código | Significado |
|---|---|
| G | Atividade geral |
| R | Atividade rural |
| A | Ambos |

### gescp_vigencia_lalur_calcular_so

Confirmado: sim

> Todos os valores observados em GESCP_VIGENCIA_LALUR.CALCULAR_BONUS_ADIMPLENCIA_FISCAL_SOBRE estão no comentário do banco (2026-10-18). Distribuição: B=17.

| Código | Significado |
|---|---|
| B | Base de cálculo da CSLL após compensação |
| N | Receita Bruta |

