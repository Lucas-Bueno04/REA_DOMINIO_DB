# Modelo — Fiscal - planejamento (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_planejamento.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

9 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efplanejamento_tributario_impostos](#efplanejamento_tributario_impostos) | `EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS` | 204 | pequeno | empresa |
| [efplanejamento_tributario_receitas](#efplanejamento_tributario_receitas) | `EFPLANEJAMENTO_TRIBUTARIO_RECEITAS` | 192 | pequeno | empresa |
| [efplanejamento_tributario_receitas_uf](#efplanejamento_tributario_receitas_uf) | `EFPLANEJAMENTO_TRIBUTARIO_RECEITAS_UF` | 150 | pequeno | empresa |
| [efplanejamento_tributario_tabela_simples_faixas](#efplanejamento_tributario_tabela_simples_faixas) | `EFPLANEJAMENTO_TRIBUTARIO_TABELA_SIMPLES_FAIXAS` | 120 | pequeno | — |
| [efplanejamento_tributario_impostos_simples](#efplanejamento_tributario_impostos_simples) | `EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS_SIMPLES` | 40 | pequeno | empresa |
| [efplanejamento_tributario_valor_folha](#efplanejamento_tributario_valor_folha) | `EFPLANEJAMENTO_TRIBUTARIO_VALOR_FOLHA` | 24 | pequeno | empresa |
| [efplanejamento_tributario_valor_despesa](#efplanejamento_tributario_valor_despesa) | `EFPLANEJAMENTO_TRIBUTARIO_VALOR_DESPESA` | 24 | pequeno | empresa |
| [efplanejamento_tributario_tabela_simples](#efplanejamento_tributario_tabela_simples) | `EFPLANEJAMENTO_TRIBUTARIO_TABELA_SIMPLES` | 20 | pequeno | — |
| [efplanejamento_tributario](#efplanejamento_tributario) | `EFPLANEJAMENTO_TRIBUTARIO` | 3 | pequeno | empresa |

## efplanejamento_tributario_impostos

**Planejamento Tributário - Impostos** — tabela `EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS` (204 linhas)

Planejamento Tributário - Impostos. 204 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO, IMPOSTO.

- **Chave:** `CODI_EMP, REGIME, PERIODO, IMPOSTO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`, `IMPOSTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 204 linhas, 1 empresa(s), PERIODO de 2026-01-01 a 2026-12-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P  - Presumido, R - Real, S - Simples) |
| periodo_planejamento | `periodo` | date(4) |  |  | Período planejamento |
| imposto | `imposto` | integer(4) |  |  | Imposto |
| competencia_da_tributacao_f_federal_e_es | `competencia_tributacao` | char(1) |  |  | Competencia da Tributacao (F - Federal, E - Estadual, M - Municipal, O - Folha) |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in), `imposto` (eq/in), `competencia_da_tributacao_f_federal_e_es` (eq/in)

## efplanejamento_tributario_receitas

**Planejamento Tributário - Receitas** — tabela `EFPLANEJAMENTO_TRIBUTARIO_RECEITAS` (192 linhas)

Planejamento Tributário - Receitas. 192 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO, TIPO_RECEITA.

- **Chave:** `CODI_EMP, REGIME, PERIODO, TIPO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`, `TIPO_RECEITA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 192 linhas, 1 empresa(s), PERIODO de 2026-01-01 a 2026-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| periodo_planejamento | `periodo` | date(4) |  |  | Periodo Planejamento |
| tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv | `tipo_receita` | char(3) |  |  | Tipo Receita (RBC, RBS, RBI, CC, CI, ED, DVC, DVI) |
| receita_interna_base | `receita_interna` | numeric(13) |  |  | Receita Interna base |
| receita_externa_base | `receita_externa` | numeric(13) |  |  | Receita Externa base |
| receita_total_base | `receita_total` | numeric(13) |  |  | Receita Total base |
| valor_ipi_interno_base | `valor_ipi_interno` | numeric(13) |  |  | Valor IPI Interno base |
| valor_ipi_externo_base | `valor_ipi_externo` | numeric(13) |  |  | Valor IPI Externo base |
| valor_ipi_total_base | `valor_ipi_total` | numeric(13) |  |  | Valor IPI Total base |
| valor_icms_st_interno_base | `valor_icms_st_interno` | numeric(13) |  |  | Valor ICMS ST Interno base |
| valor_icms_st_externo_base | `valor_icms_st_externo` | numeric(13) |  |  | Valor ICMS ST Externo base |
| valor_icms_st_total_base | `valor_icms_st_total` | numeric(13) |  |  | Valor ICMS ST Total base |
| aumento | `aumento` | numeric(13) |  |  | Aumento |
| reducao | `reducao` | numeric(13) |  |  | Reducao |
| receita_interna_estimativa | `receita_interna_estimativa` | numeric(13) |  |  | Receita Interna estimativa |
| receita_externa_estimativa | `receita_externa_estimativa` | numeric(13) |  |  | Receita Externa estimativa |
| receita_total_estimativa | `receita_total_estimativa` | numeric(13) |  |  | Receita Total estimativa |
| valor_ipi_interno_estimativa | `valor_ipi_interno_estimativa` | numeric(13) |  |  | Valor IPI Interno estimativa |
| valor_ipi_externo_estimativa | `valor_ipi_externo_estimativa` | numeric(13) |  |  | Valor IPI Externo estimativa |
| valor_ipi_total_estimativa | `valor_ipi_total_estimativa` | numeric(13) |  |  | Valor IPI Total estimativa |
| valor_icms_st_interno_estimativa | `valor_icms_st_interno_estimativa` | numeric(13) |  |  | Valor ICMS ST Interno estimativa |
| valor_icms_st_externo_estimativa | `valor_icms_st_externo_estimativa` | numeric(13) |  |  | Valor ICMS ST Externo estimativa |
| valor_icms_st_total_estimativa | `valor_icms_st_total_estimativa` | numeric(13) |  |  | Valor ICMS ST Total estimativa |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in), `tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv` (eq/in)

## efplanejamento_tributario_receitas_uf

**Planejamento Tributário - Receitas por estado** — tabela `EFPLANEJAMENTO_TRIBUTARIO_RECEITAS_UF` (150 linhas)

Planejamento Tributário - Receitas por estado. 150 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO, TIPO_RECEITA, UF_ORIGEM, UF_DESTINO.

- **Chave:** `CODI_EMP, REGIME, PERIODO, TIPO_RECEITA, UF_ORIGEM, UF_DESTINO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`, `TIPO_RECEITA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 150 linhas, 1 empresa(s), PERIODO de 2026-01-01 a 2026-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| periodo_planejamento | `periodo` | date(4) |  |  | Periodo Planejamento |
| tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv | `tipo_receita` | char(3) |  |  | Tipo Receita (RBC, RBS, RBI, CC, CI, ED, DVC, DVI) |
| estado_origem | `uf_origem` | char(2) |  |  | Estado Origem |
| estado_destino | `uf_destino` | char(2) |  |  | Estado Destino |
| receita | `receita` | numeric(13) |  |  | Receita |
| valor_ipi | `valor_ipi` | numeric(13) |  |  | Valor IPI |
| valor_icms_st | `valor_icms_st` | numeric(13) |  |  | Valor ICMS ST |
| aumento | `aumento` | numeric(13) |  |  | Aumento |
| reducao | `reducao` | numeric(13) |  |  | Reducao |
| receita_estimativa | `receita_estimativa` | numeric(13) |  |  | Receita Estimativa |
| valor_ipi_estimativa | `valor_ipi_estimativa` | numeric(13) |  |  | Valor IPI Estimativa |
| valor_icms_st_estimativa | `valor_icms_st_estimativa` | numeric(13) |  |  | Valor ICMS ST Estimativa |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in), `tipo_receita_rbc_rbs_rbi_cc_ci_ed_dvc_dv` (eq/in), `estado_origem` (eq/in), `estado_destino` (eq/in)

## efplanejamento_tributario_tabela_simples_faixas

**Planejamento Tributário - Tabela Simples Faixas** — tabela `EFPLANEJAMENTO_TRIBUTARIO_TABELA_SIMPLES_FAIXAS` (120 linhas)

Planejamento Tributário - Tabela Simples Faixas. 120 linhas no catálogo; chave: ANEXO, TIPO_ANEXO, VIGENCIA, FAIXA.

- **Chave:** `ANEXO, TIPO_ANEXO, VIGENCIA, FAIXA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `ANEXO asc`, `TIPO_ANEXO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 120 linhas, VIGENCIA de 2027-01-01 a 2033-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| anexo | `anexo` | integer(4) |  |  | Anexo |
| tipo_normal_exportacao | `tipo_anexo` | char(1) |  |  | Tipo (Normal - Exportacao) |
| vigencia | `vigencia` | date(4) |  |  | Vigencia |
| faixa | `faixa` | integer(4) |  |  | Faixa |
| receita_bruta_inicial | `receita_inicial` | numeric(13) |  |  | Receita Bruta Inicial |
| receita_bruta_final | `receita_final` | numeric(13) |  |  | Receita Bruta Final |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor_a_deduzir | `valor_deducao` | numeric(13) |  |  | Valor a deduzir |
| percentual_irpj | `perc_irpj` | numeric(5) |  |  | Percentual IRPJ |
| percentual_csll | `perc_csll` | numeric(5) |  |  | Percentual CSLL |
| percentual_inss | `perc_inss` | numeric(5) |  |  | Percentual INSS |
| percentual_ipi | `perc_ipi` | numeric(5) |  |  | Percentual IPI |
| percentual_icms | `perc_icms` | numeric(5) |  |  | Percentual ICMS |
| percentual_iss | `perc_iss` | numeric(5) |  |  | Percentual ISS |
| percentual_cbs | `perc_cbs` | numeric(5) |  |  | Percentual CBS |
| percentual_ibs | `perc_ibs` | numeric(5) |  |  | Percentual IBS |

**Filtros:** `anexo` (eq/in), `tipo_normal_exportacao` (eq/in), `vigencia` (eq/in), `faixa` (eq/in)

## efplanejamento_tributario_impostos_simples

**Planejamento Tributário - Impostos Simples** — tabela `EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS_SIMPLES` (40 linhas)

Planejamento Tributário - Impostos Simples. 40 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO, IMPOSTO, ANEXO, SECAO, TABELA, TIPO, IMPOSTO_REPARTICAO.

- **Chave:** `CODI_EMP, REGIME, PERIODO, IMPOSTO, ANEXO, SECAO, TABELA, TIPO, IMPOSTO_REPARTICAO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`, `IMPOSTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 40 linhas, 1 empresa(s), PERIODO de 2026-01-01 a 2026-08-01.
- regime_de_planejamento_p_presumido_r_rea: todos os valores reais estão no comentário do banco (S=40).
- tipo_a_ambos_i_interno_e_externo: todos os valores reais estão no comentário do banco (I=40).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  | efplanejamento_tributario_impostos_simples_regime_de_p | Regime de Planejamento (P - Presumido / R - Real / S - Simples Nacional) |
| periodo_planejamento | `periodo` | date(4) |  |  | Periodo planejamento |
| imposto | `imposto` | integer(4) |  |  | Imposto |
| anexo | `anexo` | integer(4) |  |  | Anexo |
| secao | `secao` | integer(4) |  |  | Secao |
| tabela | `tabela` | integer(4) |  |  | Tabela |
| tipo_a_ambos_i_interno_e_externo | `tipo` | char(1) |  | efplanejamento_tributario_impostos_simples_tipo_a_ambo | Tipo (A - Ambos / I - Interno / E - Externo) |
| imposto_reparticao | `imposto_reparticao` | integer(4) |  |  | Imposto - Reparticao |
| valor | `valor` | numeric(13) |  |  | Valor |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in), `imposto` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `tipo_a_ambos_i_interno_e_externo` (eq/in), `imposto_reparticao` (eq/in)

## efplanejamento_tributario_valor_folha

**Planejamento Tributário - Valor Folha** — tabela `EFPLANEJAMENTO_TRIBUTARIO_VALOR_FOLHA` (24 linhas)

Planejamento Tributário - Valor Folha. 24 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO.

- **Chave:** `CODI_EMP, REGIME, PERIODO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24 linhas, 1 empresa(s), PERIODO de 2025-01-01 a 2025-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| periodo_planejamento | `periodo` | date(4) |  |  | Periodo Planejamento |
| valor_salario | `valor_salario` | numeric(13) |  |  | Valor salário |
| valor_contribuinte | `valor_contribuinte` | numeric(13) |  |  | Valor Contribuinte |
| valor_inss_empresa_terceiros | `valor_inss` | numeric(13) |  |  | Valor INSS Empresa/Terceiros |
| valor_demais_tributos | `valor_demais_tributos` | numeric(13) |  |  | Valor Demais Tributos |
| valor_salario_valor_contribuinte_valor_i | `valor_total` | numeric(13) |  |  | Valor salário + Valor Contribuinte + Valor INSS Empresa/Terceiros + Valor Demais Tributos |
| valor_ultimo_doze_meses | `valor_ultimo_doze_meses` | numeric(13) |  |  | Valor Último Doze Meses |
| aumento | `aumento` | numeric(13) |  |  | Aumento |
| reducao | `reducao` | numeric(13) |  |  | Reducao |
| valor_salario_estimativa | `valor_salario_estimativa` | numeric(13) |  |  | Valor Salário Estimativa |
| valor_contribuinte_estimativa | `valor_contribuinte_estimativa` | numeric(13) |  |  | Valor Contribuinte Estimativa |
| valor_inss_estimativa | `valor_inss_estimativa` | numeric(13) |  |  | Valor INSS Estimativa |
| valor_demais_tributos_estimativa | `valor_demais_tributos_estimativa` | numeric(13) |  |  | Valor Demais Tributos Estimativa |
| valor_total_estimativa | `valor_total_estimativa` | numeric(13) |  |  | Valor Total Estimativa |
| valor_ultimo_doze_meses_estimativa | `valor_ultimo_doze_meses_estimativa` | numeric(13) |  |  | Valor Último Doze Meses Estimativa |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in)

## efplanejamento_tributario_valor_despesa

**Planejamento Tributário - Despesas** — tabela `EFPLANEJAMENTO_TRIBUTARIO_VALOR_DESPESA` (24 linhas)

Planejamento Tributário - Despesas. 24 linhas no catálogo; chave: CODI_EMP, REGIME, PERIODO.

- **Chave:** `CODI_EMP, REGIME, PERIODO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO`
- **Ordem padrão:** `PERIODO desc`, `REGIME asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24 linhas, 1 empresa(s), PERIODO de 2026-01-01 a 2026-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P - Presumido, R - Real, S - Simples) |
| periodo_planejamento | `periodo` | date(4) |  |  | Periodo Planejamento |
| valor_despesa | `valor_despesa` | numeric(13) |  |  | Valor despesa |
| aumento | `aumento` | numeric(13) |  |  | Aumento |
| reducao | `reducao` | numeric(13) |  |  | Reducao |
| valor_despesa_estimativa | `valor_despesa_estimativa` | numeric(13) |  |  | Valor Despesa Estimativa |

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_planejamento` (eq/in)

## efplanejamento_tributario_tabela_simples

**Planejamento Tributário - Tabela Simples** — tabela `EFPLANEJAMENTO_TRIBUTARIO_TABELA_SIMPLES` (20 linhas)

Planejamento Tributário - Tabela Simples. 20 linhas no catálogo; chave: ANEXO, TIPO_ANEXO, VIGENCIA.

- **Chave:** `ANEXO, TIPO_ANEXO, VIGENCIA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `ANEXO asc`, `TIPO_ANEXO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20 linhas, VIGENCIA de 2027-01-01 a 2033-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| anexo | `anexo` | integer(4) |  |  | Anexo |
| tipo_normal_exportacao | `tipo_anexo` | char(1) |  |  | Tipo (Normal - Exportacao) |
| vigencia | `vigencia` | date(4) |  |  | Vigencia |
| descricao | `descricao` | varchar(100) |  |  | Descricao |

**Filtros:** `anexo` (eq/in), `tipo_normal_exportacao` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo)

## efplanejamento_tributario

**Planejamento Tributário** — tabela `EFPLANEJAMENTO_TRIBUTARIO` (3 linhas)

Planejamento Tributário. 3 linhas no catálogo; chave: CODI_EMP, REGIME.

- **Chave:** `CODI_EMP, REGIME`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO_CONSIDERADO_INICIO`
- **Ordem padrão:** `PERIODO_CONSIDERADO_INICIO desc`, `REGIME asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 1 empresa(s), PERIODO_CONSIDERADO_INICIO de 2025-01-01 a 2025-01-01.
- Colunas expostas nulas em 100% das linhas (2): possui_ncm_multiplos_cclasstrib, forma_de_calculo_1_movimentacoes_da_empr.
- Vínculo geempre (geempre): 0 de 3 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| regime_de_planejamento_p_presumido_r_rea | `regime` | char(1) |  |  | Regime de Planejamento (P  - Presumido, R - Real, S - Simples) |
| ano_planejamento | `ano` | integer(4) |  |  | Ano Planejamento |
| periodo_inicial_considerado_para_calculo | `periodo_considerado_inicio` | date(4) |  |  | Periodo Inicial considerado para calculo |
| periodo_final_considerado_para_calculo | `periodo_considerado_fim` | date(4) |  |  | Periodo Final considerado para calculo |
| periodo_com_estouro_do_limite_estadual | `periodo_estouro_limite_estadual` | date(4) |  |  | Periodo com estouro do limite estadual |
| periodo_com_estouro_do_limite_federal | `periodo_estouro_limite_federal` | date(4) |  |  | Periodo com estouro do limite federal |
| empresa_estourou_limite_federal_ano_ante | `empresa_estourou_limite_federal_ano_anterior` | char(1) |  |  | Empresa estourou limite federal ano anterior |
| empresa_estourou_limite_estadual_ano_ant | `empresa_estourou_limite_estadual_ano_anterior` | char(1) |  |  | Empresa estourou limite estadual ano anterior |
| possui_socio_em_outra_empresa | `possui_socio_em_outra_empresa` | char(1) |  |  | Possui socio em outra empresa |
| possui_ncm_multiplos_cclasstrib | `possui_ncm_com_multiplo_cclasstrib` | char(1) |  |  | Possui Ncm múltiplos cclasstrib |
| forma_de_calculo_1_movimentacoes_da_empr | `forma_calculo` | tinyint(1) |  |  | Forma de cálculo (1-Movimentações da empresa,2-Manualmente) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `regime_de_planejamento_p_presumido_r_rea` (eq/in), `periodo_inicial_considerado_para_calculo` (entre/gte/lte), `periodo_final_considerado_para_calculo` (entre/gte/lte), `periodo_com_estouro_do_limite_estadual` (entre/gte/lte), `periodo_com_estouro_do_limite_federal` (entre/gte/lte), `empresa_estourou_limite_federal_ano_ante` (eq/in), `empresa_estourou_limite_estadual_ano_ant` (eq/in), `possui_socio_em_outra_empresa` (eq/in), `possui_ncm_multiplos_cclasstrib` (eq/in)

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

### efplanejamento_tributario_impostos_simples_regime_de_p

Confirmado: sim

> Todos os valores observados em EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS_SIMPLES.REGIME estão no comentário do banco (2026-10-18). Distribuição: S=40.

| Código | Significado |
|---|---|
| P | Presumido |
| R | Real |
| S | Simples Nacional |

### efplanejamento_tributario_impostos_simples_tipo_a_ambo

Confirmado: sim

> Todos os valores observados em EFPLANEJAMENTO_TRIBUTARIO_IMPOSTOS_SIMPLES.TIPO estão no comentário do banco (2026-10-18). Distribuição: I=40.

| Código | Significado |
|---|---|
| A | Ambos |
| I | Interno |
| E | Externo |

