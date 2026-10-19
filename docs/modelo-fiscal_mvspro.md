# Modelo — Fiscal - mvspro (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_mvspro.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

25 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efmvspro_apuracao_estoque](#efmvspro_apuracao_estoque) | `EFMVSPRO_APURACAO_ESTOQUE` | 1.328.105 | grande | empresa; um de: codigo_sequencial_da_nota_de_saida |
| [efmvspro_difal_nc](#efmvspro_difal_nc) | `EFMVSPRO_DIFAL_NC` | 64.689 | medio | empresa |
| [efmvspro_ibs_iva](#efmvspro_ibs_iva) | `EFMVSPRO_IBS_IVA` | 37.465 | medio | empresa |
| [efmvspro_cbs_iva](#efmvspro_cbs_iva) | `EFMVSPRO_CBS_IVA` | 37.421 | medio | empresa |
| [efmvspro_federal](#efmvspro_federal) | `EFMVSPRO_FEDERAL` | 862 | pequeno | empresa |
| [efmvspro_simples_nacional_monofasico](#efmvspro_simples_nacional_monofasico) | `EFMVSPRO_SIMPLES_NACIONAL_MONOFASICO` | 377 | pequeno | empresa |
| [efmvspro_difali](#efmvspro_difali) | `EFMVSPRO_DIFALI` | 224 | pequeno | empresa |
| [efmvspro_estadual_rj](#efmvspro_estadual_rj) | `EFMVSPRO_ESTADUAL_RJ` | 199 | pequeno | empresa |
| [efmvspro_estadual_ce](#efmvspro_estadual_ce) | `EFMVSPRO_ESTADUAL_CE` | 24 | pequeno | empresa |
| [efmvspro_fundo_ampara](#efmvspro_fundo_ampara) | `EFMVSPRO_FUNDO_AMPARA` | 8 | pequeno | empresa |
| [efmvspro_icms_stat](#efmvspro_icms_stat) | `EFMVSPRO_ICMS_STAT` | 2 | pequeno | empresa |
| [efmvspro_estadual_sp](#efmvspro_estadual_sp) | `EFMVSPRO_ESTADUAL_SP` | 2 | pequeno | empresa |
| [efmvspro_estadual_to](#efmvspro_estadual_to) | `EFMVSPRO_ESTADUAL_TO` | 2 | pequeno | empresa |
| [efmvspro_estorno_credito_presumido_pis_cofins](#efmvspro_estorno_credito_presumido_pis_cofins) | `EFMVSPRO_ESTORNO_CREDITO_PRESUMIDO_PIS_COFINS` | 2 | pequeno | empresa |
| [efmvspro_estadual_pr](#efmvspro_estadual_pr) | `EFMVSPRO_ESTADUAL_PR` | 2 | pequeno | empresa |
| [efmvspro_fecomp_ms_icms_proprio](#efmvspro_fecomp_ms_icms_proprio) | `EFMVSPRO_FECOMP_MS_ICMS_PROPRIO` | 2 | pequeno | empresa |
| [efmvspro_fecomp_ms_icms_st](#efmvspro_fecomp_ms_icms_st) | `EFMVSPRO_FECOMP_MS_ICMS_ST` | 2 | pequeno | empresa |
| [efmvspro_estadual_ro](#efmvspro_estadual_ro) | `EFMVSPRO_ESTADUAL_RO` | 2 | pequeno | empresa |
| [efmvspro_estadual_mg](#efmvspro_estadual_mg) | `EFMVSPRO_ESTADUAL_MG` | 2 | pequeno | empresa |
| [efmvspro_icmsa](#efmvspro_icmsa) | `EFMVSPRO_ICMSA` | 2 | pequeno | empresa |
| [efmvspro_estadual_rn](#efmvspro_estadual_rn) | `EFMVSPRO_ESTADUAL_RN` | 2 | pequeno | empresa |
| [efmvspro_estadual_al](#efmvspro_estadual_al) | `EFMVSPRO_ESTADUAL_AL` | 2 | pequeno | empresa |
| [efmvspro_fundeinfra](#efmvspro_fundeinfra) | `EFMVSPRO_FUNDEINFRA` | 2 | pequeno | empresa |
| [efmvspro_icms_efetivo](#efmvspro_icms_efetivo) | `EFMVSPRO_ICMS_EFETIVO` | 2 | pequeno | empresa |
| [efmvspro_is](#efmvspro_is) | `EFMVSPRO_IS` | 2 | pequeno | empresa |

## efmvspro_apuracao_estoque

**Notas Fiscais de Saída - Produtos - Apuração de estoque** — tabela `EFMVSPRO_APURACAO_ESTOQUE` (1.328.105 linhas)

Notas Fiscais de Saída - Produtos - Apuração de estoque. 1.328.105 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_MOVIMENTACAO` · exige um de: `codigo_sequencial_da_nota_de_saida`
- **Ordem padrão:** `DATA_MOVIMENTACAO desc`, `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.333.614 linhas, 145 empresa(s), DATA_MOVIMENTACAO de 2015-02-09 a 2026-09-30.
- Vínculo efmvspro (efmvspro): 0 de 303 linhas sem registro relacionado (empresa 442).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| data_da_movimentacao | `data_movimentacao` | date(4) |  |  | Data da movimentação |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| quantidade | `quantidade` | numeric(13) |  |  | Quantidade |
| valor_unitario | `valor_unitario` | numeric(15) |  |  | Valor unitário |
| valor_total | `valor_total` | numeric(15) |  |  | Valor total |
| quantidade_acumulada | `quantidade_acumulada` | numeric(13) |  |  | Quantidade acumulada |
| valor_unitario_medio | `valor_unitario_medio` | numeric(15) |  |  | Valor unitário médio |
| valor_acumulado | `valor_acumulado` | numeric(15) |  |  | Valor acumulado |
| valor_do_icms_unitario | `icms_unitario` | numeric(19) |  |  | Valor do ICMS unitário |
| valor_do_icms_total | `icms_total` | numeric(13) |  |  | Valor do ICMS total |
| valor_do_icms_unitario_medio | `icms_unitario_medio` | numeric(19) |  |  | Valor do ICMS unitário médio |
| valor_do_icms_acumulado | `icms_acumulado` | numeric(13) |  |  | Valor do ICMS acumulado |
| quantidade_icms_st | `icms_st_quantidade` | numeric(13) |  |  | Quantidade ICMS ST |
| valor_do_icms_st_unitario | `icms_st_unitario` | numeric(19) |  |  | Valor do ICMS ST unitário |
| valor_do_icms_st_total | `icms_st_total` | numeric(13) |  |  | Valor do ICMS ST total |
| quantidade_icms_st_acumulado | `icms_st_quantidade_acumulado` | numeric(13) |  |  | Quantidade ICMS ST acumulado |
| valor_do_icms_st_unitario_medio | `icms_st_unitario_medio` | numeric(19) |  |  | Valor do ICMS ST unitário médio |
| icms_st_acumulado | `icms_st_acumulado` | numeric(13) |  |  | Valor do ICMS acumulado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `data_da_movimentacao` (entre/gte/lte), `codigo_do_produto` (eq/in)

## efmvspro_difal_nc

**Notas Fiscais de Saida - Produtos - DIFAL NC** — tabela `EFMVSPRO_DIFAL_NC` (64.689 linhas)

Notas Fiscais de Saida - Produtos - DIFAL NC. 64.689 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 65.330 linhas, 22 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 26 linhas sem registro relacionado (empresa 1676).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| saida | `codi_sai` | integer(4) |  |  | SaÍda |
| sequencial | `nume_msp` | integer(4) |  |  | Sequencial |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| base_calculo | `base_calculo` | numeric(15) |  |  | Base Cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor_uf_origem | `valor_uf_origem` | numeric(15) |  |  | Valor UF Origem |
| valor_uf_destino | `valor_uf_destino` | numeric(15) |  |  | Valor UF Destino |
| valor_total | `valor_total` | numeric(15) |  |  | Valor Total |
| valor_fcp | `valor_fcp` | numeric(15) |  |  | Valor FCP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `saida` (eq/in), `sequencial` (eq/in), `produto` (eq/in)

## efmvspro_ibs_iva

**Valorer IBS Estoque - Saidas** — tabela `EFMVSPRO_IBS_IVA` (37.465 linhas)

Valorer IBS Estoque - Saidas. 37.465 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 37.465 linhas, 8 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 222 linhas sem registro relacionado (empresa 1729).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo Empresa |
| codigo_saida | `codi_sai` | integer(4) |  |  | Codigo Saida |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Codigo sequencial do estoque |
| codigo_cclasstrib | `i_cclasstrib` | char(6) |  |  | Codigo cClassTrib |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Calculo |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_cclasstrib` (eq/in)

## efmvspro_cbs_iva

**Valorer CBS Estoque - Saidas** — tabela `EFMVSPRO_CBS_IVA` (37.421 linhas)

Valorer CBS Estoque - Saidas. 37.421 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 37.421 linhas, 8 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 222 linhas sem registro relacionado (empresa 1729).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo Empresa |
| codigo_saida | `codi_sai` | integer(4) |  |  | Codigo Saida |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Codigo sequencial do estoque |
| codigo_cclasstrib | `i_cclasstrib` | char(6) |  |  | Codigo cClassTrib |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Calculo |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_cclasstrib` (eq/in)

## efmvspro_federal

**Notas Fiscais de Saida - Produtos - Federal** — tabela `EFMVSPRO_FEDERAL` (862 linhas)

Notas Fiscais de Saida - Produtos - Federal. 862 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 862 linhas, 5 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 58 linhas sem registro relacionado (empresa 808).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_da_saida | `codi_sai` | integer(4) |  |  | Código da Saída |
| numero_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Número sequêncial do estoque |
| valores_repassados_pelas_agencias_de_pro | `valor_deducao_propaganda_publicidade` | numeric(15) |  |  | Valores repassados pelas agências de propaganda a empresas de rádio, televisão e outros |
| valor_desonerado | `valor_icms_desonerado` | numeric(13) |  |  | Valor Desonerado |
| motivo_da_desoneracao | `i_motivo_desoneracao` | integer(4) |  |  | Motivo da Desoneração |
| percentual_icms_diferido | `percentual_icms_diferido` | numeric(5) |  |  | Percentual ICMS Diferido |
| valor_icms_diferido | `valor_icms_diferido` | numeric(13) |  |  | Valor ICMS Diferido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_da_saida` (eq/in), `numero_sequencial_do_estoque` (eq/in), `motivo_da_desoneracao` (eq/in)

## efmvspro_simples_nacional_monofasico

**Notas Fiscais de Saída - Produtos - Simples Nacional Produto Monofasico** — tabela `EFMVSPRO_SIMPLES_NACIONAL_MONOFASICO` (377 linhas)

Notas Fiscais de Saída - Produtos - Simples Nacional Produto Monofasico. 377 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP, ANEXO, SECAO, TABELA, CODI_ACU, TRIBUTACAO_PISCOFINS_TIPO.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP, ANEXO, SECAO, TABELA, CODI_ACU, TRIBUTACAO_PISCOFINS_TIPO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 327 linhas, 1 empresa(s), COMPETENCIA de 2026-07-01 a 2026-09-01.
- Vínculo efmvspro (efmvspro): 0 de 327 linhas sem registro relacionado (empresa 718).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| saida | `codi_sai` | integer(4) |  |  | Saida |
| sequencial | `nume_msp` | integer(4) |  |  | Sequencial |
| anexo | `anexo` | integer(4) |  |  | Anexo |
| secao | `secao` | integer(4) |  |  | Seção |
| tabela | `tabela` | integer(4) |  |  | Tabela |
| acumulador | `codi_acu` | integer(4) |  |  | Acumulador |
| tributacao_piscofins_tipo | `tributacao_piscofins_tipo` | integer(4) |  |  | Tributação PIS e COFINS - Tipo (1 / 2) |
| valor | `valor` | numeric(13) |  |  | Valor |
| competencia | `competencia` | date(4) |  |  | Competência |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `saida` (eq/in), `sequencial` (eq/in), `anexo` (eq/in), `secao` (eq/in), `tabela` (eq/in), `acumulador` (eq/in), `tributacao_piscofins_tipo` (eq/in), `competencia` (entre/gte/lte)

## efmvspro_difali

**Notas Fiscais de Saída - Produtos - DIFALI** — tabela `EFMVSPRO_DIFALI` (224 linhas)

Notas Fiscais de Saída - Produtos - DIFALI. 224 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 224 linhas, 7 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 10 linhas sem registro relacionado (empresa 1575).
- Vínculo efprodutos (efprodutos): 0 de 10 linhas sem registro relacionado (empresa 1575).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo | `base_calculo_difali` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota_difali` | numeric(7) |  |  | Alíquota |
| valor | `valor_difali` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estadual_rj

**Notas Fiscais de Saída - Produtos - Estadual RS** — tabela `EFMVSPRO_ESTADUAL_RJ` (199 linhas)

Notas Fiscais de Saída - Produtos - Estadual RS. 199 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 199 linhas, 4 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 84 linhas sem registro relacionado (empresa 1566).
- Vínculo efprodutos (efprodutos): 0 de 84 linhas sem registro relacionado (empresa 1566).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_produto | `codi_pdi` | char(14) |  |  | Código produto |
| base_de_calculo | `base_calculo_icms_efetivo` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota_icms_efetivo` | numeric(13) |  |  | Alíquota |
| valor | `valor_icms_efetivo` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_produto` (eq/in)

## efmvspro_estadual_ce

**Notas Fiscais de Saída - Produtos - Estadual CE** — tabela `EFMVSPRO_ESTADUAL_CE` (24 linhas)

Notas Fiscais de Saída - Produtos - Estadual CE. 24 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 24 linhas, 2 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 21 linhas sem registro relacionado (empresa 1474).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| fecop_ce_base_de_calculo | `fecop_ce_icms_base_calculo` | numeric(13) |  |  | FECOP-CE Base de cálculo |
| fecop_ce_aliquota | `fecop_ce_icms_aliquota` | numeric(5) |  |  | FECOP-CE Alíquota |
| fecop_ce_valor | `fecop_ce_icms_valor` | numeric(13) |  |  | FECOP-CE Valor |
| fecop_ce_st_base_de_calculo | `fecop_ce_icms_st_base_calculo` | numeric(13) |  |  | FECOP-CE ST Base de cálculo |
| fecop_ce_st_aliquota | `fecop_ce_icms_st_aliquota` | numeric(5) |  |  | FECOP-CE ST Alíquota |
| fecop_ce_st_valor | `fecop_ce_icms_st_valor` | numeric(13) |  |  | FECOP-CE ST Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in)

## efmvspro_fundo_ampara

**Notas Fiscais de Saída - Produtos - Ampara RS** — tabela `EFMVSPRO_FUNDO_AMPARA` (8 linhas)

Notas Fiscais de Saída - Produtos - Ampara RS. 8 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP, CODI_PDI.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP, CODI_PDI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 4 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_calculo_icms | `base_icms_proprio` | numeric(13) |  |  | Base cálculo ICMS |
| aliquota_icms | `aliquota_icms_proprio` | numeric(5) |  |  | Alíquota ICMS |
| valor_icms | `valor_icms_proprio` | numeric(13) |  |  | Valor ICMS |
| base_calculo_icms_st | `base_icms_st` | numeric(13) |  |  | Base cálculo ICMS ST |
| aliquota_icms_st | `aliquota_st_proprio` | numeric(5) |  |  | Alíquota ICMS ST |
| valor_icms_st | `valor_icms_st` | numeric(13) |  |  | Valor ICMS ST |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_icms_stat

**Notas Fiscais de Saída - Produtos - ICMS STAT** — tabela `EFMVSPRO_ICMS_STAT` (2 linhas)

Notas Fiscais de Saída - Produtos - ICMS STAT. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo_icms_st_antecipacao_tota | `base_calculo` | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| aliquota_icms_st_antecipacao_total | `aliquota` | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| valor_icms_st_antecipacao_total | `valor_imposto` | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| codigo_do_recolhimento_substituicao_trib | `codigo_recolhimento` | char(6) |  |  | Código do Recolhimento - Substituição Tributária |
| codigo_sequencial_do_recolhimento_substi | `i_recolhimento` | integer(4) |  |  | Código Sequencial do Recolhimento - Substituição Tributária |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `codigo_do_recolhimento_substituicao_trib` (eq/in), `codigo_sequencial_do_recolhimento_substi` (eq/in)

## efmvspro_estadual_sp

**Notas Fiscais de Saída - Produtos - Estadual SP** — tabela `EFMVSPRO_ESTADUAL_SP` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual SP. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| fecoep_icms_proprio_base_de_calculo | `base_calculo_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Base de cálculo |
| fecoep_icms_proprio_aliquota | `aliquota_fecoep_proprio` | numeric(5) |  |  | FECOEP - ICMS Próprio - Alíquota |
| fecoep_icms_proprio_valor | `valor_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Valor |
| fecoep_icms_st_base_de_calculo | `base_calculo_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Base de cálculo |
| fecoep_icms_st_aliquota | `aliquota_fecoep_st` | numeric(5) |  |  | FECOEP - ICMS ST - Alíquota |
| fecoep_icms_st_valor | `valor_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Valor |
| fcp_st_base_de_calculo | `base_calculo_fcp_st` | numeric(13) |  |  | FCP-ST - Base de cálculo |
| fcp_st_aliquota | `aliquota_fcp_st` | numeric(5) |  |  | FCP-ST - Alíquota |
| fcp_st_valor | `valor_fcp_st` | numeric(13) |  |  | FCP-ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estadual_to

**Notas Fiscais de Saída - Produtos - Estadual TO** — tabela `EFMVSPRO_ESTADUAL_TO` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual TO. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| fecoep_icms_proprio_base_de_calculo | `base_calculo_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Base de cálculo |
| fecoep_icms_proprio_aliquota | `aliquota_fecoep_proprio` | numeric(5) |  |  | FECOEP - ICMS Próprio - Alíquota |
| fecoep_icms_proprio_valor | `valor_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Valor |
| fecoep_icms_st_base_de_calculo | `base_calculo_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Base de cálculo |
| fecoep_icms_st_aliquota | `aliquota_fecoep_st` | numeric(5) |  |  | FECOEP - ICMS ST - Alíquota |
| fecoep_icms_st_valor | `valor_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estorno_credito_presumido_pis_cofins

**Notas Fiscais de Saída - Produtos - Estorno Crédito Presumido PIS/COFINS** — tabela `EFMVSPRO_ESTORNO_CREDITO_PRESUMIDO_PIS_COFINS` (2 linhas)

Notas Fiscais de Saída - Produtos - Estorno Crédito Presumido PIS/COFINS. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| valor_pis | `valor_pis` | numeric(13) |  |  | Valor PIS |
| valor_cofins | `valor_cofins` | numeric(13) |  |  | Valor COFINS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estadual_pr

**Notas Fiscais de Saída - Produtos - Estadual PR** — tabela `EFMVSPRO_ESTADUAL_PR` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual PR. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_da_nota | `codi_sai` | integer(4) |  |  | Código da Nota |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código Sequencial do Estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do Produto |
| fecop_icms_proprio_base_de_calculo | `base_calculo_fecop_proprio` | numeric(13) |  |  | FECOP - ICMS Próprio - Base de cálculo |
| fecop_icms_proprio_aliquota | `aliquota_fecop_proprio` | numeric(5) |  |  | FECOP - ICMS Próprio - Alíquota |
| fecop_icms_proprio_valor | `valor_fecop_proprio` | numeric(13) |  |  | FECOP - ICMS Próprio - Valor |
| fecop_icms_st_base_de_calculo | `base_calculo_fecop_st` | numeric(13) |  |  | FECOP - ICMS ST - Base de cálculo |
| fecop_icms_st_aliquota | `aliquota_fecop_st` | numeric(5) |  |  | FECOP - ICMS ST - Alíquota |
| fecop_icms_st_valor | `valor_fecop_st` | numeric(13) |  |  | FECOP - ICMS ST - Valor |
| fcp_st_base_de_calculo | `base_calculo_fcp_st` | numeric(13) |  |  | FCP ST - Base de cálculo |
| fcp_st_aliquota | `aliquota_fcp_st` | numeric(5) |  |  | FCP ST - Alíquota |
| fcp_st_valor | `valor_fcp_st` | numeric(13) |  |  | FCP ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_da_nota` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_fecomp_ms_icms_proprio

**Notas Fiscais de Saída - Produtos - FECOMP MS** — tabela `EFMVSPRO_FECOMP_MS_ICMS_PROPRIO` (2 linhas)

Notas Fiscais de Saída - Produtos - FECOMP MS. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_calculo_icms | `base_calculo_fecomp_ms_icms_proprio` | numeric(15) |  |  | Base cálculo ICMS |
| aliquota_icms | `aliquota_fecomp_ms_icms_proprio` | numeric(5) |  |  | Alíquota ICMS |
| valor_icms | `valor_fecomp_ms_icms_proprio` | numeric(15) |  |  | Valor ICMS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_fecomp_ms_icms_st

**Notas Fiscais de Saída - Produtos - FECOMP ST MS** — tabela `EFMVSPRO_FECOMP_MS_ICMS_ST` (2 linhas)

Notas Fiscais de Saída - Produtos - FECOMP ST MS. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_calculo_icms_st | `base_calculo_fecomp_ms_icms_st` | numeric(15) |  |  | Base cálculo ICMS ST |
| aliquota_icms_st | `aliquota_fecomp_ms_icms_st` | numeric(5) |  |  | Alíquota ICMS ST |
| valor_icms_st | `valor_fecomp_ms_icms_st` | numeric(15) |  |  | Valor ICMS ST |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estadual_ro

**Notas Fiscais de Saída - Produtos - Estadual RO** — tabela `EFMVSPRO_ESTADUAL_RO` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual RO. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| fecoep_icms_proprio_base_de_calculo | `base_calculo_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Base de cálculo |
| fecoep_icms_proprio_aliquota | `aliquota_fecoep_proprio` | numeric(5) |  |  | FECOEP - ICMS Próprio - Alíquota |
| fecoep_icms_proprio_valor | `valor_fecoep_proprio` | numeric(13) |  |  | FECOEP - ICMS Próprio - Valor |
| fecoep_icms_st_base_de_calculo | `base_calculo_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Base de cálculo |
| fecoep_icms_st_aliquota | `aliquota_fecoep_st` | numeric(5) |  |  | FECOEP - ICMS ST - Alíquota |
| fecoep_icms_st_valor | `valor_fecoep_st` | numeric(13) |  |  | FECOEP - ICMS ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_estadual_mg

**Notas Fiscais de Saída - Produtos - Estadual MG** — tabela `EFMVSPRO_ESTADUAL_MG` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual MG. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| base_de_calculo_recali | `recali_base_calculo` | numeric(13) |  |  | Base de Cálculo - RECALI |
| aliquota_recali | `recali_aliquota` | numeric(5) |  |  | Alíquota - RECALI |
| valor_recali | `recali_valor` | numeric(13) |  |  | Valor - RECALI |
| codigo_recolhimento_recali | `recali_codigo_recolhimento` | char(6) |  |  | Código Recolhimento - RECALI |
| sequencial_recolhimento_recali | `recali_i_recolhimento` | integer(4) |  |  | Sequencial Recolhimento - RECALI |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_recolhimento_recali` (eq/in)

## efmvspro_icmsa

**Notas Fiscais de Saída - Produtos - ICMSA** — tabela `EFMVSPRO_ICMSA` (2 linhas)

Notas Fiscais de Saída - Produtos - ICMSA. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| saida | `codi_sai` | integer(4) |  |  | Saída |
| sequencial | `nume_msp` | integer(4) |  |  | Sequencial |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| base_de_calculo_icmsa | `base_calculo_icmsa` | numeric(13) |  |  | Base de Cálculo - ICMSA |
| aliquota_icmsa | `aliquota_icmsa` | numeric(7) |  |  | Alíquota - ICMSA |
| valor_icmsa | `valor_icmsa` | numeric(13) |  |  | Valor - ICMSA |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `saida` (eq/in), `sequencial` (eq/in), `produto` (eq/in)

## efmvspro_estadual_rn

**Notas Fiscais de Saída - Produtos - Estadual RN** — tabela `EFMVSPRO_ESTADUAL_RN` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual RN. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_produto | `codi_pdi` | char(14) |  |  | Código produto |
| fecop_icms_proprio_base_de_calculo | `base_calculo_fecop_proprio` | numeric(13) |  |  | FECOP - ICMS Próprio - Base de cálculo |
| fecop_icms_proprio_aliquota | `aliquota_fecop_proprio` | numeric(5) |  |  | FECOP - ICMS Próprio - Alíquota |
| fecop_icms_proprio_valor | `valor_fecop_proprio` | numeric(13) |  |  | FECOP - ICMS Próprio - Valor |
| fecop_icms_st_base_de_calculo | `base_calculo_fecop_st` | numeric(13) |  |  | FECOP - ICMS ST - Base de cálculo |
| fecop_icms_st_aliquota | `aliquota_fecop_st` | numeric(5) |  |  | FECOP - ICMS ST - Alíquota |
| fecop_icms_st_valor | `valor_fecop_st` | numeric(13) |  |  | FECOP - ICMS ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_produto` (eq/in)

## efmvspro_estadual_al

**Notas Fiscais de Saída - Produtos - Estadual AL** — tabela `EFMVSPRO_ESTADUAL_AL` (2 linhas)

Notas Fiscais de Saída - Produtos - Estadual AL. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| fecoep_al_st_base_de_calculo | `fecoep_al_icms_st_base_calculo` | numeric(13) |  |  | FECOEP-AL ST Base de cálculo |
| fecoep_al_st_aliquota | `fecoep_al_icms_st_aliquota` | numeric(5) |  |  | FECOEP-AL ST Alíquota |
| fecoep_al_st_valor | `fecoep_al_icms_st_valor` | numeric(13) |  |  | FECOEP-AL ST Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in)

## efmvspro_fundeinfra

**Notas Fiscais de Saída - Produtos - FUNDEINFRA** — tabela `EFMVSPRO_FUNDEINFRA` (2 linhas)

Notas Fiscais de Saída - Produtos - FUNDEINFRA. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_sequencial_da_saida | `codi_sai` | integer(4) |  |  | Código sequencial da saida |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Codigo do Produto |
| base_de_calculo_fundeinfra | `base_calculo_fundeinfra` | numeric(13) |  |  | Base de calculo fundeinfra |
| aliquota_do_fundeinfra | `aliquota_fundeinfra` | numeric(7) |  |  | Aliquota do fundeinfra |
| valor_do_fundeinfra | `valor_fundeinfra` | numeric(13) |  |  | Valor do fundeinfra |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvspro_icms_efetivo

**Notas Fiscais de Saída - Produtos - ICMS Efetivo Geral** — tabela `EFMVSPRO_ICMS_EFETIVO` (2 linhas)

Notas Fiscais de Saída - Produtos - ICMS Efetivo Geral. 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_produto | `codi_pdi` | char(14) |  |  | Código produto |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota` | numeric(13) |  |  | Alíquota |
| valor | `valor` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_produto` (eq/in)

## efmvspro_is

**Nota Fiscais de Saidas - Produtos - IS (Imposto Seletivo)** — tabela `EFMVSPRO_IS` (2 linhas)

Nota Fiscais de Saidas - Produtos - IS (Imposto Seletivo). 2 linhas no catálogo; chave: CODI_EMP, CODI_SAI, NUME_MSP.

- **Chave:** `CODI_EMP, CODI_SAI, NUME_MSP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_SAI asc`, `NUME_MSP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo efmvspro (efmvspro): 0 de 2 linhas sem registro relacionado (empresa 1644).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_sai` | integer(4) |  |  | Código sequencial da nota de saida |
| codigo_sequencial_do_estoque | `nume_msp` | integer(4) |  |  | Código sequencial do estoque |
| codigo_produto | `codi_pdi` | char(14) |  |  | Código produto |
| classificacao_tributaria_do_imposto_sele | `cclass_trib_is` | char(6) |  |  | Classificação tributaria do imposto seletivo - IS |
| cst_do_imposto_is | `cst` | integer(4) |  |  | CST do imposto IS |
| base_calculo_is | `base_calculo` | numeric(13) |  |  | Base cálculo IS |
| aliquota_ad_valorem | `aliquota_ad_valorem_is` | numeric(5) |  |  | Alíquota Ad valorem (%) |
| quantidade_tributada | `qtde_trib` | numeric(13) |  |  | Quantidade tributada |
| aliquota_ad_rem_fixa | `aliquota_ad_rem_fixa_is` | numeric(13) |  |  | Alíquota ad rem (Fixa) |
| valor_imposto | `valor` | numeric(13) |  |  | Valor imposto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvspro` → `efmvspro` por `codi_emp` = `codi_emp` e `codi_sai` = `codi_sai` e `nume_msp` = `nume_msp`; colunas: `efmvspro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_produto` (eq/in), `classificacao_tributaria_do_imposto_sele` (eq/in)

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

