# Modelo — Fiscal - mvepro (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_mvepro.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

22 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efmvepro_apuracao_estoque](#efmvepro_apuracao_estoque) | `EFMVEPRO_APURACAO_ESTOQUE` | 618.580 | medio | empresa |
| [efmvepro_base_piscofins](#efmvepro_base_piscofins) | `EFMVEPRO_BASE_PISCOFINS` | 41.470 | medio | empresa |
| [efmvepro_difali](#efmvepro_difali) | `EFMVEPRO_DIFALI` | 22.026 | medio | empresa |
| [efmvepro_ibs_iva](#efmvepro_ibs_iva) | `EFMVEPRO_IBS_IVA` | 6.777 | pequeno | empresa |
| [efmvepro_cbs_iva](#efmvepro_cbs_iva) | `EFMVEPRO_CBS_IVA` | 6.777 | pequeno | empresa |
| [efmvepro_estadual_am](#efmvepro_estadual_am) | `EFMVEPRO_ESTADUAL_AM` | 1.887 | pequeno | empresa |
| [efmvepro_icmsa](#efmvepro_icmsa) | `EFMVEPRO_ICMSA` | 1.182 | pequeno | empresa |
| [efmvepro_icms_st_retido](#efmvepro_icms_st_retido) | `EFMVEPRO_ICMS_ST_RETIDO` | 931 | pequeno | empresa |
| [efmvepro_icmsi](#efmvepro_icmsi) | `EFMVEPRO_ICMSI` | 789 | pequeno | empresa |
| [efmvepro_icms_stat](#efmvepro_icms_stat) | `EFMVEPRO_ICMS_STAT` | 727 | pequeno | empresa |
| [efmvepro_estadual_mg](#efmvepro_estadual_mg) | `EFMVEPRO_ESTADUAL_MG` | 170 | pequeno | empresa |
| [efmvepro_fem_st_mg](#efmvepro_fem_st_mg) | `EFMVEPRO_FEM_ST_MG` | 170 | pequeno | empresa |
| [efmvepro_estadual_ro](#efmvepro_estadual_ro) | `EFMVEPRO_ESTADUAL_RO` | 110 | pequeno | empresa |
| [efmvepro_extemporaneo_piscofins](#efmvepro_extemporaneo_piscofins) | `EFMVEPRO_EXTEMPORANEO_PISCOFINS` | 56 | pequeno | empresa |
| [efmvepro_federal](#efmvepro_federal) | `EFMVEPRO_FEDERAL` | 39 | pequeno | empresa |
| [efmvepro_difal_nc](#efmvepro_difal_nc) | `EFMVEPRO_DIFAL_NC` | 27 | pequeno | empresa |
| [efmvepro_mg_sub_apuracao](#efmvepro_mg_sub_apuracao) | `EFMVEPRO_MG_SUB_APURACAO` | 14 | pequeno | empresa |
| [efmvepro_medicamento_lote](#efmvepro_medicamento_lote) | `EFMVEPRO_MEDICAMENTO_LOTE` | 14 | pequeno | empresa |
| [efmvepro_estadual_es](#efmvepro_estadual_es) | `EFMVEPRO_ESTADUAL_ES` | 7 | pequeno | empresa |
| [efmvepro_estadual_sp](#efmvepro_estadual_sp) | `EFMVEPRO_ESTADUAL_SP` | 6 | pequeno | empresa |
| [efmvepro_estadual_rj](#efmvepro_estadual_rj) | `EFMVEPRO_ESTADUAL_RJ` | 5 | pequeno | empresa |
| [efmvepro_estadual_mt](#efmvepro_estadual_mt) | `EFMVEPRO_ESTADUAL_MT` | 1 | pequeno | empresa |

## efmvepro_apuracao_estoque

**Notas Fiscais de Entrada - Produtos - Apuração de estoque** — tabela `EFMVEPRO_APURACAO_ESTOQUE` (618.580 linhas)

Notas Fiscais de Entrada - Produtos - Apuração de estoque. 618.580 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_MOVIMENTACAO`
- **Ordem padrão:** `DATA_MOVIMENTACAO desc`, `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 620.483 linhas, 364 empresa(s), DATA_MOVIMENTACAO de 2016-01-30 a 2026-09-30.
- Vínculo efmvepro (efmvepro): 0 de 46 linhas sem registro relacionado (empresa 1348).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
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

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `data_da_movimentacao` (entre/gte/lte), `codigo_do_produto` (eq/in)

## efmvepro_base_piscofins

**Notas Fiscais de Entrada - Produtos - Bases PIS COFINS** — tabela `EFMVEPRO_BASE_PISCOFINS` (41.470 linhas)

Notas Fiscais de Entrada - Produtos - Bases PIS COFINS. 41.470 linhas no catálogo; chave: CODI_EMP, NUME_MEP, CODI_IMP, TIPO_CREDITO, CODI_ENT.

- **Chave:** `CODI_EMP, NUME_MEP, CODI_IMP, TIPO_CREDITO, CODI_ENT`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `NUME_MEP asc`, `CODI_IMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 41.286 linhas, 49 empresa(s), COMPETENCIA de 2013-01-01 a 2026-09-01.
- Vínculo efmvepro (efmvepro): 0 de 88 linhas sem registro relacionado (empresa 1011).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `nume_mep` | integer(4) |  |  | Sequencial |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| tipo_de_credito | `tipo_credito` | integer(4) |  |  | Tipo de crédito |
| entrada | `codi_ent` | integer(4) |  |  | Entrada |
| receita_cumulativa | `receita_cumulativa` | numeric(13) |  |  | Receita cumulativa |
| receita_nao_cumulativa | `receita_nao_cumulativa` | numeric(13) |  |  | Receita não cumulativa |
| interna_tributada | `interna_tributada` | numeric(13) |  |  | Interna tributada |
| interna_nao_tributada | `interna_nao_tributada` | numeric(13) |  |  | Interna não tributada |
| externa | `externa` | numeric(13) |  |  | Externa |
| competencia | `competencia` | date(4) |  |  | Competencia |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `sequencial` (eq/in), `imposto` (eq/in), `tipo_de_credito` (eq/in), `entrada` (eq/in), `competencia` (entre/gte/lte)

## efmvepro_difali

**Notas Fiscais de Entrada - Produtos - DIFALI** — tabela `EFMVEPRO_DIFALI` (22.026 linhas)

Notas Fiscais de Entrada - Produtos - DIFALI. 22.026 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 22.026 linhas, 109 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): codigo_de_tributacao_do_produto_difali.
- Vínculo efmvepro (efmvepro): 0 de 45 linhas sem registro relacionado (empresa 1008).
- Vínculo efprodutos (efprodutos): 0 de 45 linhas sem registro relacionado (empresa 1008).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| codigo_de_tributacao_do_produto_difali | `codigo_tributacao_difali` | integer(4) |  |  | Código de tributação do produto DIFALI |
| base_calculo_difali | `base_calculo_difali` | numeric(13) |  |  | Base cálculo DIFALI |
| aliquota_difali | `aliquota_difali` | numeric(7) |  |  | Alíquota DIFALI |
| valor_difali | `valor_difali` | numeric(13) |  |  | Valor DIFALI |
| codigo_sequencial_do_recolhimento_difali | `i_recolhimento_difali` | integer(4) |  |  | Código Sequencial do Recolhimento - DIFALI |
| codigo_do_recolhimento_difali | `codigo_recolhimento_difali` | char(6) |  |  | Código do Recolhimento - DIFALI |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `codigo_de_tributacao_do_produto_difali` (eq/in), `codigo_sequencial_do_recolhimento_difali` (eq/in), `codigo_do_recolhimento_difali` (eq/in)

## efmvepro_ibs_iva

**Valorer IBS Estoque - Entradas** — tabela `EFMVEPRO_IBS_IVA` (6.777 linhas)

Valorer IBS Estoque - Entradas. 6.777 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.777 linhas, 7 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 687 linhas sem registro relacionado (empresa 1683).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo Empresa |
| codigo_entrada | `codi_ent` | integer(4) |  |  | Codigo Entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Codigo sequencial do estoque |
| codigo_cclasstrib | `i_cclasstrib` | char(6) |  |  | Codigo cClassTrib |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Calculo |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor | `valor` | numeric(13) |  |  | Valor |
| base_de_calculo_do_credito_presumido_ibs | `cred_presum_base_calculo` | numeric(13) |  |  | Base de cálculo do crédito presumido IBS |
| aliquota_do_credito_presumido_ibs | `cred_presum_aliquota` | numeric(5) |  |  | Alíquota do crédito presumido IBS |
| valor_do_credito_presumido_ibs | `cred_presum_valor` | numeric(13) |  |  | Valor do crédito presumido IBS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_cclasstrib` (eq/in)

## efmvepro_cbs_iva

**Valorer CBS Estoque - Entradas** — tabela `EFMVEPRO_CBS_IVA` (6.777 linhas)

Valorer CBS Estoque - Entradas. 6.777 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.777 linhas, 7 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 687 linhas sem registro relacionado (empresa 1683).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo Empresa |
| codigo_entrada | `codi_ent` | integer(4) |  |  | Codigo Entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Codigo sequencial do estoque |
| codigo_cclasstrib | `i_cclasstrib` | char(6) |  |  | Codigo cClassTrib |
| base_calculo | `base_calculo` | numeric(13) |  |  | Base Calculo |
| aliquota | `aliquota` | numeric(5) |  |  | Aliquota |
| valor | `valor` | numeric(13) |  |  | Valor |
| base_de_calculo_do_credito_presumido_cbs | `cred_presum_base_calculo` | numeric(13) |  |  | Base de cálculo do crédito presumido CBS |
| aliquota_do_credito_presumido_cbs | `cred_presum_aliquota` | numeric(5) |  |  | Alíquota do crédito presumido CBS |
| valor_do_credito_presumido_cbs | `cred_presum_valor` | numeric(13) |  |  | Valor do crédito presumido CBS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_cclasstrib` (eq/in)

## efmvepro_estadual_am

**Notas Fiscais de Entrada - Produtos - Estadual AM** — tabela `EFMVEPRO_ESTADUAL_AM` (1.887 linhas)

Notas Fiscais de Entrada - Produtos - Estadual AM. 1.887 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.887 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (4): codigo_de_tributacao_do_produto_dia, codigo_de_tributacao_do_produto_difali, codigo_de_tributacao_do_produto_icmsa, codigo_de_tributacao_do_produto_icmsst.
- Vínculo efmvepro (efmvepro): 0 de 1.887 linhas sem registro relacionado (empresa 955).
- Vínculo efprodutos (efprodutos): 0 de 1.887 linhas sem registro relacionado (empresa 955).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| possui_isencao_s_n | `dia_possui_isencao` | char(1) |  |  | Possui isenção (S/N) |
| codigo_de_tributacao_do_produto_dia | `dia_possui_isencao_codigo_tributacao` | integer(4) |  |  | Código de tributação do produto - DIA |
| codigo_de_tributacao_do_produto_difali | `difali_codigo_tributacao` | integer(4) |  |  | Código de tributação do produto - DIFALI |
| base_de_calculo_difali | `difali_base_calculo` | numeric(13) |  |  | Base de Cálculo - DIFALI |
| aliquota_difali | `difali_aliquota` | numeric(7) |  |  | Alíquota - DIFALI |
| valor_difali | `difali_valor` | numeric(13) |  |  | Valor - DIFALI |
| codigo_de_tributacao_do_produto_icmsa | `icms_antecipacao_codigo_tributacao` | integer(4) |  |  | Código de tributação do produto - ICMSA |
| base_de_calculo_icmsa | `icms_antecipacao_base_calculo` | numeric(13) |  |  | Base de Cálculo - ICMSA |
| aliquota_icmsa | `icms_antecipacao_aliquota` | numeric(7) |  |  | Alíquota - ICMSA |
| valor_icmsa | `icms_antecipacao_valor` | numeric(13) |  |  | Valor - ICMSA |
| codigo_de_tributacao_do_produto_icmsst | `icms_st_antecipacao_total_codigo_tributacao` | integer(4) |  |  | Código de tributação do produto - ICMSST |
| base_de_calculo_icmsst | `icms_st_antecipacao_total_base_calculo` | numeric(13) |  |  | Base de Cálculo - ICMSST |
| aliquota_icmsst | `icms_st_antecipacao_total_aliquota` | numeric(7) |  |  | Alíquota - ICMSST |
| valor_icmsst | `icms_st_antecipacao_total_valor` | numeric(13) |  |  | Valor - ICMSST |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `possui_isencao_s_n` (eq/in), `codigo_de_tributacao_do_produto_dia` (eq/in), `codigo_de_tributacao_do_produto_difali` (eq/in), `codigo_de_tributacao_do_produto_icmsa` (eq/in), `codigo_de_tributacao_do_produto_icmsst` (eq/in)

## efmvepro_icmsa

**Notas Fiscais de Entrada - Produtos - ICMS Antecipado** — tabela `EFMVEPRO_ICMSA` (1.182 linhas)

Notas Fiscais de Entrada - Produtos - ICMS Antecipado. 1.182 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.182 linhas, 10 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 110 linhas sem registro relacionado (empresa 501).
- Vínculo efprodutos (efprodutos): 0 de 110 linhas sem registro relacionado (empresa 501).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| codigo_sequencial_do_recolhimento_icms_a | `i_recolhimento_icmsa` | integer(4) |  |  | Código Sequencial do Recolhimento - ICMS Antecipado |
| codigo_do_recolhimento_icms_antecipado | `codigo_recolhimento_icmsa` | char(6) |  |  | Código do Recolhimento - ICMS Antecipado |
| codigo_de_tributacao_do_produto_icms_ant | `codigo_tributacao_icmsa` | integer(4) |  |  | Código de tributação do produto ICMS Antecipado |
| base_calculo_icms_antecipado | `base_calculo_icmsa` | numeric(13) |  |  | Base cálculo ICMS Antecipado |
| aliquota_icms_antecipado | `aliquota_icmsa` | numeric(7) |  |  | Alíquota ICMS Antecipado |
| valor_icms_antecipado | `valor_icmsa` | numeric(13) |  |  | Valor ICMS Antecipado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `codigo_sequencial_do_recolhimento_icms_a` (eq/in), `codigo_do_recolhimento_icms_antecipado` (eq/in), `codigo_de_tributacao_do_produto_icms_ant` (eq/in)

## efmvepro_icms_st_retido

**Notas Fiscais de Entrada - Produtos - ICMS ST Retido** — tabela `EFMVEPRO_ICMS_ST_RETIDO` (931 linhas)

Notas Fiscais de Entrada - Produtos - ICMS ST Retido. 931 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP, CODI_PDI.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP, CODI_PDI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 931 linhas, 13 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 61 linhas sem registro relacionado (empresa 1223).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| icms_st_retido_base_calculo | `icms_st_retido_base_calculo` | numeric(13) |  |  | ICMS ST Retido - Base Cálculo |
| icms_st_retido_valor | `icms_st_retido_valor` | numeric(13) |  |  | ICMS ST Retido - Valor |
| icms_st_retido_montante_imposto_presumid | `icms_st_retido_montante_imposto_presumido` | numeric(13) |  |  | ICMS ST Retido - Montante Imposto Presumido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_icmsi

**Notas Fiscais de Entrada - Produtos - ICMS Importação** — tabela `EFMVEPRO_ICMSI` (789 linhas)

Notas Fiscais de Entrada - Produtos - ICMS Importação. 789 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 789 linhas, 11 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 54 linhas sem registro relacionado (empresa 1566).
- Vínculo efprodutos (efprodutos): 0 de 54 linhas sem registro relacionado (empresa 1566).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_calculo_icms_importacao | `base_calculo_icmsi` | numeric(13) |  |  | Base cálculo ICMS Importação |
| aliquota_icms_importacao | `aliquota_icmsi` | numeric(7) |  |  | Alíquota ICMS Importação |
| valor_icms_importacao | `valor_icmsi` | numeric(13) |  |  | Valor ICMS Importação |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_icms_stat

**Notas Fiscais de Entrada - Produtos - ICMS STAT** — tabela `EFMVEPRO_ICMS_STAT` (727 linhas)

Notas Fiscais de Entrada - Produtos - ICMS STAT. 727 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 727 linhas, 35 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 9 linhas sem registro relacionado (empresa 929).
- Vínculo efprodutos (efprodutos): 0 de 9 linhas sem registro relacionado (empresa 929).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| codigo_de_tributacao_do_produto | `codigo_tributacao` | integer(4) |  |  | Código de tributação do produto |
| base_de_calculo_icms_st_antecipacao_tota | `base_calculo` | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| aliquota_icms_st_antecipacao_total | `aliquota` | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| valor_icms_st_antecipacao_total | `valor_imposto` | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| codigo_do_recolhimento_substituicao_trib | `codigo_recolhimento_stat` | char(6) |  |  | Código do Recolhimento - Substituição Tributária |
| codigo_sequencial_do_recolhimento_substi | `i_recolhimento_stat` | integer(4) |  |  | Código Sequencial do Recolhimento - Substituição Tributária |
| base_calculo_st | `base_calculo_st` | char(1) |  |  | Base cálculo ST |
| valor_icms_proprio | `valor_icms_proprio` | numeric(13) |  |  | Valor ICMS Próprio |
| valor_icms_retido | `valor_icms_retido` | numeric(13) |  |  | Valor ICMS Retido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `codigo_de_tributacao_do_produto` (eq/in), `codigo_do_recolhimento_substituicao_trib` (eq/in), `codigo_sequencial_do_recolhimento_substi` (eq/in), `base_calculo_st` (eq/in)

## efmvepro_estadual_mg

**Notas Fiscais de Entrada - Produtos - Estadual MG** — tabela `EFMVEPRO_ESTADUAL_MG` (170 linhas)

Notas Fiscais de Entrada - Produtos - Estadual MG. 170 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 170 linhas, 4 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 69 linhas sem registro relacionado (empresa 1473).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| base_de_calculo_difali | `difali_base_calculo` | numeric(13) |  |  | Base de Cálculo - DIFALI |
| aliquota_difali | `difali_aliquota` | numeric(7) |  |  | Alíquota - DIFALI |
| valor_difali | `difali_valor` | numeric(13) |  |  | Valor - DIFALI |
| base_de_calculo_icms_st_antecipacao_tota | `icms_st_antecipacao_total_base_calculo` | numeric(13) |  |  | Base de Cálculo - ICMS ST Antecipação Total |
| aliquota_icms_st_antecipacao_total | `icms_st_antecipacao_total_aliquota` | numeric(7) |  |  | Alíquota - ICMS ST Antecipação Total |
| valor_icms_st_antecipacao_total | `icms_st_antecipacao_total_valor` | numeric(13) |  |  | Valor - ICMS ST Antecipação Total |
| base_de_calculo_recali | `recali_base_calculo` | numeric(13) |  |  | Base de Cálculo - RECALI |
| aliquota_recali | `recali_aliquota` | numeric(5) |  |  | Alíquota - RECALI |
| valor_recali | `recali_valor` | numeric(13) |  |  | Valor - RECALI |
| codigo_recolhimento_recali | `recali_codigo_recolhimento` | char(6) |  |  | Código Recolhimento - RECALI |
| sequencial_recolhimento_recali | `recali_i_recolhimento` | integer(4) |  |  | Sequencial Recolhimento - RECALI |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_recolhimento_recali` (eq/in)

## efmvepro_fem_st_mg

**Notas Fiscais de Entrada - Produtos - FEM-ST/MG** — tabela `EFMVEPRO_FEM_ST_MG` (170 linhas)

Notas Fiscais de Entrada - Produtos - FEM-ST/MG. 170 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 170 linhas, 4 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 69 linhas sem registro relacionado (empresa 1473).
- Vínculo efprodutos (efprodutos): 0 de 69 linhas sem registro relacionado (empresa 1473).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| entrada | `codi_ent` | integer(4) |  |  | Entrada |
| sequencial | `nume_mep` | integer(4) |  |  | Sequencial |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo | `base_calculo_fem_st` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota_fem_st` | numeric(5) |  |  | Alíquota |
| valor | `valor_fem_st` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `entrada` (eq/in), `sequencial` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_estadual_ro

**Notas Fiscais de Entrada - Produtos - Estadual RO** — tabela `EFMVEPRO_ESTADUAL_RO` (110 linhas)

Notas Fiscais de Entrada - Produtos - Estadual RO. 110 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 110 linhas, 1 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 110 linhas sem registro relacionado (empresa 501).
- Vínculo efprodutos (efprodutos): 0 de 110 linhas sem registro relacionado (empresa 501).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_saida | `codi_ent` | integer(4) |  |  | Código sequencial da nota de saída |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo_icms_antecipado | `bc_icmsa_mep` | numeric(13) |  |  | Base de cálculo ICMS Antecipado |
| aiquota_icms_antecipado | `aliq_icmsa_mep` | numeric(7) |  |  | Aíquota ICMS Antecipado |
| valor_icms_antecipado | `valor_icmsa_mep` | numeric(13) |  |  | Valor ICMS Antecipado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_saida` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_extemporaneo_piscofins

**Notas Fiscais de Entrada - Produtos - Extemporâneo PIS COFINS** — tabela `EFMVEPRO_EXTEMPORANEO_PISCOFINS` (56 linhas)

Notas Fiscais de Entrada - Produtos - Extemporâneo PIS COFINS. 56 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP, CODI_IMP, TIPO_CREDITO.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP, CODI_IMP, TIPO_CREDITO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 56 linhas, 3 empresa(s), COMPETENCIA de 2018-07-01 a 2026-06-01.
- Vínculo efmvepro (efmvepro): 0 de 2 linhas sem registro relacionado (empresa 604).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| entrada | `codi_ent` | integer(4) |  |  | Entrada |
| sequencial | `nume_mep` | integer(4) |  |  | Sequencial |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |
| tipo_de_credito | `tipo_credito` | integer(4) |  |  | Tipo de crédito |
| receita_cumulativa | `receita_cumulativa` | numeric(13) |  |  | Receita cumulativa |
| receita_nao_cumulativa | `receita_nao_cumulativa` | numeric(13) |  |  | Receita não cumulativa |
| interna_tributada | `interna_tributada` | numeric(13) |  |  | Interna tributada |
| interna_nao_tributada | `interna_nao_tributada` | numeric(13) |  |  | Interna não tributada |
| externa | `externa` | numeric(13) |  |  | Externa |
| competencia | `competencia` | date(4) |  |  | Competencia |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `entrada` (eq/in), `sequencial` (eq/in), `imposto` (eq/in), `tipo_de_credito` (eq/in), `competencia` (entre/gte/lte)

## efmvepro_federal

**Valor ICMS desonerado Estoque** — tabela `EFMVEPRO_FEDERAL` (39 linhas)

Valor ICMS desonerado Estoque. 39 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 39 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): motivo_desoneracao.
- Vínculo efmvepro (efmvepro): 0 de 35 linhas sem registro relacionado (empresa 955).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| valor_icms_desonerado | `valor_icms_desonerado` | numeric(13) |  |  | Valor ICMS desonerado |
| motivo_desoneracao | `i_motivo_desoneracao` | integer(4) |  |  | Motivo Desoneração |
| base_de_calculo_icms_diferido | `base_calculo_icms_diferido` | numeric(13) |  |  | Base de Cálculo ICMS Diferido |
| percentual_icms_diferido | `percentual_icms_diferido` | numeric(5) |  |  | Percentual ICMS Diferido |
| valor_icms_diferido | `valor_icms_diferido` | numeric(13) |  |  | Valor ICMS Diferido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `motivo_desoneracao` (eq/in)

## efmvepro_difal_nc

**Notas Fiscais de Entrada - Produtos - DIFAL NC** — tabela `EFMVEPRO_DIFAL_NC` (27 linhas)

Notas Fiscais de Entrada - Produtos - DIFAL NC. 27 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 27 linhas, 1 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 27 linhas sem registro relacionado (empresa 1676).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_calculo | `base_calculo` | numeric(15) |  |  | Base Cálculo |
| aliquota | `aliquota` | numeric(5) |  |  | Alíquota |
| valor_uf_origem | `valor_uf_origem` | numeric(15) |  |  | Valor UF Origem |
| valor_uf_destino | `valor_uf_destino` | numeric(15) |  |  | Valor UF Destino |
| valor_total | `valor_total` | numeric(15) |  |  | Valor Total |
| valor_fcp | `valor_fcp` | numeric(15) |  |  | Valor FCP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_mg_sub_apuracao

**Notas Fiscais de Entrada - Produtos - MG Sub Apuração** — tabela `EFMVEPRO_MG_SUB_APURACAO` (14 linhas)

Notas Fiscais de Entrada - Produtos - MG Sub Apuração. 14 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP, I_SUB_APURACAO.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP, I_SUB_APURACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14 linhas, 1 empresa(s), COMPETENCIA de 2026-02-07 a 2026-05-20.
- Vínculo efmvepro (efmvepro): 0 de 14 linhas sem registro relacionado (empresa 1473).
- Vínculo efprodutos (efprodutos): 0 de 14 linhas sem registro relacionado (empresa 1473).
- Vínculo eftabela_mg_sub_apuracao (EFTABELA_MG_SUB_APURACAO): 0 de 14 linhas sem registro relacionado (empresa 1473).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| sequencial | `i_sub_apuracao` | integer(4) |  |  | Sequencial |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo | `base_calculo` | numeric(13) |  |  | Base de cálculo |
| valor_icms | `valor_icms` | numeric(13) |  |  | Valor ICMS |
| proporcao | `proporcao` | numeric(5) |  |  | Proporção |
| competencia | `competencia` | date(4) |  |  | Competência |
| estorno_do_fem_de_mercadorias_devolvidas | `estorno_fem_mercadorias_credito_presumido_devolucao` | numeric(13) |  |  | Estorno do FEM de mercadorias devolvidas alcançadas pelo crédito presumido |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `eftabela_mg_sub_apuracao` → `EFTABELA_MG_SUB_APURACAO` por `i_sub_apuracao` = `i_sub_apuracao_mg`; colunas: `eftabela_mg_sub_apuracao_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `sequencial` (eq/in), `competencia` (entre/gte/lte), `codigo_do_produto` (eq/in)

## efmvepro_medicamento_lote

**Notas Fiscais de Entrada - Produtos - Medicamento - Lote** — tabela `EFMVEPRO_MEDICAMENTO_LOTE` (14 linhas)

Notas Fiscais de Entrada - Produtos - Medicamento - Lote. 14 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP, I_LOTE.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP, I_LOTE`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_FABRICACAO`
- **Ordem padrão:** `DATA_FABRICACAO desc`, `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14 linhas, 2 empresa(s), DATA_FABRICACAO de 2018-09-27 a 2018-10-31.
- Vínculo efmvepro (efmvepro): 0 de 12 linhas sem registro relacionado (empresa 418).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_sequencial_do_lote | `i_lote` | integer(4) |  |  | Código sequencial do lote |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| lote | `lote` | varchar(255) |  |  | Lote |
| qtd_item_lote | `quantidade_item_por_lote` | integer(4) |  |  | Qtd. item/lote |
| data_fabricacao | `data_fabricacao` | date(4) |  |  | Data Fabricação |
| data_validade | `data_validade` | date(4) |  |  | Data Validade |
| referencia_base_calculo | `referencia_base_calculo` | integer(4) |  |  | REF. BASE DE CÁLCULO (0 / 1 / 2 / 3 / 4 / 5 / 6) |
| preco_tab_max | `preco_tabelado_maximo` | numeric(13) |  |  | Preço Tab./Máx |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_sequencial_do_lote` (eq/in), `data_fabricacao` (entre/gte/lte), `data_validade` (entre/gte/lte), `codigo_do_produto` (eq/in), `lote` (contem/prefixo)

## efmvepro_estadual_es

**Notas Fiscais de Entrada - Produtos - Estadual ES** — tabela `EFMVEPRO_ESTADUAL_ES` (7 linhas)

Notas Fiscais de Entrada - Produtos - Estadual ES. 7 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): situacao_tributaria_dief.
- Vínculo efmvepro (efmvepro): 0 de 7 linhas sem registro relacionado (empresa 1575).
- Vínculo efprodutos (efprodutos): 0 de 7 linhas sem registro relacionado (empresa 1575).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo_difali | `difali_base_calculo` | numeric(13) |  |  | Base de Cálculo - DIFALI |
| aliquota_difali | `difali_aliquota` | numeric(7) |  |  | Alíquota - DIFALI |
| valor_difali | `difali_valor` | numeric(13) |  |  | Valor - DIFALI |
| situacao_tributaria_dief | `situacao_tributaria_dief_cafe_cru` | integer(4) |  |  | Situação Tributária DIEF |
| base_de_calculo_icms_complementar | `icms_complementar_base_calculo` | numeric(13) |  |  | Base de Calculo ICMS Complementar |
| aliquota_icms_complementar | `icms_complementar_aliquota` | numeric(5) |  |  | Aliquota - ICMS Complementar |
| valor_icms_complementar | `icms_complementar_valor` | numeric(13) |  |  | Valor - ICMS Complementar |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `situacao_tributaria_dief` (eq/in)

## efmvepro_estadual_sp

**Notas Fiscais de Entrada - Produtos - Estadual SP** — tabela `EFMVEPRO_ESTADUAL_SP` (6 linhas)

Notas Fiscais de Entrada - Produtos - Estadual SP. 6 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 6 linhas sem registro relacionado (empresa 1446).
- Vínculo efprodutos (efprodutos): 0 de 6 linhas sem registro relacionado (empresa 1446).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| icms_st_retido_base_de_calculo | `icms_st_retido_base_calculo` | numeric(13) |  |  | ICMS ST Retido - Base de Calculo |
| icms_st_retido_valor | `icms_st_retido_valor` | numeric(13) |  |  | ICMS ST Retido - Valor |
| possui_a_tag_preenchida_no_xml | `possui_tag_preenchida_xml` | char(1) |  |  | Possui a tag preenchida no XML |
| base_calculo_fcp_st | `base_calculo_fcp_st` | numeric(13) |  |  | Base calculo FCP ST |
| aliquota_fcp_st | `aliquota_fcp_st` | numeric(5) |  |  | Aliquota FCP ST |
| valor_fcp_st | `valor_fcp_st` | numeric(13) |  |  | Valor FCP ST |
| icms_st_retido_aliquota | `icms_st_retido_aliquota` | numeric(13) |  |  | ICMS ST Retido - Alíquota |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `possui_a_tag_preenchida_no_xml` (eq/in)

## efmvepro_estadual_rj

**Notas Fiscais de Entrada - Produtos - Estadual RJ** — tabela `EFMVEPRO_ESTADUAL_RJ` (5 linhas)

Notas Fiscais de Entrada - Produtos - Estadual RJ. 5 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas, 1 empresa(s).
- Vínculo efmvepro (efmvepro): 0 de 5 linhas sem registro relacionado (empresa 1574).
- Vínculo efprodutos (efprodutos): 0 de 5 linhas sem registro relacionado (empresa 1574).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo | `base_calculo_fecp` | numeric(13) |  |  | Base de cálculo |
| aliquota | `aliquota_fecp` | numeric(5) |  |  | Alíquota |
| valor | `valor_fecp` | numeric(13) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in)

## efmvepro_estadual_mt

**Notas Fiscais de Entrada - Produtos - Estadual MT** — tabela `EFMVEPRO_ESTADUAL_MT` (1 linhas)

Notas Fiscais de Entrada - Produtos - Estadual MT. 1 linhas no catálogo; chave: CODI_EMP, CODI_ENT, NUME_MEP.

- **Chave:** `CODI_EMP, CODI_ENT, NUME_MEP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_ENT asc`, `NUME_MEP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): sequencial_recolhimento_icmsa, codigo_recolhimento_icmsa.
- Vínculo efmvepro (efmvepro): 0 de 1 linhas sem registro relacionado (empresa 466).
- Vínculo efprodutos (efprodutos): 0 de 1 linhas sem registro relacionado (empresa 466).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_da_nota_de_entrada | `codi_ent` | integer(4) |  |  | Código sequencial da nota de entrada |
| codigo_sequencial_do_estoque | `nume_mep` | integer(4) |  |  | Código sequencial do estoque |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| base_de_calculo_icms | `icms_estimativa_simplificado_base_calculo` | numeric(13) |  |  | Base de cálculo ICMS |
| aliquota_icms | `icms_estimativa_simplificado_aliquota` | numeric(5) |  |  | Alíquota ICMS |
| valor_icms | `icms_estimativa_simplificado_valor` | numeric(13) |  |  | Valor ICMS |
| base_de_calculo_icms_st | `icms_st_estimativa_simplificado_base_calculo` | numeric(13) |  |  | Base de cálculo ICMS ST |
| aliquota_icms_st | `icms_st_estimativa_simplificado_aliquota` | numeric(5) |  |  | Alíquota ICMS ST |
| valor_icms_st | `icms_st_estimativa_simplificado_valor` | numeric(13) |  |  | Valor ICMS ST |
| base_de_calculo_icmsa | `icmsa_base_calculo` | numeric(13) |  |  | Base de cálculo ICMSA |
| aliquota_icmsa | `icmsa_aliquota` | numeric(13) |  |  | Alíquota ICMSA |
| valor_icmsa | `icmsa_valor` | numeric(13) |  |  | Valor ICMSA |
| sequencial_recolhimento_icmsa | `i_recolhimento_icmsa` | integer(4) |  |  | Sequencial recolhimento ICMSA |
| codigo_recolhimento_icmsa | `codigo_recolhimento_icmsa` | char(6) |  |  | Código recolhimento ICMSA |
| base_de_calculo_fecep_mt | `fecep_mt_icms_es_base_calculo` | numeric(13) |  |  | Base de cálculo FECEP-MT |
| aliquota_fecep_mt | `fecep_mt_icms_es_aliquota` | numeric(5) |  |  | Alíquota FECEP-MT |
| valor_fecep_mt | `fecep_mt_icms_es_valor` | numeric(13) |  |  | Valor FECEP-MT |
| fecep_mt_icms_st_base_calculo | `fecep_mt_icms_st_base_calculo` | numeric(13) |  |  | FECEP-MT - ICMS ST - Base Cálculo |
| fecep_mt_icms_st_aliquota | `fecep_mt_icms_st_aliquota` | numeric(5) |  |  | FECEP-MT - ICMS ST - Alíquota |
| fecep_mt_icms_st_valor | `fecep_mt_icms_st_valor` | numeric(13) |  |  | FECEP-MT - ICMS ST - Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efmvepro` → `efmvepro` por `codi_emp` = `codi_emp` e `codi_ent` = `codi_ent` e `nume_mep` = `nume_mep`; colunas: `efmvepro_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_sequencial_da_nota_de_entrada` (eq/in), `codigo_sequencial_do_estoque` (eq/in), `codigo_do_produto` (eq/in), `sequencial_recolhimento_icmsa` (eq/in), `codigo_recolhimento_icmsa` (eq/in)

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

