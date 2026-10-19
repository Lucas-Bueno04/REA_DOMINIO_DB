# Modelo — Fiscal - credito (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_credito.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efcredito_presumido_piscofins_receitas_vigencia_detalhamento](#efcredito_presumido_piscofins_receitas_vigencia_detalhamento) | `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA_DETALHAMENTO` | 4.424 | pequeno | empresa |
| [efcredito_presumido_piscofins_receitas](#efcredito_presumido_piscofins_receitas) | `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS` | 632 | pequeno | empresa |
| [efcredito_presumido_piscofins_receitas_vigencia](#efcredito_presumido_piscofins_receitas_vigencia) | `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA` | 632 | pequeno | empresa |
| [efcredito_presumido_piscofins_vigencia_detalhamento](#efcredito_presumido_piscofins_vigencia_detalhamento) | `EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA_DETALHAMENTO` | 9 | pequeno | — |
| [efcredito_presumido_piscofins_vigencia](#efcredito_presumido_piscofins_vigencia) | `EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA` | 3 | pequeno | — |
| [efcredito_presumido_piscofins](#efcredito_presumido_piscofins) | `EFCREDITO_PRESUMIDO_PISCOFINS` | 2 | pequeno | — |

## efcredito_presumido_piscofins_receitas_vigencia_detalhamento

**Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Relação de NCM** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA_DETALHAMENTO` (4.424 linhas)

Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Relação de NCM. 4.424 linhas no catálogo; chave: CODI_EMP, I_CREDITO_PRESUMIDO, VIGENCIA, I_CREDITO_PRESUMIDO_DETALHAMENTO.

- **Chave:** `CODI_EMP, I_CREDITO_PRESUMIDO, VIGENCIA, I_CREDITO_PRESUMIDO_DETALHAMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_CREDITO_PRESUMIDO asc`, `I_CREDITO_PRESUMIDO_DETALHAMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.424 linhas, 632 empresa(s), VIGENCIA de 2013-10-01 a 2013-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_credito_presumido` | integer(4) |  |  | Sequencial |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| sequencial_detalhamento | `i_credito_presumido_detalhamento` | integer(4) |  |  | Sequencial detalhamento |
| ncm | `ncm` | char(8) |  |  | NCM |
| descricao_ncm | `descricao` | char(1024) |  |  | Descrição NCM |
| percentual_credito_presumido | `percentual_credito_presumido` | numeric(4) |  |  | Percentual Crédito Presumido |
| aliquota_pis_ajustada | `aliquota_pis_ajustada` | numeric(6) |  |  | Alíquota PIS Ajustada |
| aliquota_cofins_ajustada | `aliquota_cofins_ajustada` | numeric(6) |  |  | Alíquota COFINS Ajustada |
| utilizado_como_insumo | `utilizado_como_insumo` | char(1) |  |  | Utilizado como insumo |

**Filtros:** `sequencial` (eq/in), `vigencia` (eq/in), `sequencial_detalhamento` (eq/in), `ncm` (eq/in), `descricao_ncm` (contem/prefixo), `utilizado_como_insumo` (eq/in)

## efcredito_presumido_piscofins_receitas

**Tabela de Crédito Presumido PIS e COFINS Sobre as Receitas - Geral** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS` (632 linhas)

Tabela de Crédito Presumido PIS e COFINS Sobre as Receitas - Geral. 632 linhas no catálogo; chave: CODI_EMP, I_CREDITO_PRESUMIDO.

- **Chave:** `CODI_EMP, I_CREDITO_PRESUMIDO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CREDITO_PRESUMIDO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 632 linhas, 632 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 884).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_credito_presumido` | integer(4) |  |  | Sequencial |
| codigo_interno_do_credito_presumido | `codigo_tabela` | integer(4) |  |  | Código Interno do Crédito Presumido |
| descricao | `descricao` | varchar(255) |  |  | Descrição |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `codigo_interno_do_credito_presumido` (eq/in), `descricao` (contem/prefixo)

## efcredito_presumido_piscofins_receitas_vigencia

**Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Vigência** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS_RECEITAS_VIGENCIA` (632 linhas)

Tabela de Crédito Presumido PIS e COFINS sobre as Receitas - Vigência. 632 linhas no catálogo; chave: CODI_EMP, I_CREDITO_PRESUMIDO, VIGENCIA.

- **Chave:** `CODI_EMP, I_CREDITO_PRESUMIDO, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_CREDITO_PRESUMIDO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 632 linhas, 632 empresa(s), VIGENCIA de 2013-10-01 a 2013-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_credito_presumido` | integer(4) |  |  | Sequencial |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(80) |  |  | Descrição |
| aliquota_pis | `aliquota_pis` | numeric(7) |  |  | Alíquota PIS |
| aliquota_cofins | `aliquota_cofins` | numeric(7) |  |  | Alíquota COFINS |

**Filtros:** `sequencial` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo)

## efcredito_presumido_piscofins_vigencia_detalhamento

**Tabela de Crédito Presumido PIS e COFINS - Relação de NCM** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA_DETALHAMENTO` (9 linhas)

Tabela de Crédito Presumido PIS e COFINS - Relação de NCM. 9 linhas no catálogo; chave: I_CREDITO_PRESUMIDO, VIGENCIA, I_CREDITO_PRESUMIDO_DETALHAMENTO.

- **Chave:** `I_CREDITO_PRESUMIDO, VIGENCIA, I_CREDITO_PRESUMIDO_DETALHAMENTO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_CREDITO_PRESUMIDO asc`, `I_CREDITO_PRESUMIDO_DETALHAMENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas, VIGENCIA de 2013-05-01 a 2015-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_do_credito_presumido | `i_credito_presumido` | integer(4) |  |  | Sequencial do Crédito Presumido |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| sequencial_do_detalhamento | `i_credito_presumido_detalhamento` | integer(4) |  |  | Sequencial do Detalhamento |
| ncm | `ncm` | char(8) |  |  | NCM |
| descricao_do_ncm | `descricao` | varchar(1024) |  |  | Descrição do NCM |
| ex_tipi | `ex_tipi` | char(3) |  |  | EX TIPI |
| valor_de_pis | `valor_pis` | numeric(13) |  |  | Valor de PIS |
| valor_de_cofins | `valor_cofins` | numeric(13) |  |  | Valor de COFINS |

**Filtros:** `sequencial_do_credito_presumido` (eq/in), `vigencia` (eq/in), `sequencial_do_detalhamento` (eq/in), `ncm` (eq/in), `descricao_do_ncm` (contem/prefixo), `ex_tipi` (eq/in)

## efcredito_presumido_piscofins_vigencia

**Tabela de Crédito Presumido PIS e COFINS - Vigência** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS_VIGENCIA` (3 linhas)

Tabela de Crédito Presumido PIS e COFINS - Vigência. 3 linhas no catálogo; chave: I_CREDITO_PRESUMIDO, VIGENCIA.

- **Chave:** `I_CREDITO_PRESUMIDO, VIGENCIA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_CREDITO_PRESUMIDO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, VIGENCIA de 2013-05-01 a 2015-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_do_credito_presumido | `i_credito_presumido` | integer(4) |  |  | Sequencial do Crédito Presumido |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(80) |  |  | Descrição |
| percentual_do_credito_presumido_na_aquis | `percentual_aquisicao_simples_nacional_pis` | numeric(7) |  |  | Percentual do Crédito Presumido na aquisição de contribuinte optante pelo Simples Nacional - PIS |
| percentual_aquisicao_simples_nacional_co | `percentual_aquisicao_simples_nacional_cofins` | numeric(7) |  |  | Percentual do Crédito Presumido na aquisição de contribuinte optante pelo Simples Nacional - COFINS |

**Filtros:** `sequencial_do_credito_presumido` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo)

## efcredito_presumido_piscofins

**Tabela de Crédito Presumido PIS e COFINS - Geral** — tabela `EFCREDITO_PRESUMIDO_PISCOFINS` (2 linhas)

Tabela de Crédito Presumido PIS e COFINS - Geral. 2 linhas no catálogo; chave: I_CREDITO_PRESUMIDO.

- **Chave:** `I_CREDITO_PRESUMIDO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CREDITO_PRESUMIDO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_do_credito_presumido | `i_credito_presumido` | integer(4) |  |  | Sequencial do Crédito Presumido |
| codigo_interno_do_credito_presumido | `codigo_tabela` | integer(4) |  |  | Código Interno do Crédito Presumido |
| descricao | `descricao` | varchar(255) |  |  | Descrição |

**Filtros:** `sequencial_do_credito_presumido` (eq/in), `codigo_interno_do_credito_presumido` (eq/in), `descricao` (contem/prefixo)

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

