# Modelo — Fiscal - simulacao (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_simulacao.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

10 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efsimulacao_reforma_tributaria_cfop_sem_credito](#efsimulacao_reforma_tributaria_cfop_sem_credito) | `EFSIMULACAO_REFORMA_TRIBUTARIA_CFOP_SEM_CREDITO` | 146.940 | medio | empresa |
| [efsimulacao_reforma_tributaria_impostos](#efsimulacao_reforma_tributaria_impostos) | `EFSIMULACAO_REFORMA_TRIBUTARIA_IMPOSTOS` | 131 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_ano_iva](#efsimulacao_reforma_tributaria_ano_iva) | `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA` | 128 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_base_por_acumulador](#efsimulacao_reforma_tributaria_base_por_acumulador) | `EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_ACUMULADOR` | 121 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_ano_impostos](#efsimulacao_reforma_tributaria_ano_impostos) | `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IMPOSTOS` | 118 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_base_por_regime_fornecedor](#efsimulacao_reforma_tributaria_base_por_regime_fornecedor) | `EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_REGIME_FORNECEDOR` | 111 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_ano](#efsimulacao_reforma_tributaria_ano) | `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO` | 76 | pequeno | empresa |
| [efsimulacao_reforma_tributaria](#efsimulacao_reforma_tributaria) | `EFSIMULACAO_REFORMA_TRIBUTARIA` | 38 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_ano_iva_simples](#efsimulacao_reforma_tributaria_ano_iva_simples) | `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA_SIMPLES` | 14 | pequeno | empresa |
| [efsimulacao_reforma_tributaria_impostos_simples_nacional](#efsimulacao_reforma_tributaria_impostos_simples_nacional) | `EFSIMULACAO_REFORMA_TRIBUTARIA_IMPOSTOS_SIMPLES_NACIONAL` | 7 | pequeno | empresa |

## efsimulacao_reforma_tributaria_cfop_sem_credito

**Simulador Reforma Tributária - Configuração CFOP** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_CFOP_SEM_CREDITO` (146.940 linhas)

Simulador Reforma Tributária - Configuração CFOP. 146.940 linhas no catálogo; chave: CODI_EMP, I_CONFIGURACAO_CFOP.

- **Chave:** `CODI_EMP, I_CONFIGURACAO_CFOP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONFIGURACAO_CFOP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 146.940 linhas, 1.860 empresa(s).
- Vínculo geempre (geempre): 0 de 79 linhas sem registro relacionado (empresa 117).
- Vínculo efnatureza (efnatureza): 0 de 79 linhas sem registro relacionado (empresa 117).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_configuracao_cfop | `i_configuracao_cfop` | integer(4) |  |  | Sequencial configuração CFOP |
| cfop | `codi_nat` | integer(4) |  |  | CFOP |
| versao_do_cfop | `versao_nat` | smallint(2) |  |  | Versão do CFOP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efnatureza` → `efnatureza` por `codi_nat` = `codi_nat` e `versao_nat` = `versao_nat`; colunas: `efnatureza_nome`

**Filtros:** `sequencial_configuracao_cfop` (eq/in), `cfop` (eq/in)

## efsimulacao_reforma_tributaria_impostos

**Simulador Reforma Tributaria - Impostos Apuracao** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_IMPOSTOS` (131 linhas)

Simulador Reforma Tributaria - Impostos Apuracao. 131 linhas no catálogo; chave: CODI_EMP, PERIODO, CODI_IMP.

- **Chave:** `CODI_EMP, PERIODO, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 131 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.
- Vínculo geimposto (geimposto): 0 de 10 linhas sem registro relacionado (empresa 317).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| codigo_imposto | `codi_imp` | integer(4) |  |  | Codigo Imposto |
| competencia_da_tributacao_f_federal_e_es | `competencia_tributacao` | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal) |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |
| valor_do_imposto_retido | `valor_imposto_retido` | numeric(13) |  |  | Valor do Imposto Retido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geimposto` → `geimposto` por `codi_emp` = `codi_emp` e `codi_imp` = `codi_imp`; colunas: `geimposto_nome`

**Filtros:** `periodo_competencia` (eq/in), `codigo_imposto` (eq/in), `competencia_da_tributacao_f_federal_e_es` (eq/in)

## efsimulacao_reforma_tributaria_ano_iva

**Simulador Reforma Tributaria - Impostos IVA** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA` (128 linhas)

Simulador Reforma Tributaria - Impostos IVA. 128 linhas no catálogo; chave: CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IVA, REDUCAO_ALIQUOTA, REDUCAO_ALIQUOTA_AGRUPADOR.

- **Chave:** `CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IVA, REDUCAO_ALIQUOTA, REDUCAO_ALIQUOTA_AGRUPADOR`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REFORMA_TRIBUTARIA_ANO asc`, `CODI_IVA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 128 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| reforma_tributaria_conforme_ano | `reforma_tributaria_ano` | integer(4) |  |  | Reforma tributaria conforme ano |
| codigo_imposto_iva | `codi_iva` | integer(4) |  |  | Codigo imposto IVA |
| reducao_aliquota | `reducao_aliquota` | numeric(5) |  |  | Reducao Aliquota |
| agrupador_de_reducao_de_aliquota | `reducao_aliquota_agrupador` | char(15) |  |  | Agrupador de redução de aliquota |
| competencia_da_tributacao_f_federal_e_es | `competencia_tributacao` | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal) |
| base_de_credito_pelas_entradas | `base_credito_entradas` | numeric(13) |  |  | Base de credito pelas entradas |
| base_de_debito_pelas_saidas | `base_debito_saidas` | numeric(13) |  |  | Base de debito pelas saidas |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor_de_credito_pelas_entradas | `credito_entradas` | numeric(13) |  |  | Valor de credito pelas entradas |
| valor_de_debito_pelas_saidas | `debito_saidas` | numeric(13) |  |  | Valor de debito pelas saidas |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |
| base_de_debito_pelas_entradas | `base_debito_entradas` | numeric(13) |  |  | Base de debito pelas entradas |
| valor_de_debito_pelas_entradas | `debito_entradas` | numeric(13) |  |  | Valor de debito pelas entradas |

**Filtros:** `periodo_competencia` (eq/in), `reforma_tributaria_conforme_ano` (eq/in), `codigo_imposto_iva` (eq/in), `reducao_aliquota` (eq/in), `agrupador_de_reducao_de_aliquota` (eq/in), `competencia_da_tributacao_f_federal_e_es` (eq/in)

## efsimulacao_reforma_tributaria_base_por_acumulador

**Simulador Reforma Tributaria - Base por Acumulador** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_ACUMULADOR` (121 linhas)

Simulador Reforma Tributaria - Base por Acumulador. 121 linhas no catálogo; chave: CODI_EMP, PERIODO, FILIAL, CODI_ACU, TIPO_MOVIMENTO.

- **Chave:** `CODI_EMP, PERIODO, FILIAL, CODI_ACU, TIPO_MOVIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `FILIAL asc`, `CODI_ACU asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 121 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.
- tipo_movimento_ce_credito_entrada_de_deb: todos os valores reais estão no comentário do banco (CE=63, DS=57, DE=1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| filial | `filial` | integer(4) |  |  | Filial |
| codigo_acumulador | `codi_acu` | integer(4) |  |  | Codigo Acumulador |
| tipo_movimento_ce_credito_entrada_de_deb | `tipo_movimento` | char(2) |  | efsimulacao_reforma_tributaria_base_por_acumulador_tipo_movimen | TIPO MOVIMENTO (CE - CREDITO ENTRADA / DE - DEBITO ENTRADA / DS - DEBITO SAIDA) |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contabil |
| valor_icms | `valor_icms` | numeric(13) |  |  | Valor ICMS |
| valor_difal | `valor_difal` | numeric(13) |  |  | Valor DIFAL |
| valor_icms_st | `valor_icms_st` | numeric(13) |  |  | Valor ICMS ST |
| valor_iss | `valor_iss` | numeric(13) |  |  | Valor ISS |
| valor_pis | `valor_pis` | numeric(13) |  |  | Valor PIS |
| valor_cofins | `valor_cofins` | numeric(13) |  |  | Valor COFINS |
| valor_liquido | `valor_liquido` | numeric(13) |  |  | Valor Liquido |
| valor_liquido_2027 | `valor_liquido_2027` | numeric(13) |  |  | Valor Liquido base para 2027 |
| valor_liquido_2033 | `valor_liquido_2033` | numeric(13) |  |  | Valor Liquido base para 2033 |

**Filtros:** `periodo_competencia` (eq/in), `filial` (eq/in), `codigo_acumulador` (eq/in), `tipo_movimento_ce_credito_entrada_de_deb` (eq/in)

## efsimulacao_reforma_tributaria_ano_impostos

**Simulador Reforma Tributaria - Impostos nova tributacao** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IMPOSTOS` (118 linhas)

Simulador Reforma Tributaria - Impostos nova tributacao. 118 linhas no catálogo; chave: CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IMP.

- **Chave:** `CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REFORMA_TRIBUTARIA_ANO asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 118 linhas, 4 empresa(s), PERIODO de 2024-01-01 a 2025-08-01.
- Vínculo geimposto (geimposto): 0 de 32 linhas sem registro relacionado (empresa 236).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| reforma_tributaria_conforme_ano | `reforma_tributaria_ano` | integer(4) |  |  | Reforma tributaria conforme ano |
| codigo_imposto | `codi_imp` | integer(4) |  |  | Codigo imposto |
| competencia_da_tributacao_f_federal_e_es | `competencia_tributacao` | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal) |
| valor_do_imposto | `valor_imposto` | numeric(13) |  |  | Valor do Imposto |
| valor_do_imposto_retido | `valor_imposto_retido` | numeric(13) |  |  | Valor do Imposto Retido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geimposto` → `geimposto` por `codi_emp` = `codi_emp` e `codi_imp` = `codi_imp`; colunas: `geimposto_nome`

**Filtros:** `periodo_competencia` (eq/in), `reforma_tributaria_conforme_ano` (eq/in), `codigo_imposto` (eq/in), `competencia_da_tributacao_f_federal_e_es` (eq/in)

## efsimulacao_reforma_tributaria_base_por_regime_fornecedor

**Simulador Reforma Tributaria - Base por Regime de Fornecedor/Cliente** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_REGIME_FORNECEDOR` (111 linhas)

Simulador Reforma Tributaria - Base por Regime de Fornecedor/Cliente. 111 linhas no catálogo; chave: CODI_EMP, PERIODO, FILIAL, CLI_FOR, TIPO_REGIME, TIPO_MOVIMENTO.

- **Chave:** `CODI_EMP, PERIODO, FILIAL, CLI_FOR, TIPO_REGIME, TIPO_MOVIMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `FILIAL asc`, `CLI_FOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 111 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.
- tipo_movimento_ce_credito_entrada_ds_deb: todos os valores reais estão no comentário do banco (DS=58, CE=53).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| filial | `filial` | integer(4) |  |  | Filial |
| cliente_ou_fornecedor | `cli_for` | char(1) |  |  | Cliente ou Fornecedor |
| regime_fornecedor | `tipo_regime` | char(1) |  |  | Regime Fornecedor |
| tipo_movimento_ce_credito_entrada_ds_deb | `tipo_movimento` | char(2) |  | efsimulacao_reforma_tributaria_base_por_regime_fornecedor_tipo_movimen | Tipo Movimento (CE - Credito Entrada / DS - Debito Saida) |
| valor_contabil | `valor_contabil` | numeric(13) |  |  | Valor contabil |
| percentual_representacao | `percentual` | numeric(5) |  |  | Percentual representacao |

**Filtros:** `periodo_competencia` (eq/in), `filial` (eq/in), `cliente_ou_fornecedor` (eq/in), `regime_fornecedor` (eq/in), `tipo_movimento_ce_credito_entrada_ds_deb` (eq/in)

## efsimulacao_reforma_tributaria_ano

**Simulador Reforma Tributaria** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO` (76 linhas)

Simulador Reforma Tributaria. 76 linhas no catálogo; chave: CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO.

- **Chave:** `CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REFORMA_TRIBUTARIA_ANO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 76 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| reforma_tributaria_conforme_ano | `reforma_tributaria_ano` | integer(4) |  |  | Reforma tributaria conforme ano |
| valor_tributos_atuais | `tributos_atuais` | numeric(13) |  |  | Valor tributos atuais |
| valor_tributos_apos_reforma | `tributos_apos_reforma` | numeric(13) |  |  | Valor tributos apos reforma |
| diferenca_apos_reforma_tributaria | `diferenca_apos_reforma` | numeric(13) |  |  | Diferenca apos reforma tributaria |
| diferenca_apos_reforma_tributaria_percen | `diferenca_apos_reforma_percentual` | numeric(13) |  |  | Diferenca apos reforma tributaria - Percentual |

**Filtros:** `periodo_competencia` (eq/in), `reforma_tributaria_conforme_ano` (eq/in)

## efsimulacao_reforma_tributaria

**Simulador Reforma Tributaria** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA` (38 linhas)

Simulador Reforma Tributaria. 38 linhas no catálogo; chave: CODI_EMP, PERIODO.

- **Chave:** `CODI_EMP, PERIODO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 38 linhas, 6 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.
- Vínculo geempre (geempre): 0 de 5 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| tipo_calculo_simples_normal | `tipo_calculo` | char(1) |  |  | Tipo Calculo (Simples/Normal) |
| aliquota_cbs | `aliquota_cbs` | numeric(5) |  |  | Alíquota CBS |
| aliquota_ibs | `aliquota_ibs` | numeric(5) |  |  | Alíquota IBS |
| base_calculo_iva | `base_calculo_iva` | char(1) |  |  | Base calculo IVA |
| reducao_aliquota | `reducao_aliquota` | numeric(5) |  |  | Reducao aliquota |
| calcular_credito_de_iva_para_fornecedor | `calcular_credito_fornecedor_simples` | char(1) |  |  | Calcular credito de IVA para fornecedor simples nacional |
| forma_calculo | `forma_calculo` | integer(4) |  |  | FORMA_CALCULO IN (1, 2) |
| produtos_com_reducao_de_aliquota | `produtos_reducao_aliquota` | char(1) |  |  | Produtos com redução de alíquota |
| considerar_os_impostos_retidos_a_compens | `considera_impostos_retidos_compensar` | char(1) |  |  | Considerar os impostos retidos a compensar |
| atividade_com_reducao_de_aliquota | `atividade_reducao_aliquota` | char(1) |  |  | Atividade com redução de aliquota |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `periodo_competencia` (eq/in), `tipo_calculo_simples_normal` (eq/in), `base_calculo_iva` (eq/in), `calcular_credito_de_iva_para_fornecedor` (eq/in), `produtos_com_reducao_de_aliquota` (eq/in), `considerar_os_impostos_retidos_a_compens` (eq/in), `atividade_com_reducao_de_aliquota` (eq/in)

## efsimulacao_reforma_tributaria_ano_iva_simples

**Simulador Reforma Tributaria - IVA Detalhamento Simples Nacional** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_ANO_IVA_SIMPLES` (14 linhas)

Simulador Reforma Tributaria - IVA Detalhamento Simples Nacional. 14 linhas no catálogo; chave: CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IVA.

- **Chave:** `CODI_EMP, PERIODO, REFORMA_TRIBUTARIA_ANO, CODI_IVA`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REFORMA_TRIBUTARIA_ANO asc`, `CODI_IVA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14 linhas, 3 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| reforma_tributaria_conforme_ano | `reforma_tributaria_ano` | integer(4) |  |  | Reforma tributaria conforme ano |
| codigo_imposto_iva | `codi_iva` | integer(4) |  |  | Codigo imposto IVA |
| valor_irpj | `valor_irpj` | numeric(13) |  |  | Valor IRPJ |
| valor_csll | `valor_csll` | numeric(13) |  |  | Valor CSLL |
| valor_inss | `valor_inss` | numeric(13) |  |  | Valor INSS |
| valor_ipi | `valor_ipi` | numeric(13) |  |  | Valor IPI |
| valor_icms | `valor_icms` | numeric(13) |  |  | Valor ICMS |
| valor_iss | `valor_iss` | numeric(13) |  |  | Valor ISS |

**Filtros:** `periodo_competencia` (eq/in), `reforma_tributaria_conforme_ano` (eq/in), `codigo_imposto_iva` (eq/in)

## efsimulacao_reforma_tributaria_impostos_simples_nacional

**Simulador Reforma Tributaria - Impostos Apuracao** — tabela `EFSIMULACAO_REFORMA_TRIBUTARIA_IMPOSTOS_SIMPLES_NACIONAL` (7 linhas)

Simulador Reforma Tributaria - Impostos Apuracao. 7 linhas no catálogo; chave: CODI_EMP, PERIODO, CODI_IMP.

- **Chave:** `CODI_EMP, PERIODO, CODI_IMP`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 3 empresa(s), PERIODO de 2024-01-01 a 2026-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| periodo_competencia | `periodo` | date(4) |  |  | Periodo - Competencia |
| codigo_imposto | `codi_imp` | integer(4) |  |  | Codigo Imposto |
| valor_irpj | `valor_irpj` | numeric(13) |  |  | Valor IRPJ |
| valor_csll | `valor_csll` | numeric(13) |  |  | Valor CSLL |
| valor_inss | `valor_inss` | numeric(13) |  |  | Valor INSS |
| valor_ipi | `valor_ipi` | numeric(13) |  |  | Valor IPI |
| valor_icms | `valor_icms` | numeric(13) |  |  | Valor ICMS |
| valor_iss | `valor_iss` | numeric(13) |  |  | Valor ISS |
| valor_pis | `valor_pis` | numeric(13) |  |  | Valor PIS |
| valor_cofins | `valor_cofins` | numeric(13) |  |  | Valor COFINS |

**Filtros:** `periodo_competencia` (eq/in), `codigo_imposto` (eq/in)

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

### efsimulacao_reforma_tributaria_base_por_acumulador_tipo_movimen

Confirmado: sim

> Todos os valores observados em EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_ACUMULADOR.TIPO_MOVIMENTO estão no comentário do banco (2026-10-18). Distribuição: CE=63, DS=57, DE=1.

| Código | Significado |
|---|---|
| CE | CREDITO ENTRADA |
| DE | DEBITO ENTRADA |
| DS | DEBITO SAIDA |

### efsimulacao_reforma_tributaria_base_por_regime_fornecedor_tipo_movimen

Confirmado: sim

> Todos os valores observados em EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_REGIME_FORNECEDOR.TIPO_MOVIMENTO estão no comentário do banco (2026-10-18). Distribuição: DS=58, CE=53.

| Código | Significado |
|---|---|
| CE | Credito Entrada |
| DS | Debito Saida |

