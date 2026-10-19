# Modelo — Contábil - calculo (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_calculo.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

20 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [pmcalculo_depreciacao_fiscal](#pmcalculo_depreciacao_fiscal) | `PMCALCULO_DEPRECIACAO_FISCAL` | 112.969 | medio | empresa |
| [pmcalculo_depreciacao_lancto](#pmcalculo_depreciacao_lancto) | `PMCALCULO_DEPRECIACAO_LANCTO` | 24.647 | medio | empresa |
| [pmcalculo_depreciacao_societaria](#pmcalculo_depreciacao_societaria) | `PMCALCULO_DEPRECIACAO_SOCIETARIA` | 6 | pequeno | empresa |
| [pmcalculo_credito_icms](#pmcalculo_credito_icms) | `PMCALCULO_CREDITO_ICMS` | 6 | pequeno | empresa |
| [pmcalculo_credito_piscofins](#pmcalculo_credito_piscofins) | `PMCALCULO_CREDITO_PISCOFINS` | 6 | pequeno | empresa |
| [pmcalculo_credito_icms_lancto](#pmcalculo_credito_icms_lancto) | `PMCALCULO_CREDITO_ICMS_LANCTO` | 4 | pequeno | empresa |
| [pmcalculo_credito_piscofins_lancto](#pmcalculo_credito_piscofins_lancto) | `PMCALCULO_CREDITO_PISCOFINS_LANCTO` | 4 | pequeno | empresa |
| [lrcalculo_csll_estimado](#lrcalculo_csll_estimado) | `LRCALCULO_CSLL_ESTIMADO` | 1.278 | pequeno | empresa |
| [lrcalculo_irpj_estimado](#lrcalculo_irpj_estimado) | `LRCALCULO_IRPJ_ESTIMADO` | 1.278 | pequeno | empresa |
| [lrcalculo_irpj_real_adicao](#lrcalculo_irpj_real_adicao) | `LRCALCULO_IRPJ_REAL_ADICAO` | 815 | pequeno | empresa |
| [lrcalculo_irpj_estimado_operacao_receita](#lrcalculo_irpj_estimado_operacao_receita) | `LRCALCULO_IRPJ_ESTIMADO_OPERACAO_RECEITA` | 722 | pequeno | empresa |
| [lrcalculo_csll_estimado_operacao_receita](#lrcalculo_csll_estimado_operacao_receita) | `LRCALCULO_CSLL_ESTIMADO_OPERACAO_RECEITA` | 713 | pequeno | empresa |
| [lrcalculo_csll_real_adicao](#lrcalculo_csll_real_adicao) | `LRCALCULO_CSLL_REAL_ADICAO` | 545 | pequeno | empresa |
| [lrcalculo_irpj_real_deducao](#lrcalculo_irpj_real_deducao) | `LRCALCULO_IRPJ_REAL_DEDUCAO` | 283 | pequeno | empresa |
| [lrcalculo_irpj_incentivo_fiscal](#lrcalculo_irpj_incentivo_fiscal) | `LRCALCULO_IRPJ_INCENTIVO_FISCAL` | 212 | pequeno | empresa |
| [lrcalculo_irpj_estimado_deducao](#lrcalculo_irpj_estimado_deducao) | `LRCALCULO_IRPJ_ESTIMADO_DEDUCAO` | 200 | pequeno | empresa |
| [lrcalculo_csll_real_exclusao](#lrcalculo_csll_real_exclusao) | `LRCALCULO_CSLL_REAL_EXCLUSAO` | 148 | pequeno | empresa |
| [lrcalculo_irpj_real_exclusao](#lrcalculo_irpj_real_exclusao) | `LRCALCULO_IRPJ_REAL_EXCLUSAO` | 148 | pequeno | empresa |
| [lrcalculo_csll_real_deducao](#lrcalculo_csll_real_deducao) | `LRCALCULO_CSLL_REAL_DEDUCAO` | 105 | pequeno | empresa |
| [lrcalculo_csll_estimado_deducao](#lrcalculo_csll_estimado_deducao) | `LRCALCULO_CSLL_ESTIMADO_DEDUCAO` | 93 | pequeno | empresa |

## pmcalculo_depreciacao_fiscal

**Cálculo patrimonial - Depreciação Fsical** — tabela `PMCALCULO_DEPRECIACAO_FISCAL` (112.969 linhas)

Cálculo patrimonial - Depreciação Fsical. 112.969 linhas no catálogo; chave: CODI_EMP, I_CALCULO.

- **Chave:** `CODI_EMP, I_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 113.024 linhas, 240 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_calculo` | integer(4) |  |  | Código |
| numero_da_parcela | `parcela` | integer(4) |  |  | Número da parcela |
| valor_depreciado | `valor_depreciado` | numeric(13) |  |  | Valor depreciado |
| valor_depreciacao_acumulada | `valor_depreciado_acumulado` | numeric(13) |  |  | Valor depreciação acumulada |
| valor_atual_do_bem | `valor_bem_atual` | numeric(13) |  |  | Valor atual do bem |
| valor_da_base_de_calculo_de_pis_e_cofins | `valor_base_calculo_pis_cofins` | numeric(13) |  |  | Valor da Base de Cálculo de PIS e COFINS |

**Filtros:** `codigo` (eq/in)

## pmcalculo_depreciacao_lancto

**Cálculo patrimonial - Depreciação - Lançamentos Contábeis** — tabela `PMCALCULO_DEPRECIACAO_LANCTO` (24.647 linhas)

Cálculo patrimonial - Depreciação - Lançamentos Contábeis. 24.647 linhas no catálogo; chave: CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_LANCAMENTO asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24.670 linhas, 227 empresa(s), COMPETENCIA de 2013-01-31 a 2026-09-30.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_lancamento` | integer(4) |  |  | Código |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lançamento contábil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Número do lançamento contábil |
| competencia | `competencia` | date(4) |  |  | Competência |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lançamento contábil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Código do lote |

**Filtros:** `codigo` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `competencia` (entre/gte/lte), `codigo_do_lote` (eq/in)

## pmcalculo_depreciacao_societaria

**Cálculo patrimonial - Depreciação Societária** — tabela `PMCALCULO_DEPRECIACAO_SOCIETARIA` (6 linhas)

Cálculo patrimonial - Depreciação Societária. 6 linhas no catálogo; chave: CODI_EMP, I_CALCULO.

- **Chave:** `CODI_EMP, I_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_calculo` | integer(4) |  |  | Código |
| numero_da_parcela | `parcela` | integer(4) |  |  | Número da parcela |
| valor_depreciado | `valor_depreciado` | numeric(13) |  |  | Valor depreciado |
| valor_depreciacao_acumulada | `valor_depreciado_acumulado` | numeric(13) |  |  | Valor depreciação acumulada |
| valor_atual_do_bem | `valor_bem_atual` | numeric(13) |  |  | Valor atual do bem |
| base_de_calculo_da_depreciacao | `base_calculo` | numeric(13) |  |  | Base de cálculo da depreciação |

**Filtros:** `codigo` (eq/in)

## pmcalculo_credito_icms

**Cálculo patrimonial - Crédito ICMS** — tabela `PMCALCULO_CREDITO_ICMS` (6 linhas)

Cálculo patrimonial - Crédito ICMS. 6 linhas no catálogo; chave: CODI_EMP, I_CALCULO, MENSAL_QUINZENAL.

- **Chave:** `CODI_EMP, I_CALCULO, MENSAL_QUINZENAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `MENSAL_QUINZENAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_calculo` | integer(4) |  |  | Código |
| periodicidade_0_mensal_1_primeira_quinze | `mensal_quinzenal` | tinyint(1) |  |  | Periodicidade (0=Mensal, 1=Primeira Quinzena, 2=Segunda Quinzena) |
| numero_da_parcela | `parcela` | integer(4) |  |  | Número da parcela |
| valor_do_credito | `valor_credito` | numeric(13) |  |  | Valor do crédito |
| valor_do_credito_acumulado | `valor_credito_acumulado` | numeric(13) |  |  | Valor do crédito acumulado |
| valor_nao_creditavel | `valor_nao_creditavel` | numeric(13) |  |  | Valor não creditável |
| valor_nao_creditavel_acumulado | `valor_nao_creditavel_acumulado` | numeric(13) |  |  | Valor não creditável acumulado |
| valor_do_credito_original | `valor_credito_original` | numeric(13) |  |  | Valor do crédito - Original |
| valor_do_credito_acumulado_original | `valor_credito_acumulado_original` | numeric(13) |  |  | Valor do crédito acumulado - Original |
| valor_nao_creditavel_original | `valor_nao_creditavel_original` | numeric(13) |  |  | Valor não creditável - Original |
| valor_nao_creditavel_acumulado_original | `valor_nao_creditavel_acumulado_original` | numeric(13) |  |  | Valor não creditável acumulado - Original |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_do_credito_total_calculado_na_comp | `valor_credito_total` | numeric(13) |  |  | Valor do crédito total calculado na competência(Creditavel e não Creditável) |

**Filtros:** `codigo` (eq/in), `periodicidade_0_mensal_1_primeira_quinze` (eq/in)

## pmcalculo_credito_piscofins

**Cálculo patrimonial - Crédito PIS/COFINS** — tabela `PMCALCULO_CREDITO_PISCOFINS` (6 linhas)

Cálculo patrimonial - Crédito PIS/COFINS. 6 linhas no catálogo; chave: CODI_EMP, I_CALCULO.

- **Chave:** `CODI_EMP, I_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_calculo` | integer(4) |  |  | Código |
| numero_da_parcela | `parcela` | integer(4) |  |  | Número da parcela |
| valor_do_pis | `valor_pis` | numeric(13) |  |  | Valor do PIS |
| valor_do_pis_acumulado | `valor_pis_acumulado` | numeric(13) |  |  | Valor do PIS acumulado |
| valor_do_cofins | `valor_cofins` | numeric(13) |  |  | Valor do COFINS |
| valor_do_cofins_acumulado | `valor_cofins_acumulado` | numeric(13) |  |  | Valor do COFINS acumulado |
| base_de_calculo_da_pis_cofins | `base_calculo` | numeric(13) |  |  | Base de cÃ¡lculo da PIS/COFINS |

**Filtros:** `codigo` (eq/in)

## pmcalculo_credito_icms_lancto

**Cálculo patrimonial - Crédito ICMS - Lançamentos Contábeis** — tabela `PMCALCULO_CREDITO_ICMS_LANCTO` (4 linhas)

Cálculo patrimonial - Crédito ICMS - Lançamentos Contábeis. 4 linhas no catálogo; chave: CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_LANCAMENTO asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s), COMPETENCIA de 2013-01-31 a 2013-01-31.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_lancamento` | integer(4) |  |  | Código |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lançamento contábil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Número do lançamento contábil |
| competencia | `competencia` | date(4) |  |  | Competência |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lançamento contábil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Código do lote |

**Filtros:** `codigo` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `competencia` (entre/gte/lte), `codigo_do_lote` (eq/in)

## pmcalculo_credito_piscofins_lancto

**Cálculo patrimonial - Crédito PIS/COFINS - Lançamentos Contábeis** — tabela `PMCALCULO_CREDITO_PISCOFINS_LANCTO` (4 linhas)

Cálculo patrimonial - Crédito PIS/COFINS - Lançamentos Contábeis. 4 linhas no catálogo; chave: CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN.

- **Chave:** `CODI_EMP, I_LANCAMENTO, EMPRESA_LAN, NUME_LAN`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_LANCAMENTO asc`, `EMPRESA_LAN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s), COMPETENCIA de 2013-01-02 a 2013-01-02.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `i_lancamento` | integer(4) |  |  | Código |
| empresa_do_lancamento_contabil | `empresa_lan` | integer(4) |  |  | Empresa do lançamento contábil |
| numero_do_lancamento_contabil | `nume_lan` | integer(4) |  |  | Número do lançamento contábil |
| competencia | `competencia` | date(4) |  |  | Competência |
| empresa_que_originou_o_lancamento_contab | `fili_lan` | integer(4) |  |  | Empresa que originou o lançamento contábil |
| codigo_do_lote | `codi_lote` | integer(4) |  |  | Código do lote |

**Filtros:** `codigo` (eq/in), `empresa_do_lancamento_contabil` (eq/in), `numero_do_lancamento_contabil` (eq/in), `competencia` (entre/gte/lte), `codigo_do_lote` (eq/in)

## lrcalculo_csll_estimado

**Cálculo do Lalur - Imposto CSLL Estimado** — tabela `LRCALCULO_CSLL_ESTIMADO` (1.278 linhas)

Cálculo do Lalur - Imposto CSLL Estimado. 1.278 linhas no catálogo; chave: CODI_EMP, I_CALCULO.

- **Chave:** `CODI_EMP, I_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.278 linhas, 43 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| base_de_calculo_das_vendas | `valor_base_calculo_venda` | numeric(13) |  |  | Base de cálculo das vendas |
| base_de_calculo_dos_servicos | `valor_base_calculo_servico` | numeric(13) |  |  | Base de cálculo dos serviços |
| base_de_calculo_dos_ganhos | `valor_base_calculo_ganho` | numeric(13) |  |  | Base de cálculo dos ganhos |
| total_da_base_de_calculo | `valor_base_calculo` | numeric(13) |  |  | Total da base de cálculo |
| csll_devida | `valor_csll_devida` | numeric(13) |  |  | CSLL devida |
| deducoes | `valor_deducao` | numeric(13) |  |  | Deduções |
| deducao_csll_retida_por_orgaos_publicos | `valor_deducao_orgao_publico_federal` | numeric(13) |  |  | Dedução - CSLL retida por Órgãos Públicos Federais |
| deducao_pago_em_meses_anteriores | `valor_deducao_pago_em_mes_anterior` | numeric(13) |  |  | Dedução - pago em meses anteriores |
| deducao_csll_retida_por_outras_pessoas_j | `valor_deducao_outra_pessoa_juridica` | numeric(13) |  |  | Dedução - CSLL retida por outras pessoas jurídicas |
| deducao_csll_retida_por_esados_municipio | `valor_deducao_estado_municipio` | numeric(13) |  |  | Dedução - CSLL retida por Esados, Municípios |
| deducao_csll_retida_pela_administracao_p | `valor_deducao_administracao_publica` | numeric(13) |  |  | Dedução - CSLL retida pela Administração Pública |
| deducao_outras_deducoes | `valor_deducao_outra_deducao` | numeric(13) |  |  | Dedução - Outras Deduções |
| bonus_por_adimplencia | `valor_bonus_adimplencia` | numeric(13) |  |  | Bônus por adimplência |
| csll_diferido_do_periodo_anterior | `valor_diferido_periodo_anterior` | numeric(13) |  |  | CSLL diferido do período anterior |
| csll_diferido_do_periodo | `valor_diferido_periodo` | numeric(13) |  |  | CSLL diferido do período |
| csll_a_recolher | `valor_a_recolher` | numeric(13) |  |  | CSLL a recolher |
| valor_a_compensar_para_o_periodo_seguint | `valor_compensar_periodo_seguinte` | numeric(13) |  |  | Valor a compensar para o período seguinte |
| valor_compensar_periodo_seguinte_geral | `valor_compensar_periodo_seguinte_geral` | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral |
| valor_compensar_periodo_seguinte_rural | `valor_compensar_periodo_seguinte_rural` | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| valor_a_deduzir_para_o_periodo_seguinte | `valor_deduzir_periodo_seguinte` | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| deducao_pago_no_exterior_sobre_lucros_re | `valor_deducao_pago_exterior` | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| deducao_recuperacao_de_credito_de_csll | `valor_deducao_recuperacao_credito` | numeric(13) |  |  | Dedução - Recuperação de crédito de CSLL |
| deducao_creditos_sobre_depreciacao_de_im | `valor_deducao_credito_depreciacao_imobilizado` | numeric(13) |  |  | Dedução - Créditos sobre depreciação de imobilizado |
| aliquota_do_csll | `valor_aliquota_csll` | numeric(5) |  |  | Alíquota do CSLL |
| compensacao_de_impostos_federais_de_peri | `valor_deducao_compensacao_imposto_federal_periodo_anterior` | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| saldo_de_deducoes_do_periodo_anterior | `valor_deducao_saldo_periodo_anterior` | numeric(13) |  |  | Saldo de deduções do período anterior |
| adicional_proporcionalidade_csll | `valor_adicional_proporcionalidade_csll` | numeric(13) |  |  | Adicional proporcionalidade CSLL |
| valor_de_base_de_calculo_de_juros_multa | `valor_base_calculo_juros_multa_outro` | numeric(13) |  |  | Valor de base de calculo de juros, multa e outros |
| valor_deducao_perse_pgsc | `valor_deducao_perse_pgsc` | decimal(13) |  |  | Lei Perse e PGSC - Lei 14.148/21 |
| campo_criado_internamento_para_guardar_o | `valor_imposto_devido_mes_antes_retencoes_pagamentos` | decimal(13) |  |  | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |

**Filtros:** `codigo_do_calculo` (eq/in)

## lrcalculo_irpj_estimado

**Cálculo do Lalur - Imposto IRPJ Estimado** — tabela `LRCALCULO_IRPJ_ESTIMADO` (1.278 linhas)

Cálculo do Lalur - Imposto IRPJ Estimado. 1.278 linhas no catálogo; chave: CODI_EMP, I_CALCULO.

- **Chave:** `CODI_EMP, I_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.278 linhas, 43 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| base_de_calculo_das_vendas | `valor_base_calculo_venda` | numeric(13) |  |  | Base de cálculo das vendas |
| base_de_calculo_dos_servicos | `valor_base_calculo_servico` | numeric(13) |  |  | Base de cálculo dos serviços |
| base_de_calculo_do_valor_nao_operacional | `valor_base_calculo_nao_operacional` | numeric(13) |  |  | Base de cálculo do valor não operacional |
| total_da_base_de_calculo | `valor_base_calculo` | numeric(13) |  |  | Total da base de cálculo |
| irpj_devido | `valor_irpj_devido` | numeric(13) |  |  | IRPJ devido |
| adicional_de_irpj | `valor_adicional` | numeric(13) |  |  | Adicional de IRPJ |
| deducoes | `valor_deducao` | numeric(13) |  |  | Deduções |
| deducao_ir_pago_em_meses_anteriores | `valor_deducao_pago_em_mes_anterior` | numeric(13) |  |  | Dedução - IR pago em meses anteriores |
| deducao_irrf | `valor_deducao_irrf` | numeric(13) |  |  | Dedução - IRRF |
| deducao_irrf_por_orgaos_publicos_federai | `valor_deducao_orgao_publico_federal` | numeric(13) |  |  | Dedução - IRRF por Órgãos Públicos Federais |
| deducao_irrf_administracao_publica | `valor_deducao_administracao_publica` | numeric(13) |  |  | Dedução - IRRF Administração Pública |
| deducao_outras_deducoes | `valor_deducao_outra_deducao` | numeric(13) |  |  | Dedução - Outras Deduções |
| incentivos_fiscais | `valor_incentivo_fiscal` | numeric(13) |  |  | Incentivos Fiscais |
| irpj_diferido_do_periodo_anterior | `valor_diferido_periodo_anterior` | numeric(13) |  |  | IRPJ diferido do período anterior |
| irpj_diferido_do_periodo | `valor_diferido_periodo` | numeric(13) |  |  | IRPJ diferido do período |
| irpj_a_recolher | `valor_a_recolher` | numeric(13) |  |  | IRPJ a recolher |
| valor_a_compensar_para_o_periodo_seguint | `valor_compensar_periodo_seguinte` | numeric(13) |  |  | Valor a compensar para o período seguinte |
| valor_compensar_periodo_seguinte_geral_o | `valor_compensar_periodo_seguinte_geral_op` | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Operacional |
| valor_compensar_periodo_seguinte_geral_n | `valor_compensar_periodo_seguinte_geral_nao_op` | numeric(13) |  |  | Valor a compensar para o período seguinte - Geral - Não Operacional |
| valor_compensar_periodo_seguinte_rural | `valor_compensar_periodo_seguinte_rural` | numeric(13) |  |  | Valor a compensar para o período seguinte - Rural |
| valor_a_deduzir_para_o_periodo_seguinte | `valor_deduzir_periodo_seguinte` | numeric(13) |  |  | Valor a deduzir para o período seguinte |
| valor_nao_operacional_transferido | `valor_nao_operacional_transferido` | numeric(13) |  |  | Valor não operacional transferido |
| deducao_pago_no_exterior_sobre_lucros_re | `valor_deducao_pago_exterior` | numeric(13) |  |  | Dedução - Pago no exterior sobre lucros, rendimentos e ganhos de capital |
| deducao_pago_incidente_sobre_ganhos_no_m | `valor_deducao_pago_incidente_sobre_ganhos` | numeric(13) |  |  | Dedução - Pago incidente sobre ganhos no mercado de renda variável |
| compensacao_de_impostos_federais_de_peri | `valor_deducao_compensacao_imposto_federal_periodo_anterior` | numeric(13) |  |  | Compensação de impostos federais de períodos anteriores |
| saldo_de_deducoes_do_periodo_anterior | `valor_deducao_saldo_periodo_anterior` | numeric(13) |  |  | Saldo de deduções do período anterior |
| valor_de_base_de_calculo_de_juros_multa | `valor_base_calculo_juros_multa_outro` | numeric(13) |  |  | Valor de base de calculo de juros, multa e outros |
| valor_deducao_perse_pgsc | `valor_deducao_perse_pgsc` | decimal(13) |  |  | Lei Perse e PGSC - Lei 14.148/21 |
| campo_criado_internamento_para_guardar_o | `valor_imposto_devido_mes_antes_retencoes_pagamentos` | decimal(13) |  |  | Campo criado internamento para guardar o valor e apresentar no calculo quando o tipo do calculo for Anual/Balanço de Redução e Suspensão |

**Filtros:** `codigo_do_calculo` (eq/in)

## lrcalculo_irpj_real_adicao

**Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Adições** — tabela `LRCALCULO_IRPJ_REAL_ADICAO` (815 linhas)

Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Adições. 815 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_ADICAO, AJUSTE_ANUAL.

- **Chave:** `CODI_EMP, I_CALCULO, I_ADICAO, AJUSTE_ANUAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_ADICAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 815 linhas, 59 empresa(s).
- Vínculo lradicao (LRADICAO): 0 de 10 linhas sem registro relacionado (empresa 1555).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| adicao | `i_adicao` | integer(4) |  |  | Adição |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_geral | `valor_geral` | numeric(13) |  |  | Valor - Geral |
| valor_rural | `valor_rural` | numeric(13) |  |  | Valor - Rural |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lradicao` → `LRADICAO` por `codi_emp` = `codi_emp` e `i_adicao` = `i_adicao`; colunas: `lradicao_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `adicao` (eq/in), `ajuste_anual` (eq/in)

## lrcalculo_irpj_estimado_operacao_receita

**Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Vendas, Serviços e Não Operacional** — tabela `LRCALCULO_IRPJ_ESTIMADO_OPERACAO_RECEITA` (722 linhas)

Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Vendas, Serviços e Não Operacional. 722 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_OPERACAO_RECEITA.

- **Chave:** `CODI_EMP, I_CALCULO, I_OPERACAO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_OPERACAO_RECEITA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 722 linhas, 23 empresa(s).
- Vínculo lroperacao_receita (LROPERACAO_RECEITA): 0 de 24 linhas sem registro relacionado (empresa 1507).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| operacao_de_receita_vendas_servicos_ou_n | `i_operacao_receita` | integer(4) |  |  | Operação de receita (vendas, serviços ou não operacional) |
| receita_bruta | `valor_receita` | numeric(13) |  |  | Receita Bruta |
| aliquota | `aliquota` | numeric(13) |  |  | Alíquota |
| base_de_calculo | `valor_base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_de_juros_multa_e_outros | `valor_juros_multa_outra` | numeric(13) |  |  | Valor de juros, multa e outros |
| aliquota_de_juros_multa_e_outros | `aliquota_juros_multa_outra` | numeric(5) |  |  | Aliquota de juros, multa e outros |
| base_de_calculo_de_juros_multa_e_outros | `base_calculo_juros_multa_outra` | numeric(13) |  |  | Base de calculo de juros, multa e outros |
| receita | `receita` | numeric(13) |  |  | Receita |
| deducao | `deducao` | numeric(13) |  |  | Dedução |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lroperacao_receita` → `LROPERACAO_RECEITA` por `codi_emp` = `codi_emp` e `i_operacao_receita` = `i_operacao_receita`; colunas: `lroperacao_receita_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `operacao_de_receita_vendas_servicos_ou_n` (eq/in)

## lrcalculo_csll_estimado_operacao_receita

**Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Vendas e Serviços** — tabela `LRCALCULO_CSLL_ESTIMADO_OPERACAO_RECEITA` (713 linhas)

Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Vendas e Serviços. 713 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_OPERACAO_RECEITA.

- **Chave:** `CODI_EMP, I_CALCULO, I_OPERACAO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_OPERACAO_RECEITA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 713 linhas, 23 empresa(s).
- Vínculo lroperacao_receita (LROPERACAO_RECEITA): 0 de 24 linhas sem registro relacionado (empresa 1507).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| operacao_de_receita_vendas_ou_servicos | `i_operacao_receita` | integer(4) |  |  | Operação de receita (vendas ou serviços) |
| receita_bruta | `valor_receita` | numeric(13) |  |  | Receita Bruta |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| base_de_calculo | `valor_base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_de_juros_multa_e_outros | `valor_juros_multa_outra` | numeric(13) |  |  | Valor de juros, multa e outros |
| aliquota_de_juros_multa_e_outros | `aliquota_juros_multa_outra` | numeric(5) |  |  | Aliquota de juros, multa e outros |
| base_de_calculo_de_juros_multa_e_outros | `base_calculo_juros_multa_outra` | numeric(13) |  |  | Base de calculo de juros, multa e outros |
| receita | `receita` | numeric(13) |  |  | Receita |
| deducao | `deducao` | numeric(13) |  |  | Dedução |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lroperacao_receita` → `LROPERACAO_RECEITA` por `codi_emp` = `codi_emp` e `i_operacao_receita` = `i_operacao_receita`; colunas: `lroperacao_receita_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `operacao_de_receita_vendas_ou_servicos` (eq/in)

## lrcalculo_csll_real_adicao

**Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Adições** — tabela `LRCALCULO_CSLL_REAL_ADICAO` (545 linhas)

Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Adições. 545 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_ADICAO, AJUSTE_ANUAL.

- **Chave:** `CODI_EMP, I_CALCULO, I_ADICAO, AJUSTE_ANUAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_ADICAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 545 linhas, 45 empresa(s).
- Vínculo lradicao (LRADICAO): 0 de 11 linhas sem registro relacionado (empresa 1014).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| adicao | `i_adicao` | integer(4) |  |  | Adição |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_geral | `valor_geral` | numeric(13) |  |  | Valor - Geral |
| valor_rural | `valor_rural` | numeric(13) |  |  | Valor - Rural |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lradicao` → `LRADICAO` por `codi_emp` = `codi_emp` e `i_adicao` = `i_adicao`; colunas: `lradicao_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `adicao` (eq/in), `ajuste_anual` (eq/in)

## lrcalculo_irpj_real_deducao

**Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Deduções** — tabela `LRCALCULO_IRPJ_REAL_DEDUCAO` (283 linhas)

Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Deduções. 283 linhas no catálogo; chave: CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_IRPJ_REAL_DEDUCAO.

- **Chave:** `CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_IRPJ_REAL_DEDUCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `AJUSTE_ANUAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 283 linhas, 22 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| deducao | `i_irpj_real_deducao` | integer(4) |  |  | Dedução |
| valor_irrf | `valor_irrf` | numeric(13) |  |  | Valor IRRF |
| valor_irrf_por_orgaos_publicos_federais | `valor_irrf_orgao_publico_federal` | numeric(13) |  |  | Valor IRRF por Órgãos Públicos Federais |
| valor_irrf_administracao_publica | `valor_irrf_administracao_publica` | numeric(13) |  |  | Valor IRRF Administração Pública |

**Filtros:** `codigo_do_calculo` (eq/in), `ajuste_anual` (eq/in), `deducao` (eq/in)

## lrcalculo_irpj_incentivo_fiscal

**Cálculo do Lalur - Imposto IRPJ - Detalhamento de Incentivos Fiscais** — tabela `LRCALCULO_IRPJ_INCENTIVO_FISCAL` (212 linhas)

Cálculo do Lalur - Imposto IRPJ - Detalhamento de Incentivos Fiscais. 212 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_IRPJ_INCENTIVO_FISCAL, AJUSTE_ANUAL.

- **Chave:** `CODI_EMP, I_CALCULO, I_IRPJ_INCENTIVO_FISCAL, AJUSTE_ANUAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_IRPJ_INCENTIVO_FISCAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 212 linhas, 7 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| codigo_do_movimento_do_incentivo_fiscal | `i_irpj_incentivo_fiscal` | integer(4) |  |  | Código do movimento do Incentivo Fiscal |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| valor_aproveitado_real | `valor_real` | numeric(13) |  |  | Valor aproveitado - Real |
| valor_aproveitado_estiamdo | `valor_estimado` | numeric(13) |  |  | Valor aproveitado - Estiamdo |
| valor_real_do_incentivo_fiscal_antes_da | `valor_antes_lc224_real` | numeric(13) |  |  | Valor real do incentivo fiscal antes da redução LC 224/25 (sem fator 0,90) |
| valor_estimado_do_incentivo_fiscal_antes | `valor_antes_lc224_estimado` | numeric(13) |  |  | Valor estimado do incentivo fiscal antes da redução LC 224/25 (sem fator 0,90) |

**Filtros:** `codigo_do_calculo` (eq/in), `codigo_do_movimento_do_incentivo_fiscal` (eq/in), `ajuste_anual` (eq/in)

## lrcalculo_irpj_estimado_deducao

**Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Deduções** — tabela `LRCALCULO_IRPJ_ESTIMADO_DEDUCAO` (200 linhas)

Cálculo do Lalur - Imposto IRPJ Estimado - Detalhamento de Deduções. 200 linhas no catálogo; chave: CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_IRPJ_ESTIMADO_DEDUCAO.

- **Chave:** `CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_IRPJ_ESTIMADO_DEDUCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `AJUSTE_ANUAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 200 linhas, 13 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| deducao | `i_irpj_estimado_deducao` | integer(4) |  |  | Dedução |
| valor_irrf | `valor_irrf` | numeric(13) |  |  | Valor IRRF |
| valor_irrf_por_orgaos_publicos_federais | `valor_irrf_orgao_publico_federal` | numeric(13) |  |  | Valor IRRF por Órgãos Públicos Federais |
| valor_irrf_administracao_publica | `valor_irrf_administracao_publica` | numeric(13) |  |  | Valor IRRF Administração Pública |

**Filtros:** `codigo_do_calculo` (eq/in), `ajuste_anual` (eq/in), `deducao` (eq/in)

## lrcalculo_csll_real_exclusao

**Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Exclusões** — tabela `LRCALCULO_CSLL_REAL_EXCLUSAO` (148 linhas)

Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Exclusões. 148 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_EXCLUSAO, AJUSTE_ANUAL.

- **Chave:** `CODI_EMP, I_CALCULO, I_EXCLUSAO, AJUSTE_ANUAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_EXCLUSAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 148 linhas, 8 empresa(s).
- Vínculo lrexclusao (LREXCLUSAO): 0 de 13 linhas sem registro relacionado (empresa 1222).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| exclusao | `i_exclusao` | integer(4) |  |  | Exclusão |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_geral | `valor_geral` | numeric(13) |  |  | Valor - Geral |
| valor_rural | `valor_rural` | numeric(13) |  |  | Valor - Rural |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lrexclusao` → `LREXCLUSAO` por `codi_emp` = `codi_emp` e `i_exclusao` = `i_exclusao`; colunas: `lrexclusao_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `exclusao` (eq/in), `ajuste_anual` (eq/in)

## lrcalculo_irpj_real_exclusao

**Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Exclusões** — tabela `LRCALCULO_IRPJ_REAL_EXCLUSAO` (148 linhas)

Cálculo do Lalur - Imposto IRPJ Real - Detalhamento de Exclusões. 148 linhas no catálogo; chave: CODI_EMP, I_CALCULO, I_EXCLUSAO, AJUSTE_ANUAL.

- **Chave:** `CODI_EMP, I_CALCULO, I_EXCLUSAO, AJUSTE_ANUAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `I_EXCLUSAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 148 linhas, 8 empresa(s).
- Vínculo lrexclusao (LREXCLUSAO): 0 de 13 linhas sem registro relacionado (empresa 1222).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| exclusao | `i_exclusao` | integer(4) |  |  | Exclusão |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_geral | `valor_geral` | numeric(13) |  |  | Valor - Geral |
| valor_rural | `valor_rural` | numeric(13) |  |  | Valor - Rural |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `lrexclusao` → `LREXCLUSAO` por `codi_emp` = `codi_emp` e `i_exclusao` = `i_exclusao`; colunas: `lrexclusao_nome`

**Filtros:** `codigo_do_calculo` (eq/in), `exclusao` (eq/in), `ajuste_anual` (eq/in)

## lrcalculo_csll_real_deducao

**Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Deduções** — tabela `LRCALCULO_CSLL_REAL_DEDUCAO` (105 linhas)

Cálculo do Lalur - Imposto CSLL Real - Detalhamento de Deduções. 105 linhas no catálogo; chave: CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_CSLL_REAL_DEDUCAO.

- **Chave:** `CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_CSLL_REAL_DEDUCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `AJUSTE_ANUAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 105 linhas, 8 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| deducao | `i_csll_real_deducao` | integer(4) |  |  | Dedução |
| valor_csll_orgaos_publicos_federais | `valor_orgao_publico_federal` | numeric(13) |  |  | Valor CSLL Órgãos Públicos Federais |
| valor_csll_outras_pessoas_juridicas | `valor_outra_pessoa_juridica` | numeric(13) |  |  | Valor CSLL Outras Pessoas Jurídicas |
| valor_csll_estados_e_municipios | `valor_estado_municipio` | numeric(13) |  |  | Valor CSLL Estados e Municípios |
| valor_csll_administracao_publica | `valor_administracao_publica` | numeric(13) |  |  | Valor CSLL Administração Pública |

**Filtros:** `codigo_do_calculo` (eq/in), `ajuste_anual` (eq/in), `deducao` (eq/in)

## lrcalculo_csll_estimado_deducao

**Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Deduções** — tabela `LRCALCULO_CSLL_ESTIMADO_DEDUCAO` (93 linhas)

Cálculo do Lalur - Imposto CSLL Estimado - Detalhamento de Deduções. 93 linhas no catálogo; chave: CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_CSLL_ESTIMADO_DEDUCAO.

- **Chave:** `CODI_EMP, I_CALCULO, AJUSTE_ANUAL, I_CSLL_ESTIMADO_DEDUCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULO asc`, `AJUSTE_ANUAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 93 linhas, 6 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_calculo | `i_calculo` | integer(4) |  |  | Código do cálculo |
| ajuste_anual | `ajuste_anual` | integer(4) |  |  | Ajuste Anual |
| deducao | `i_csll_estimado_deducao` | integer(4) |  |  | Dedução |
| valor_csll_orgaos_publicos_federais | `valor_orgao_publico_federal` | numeric(13) |  |  | Valor CSLL Órgãos Públicos Federais |
| valor_csll_outras_pessoas_juridicas | `valor_outra_pessoa_juridica` | numeric(13) |  |  | Valor CSLL Outras Pessoas Jurídicas |
| valor_csll_estados_e_municipios | `valor_estado_municipio` | numeric(13) |  |  | Valor CSLL Estados e Municípios |
| valor_csll_administracao_publica | `valor_administracao_publica` | numeric(13) |  |  | Valor CSLL Administração Pública |

**Filtros:** `codigo_do_calculo` (eq/in), `ajuste_anual` (eq/in), `deducao` (eq/in)

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

