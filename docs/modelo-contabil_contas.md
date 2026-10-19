# Modelo — Contábil - contas (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_contas.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

24 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [ctcontas_sped_ecf_geral_ref_sa_scp](#ctcontas_sped_ecf_geral_ref_sa_scp) | `CTCONTAS_SPED_ECF_GERAL_REF_SA_SCP` | 26.875 | medio | empresa |
| [ctcontas_ans](#ctcontas_ans) | `CTCONTAS_ANS` | 21.970 | medio | empresa |
| [ctcontas_grupos_dlpa](#ctcontas_grupos_dlpa) | `CTCONTAS_GRUPOS_DLPA` | 17.562 | medio | empresa |
| [ctcontas_equivalentes](#ctcontas_equivalentes) | `CTCONTAS_EQUIVALENTES` | 15.344 | medio | empresa |
| [ctcontas_bc_geral](#ctcontas_bc_geral) | `CTCONTAS_BC_GERAL` | 9.017 | pequeno | — |
| [ctcontas_aneel](#ctcontas_aneel) | `CTCONTAS_ANEEL` | 8.998 | pequeno | — |
| [ctcontas_sped_ecf_sistema_financeiro](#ctcontas_sped_ecf_sistema_financeiro) | `CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO` | 6.013 | pequeno | — |
| [ctcontas_sped_ecf_sistema_financeiro_presumido](#ctcontas_sped_ecf_sistema_financeiro_presumido) | `CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO_PRESUMIDO` | 5.453 | pequeno | — |
| [ctcontas_bc_bancos_cambio](#ctcontas_bc_bancos_cambio) | `CTCONTAS_BC_BANCOS_CAMBIO` | 4.393 | pequeno | — |
| [ctcontas_bc_valores_mobiliarios](#ctcontas_bc_valores_mobiliarios) | `CTCONTAS_BC_VALORES_MOBILIARIOS` | 4.273 | pequeno | — |
| [ctcontas_cosif](#ctcontas_cosif) | `CTCONTAS_COSIF` | 3.884 | pequeno | — |
| [ctcontas_idiomas](#ctcontas_idiomas) | `CTCONTAS_IDIOMAS` | 3.858 | pequeno | empresa |
| [ctcontas_susep](#ctcontas_susep) | `CTCONTAS_SUSEP` | 3.399 | pequeno | — |
| [ctcontas_sped_ecf_imune_isenta_ref_sa_scp](#ctcontas_sped_ecf_imune_isenta_ref_sa_scp) | `CTCONTAS_SPED_ECF_IMUNE_ISENTA_REF_SA_SCP` | 3.328 | pequeno | empresa |
| [ctcontas_bc_sociedade_corretora_cambio](#ctcontas_bc_sociedade_corretora_cambio) | `CTCONTAS_BC_SOCIEDADE_CORRETORA_CAMBIO` | 3.199 | pequeno | — |
| [ctcontas_bc_sociedade_corretora_titulos](#ctcontas_bc_sociedade_corretora_titulos) | `CTCONTAS_BC_SOCIEDADE_CORRETORA_TITULOS` | 3.199 | pequeno | — |
| [ctcontas_sped_ecf_partido_politico](#ctcontas_sped_ecf_partido_politico) | `CTCONTAS_SPED_ECF_PARTIDO_POLITICO` | 2.657 | pequeno | — |
| [ctcontas_bc_adm_consorcios](#ctcontas_bc_adm_consorcios) | `CTCONTAS_BC_ADM_CONSORCIOS` | 1.202 | pequeno | — |
| [ctcontas_bc_instituicao_pagamento](#ctcontas_bc_instituicao_pagamento) | `CTCONTAS_BC_INSTITUICAO_PAGAMENTO` | 1.182 | pequeno | — |
| [ctcontas_sped_ecf_entidade_fechada](#ctcontas_sped_ecf_entidade_fechada) | `CTCONTAS_SPED_ECF_ENTIDADE_FECHADA` | 904 | pequeno | — |
| [ctcontas_cofi](#ctcontas_cofi) | `CTCONTAS_COFI` | 492 | pequeno | — |
| [ctcontas_sped_ecf_seguradora](#ctcontas_sped_ecf_seguradora) | `CTCONTAS_SPED_ECF_SEGURADORA` | 332 | pequeno | — |
| [ctcontas_sped_ecf_tef](#ctcontas_sped_ecf_tef) | `CTCONTAS_SPED_ECF_TEF` | 324 | pequeno | — |
| [ctcontas_scp](#ctcontas_scp) | `CTCONTAS_SCP` | 14 | pequeno | empresa |

## ctcontas_sped_ecf_geral_ref_sa_scp

**Plano de contas SPED ECF Geral Referencial - Saldo anterior por SCP** — tabela `CTCONTAS_SPED_ECF_GERAL_REF_SA_SCP` (26.875 linhas)

Plano de contas SPED ECF Geral Referencial - Saldo anterior por SCP. 26.875 linhas no catálogo; chave: CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE, CODIGO_CTA_SPED_ECF_GERAL, SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE, CODIGO_CTA_SPED_ECF_GERAL, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`, `CODI_EMP_CORRENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 26.879 linhas, 599 empresa(s).
- tipo_do_saldo_anterior_c_credito_d_debit: todos os valores reais estão no comentário do banco (D=16.743, C=10.136).
- sa3cio_ostensivo_s_sim_n_nao: todos os valores reais estão no comentário do banco (S=23.241, N=3.638).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |
| empresa_corrente | `codi_emp_corrente` | integer(4) |  |  | Empresa corrente |
| conta_sped_ecf | `codigo_cta_sped_ecf_geral` | integer(4) |  |  | Conta SPED ECF |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| scp | `i_scp` | integer(4) |  |  | SCP |
| saldo_anterior | `saldo_anterior` | numeric(13) |  |  | Saldo Anterior |
| tipo_do_saldo_anterior_c_credito_d_debit | `tipo_saldo_anterior` | char(1) |  | ctcontas_sped_ecf_geral_ref_sa_scp_tipo_do_sal | Tipo do Saldo Anterior (C=Crédito / D-Débito) |
| sa3cio_ostensivo_s_sim_n_nao | `socio_ostensivo` | char(1) |  | ctcontas_sped_ecf_geral_ref_sa_scp_sa3cio_oste | SÃ³cio Ostensivo (S=SIM/N=NÃƒO) |

**Filtros:** `conta_contabil` (eq/in), `empresa_corrente` (eq/in), `conta_sped_ecf` (eq/in), `sequencial` (eq/in), `scp` (eq/in), `tipo_do_saldo_anterior_c_credito_d_debit` (eq/in), `sa3cio_ostensivo_s_sim_n_nao` (eq/in)

## ctcontas_ans

**Plano de contas ANS** — tabela `CTCONTAS_ANS` (21.970 linhas)

Plano de contas ANS. 21.970 linhas no catálogo; chave: CODIGO_CTA_ANS, CODI_EMP.

- **Chave:** `CODIGO_CTA_ANS, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_ANS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 21.970 linhas, 5 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): inicio_validade.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=13.210, S=8.760).
- tipo_de_registro_p_padrao_m_manual: todos os valores reais estão no comentário do banco (P=21.970).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_ans` | integer(4) |  |  | Código |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| classificacao | `classificacao_ans` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_ans_natureza_s_sintetica_a_analiti | Natureza (S=Sintética / A=Analítica) |
| tipo_de_registro_p_padrao_m_manual | `tipo_registro` | char(1) |  | ctcontas_ans_tipo_de_registro_p_padrao_m_ma | Tipo de registro (P = Padrão / M = Manual) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in), `tipo_de_registro_p_padrao_m_manual` (eq/in)

## ctcontas_grupos_dlpa

**Grupos DLPA que fazem parte da conta** — tabela `CTCONTAS_GRUPOS_DLPA` (17.562 linhas)

Grupos DLPA que fazem parte da conta. 17.562 linhas no catálogo; chave: CODI_EMP, CODI_CTA, DLPA_CTA.

- **Chave:** `CODI_EMP, CODI_CTA, DLPA_CTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`, `DLPA_CTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17.562 linhas, 1.291 empresa(s).
- Vínculo ctcontas (ctcontas): 0 de 13 linhas sem registro relacionado (empresa 129).
- Vínculo geempre (geempre): 0 de 13 linhas sem registro relacionado (empresa 129).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa_do_plano | `codi_emp` | integer(4) |  |  | Empresa do plano |
| codigo_da_conta | `codi_cta` | integer(4) |  |  | Código da conta |
| codigo_do_grupo_dlpa | `dlpa_cta` | integer(4) |  |  | Código do grupo dlpa |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctcontas` → `ctcontas` por `codi_cta` = `codi_cta` e `codi_emp` = `codi_emp`; colunas: `ctcontas_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo_da_conta` (eq/in), `codigo_do_grupo_dlpa` (eq/in)

## ctcontas_equivalentes

**Contas equivalentes de caixa** — tabela `CTCONTAS_EQUIVALENTES` (15.344 linhas)

Contas equivalentes de caixa. 15.344 linhas no catálogo; chave: CODI_EMP, CODI_CTA.

- **Chave:** `CODI_EMP, CODI_CTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15.344 linhas, 476 empresa(s).
- Vínculo ctcontas (ctcontas): 0 de 33 linhas sem registro relacionado (empresa 1147).
- Vínculo geempre (geempre): 0 de 33 linhas sem registro relacionado (empresa 1147).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| conta_equivalente_caixa | `codi_cta` | integer(4) |  |  | Conta equivalente caixa |
| empresa_do_plano_de_contas | `codi_emp_plano` | integer(4) |  |  | Empresa do plano de contas |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctcontas` → `ctcontas` por `codi_emp_plano` = `codi_emp` e `codi_cta` = `codi_cta`; colunas: `ctcontas_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `conta_equivalente_caixa` (eq/in), `empresa_do_plano_de_contas` (eq/in)

## ctcontas_bc_geral

**Plano de contas Banco Central - Geral** — tabela `CTCONTAS_BC_GERAL` (9.017 linhas)

Plano de contas Banco Central - Geral. 9.017 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9.017 linhas, VALIDADE_INICIO de 1988-06-01 a 2027-07-01.
- utilizacao_f_fiscal_s_societaria_a_ambas: todos os valores reais estão no comentário do banco (F=4.717, S=4.300).
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=7.311, S=1.706).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_geral` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| utilizacao_f_fiscal_s_societaria_a_ambas | `utilizacao` | char(1) |  | ctcontas_bc_geral_utilizacao_f_f | Utilização (F=Fiscal / S=Societária / A=Ambas) |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_geral_natureza_s_sin | Natureza (S=Sintética / A=Analítica) |
| grau_para_calcular_o_valor_do_pai | `clas_cta_grau` | varchar(20) |  |  | Grau para calcular o valor do pai |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `utilizacao_f_fiscal_s_societaria_a_ambas` (eq/in), `natureza_s_sintetica_a_analitica` (eq/in), `grau_para_calcular_o_valor_do_pai` (eq/in)

## ctcontas_aneel

**Plano de contas referencial da ANEEL** — tabela `CTCONTAS_ANEEL` (8.998 linhas)

Plano de contas referencial da ANEEL. 8.998 linhas no catálogo; chave: CODIGO_CTA_ANEEL, VIGENCIA.

- **Chave:** `CODIGO_CTA_ANEEL, VIGENCIA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `INICIO_VALIDADE`
- **Ordem padrão:** `INICIO_VALIDADE desc`, `CODIGO_CTA_ANEEL asc`, `VIGENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8.998 linhas, INICIO_VALIDADE de 2015-01-01 a 2022-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `codigo_cta_aneel` | integer(4) |  |  | Código sequencial |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| classificacao | `classificacao_aneel` | char(20) |  |  | Classificação |
| descricao | `descricao_aneel` | varchar(200) |  |  | Descrição |
| permite_lancamento_s_n | `permite_lancamento_aneel` | char(1) |  |  | Permite lançamento (S/N) |
| inicio_da_validade | `inicio_validade` | date(4) |  |  | Início da validade |
| fim_da_validade | `fim_validade` | date(4) |  |  | Fim da validade |

**Filtros:** `codigo_sequencial` (eq/in), `vigencia` (eq/in), `inicio_da_validade` (entre/gte/lte), `fim_da_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `permite_lancamento_s_n` (eq/in)

## ctcontas_sped_ecf_sistema_financeiro

**Plano de contas SPED ECF Sistema Financeiro** — tabela `CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO` (6.013 linhas)

Plano de contas SPED ECF Sistema Financeiro. 6.013 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_SF.

- **Chave:** `CODIGO_CTA_SPED_ECF_SF`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_SF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.013 linhas, VALIDADE_INICIO de 2014-01-01 a 2026-07-01.
- Colunas expostas nulas em 100% das linhas (1): layout_de_fim_de_utilizacao_da_conta.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=4.805, S=1.208).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (1=2.856, 2=1.402, 4=1.341, 3=414).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_sf` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_sf` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_sistema_financeiro_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_sistema_financeiro_natureza_1_ | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| layout_de_inicio_de_utilizacao_da_conta | `layout_inicio` | integer(4) |  |  | Layout de início de utilização da conta |
| layout_de_fim_de_utilizacao_da_conta | `layout_fim` | integer(4) |  |  | Layout de fim de utilização da conta |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in)

## ctcontas_sped_ecf_sistema_financeiro_presumido

**Plano de contas SPED ECF Pessoa Jurídica Financeira - Lucro Presumido** — tabela `CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO_PRESUMIDO` (5.453 linhas)

Plano de contas SPED ECF Pessoa Jurídica Financeira - Lucro Presumido. 5.453 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_SF_LP.

- **Chave:** `CODIGO_CTA_SPED_ECF_SF_LP`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_SF_LP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.453 linhas, VALIDADE_INICIO de 2015-01-01 a 2026-07-01.
- Colunas expostas nulas em 100% das linhas (1): layout_de_fim_de_utilizacao_da_conta.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=4.340, S=1.113).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (1=2.485, 2=1.398, 4=1.336, 3=234).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_sf_lp` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_sf_lp` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_sistema_financeiro_presumido_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_sistema_financeiro_presumido_natureza_1_ | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| layout_de_inicio_de_utilizacao_da_conta | `layout_inicio` | integer(4) |  |  | Layout de início de utilização da conta |
| layout_de_fim_de_utilizacao_da_conta | `layout_fim` | integer(4) |  |  | Layout de fim de utilização da conta |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | Data em formato integer para otimizar informatico ecf |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | Data em formato integer para otimizar informatico ecf |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in)

## ctcontas_bc_bancos_cambio

**Plano de contas Banco Central - Bancos de Câmbio** — tabela `CTCONTAS_BC_BANCOS_CAMBIO` (4.393 linhas)

Plano de contas Banco Central - Bancos de Câmbio. 4.393 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.393 linhas, VALIDADE_INICIO de 1988-06-01 a 2022-01-03.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=3.663, S=730).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_bancos_cambio` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_bancos_cambio_natureza_s_ | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_bc_valores_mobiliarios

**Plano de contas Banco Central - Distribuidora de Títulos e Valores Mobiliários** — tabela `CTCONTAS_BC_VALORES_MOBILIARIOS` (4.273 linhas)

Plano de contas Banco Central - Distribuidora de Títulos e Valores Mobiliários. 4.273 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.273 linhas, VALIDADE_INICIO de 1988-06-01 a 2023-07-01.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=3.545, S=728).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_valores_mobiliarios` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_valores_mobiliarios_natureza_s_ | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_cosif

**Plano de contas COSIF** — tabela `CTCONTAS_COSIF` (3.884 linhas)

Plano de contas COSIF. 3.884 linhas no catálogo; chave: CODIGO_CTA_COSIF.

- **Chave:** `CODIGO_CTA_COSIF`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO_COSIF`
- **Ordem padrão:** `VALIDADE_INICIO_COSIF desc`, `CODIGO_CTA_COSIF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.884 linhas, VALIDADE_INICIO_COSIF de 1988-06-01 a 2016-01-01.
- utilizacao_f_fiscal_s_societaria_a_ambas: todos os valores reais estão no comentário do banco (S=3.884).
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=3.185, S=699).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_cosif` | integer(4) |  |  | Codigo |
| classificacao | `classificacao_cosif` | varchar(20) |  |  | Classificacao |
| descricao | `descricao_cosif` | varchar(80) |  |  | Descricao |
| inicio_validade | `validade_inicio_cosif` | date(4) |  |  | Inicio validade |
| fim_validade | `validade_fim_cosif` | date(4) |  |  | Fim validade |
| utilizacao_f_fiscal_s_societaria_a_ambas | `utilizacao_cosif` | char(1) |  | ctcontas_cosif_utilizacao_f_fiscal_s_societ | Utilização (F=Fiscal / S=Societária / A=Ambas) |
| natureza_s_sintetica_a_analitica | `natureza_cosif` | char(1) |  | ctcontas_cosif_natureza_s_sintetica_a_anali | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `utilizacao_f_fiscal_s_societaria_a_ambas` (eq/in), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_idiomas

**Contas Contabeis Outros Idiomas** — tabela `CTCONTAS_IDIOMAS` (3.858 linhas)

Contas Contabeis Outros Idiomas. 3.858 linhas no catálogo; chave: CODI_EMP, CODI_CTA, I_IDIOMAS.

- **Chave:** `CODI_EMP, CODI_CTA, I_IDIOMAS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`, `I_IDIOMAS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.858 linhas, 8 empresa(s).
- Vínculo ctcontas (ctcontas): 0 de 485 linhas sem registro relacionado (empresa 9998).
- Vínculo ctidiomas (CTIDIOMAS): 0 de 485 linhas sem registro relacionado (empresa 9998).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_da_conta | `codi_cta` | integer(4) |  |  | Codigo da conta |
| codigo_do_idioma | `i_idiomas` | integer(4) |  |  | Codigo do idioma |
| descricao_da_conta | `descricao` | char(40) |  |  | Descricao da conta |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctcontas` → `ctcontas` por `codi_emp` = `codi_emp` e `codi_cta` = `codi_cta`; colunas: `ctcontas_nome`
- `ctidiomas` → `CTIDIOMAS` por `i_idiomas` = `i_idiomas`; colunas: `ctidiomas_nome`

**Filtros:** `codigo_da_conta` (eq/in), `codigo_do_idioma` (eq/in), `descricao_da_conta` (contem/prefixo)

## ctcontas_susep

**Plano de contas SUSEP** — tabela `CTCONTAS_SUSEP` (3.399 linhas)

Plano de contas SUSEP. 3.399 linhas no catálogo; chave: CODIGO_CTA_SUSEP.

- **Chave:** `CODIGO_CTA_SUSEP`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SUSEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.399 linhas.
- Colunas expostas nulas em 100% das linhas (2): inicio_validade, fim_validade.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=3.166, S=233).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_susep` | integer(4) |  |  | Código |
| classificacao | `classificacao_susep` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_susep_tipo_a_analitica_s_sintetica | Tipo (A = Analítica / S = Sintética) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in)

## ctcontas_sped_ecf_imune_isenta_ref_sa_scp

**Plano de contas SPED ECF Imunes e Isentas Referencial - Saldo anterior por SCP** — tabela `CTCONTAS_SPED_ECF_IMUNE_ISENTA_REF_SA_SCP` (3.328 linhas)

Plano de contas SPED ECF Imunes e Isentas Referencial - Saldo anterior por SCP. 3.328 linhas no catálogo; chave: CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE, CODIGO_CTA_SPED_ECF_IMUNE_ISENTA, SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE, CODIGO_CTA_SPED_ECF_IMUNE_ISENTA, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`, `CODI_EMP_CORRENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.328 linhas, 32 empresa(s).
- tipo_do_saldo_anterior_c_credito_d_debit: todos os valores reais estão no comentário do banco (D=2.204, C=1.124).
- sa3cio_ostensivo_s_sim_n_nao: todos os valores reais estão no comentário do banco (S=3.309, N=19).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |
| empresa_corrente | `codi_emp_corrente` | integer(4) |  |  | Empresa corrente |
| conta_sped_ecf | `codigo_cta_sped_ecf_imune_isenta` | integer(4) |  |  | Conta SPED ECF |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| scp | `i_scp` | integer(4) |  |  | SCP |
| saldo_anterior | `saldo_anterior` | numeric(13) |  |  | Saldo Anterior |
| tipo_do_saldo_anterior_c_credito_d_debit | `tipo_saldo_anterior` | char(1) |  | ctcontas_sped_ecf_imune_isenta_ref_sa_scp_tipo_do_sal | Tipo do Saldo Anterior (C=Crédito / D-Débito) |
| sa3cio_ostensivo_s_sim_n_nao | `socio_ostensivo` | char(1) |  | ctcontas_sped_ecf_imune_isenta_ref_sa_scp_sa3cio_oste | SÃ³cio Ostensivo (S=SIM/N=NÃƒO) |

**Filtros:** `conta_contabil` (eq/in), `empresa_corrente` (eq/in), `conta_sped_ecf` (eq/in), `sequencial` (eq/in), `scp` (eq/in), `tipo_do_saldo_anterior_c_credito_d_debit` (eq/in), `sa3cio_ostensivo_s_sim_n_nao` (eq/in)

## ctcontas_bc_sociedade_corretora_cambio

**Plano de contas Banco Central - Sociedade Corretora de Câmbio** — tabela `CTCONTAS_BC_SOCIEDADE_CORRETORA_CAMBIO` (3.199 linhas)

Plano de contas Banco Central - Sociedade Corretora de Câmbio. 3.199 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.199 linhas, VALIDADE_INICIO de 1988-06-01 a 2022-02-01.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=2.649, S=550).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_soc_cor_cambio` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_sociedade_corretora_cambio_natureza_s_ | Natureza (S=Sintética / A=Analítica) |
| exibe_saldo_1_saldo_somente_na_coluna_to | `exige_saldo` | integer(4) |  |  | Exibe Saldo (1=Saldo somente na coluna total / 2=Saldo na coluna total e realizável até 90 dias / 3=Saldo na coluna total e em pelo menos mais uma coluna |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_bc_sociedade_corretora_titulos

**Plano de contas Banco Central - Sociedade Corretora de Títulos e Valores Mobiliários** — tabela `CTCONTAS_BC_SOCIEDADE_CORRETORA_TITULOS` (3.199 linhas)

Plano de contas Banco Central - Sociedade Corretora de Títulos e Valores Mobiliários. 3.199 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.199 linhas, VALIDADE_INICIO de 1988-06-01 a 2022-02-01.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=2.646, S=553).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_soc_cor_titulos` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_sociedade_corretora_titulos_natureza_s_ | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_sped_ecf_partido_politico

**Plano de contas SPED ECF Partidos Políticos** — tabela `CTCONTAS_SPED_ECF_PARTIDO_POLITICO` (2.657 linhas)

Plano de contas SPED ECF Partidos Políticos. 2.657 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_PARTIDO_POLITICO.

- **Chave:** `CODIGO_CTA_SPED_ECF_PARTIDO_POLITICO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_PARTIDO_POLITICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.657 linhas, VALIDADE_INICIO de 2014-01-01 a 2022-01-01.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=1.952, S=705).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (4=1.298, 1=720, 2=563, 3=57, 5=19).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_partido_politico` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_partido_politico` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_partido_politico_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_partido_politico_natureza_1_ | NATUREZA (1 - ATIVO / 2 - PASSIVO / 3 - PATRIMÔNIO LÍQUIDO / 4 - RESULTADO / 5 - OUTRAS) |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in)

## ctcontas_bc_adm_consorcios

**Plano de contas Banco Central - Administradoras de Consórcio** — tabela `CTCONTAS_BC_ADM_CONSORCIOS` (1.202 linhas)

Plano de contas Banco Central - Administradoras de Consórcio. 1.202 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.202 linhas, VALIDADE_INICIO de 2014-07-01 a 2022-01-03.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=909, S=293).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_adm_consorcios` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_adm_consorcios_natureza_s_ | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_bc_instituicao_pagamento

**Plano de contas Banco Central - Administradoras de Consórcio** — tabela `CTCONTAS_BC_INSTITUICAO_PAGAMENTO` (1.182 linhas)

Plano de contas Banco Central - Administradoras de Consórcio. 1.182 linhas no catálogo; chave: I_CONTA.

- **Chave:** `I_CONTA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.182 linhas, VALIDADE_INICIO de 2017-01-01 a 2023-07-01.
- natureza_s_sintetica_a_analitica: todos os valores reais estão no comentário do banco (A=901, S=281).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_conta` | integer(4) |  |  | Código |
| classificacao | `classificacao_bc_instituicao_pagamento` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(512) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| natureza_s_sintetica_a_analitica | `natureza` | char(1) |  | ctcontas_bc_instituicao_pagamento_natureza_s_ | Natureza (S=Sintética / A=Analítica) |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `natureza_s_sintetica_a_analitica` (eq/in)

## ctcontas_sped_ecf_entidade_fechada

**Plano de contas SPED ECF Entidades Fechadas da Previdência Complementar** — tabela `CTCONTAS_SPED_ECF_ENTIDADE_FECHADA` (904 linhas)

Plano de contas SPED ECF Entidades Fechadas da Previdência Complementar. 904 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_ENTIDADE_FECHADA.

- **Chave:** `CODIGO_CTA_SPED_ECF_ENTIDADE_FECHADA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_ENTIDADE_FECHADA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 904 linhas, VALIDADE_INICIO de 2014-01-01 a 2023-01-01.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=687, S=217).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (1=405, 4=249, 2=147, 3=103).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_entidade_fechada` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_entidade_fechada` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_entidade_fechada_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_entidade_fechada_natureza_1_ | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in)

## ctcontas_cofi

**Plano de contas COFI** — tabela `CTCONTAS_COFI` (492 linhas)

Plano de contas COFI. 492 linhas no catálogo; chave: CODIGO_CTA_COFI.

- **Chave:** `CODIGO_CTA_COFI`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_INICIO_COFI`
- **Ordem padrão:** `DATA_INICIO_COFI desc`, `CODIGO_CTA_COFI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 492 linhas, DATA_INICIO_COFI de 2006-08-12 a 2016-07-07.
- Colunas expostas nulas em 100% das linhas (1): data_fim.
- normal_ou_retificadora_n_normal_r_retifi: todos os valores reais estão no comentário do banco (N=411, R=68, NR=13).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_cofi` | integer(4) |  |  | Código |
| classificacao | `classificacao_cofi` | varchar(20) |  |  | Classificação |
| descricao | `descricao_cofi` | varchar(100) |  |  | Descrição |
| data_inicio | `data_inicio_cofi` | date(4) |  |  | Data início |
| data_fim | `data_fim_cofi` | date(4) |  |  | Data fim |
| permite_relacionamento_s_n | `permite_relacionamento_cofi` | char(1) |  |  | Permite relacionamento (S/N) |
| normal_ou_retificadora_n_normal_r_retifi | `normal_retificadora_cofi` | varchar(2) |  | ctcontas_cofi_normal_ou_retificadora_n_norm | Normal ou retificadora (N=Normal/ R=Retificadora/ NR=Normal e Retificadora) |
| conta_superior | `conta_superior_cofi` | varchar(20) |  |  | Conta superior |
| classificacao_auxiliar | `classificacao_cofi_auxiliar` | varchar(20) |  |  | Classificação auxiliar |

**Filtros:** `codigo` (eq/in), `data_inicio` (entre/gte/lte), `data_fim` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `permite_relacionamento_s_n` (eq/in), `normal_ou_retificadora_n_normal_r_retifi` (eq/in), `conta_superior` (eq/in), `classificacao_auxiliar` (eq/in)

## ctcontas_sped_ecf_seguradora

**Plano de contas SPED ECF Seguradoras ou Entidades Abertas de Previdência Complementar** — tabela `CTCONTAS_SPED_ECF_SEGURADORA` (332 linhas)

Plano de contas SPED ECF Seguradoras ou Entidades Abertas de Previdência Complementar. 332 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_SEGURADORA.

- **Chave:** `CODIGO_CTA_SPED_ECF_SEGURADORA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_SEGURADORA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 332 linhas, VALIDADE_INICIO de 2014-01-01 a 2023-01-01.
- Colunas expostas nulas em 100% das linhas (2): fim_validade, layout_de_fim_de_utilizacao_da_conta.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=281, S=51).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (4=120, 1=104, 2=92, 3=16).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_seguradora` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_seguradora` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_seguradora_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_seguradora_natureza_1_ | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| layout_de_inicio_de_utilizacao_da_conta | `layout_inicio` | integer(4) |  |  | Layout de início de utilização da conta |
| layout_de_fim_de_utilizacao_da_conta | `layout_fim` | integer(4) |  |  | Layout de fim de utilização da conta |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in)

## ctcontas_sped_ecf_tef

**Plano de contas SPED ECF - TEF Tributação Específica do Futebol** — tabela `CTCONTAS_SPED_ECF_TEF` (324 linhas)

Plano de contas SPED ECF - TEF Tributação Específica do Futebol. 324 linhas no catálogo; chave: CODIGO_CTA_SPED_ECF_TEF.

- **Chave:** `CODIGO_CTA_SPED_ECF_TEF`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VALIDADE_INICIO`
- **Ordem padrão:** `VALIDADE_INICIO desc`, `CODIGO_CTA_SPED_ECF_TEF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 324 linhas, VALIDADE_INICIO de 2021-01-01 a 2021-01-01.
- Colunas expostas nulas em 100% das linhas (1): fim_validade.
- tipo_a_analitica_s_sintetica: todos os valores reais estão no comentário do banco (A=261, S=63).
- natureza_1_ativo_2_passivo_3_patrimonio: todos os valores reais estão no comentário do banco (1=125, 4=92, 2=84, 3=23).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_cta_sped_ecf_tef` | integer(4) |  |  | Código |
| classificacao | `classificacao_sped_ecf_tef` | varchar(20) |  |  | Classificação |
| descricao | `descricao` | varchar(255) |  |  | Descrição |
| inicio_validade | `validade_inicio` | date(4) |  |  | Início validade |
| fim_validade | `validade_fim` | date(4) |  |  | Fim validade |
| tipo_a_analitica_s_sintetica | `tipo` | char(1) |  | ctcontas_sped_ecf_tef_tipo_a_anal | Tipo (A = Analítica / S = Sintética) |
| conta_pai_superior | `conta_superior` | varchar(20) |  |  | Conta pai (superior) |
| nivel | `nivel` | integer(4) |  |  | Nível |
| natureza_1_ativo_2_passivo_3_patrimonio | `natureza` | integer(4) |  | ctcontas_sped_ecf_tef_natureza_1_ | Natureza (1 - Ativo / 2 - Passivo / 3 - Patrimônio Líquido / 4 - Resultado) |
| data_em_formato_integer_para_otimizar_in | `validade_inicio_busca` | integer(4) |  |  | Data em formato integer para otimizar informatico ecf |
| validade_fim_busca | `validade_fim_busca` | integer(4) |  |  | Data em formato integer para otimizar informatico ecf |
| mascara_da_conta | `mascara_conta` | varchar(15) |  |  | Mascara da conta |

**Filtros:** `codigo` (eq/in), `inicio_validade` (entre/gte/lte), `fim_validade` (entre/gte/lte), `classificacao` (eq/in), `descricao` (contem/prefixo), `tipo_a_analitica_s_sintetica` (eq/in), `conta_pai_superior` (eq/in), `mascara_da_conta` (eq/in)

## ctcontas_scp

**Contas Contabeis - SCP** — tabela `CTCONTAS_SCP` (14 linhas)

Contas Contabeis - SCP. 14 linhas no catálogo; chave: CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE.

- **Chave:** `CODI_EMP, CODI_CTA, CODI_EMP_CORRENTE`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_CTA asc`, `CODI_EMP_CORRENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14 linhas, 3 empresa(s).
- Vínculo ctcontas (ctcontas): 0 de 5 linhas sem registro relacionado (empresa 612).
- Vínculo geempre (geempre): 0 de 5 linhas sem registro relacionado (empresa 612).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa_do_plano | `codi_emp` | integer(4) |  |  | Empresa do plano |
| codigo_da_conta | `codi_cta` | integer(4) |  |  | Código da conta |
| empresa_corrente | `codi_emp_corrente` | integer(4) |  |  | Empresa corrente |
| definir_scp_padrao_para_o_lancamento_s_n | `definir_scp_padrao` | char(1) |  |  | Definir SCP padrão para o lançamento (S/N) |
| empresa_para_listar_o_cadastro_de_scp | `filial` | integer(4) |  |  | Empresa para listar o cadastro de SCP |
| scp | `i_scp` | integer(4) |  |  | SCP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctcontas` → `ctcontas` por `codi_emp` = `codi_emp` e `codi_cta` = `codi_cta`; colunas: `ctcontas_nome`
- `geempre` → `geempre` por `codi_emp_corrente` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo_da_conta` (eq/in), `empresa_corrente` (eq/in), `definir_scp_padrao_para_o_lancamento_s_n` (eq/in), `scp` (eq/in)

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

### ctcontas_sped_ecf_geral_ref_sa_scp_tipo_do_sal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_GERAL_REF_SA_SCP.TIPO_SALDO_ANTERIOR estão no comentário do banco (2026-10-18). Distribuição: D=16.743, C=10.136.

| Código | Significado |
|---|---|
| C | Crédito |
| D | Débito |

### ctcontas_sped_ecf_geral_ref_sa_scp_sa3cio_oste

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_GERAL_REF_SA_SCP.SOCIO_OSTENSIVO estão no comentário do banco (2026-10-18). Distribuição: S=23.241, N=3.638.

| Código | Significado |
|---|---|
| S | SIM |
| N | NÃƒO |

### ctcontas_ans_natureza_s_sintetica_a_analiti

Confirmado: sim

> Todos os valores observados em CTCONTAS_ANS.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=13.210, S=8.760.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_ans_tipo_de_registro_p_padrao_m_ma

Confirmado: sim

> Todos os valores observados em CTCONTAS_ANS.TIPO_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: P=21.970.

| Código | Significado |
|---|---|
| P | Padrão |
| M | Manual |

### ctcontas_bc_geral_utilizacao_f_f

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_GERAL.UTILIZACAO estão no comentário do banco (2026-10-18). Distribuição: F=4.717, S=4.300.

| Código | Significado |
|---|---|
| F | Fiscal |
| S | Societária |
| A | Ambas |

### ctcontas_bc_geral_natureza_s_sin

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_GERAL.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=7.311, S=1.706.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_sped_ecf_sistema_financeiro_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=4.805, S=1.208.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_sistema_financeiro_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 1=2.856, 2=1.402, 4=1.341, 3=414.

| Código | Significado |
|---|---|
| 1 | Ativo |
| 2 | Passivo |
| 3 | Patrimônio Líquido |
| 4 | Resultado |

### ctcontas_sped_ecf_sistema_financeiro_presumido_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO_PRESUMIDO.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=4.340, S=1.113.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_sistema_financeiro_presumido_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SISTEMA_FINANCEIRO_PRESUMIDO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 1=2.485, 2=1.398, 4=1.336, 3=234.

| Código | Significado |
|---|---|
| 1 | Ativo |
| 2 | Passivo |
| 3 | Patrimônio Líquido |
| 4 | Resultado |

### ctcontas_bc_bancos_cambio_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_BANCOS_CAMBIO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=3.663, S=730.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_bc_valores_mobiliarios_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_VALORES_MOBILIARIOS.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=3.545, S=728.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_cosif_utilizacao_f_fiscal_s_societ

Confirmado: sim

> Todos os valores observados em CTCONTAS_COSIF.UTILIZACAO_COSIF estão no comentário do banco (2026-10-18). Distribuição: S=3.884.

| Código | Significado |
|---|---|
| F | Fiscal |
| S | Societária |
| A | Ambas |

### ctcontas_cosif_natureza_s_sintetica_a_anali

Confirmado: sim

> Todos os valores observados em CTCONTAS_COSIF.NATUREZA_COSIF estão no comentário do banco (2026-10-18). Distribuição: A=3.185, S=699.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_susep_tipo_a_analitica_s_sintetica

Confirmado: sim

> Todos os valores observados em CTCONTAS_SUSEP.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=3.166, S=233.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_imune_isenta_ref_sa_scp_tipo_do_sal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_IMUNE_ISENTA_REF_SA_SCP.TIPO_SALDO_ANTERIOR estão no comentário do banco (2026-10-18). Distribuição: D=2.204, C=1.124.

| Código | Significado |
|---|---|
| C | Crédito |
| D | Débito |

### ctcontas_sped_ecf_imune_isenta_ref_sa_scp_sa3cio_oste

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_IMUNE_ISENTA_REF_SA_SCP.SOCIO_OSTENSIVO estão no comentário do banco (2026-10-18). Distribuição: S=3.309, N=19.

| Código | Significado |
|---|---|
| S | SIM |
| N | NÃƒO |

### ctcontas_bc_sociedade_corretora_cambio_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_SOCIEDADE_CORRETORA_CAMBIO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=2.649, S=550.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_bc_sociedade_corretora_titulos_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_SOCIEDADE_CORRETORA_TITULOS.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=2.646, S=553.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_sped_ecf_partido_politico_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_PARTIDO_POLITICO.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=1.952, S=705.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_partido_politico_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_PARTIDO_POLITICO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 4=1.298, 1=720, 2=563, 3=57, 5=19.

| Código | Significado |
|---|---|
| 1 | ATIVO |
| 2 | PASSIVO |
| 3 | PATRIMÔNIO LÍQUIDO |
| 4 | RESULTADO |
| 5 | OUTRAS |

### ctcontas_bc_adm_consorcios_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_ADM_CONSORCIOS.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=909, S=293.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_bc_instituicao_pagamento_natureza_s_

Confirmado: sim

> Todos os valores observados em CTCONTAS_BC_INSTITUICAO_PAGAMENTO.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: A=901, S=281.

| Código | Significado |
|---|---|
| S | Sintética |
| A | Analítica |

### ctcontas_sped_ecf_entidade_fechada_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_ENTIDADE_FECHADA.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=687, S=217.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_entidade_fechada_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_ENTIDADE_FECHADA.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 1=405, 4=249, 2=147, 3=103.

| Código | Significado |
|---|---|
| 1 | Ativo |
| 2 | Passivo |
| 3 | Patrimônio Líquido |
| 4 | Resultado |

### ctcontas_cofi_normal_ou_retificadora_n_norm

Confirmado: sim

> Todos os valores observados em CTCONTAS_COFI.NORMAL_RETIFICADORA_COFI estão no comentário do banco (2026-10-18). Distribuição: N=411, R=68, NR=13.

| Código | Significado |
|---|---|
| N | Normal |
| R | Retificadora |
| NR | Normal e Retificadora |

### ctcontas_sped_ecf_seguradora_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SEGURADORA.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=281, S=51.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_seguradora_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_SEGURADORA.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 4=120, 1=104, 2=92, 3=16.

| Código | Significado |
|---|---|
| 1 | Ativo |
| 2 | Passivo |
| 3 | Patrimônio Líquido |
| 4 | Resultado |

### ctcontas_sped_ecf_tef_tipo_a_anal

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_TEF.TIPO estão no comentário do banco (2026-10-18). Distribuição: A=261, S=63.

| Código | Significado |
|---|---|
| A | Analítica |
| S | Sintética |

### ctcontas_sped_ecf_tef_natureza_1_

Confirmado: sim

> Todos os valores observados em CTCONTAS_SPED_ECF_TEF.NATUREZA estão no comentário do banco (2026-10-18). Distribuição: 1=125, 4=92, 2=84, 3=23.

| Código | Significado |
|---|---|
| 1 | Ativo |
| 2 | Passivo |
| 3 | Patrimônio Líquido |
| 4 | Resultado |

