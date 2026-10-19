# Modelo — Fiscal - piscofins (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_piscofins.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efpiscofins_outros_saldo_retencao](#efpiscofins_outros_saldo_retencao) | `EFPISCOFINS_OUTROS_SALDO_RETENCAO` | 26 | pequeno | empresa |
| [efpiscofins_outros_saldo_retencao_item](#efpiscofins_outros_saldo_retencao_item) | `EFPISCOFINS_OUTROS_SALDO_RETENCAO_ITEM` | 26 | pequeno | empresa |
| [efpiscofins_apropriacao_direta_credito](#efpiscofins_apropriacao_direta_credito) | `EFPISCOFINS_APROPRIACAO_DIRETA_CREDITO` | 15 | pequeno | empresa |
| [efpiscofins_apropriacao_direta_credito_vigencia](#efpiscofins_apropriacao_direta_credito_vigencia) | `EFPISCOFINS_APROPRIACAO_DIRETA_CREDITO_VIGENCIA` | 15 | pequeno | empresa |

## efpiscofins_outros_saldo_retencao

**Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções** — tabela `EFPISCOFINS_OUTROS_SALDO_RETENCAO` (26 linhas)

Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções. 26 linhas no catálogo; chave: CODI_EMP, I_COMPENSACAO_RETENCAO.

- **Chave:** `CODI_EMP, I_COMPENSACAO_RETENCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_COMPENSACAO_RETENCAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 26 linhas, 2 empresa(s), COMPETENCIA de 2024-09-01 a 2025-08-01.
- Vínculo geempre (geempre): 0 de 20 linhas sem registro relacionado (empresa 1558).
- Vínculo geimposto (geimposto): 0 de 20 linhas sem registro relacionado (empresa 1558).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_sequencial | `i_compensacao_retencao` | integer(4) |  |  | Código sequencial |
| competencia | `competencia` | date(4) |  |  | Competência |
| imposto | `codi_imp` | integer(4) |  |  | Imposto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `geimposto` → `geimposto` por `codi_emp` = `codi_emp` e `codi_imp` = `codi_imp`; colunas: `geimposto_nome`

**Filtros:** `codigo_sequencial` (eq/in), `competencia` (entre/gte/lte), `imposto` (eq/in)

## efpiscofins_outros_saldo_retencao_item

**Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções - Retenções** — tabela `EFPISCOFINS_OUTROS_SALDO_RETENCAO_ITEM` (26 linhas)

Saldo de Retenções PIS/COFINS/Outros Saldos de Retenções - Retenções. 26 linhas no catálogo; chave: CODI_EMP, I_COMPENSACAO_RETENCAO, PERIODO_APURACAO, NATUREZA_RETENCAO.

- **Chave:** `CODI_EMP, I_COMPENSACAO_RETENCAO, PERIODO_APURACAO, NATUREZA_RETENCAO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO_APURACAO`
- **Ordem padrão:** `PERIODO_APURACAO desc`, `I_COMPENSACAO_RETENCAO asc`, `NATUREZA_RETENCAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 26 linhas, 2 empresa(s), PERIODO_APURACAO de 2024-09-01 a 2025-08-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| codigo_sequencial | `i_compensacao_retencao` | integer(4) |  |  | Código sequencial |
| periodo_da_retencao | `periodo_apuracao` | date(4) |  |  | Período da retenção |
| natureza_da_retencao | `natureza_retencao` | integer(4) |  |  | Natureza da retenção |
| valor_total_da_retencao | `valor_total_retencao` | numeric(13) |  |  | Valor total da retenção |
| valor_ja_aproveitado | `valor_ja_aproveitado` | numeric(13) |  |  | Valor já aproveitado |
| valor_utilizado_mediante_restituicao | `valor_utilizado_mediante_restituicao` | numeric(13) |  |  | Valor utilizado mediante restituição |
| valor_utilizado_mediante_dcomp | `valor_utilizado_mediante_dcomp` | numeric(13) |  |  | Valor utilizado mediante DCOMP |
| valor_da_retencao_disponivel | `valor_retencao_disponivel` | numeric(13) |  |  | Valor da retenção disponível |

**Filtros:** `codigo_sequencial` (eq/in), `periodo_da_retencao` (eq/in), `natureza_da_retencao` (eq/in)

## efpiscofins_apropriacao_direta_credito

**Apropriação Direta de Créditos de PIS e COFINS - Geral** — tabela `EFPISCOFINS_APROPRIACAO_DIRETA_CREDITO` (15 linhas)

Apropriação Direta de Créditos de PIS e COFINS - Geral. 15 linhas no catálogo; chave: CODI_EMP, I_APROPRIACAO.

- **Chave:** `CODI_EMP, I_APROPRIACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_APROPRIACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15 linhas, 15 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): sequencial_do_scp.
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1013).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_apropriacao` | integer(4) |  |  | Sequencial |
| descricao | `descricao` | varchar(60) |  |  | Descrição |
| sequencial_do_scp | `i_scp` | integer(4) |  |  | Sequencial do SCP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `descricao` (contem/prefixo), `sequencial_do_scp` (eq/in)

## efpiscofins_apropriacao_direta_credito_vigencia

**Apropriação Direta de Créditos de PIS e COFINS - Vigência** — tabela `EFPISCOFINS_APROPRIACAO_DIRETA_CREDITO_VIGENCIA` (15 linhas)

Apropriação Direta de Créditos de PIS e COFINS - Vigência. 15 linhas no catálogo; chave: CODI_EMP, I_APROPRIACAO, VIGENCIA.

- **Chave:** `CODI_EMP, I_APROPRIACAO, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_APROPRIACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15 linhas, 15 empresa(s), VIGENCIA de 2020-01-01 a 2022-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_apropriacao` | integer(4) |  |  | Sequencial |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(40) |  |  | Descrição |
| receita_tributada_no_mercado_interno | `receita_tributada_mercado_interno` | decimal(7) |  |  | Receita tributada no mercado interno |
| receita_nao_tributada_no_mercado_interno | `receita_nao_tributada_mercado_interno` | decimal(7) |  |  | Receita não tributada no mercado interno |
| receita_de_exportacao | `receita_exportacao` | decimal(7) |  |  | Receita de exportação |

**Filtros:** `sequencial` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo)

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

