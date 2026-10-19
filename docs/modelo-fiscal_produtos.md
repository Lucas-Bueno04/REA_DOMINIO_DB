# Modelo — Fiscal - produtos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_produtos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

13 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efprodutos_valor_unitario](#efprodutos_valor_unitario) | `EFPRODUTOS_VALOR_UNITARIO` | 222.611 | medio | empresa |
| [efprodutos_importacao_entradas_produtos](#efprodutos_importacao_entradas_produtos) | `EFPRODUTOS_IMPORTACAO_ENTRADAS_PRODUTOS` | 121.876 | medio | empresa |
| [efprodutos_importacao_entradas](#efprodutos_importacao_entradas) | `EFPRODUTOS_IMPORTACAO_ENTRADAS` | 121.652 | medio | empresa |
| [efprodutos_fator_conversao](#efprodutos_fator_conversao) | `EFPRODUTOS_FATOR_CONVERSAO` | 15.295 | medio | empresa |
| [efprodutos_saldos](#efprodutos_saldos) | `efprodutos_saldos` | 4.106 | pequeno | empresa |
| [efprodutos_mssefaz](#efprodutos_mssefaz) | `efprodutos_mssefaz` | 399 | pequeno | — |
| [efprodutos_importacao_saidas](#efprodutos_importacao_saidas) | `EFPRODUTOS_IMPORTACAO_SAIDAS` | 260 | pequeno | empresa |
| [efprodutos_pasefa](#efprodutos_pasefa) | `efprodutos_pasefa` | 197 | pequeno | — |
| [efprodutos_alteracao](#efprodutos_alteracao) | `EFPRODUTOS_ALTERACAO` | 127 | pequeno | empresa |
| [efprodutos_importacao_cfops](#efprodutos_importacao_cfops) | `EFPRODUTOS_IMPORTACAO_CFOPS` | 66 | pequeno | empresa |
| [efprodutos_importacao_cfops_cfop_saida](#efprodutos_importacao_cfops_cfop_saida) | `EFPRODUTOS_IMPORTACAO_CFOPS_CFOP_SAIDA` | 66 | pequeno | empresa |
| [efprodutos_dam_am](#efprodutos_dam_am) | `efprodutos_dam_am` | 12 | pequeno | — |
| [efprodutos_inss_folha](#efprodutos_inss_folha) | `EFPRODUTOS_INSS_FOLHA` | 5 | pequeno | empresa |

## efprodutos_valor_unitario

**Produtos - Cadastros - Valor unitário** — tabela `EFPRODUTOS_VALOR_UNITARIO` (222.611 linhas)

Produtos - Cadastros - Valor unitário. 222.611 linhas no catálogo; chave: CODI_EMP, CODI_PDI, SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_PDI, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `CODI_PDI asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 222.663 linhas, 472 empresa(s), VIGENCIA de 2013-01-01 a 2026-09-01.
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 726).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| data | `vigencia` | date(4) |  |  | Data |
| valor_unitario | `valor_unitario` | numeric(15) |  |  | Valor unitário |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `codigo_do_produto` (eq/in), `sequencial` (eq/in), `data` (entre/gte/lte)

## efprodutos_importacao_entradas_produtos

**Tabela de relacionamento de importação de produtos - Entradas - Fornecedores - Produtos** — tabela `EFPRODUTOS_IMPORTACAO_ENTRADAS_PRODUTOS` (121.876 linhas)

Tabela de relacionamento de importação de produtos - Entradas - Fornecedores - Produtos. 121.876 linhas no catálogo; chave: CODI_EMP, CODI_PDI, SEQUENCIAL, CODI_PDI_IMPORTACAO.

- **Chave:** `CODI_EMP, CODI_PDI, SEQUENCIAL, CODI_PDI_IMPORTACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 121.889 linhas, 210 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| produto_importacao | `codi_pdi_importacao` | char(60) |  |  | Produto importação |

**Filtros:** `produto` (eq/in), `sequencial` (eq/in), `produto_importacao` (eq/in)

## efprodutos_importacao_entradas

**Tabela de relacionamento de importação de produtos - Entradas - Fornecedores** — tabela `EFPRODUTOS_IMPORTACAO_ENTRADAS` (121.652 linhas)

Tabela de relacionamento de importação de produtos - Entradas - Fornecedores. 121.652 linhas no catálogo; chave: CODI_EMP, CODI_PDI, SEQUENCIAL.

- **Chave:** `CODI_EMP, CODI_PDI, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 121.665 linhas, 210 empresa(s).
- Vínculo geempre (geempre): 0 de 165 linhas sem registro relacionado (empresa 1733).
- Vínculo efprodutos (efprodutos): 0 de 165 linhas sem registro relacionado (empresa 1733).
- Vínculo effornece (effornece): 0 de 165 linhas sem registro relacionado (empresa 1733).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| fornecedor | `codi_for` | integer(4) |  |  | Fornecedor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `effornece` → `effornece` por `codi_emp` = `codi_emp` e `codi_for` = `codi_for`; colunas: `effornece_nome`

**Filtros:** `produto` (eq/in), `sequencial` (eq/in), `fornecedor` (eq/in)

## efprodutos_fator_conversao

**Produtos - Cadastro - Fator de conversão** — tabela `EFPRODUTOS_FATOR_CONVERSAO` (15.295 linhas)

Produtos - Cadastro - Fator de conversão. 15.295 linhas no catálogo; chave: CODI_PDI, CODI_EMP, CODIGO_UNIDADE.

- **Chave:** `CODI_PDI, CODI_EMP, CODIGO_UNIDADE`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `CODIGO_UNIDADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15.297 linhas, 136 empresa(s).
- Vínculo efprodutos (efprodutos): 0 de 25 linhas sem registro relacionado (empresa 1022).
- Vínculo efunidades (efunidades): 0 de 25 linhas sem registro relacionado (empresa 1022).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| produto | `codi_pdi` | char(14) |  |  | Produto |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo | `codigo_unidade` | integer(4) |  |  | Código |
| unidade | `unidade` | char(6) |  |  | Unidade |
| fator_de_conversao | `fator_conversao` | numeric(15) |  |  | Fator de conversão |
| codigo_de_barras | `codigo_barras` | char(16) |  |  | Código de barras |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `efunidades` → `efunidades` por `codigo_unidade` = `codigo_unidade`; colunas: `efunidades_nome`

**Filtros:** `produto` (eq/in), `codigo` (eq/in), `unidade` (eq/in), `codigo_de_barras` (eq/in)

## efprodutos_saldos

**Produtos - Cadastro - Saldos** — tabela `efprodutos_saldos` (4.106 linhas)

Produtos - Cadastro - Saldos. 4.106 linhas no catálogo; chave: codi_pdi, codi_emp, data_sal.

- **Chave:** `codi_pdi, codi_emp, data_sal`
- **Empresa:** `codi_emp`
- **Período:** `data_sal`
- **Ordem padrão:** `data_sal desc`, `codi_pdi asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.106 linhas, 39 empresa(s), data_sal de 2017-12-31 a 2024-12-31.
- Vínculo efprodutos (efprodutos): 0 de 29 linhas sem registro relacionado (empresa 1575).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| produto | `codi_pdi` | char(14) |  |  | Produto |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| data_do_saldo | `data_sal` | date(4) |  |  | Data do saldo |
| quantidade_final | `qfin_sal` | numeric(13) |  |  | Quantidade final |
| valor_final | `vlfin_sal` | numeric(14) |  |  | Valor final |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_unitario | `vuni_sal` | numeric(16) |  |  | Valor unitario |
| icms_recuperavel | `icms_recuperavel` | numeric(13) |  |  | ICMS Recuperável |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `produto` (eq/in), `data_do_saldo` (eq/in)

## efprodutos_mssefaz

**Produtos MS SEFAZ** — tabela `efprodutos_mssefaz` (399 linhas)

Produtos MS SEFAZ. 399 linhas no catálogo; chave: codigo_pms.

- **Chave:** `codigo_pms`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `codigo_pms asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 399 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_pms` | integer(4) |  |  | Codigo |
| descricao | `descricao_pms` | varchar(60) |  |  | Descricao |
| unidade | `unidade_pms` | char(10) |  |  | Unidade |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo), `unidade` (eq/in)

## efprodutos_importacao_saidas

**Tabela de relacionamento de importação de produtos - Saídas** — tabela `EFPRODUTOS_IMPORTACAO_SAIDAS` (260 linhas)

Tabela de relacionamento de importação de produtos - Saídas. 260 linhas no catálogo; chave: CODI_EMP, CODI_PDI, CODI_PDI_IMPORTACAO.

- **Chave:** `CODI_EMP, CODI_PDI, CODI_PDI_IMPORTACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `CODI_PDI_IMPORTACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 260 linhas, 12 empresa(s).
- Vínculo geempre (geempre): 0 de 7 linhas sem registro relacionado (empresa 614).
- Vínculo efprodutos (efprodutos): 0 de 7 linhas sem registro relacionado (empresa 614).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| produto_importacao | `codi_pdi_importacao` | char(60) |  |  | Produto importação |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `produto` (eq/in), `produto_importacao` (eq/in)

## efprodutos_pasefa

**Tabela de Produtos SEFA - PA** — tabela `efprodutos_pasefa` (197 linhas)

Tabela de Produtos SEFA - PA. 197 linhas no catálogo; chave: codigo.

- **Chave:** `codigo`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `codigo asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 197 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Codigo |
| descricao | `descricao` | char(128) |  |  | Descricao |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## efprodutos_alteracao

**Produtos - Alterações - Cadastro** — tabela `EFPRODUTOS_ALTERACAO` (127 linhas)

Produtos - Alterações - Cadastro. 127 linhas no catálogo; chave: CODI_EMP, CODI_PDI, DATA_ALTERACAO, CAMPO.

- **Chave:** `CODI_EMP, CODI_PDI, DATA_ALTERACAO, CAMPO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ALTERACAO`
- **Ordem padrão:** `DATA_ALTERACAO desc`, `CODI_PDI asc`, `CAMPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 127 linhas, 36 empresa(s), DATA_ALTERACAO de 2017-10-01 a 2026-08-04.
- Vínculo efprodutos (efprodutos): 0 de 2 linhas sem registro relacionado (empresa 808).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| data_da_alteracao | `data_alteracao` | date(4) |  |  | Data da alteração |
| campo_alterado | `campo` | integer(4) |  |  | Campo alterado |
| valor_anterior_a_alteracao | `de` | varchar(255) |  |  | Valor anterior a alteração |
| valor_posterior_a_alteracao | `para` | varchar(255) |  |  | Valor posterior a alteração |
| competencia_geracao_registro_0205 | `competencia_geracao_registro_0205` | date(4) |  |  | Competência de geração do registro 0205 |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`

**Filtros:** `produto` (eq/in), `data_da_alteracao` (eq/in), `campo_alterado` (eq/in), `competencia_geracao_registro_0205` (entre/gte/lte), `valor_anterior_a_alteracao` (contem/prefixo), `valor_posterior_a_alteracao` (contem/prefixo)

## efprodutos_importacao_cfops

**Produtos - Cadastro - Importação - Relacionamento de CFOPs** — tabela `EFPRODUTOS_IMPORTACAO_CFOPS` (66 linhas)

Produtos - Cadastro - Importação - Relacionamento de CFOPs. 66 linhas no catálogo; chave: CODI_EMP, CODI_PDI, I_CFOP_ENTRADA.

- **Chave:** `CODI_EMP, CODI_PDI, I_CFOP_ENTRADA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `I_CFOP_ENTRADA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 66 linhas, 2 empresa(s).
- Vínculo efnatureza (efnatureza): 0 de 63 linhas sem registro relacionado (empresa 9999).
- Vínculo efprodutos (efprodutos): 0 de 63 linhas sem registro relacionado (empresa 9999).
- Vínculo geempre (geempre): 0 de 63 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| sequencial_do_cfop_de_entrada | `i_cfop_entrada` | integer(4) |  |  | Sequencial do CFOP de entrada |
| cfop_de_entrada | `cfop` | integer(4) |  |  | CFOP de entrada |
| versao_do_cfop_de_entrada | `versao_cfop` | smallint(2) |  |  | Versão do CFOP de entrada |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efnatureza` → `efnatureza` por `cfop` = `codi_nat` e `versao_cfop` = `versao_nat`; colunas: `efnatureza_nome`
- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `produto` (eq/in), `sequencial_do_cfop_de_entrada` (eq/in)

## efprodutos_importacao_cfops_cfop_saida

**Produtos - Cadastro - Importação - Relacionamento de CFOPs - CFOP saída** — tabela `EFPRODUTOS_IMPORTACAO_CFOPS_CFOP_SAIDA` (66 linhas)

Produtos - Cadastro - Importação - Relacionamento de CFOPs - CFOP saída. 66 linhas no catálogo; chave: CODI_EMP, CODI_PDI, I_CFOP_ENTRADA, I_CFOP_SAIDA.

- **Chave:** `CODI_EMP, CODI_PDI, I_CFOP_ENTRADA, I_CFOP_SAIDA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `I_CFOP_ENTRADA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 66 linhas, 2 empresa(s).
- Vínculo efnatureza (efnatureza): 0 de 63 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| sequencial_do_cfop_de_entrada | `i_cfop_entrada` | integer(4) |  |  | Sequencial do CFOP de entrada |
| sequencial_do_cfop_de_saida | `i_cfop_saida` | integer(4) |  |  | Sequencial do CFOP de saída |
| cfop_de_saida | `cfop` | integer(4) |  |  | CFOP de saída |
| versao_do_cfop_de_saida | `versao_cfop` | smallint(2) |  |  | Versão do CFOP de saída |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efnatureza` → `efnatureza` por `cfop` = `codi_nat` e `versao_cfop` = `versao_nat`; colunas: `efnatureza_nome`

**Filtros:** `produto` (eq/in), `sequencial_do_cfop_de_entrada` (eq/in), `sequencial_do_cfop_de_saida` (eq/in)

## efprodutos_dam_am

**Codigo dos produtos na DAM - AM** — tabela `efprodutos_dam_am` (12 linhas)

Codigo dos produtos na DAM - AM. 12 linhas no catálogo; chave: codigo.

- **Chave:** `codigo`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `codigo asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 12 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_produto | `codigo` | integer(4) |  |  | Codigo do produto |
| descricao | `descricao` | char(128) |  |  | Descricao |

**Filtros:** `codigo_do_produto` (eq/in), `descricao` (contem/prefixo)

## efprodutos_inss_folha

**Produtos - Cadastro - INSS folha** — tabela `EFPRODUTOS_INSS_FOLHA` (5 linhas)

Produtos - Cadastro - INSS folha. 5 linhas no catálogo; chave: CODI_EMP, CODI_PDI, I_ATIVIDADE_INSS_FOLHA.

- **Chave:** `CODI_EMP, CODI_PDI, I_ATIVIDADE_INSS_FOLHA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_FINAL`
- **Ordem padrão:** `VIGENCIA_FINAL desc`, `CODI_PDI asc`, `I_ATIVIDADE_INSS_FOLHA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas, 4 empresa(s), VIGENCIA_FINAL de 2050-12-31 a 2050-12-31.
- Vínculo efprodutos (efprodutos): 0 de 1 linhas sem registro relacionado (empresa 909).
- Vínculo eftabela_atividade_servi (EFTABELA_ATIVIDADE_SERVICO_FOLHA): 0 de 1 linhas sem registro relacionado (empresa 909).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_produto | `codi_pdi` | char(14) |  |  | Código do produto |
| codigo_da_atividade | `i_atividade_inss_folha` | char(8) |  |  | Código da atividade |
| aliquota | `aliquota` | numeric(7) |  |  | Alíquota |
| vigencia_final | `vigencia_final` | date(4) |  |  | Vigência Final |
| vigencia_inicial | `vigencia_inicial` | date(4) |  |  | Vigência Inicial |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efprodutos` → `efprodutos` por `codi_pdi` = `codi_pdi` e `codi_emp` = `codi_emp`; colunas: `efprodutos_nome`
- `eftabela_atividade_servi` → `EFTABELA_ATIVIDADE_SERVICO_FOLHA` por `i_atividade_inss_folha` = `i_atividade`; colunas: `eftabela_atividade_servi_nome`

**Filtros:** `codigo_do_produto` (eq/in), `codigo_da_atividade` (eq/in), `vigencia_final` (entre/gte/lte), `vigencia_inicial` (entre/gte/lte)

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

