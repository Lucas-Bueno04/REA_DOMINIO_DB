# Modelo — Fiscal - combustivel (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_combustivel.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efcombustivel_tabela_anp](#efcombustivel_tabela_anp) | `EFCOMBUSTIVEL_TABELA_ANP` | 1.028 | pequeno | — |
| [efcombustivel_tabela_df](#efcombustivel_tabela_df) | `EFCOMBUSTIVEL_TABELA_DF` | 29 | pequeno | — |
| [efcombustivel_bico](#efcombustivel_bico) | `EFCOMBUSTIVEL_BICO` | 4 | pequeno | empresa |
| [efcombustivel_bico_vigencia](#efcombustivel_bico_vigencia) | `EFCOMBUSTIVEL_BICO_VIGENCIA` | 4 | pequeno | empresa |
| [efcombustivel_tanque](#efcombustivel_tanque) | `EFCOMBUSTIVEL_TANQUE` | 1 | pequeno | empresa |
| [efcombustivel_tanque_vigencia](#efcombustivel_tanque_vigencia) | `EFCOMBUSTIVEL_TANQUE_VIGENCIA` | 1 | pequeno | empresa |
| [efcombustivel_tanque_vigencia_codigo_arquivo](#efcombustivel_tanque_vigencia_codigo_arquivo) | `EFCOMBUSTIVEL_TANQUE_VIGENCIA_CODIGO_ARQUIVO` | 1 | pequeno | empresa |

## efcombustivel_tabela_anp

**Tabela de códigos de combustível da ANP** — tabela `EFCOMBUSTIVEL_TABELA_ANP` (1.028 linhas)

Tabela de códigos de combustível da ANP. 1.028 linhas no catálogo; chave: CODIGO_COMBUSTIVEL_ANP.

- **Chave:** `CODIGO_COMBUSTIVEL_ANP`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO_COMBUSTIVEL_ANP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.028 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_combustivel_anp` | char(9) |  |  | Código |
| descricao | `descricao` | char(128) |  |  | Descrição |
| grupo | `grupo` | varchar(255) |  |  | Grupo |
| unidade_de_medida_simp | `unidade_medida_simp` | varchar(255) |  |  | Unidade de Medida SIMP |
| unidade_de_grandeza | `unidade_grandeza` | varchar(255) |  |  | Unidade de Grandeza |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo), `grupo` (contem/prefixo), `unidade_de_medida_simp` (contem/prefixo), `unidade_de_grandeza` (contem/prefixo)

## efcombustivel_tabela_df

**Tabela de códigos de combustível do DF** — tabela `EFCOMBUSTIVEL_TABELA_DF` (29 linhas)

Tabela de códigos de combustível do DF. 29 linhas no catálogo; chave: CODIGO_COMBUSTIVEL_DF.

- **Chave:** `CODIGO_COMBUSTIVEL_DF`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO_COMBUSTIVEL_DF asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 29 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo_combustivel_df` | char(4) |  |  | Código |
| descricao | `descricao` | char(128) |  |  | Descrição |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## efcombustivel_bico

**Combustível - Bicos** — tabela `EFCOMBUSTIVEL_BICO` (4 linhas)

Combustível - Bicos. 4 linhas no catálogo; chave: CODI_EMP, I_BICO.

- **Chave:** `CODI_EMP, I_BICO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_BICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 4 linhas sem registro relacionado (empresa 10107).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_bico` | integer(4) |  |  | Sequencial |
| numero_do_bico | `nro_bico` | integer(4) |  |  | Número do bico |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in)

## efcombustivel_bico_vigencia

**Combustível - Bicos - Vigência** — tabela `EFCOMBUSTIVEL_BICO_VIGENCIA` (4 linhas)

Combustível - Bicos - Vigência. 4 linhas no catálogo; chave: CODI_EMP, I_BICO, VIGENCIA_BICO.

- **Chave:** `CODI_EMP, I_BICO, VIGENCIA_BICO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_BICO`
- **Ordem padrão:** `VIGENCIA_BICO desc`, `I_BICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s), VIGENCIA_BICO de 2015-01-01 a 2015-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_bico` | integer(4) |  |  | Sequencial |
| vigencia | `vigencia_bico` | date(4) |  |  | Vigência |
| encerrante_inicial | `encerrante_inicial` | numeric(13) |  |  | Encerrante inicial |
| descricao | `descricao` | char(128) |  |  | Descrição |
| observacao | `observacao` | varchar(250) |  |  | Observação |

**Filtros:** `sequencial` (eq/in), `vigencia` (eq/in), `descricao` (contem/prefixo), `observacao` (contem/prefixo)

## efcombustivel_tanque

**Combustível - Tanques** — tabela `EFCOMBUSTIVEL_TANQUE` (1 linhas)

Combustível - Tanques. 1 linhas no catálogo; chave: CODI_EMP, I_TANQUE.

- **Chave:** `CODI_EMP, I_TANQUE`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_TANQUE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 10107).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_tanque` | integer(4) |  |  | Sequencial |
| descricao | `descricao` | char(128) |  |  | Descrição |
| identificador | `identificador` | varchar(3) |  |  | Identificador |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `descricao` (contem/prefixo), `identificador` (eq/in)

## efcombustivel_tanque_vigencia

**Combustível - Tanques - Vigência** — tabela `EFCOMBUSTIVEL_TANQUE_VIGENCIA` (1 linhas)

Combustível - Tanques - Vigência. 1 linhas no catálogo; chave: CODI_EMP, I_TANQUE, I_VIGENCIA_TANQUE.

- **Chave:** `CODI_EMP, I_TANQUE, I_VIGENCIA_TANQUE`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA_TANQUE`
- **Ordem padrão:** `VIGENCIA_TANQUE desc`, `I_TANQUE asc`, `I_VIGENCIA_TANQUE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), VIGENCIA_TANQUE de 2015-01-01 a 2015-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_tanque` | integer(4) |  |  | Sequencial |
| sequencial_da_vigencia | `i_vigencia_tanque` | integer(4) |  |  | Sequencial da vigência |
| vigencia | `vigencia_tanque` | date(4) |  |  | Vigência |
| produto | `codi_pdi` | char(14) |  |  | Produto |
| estoque_inicial | `estoque_inicial` | numeric(13) |  |  | Estoque inicial |
| codigo_do_tanque_no_arquivo | `i_tanque_arquivo` | integer(4) |  |  | Código do tanque no arquivo |
| capacidade_nominal | `capacidade_nominal` | numeric(13) |  |  | Capacidade nominal |

**Filtros:** `sequencial` (eq/in), `sequencial_da_vigencia` (eq/in), `vigencia` (entre/gte/lte), `produto` (eq/in), `codigo_do_tanque_no_arquivo` (eq/in)

## efcombustivel_tanque_vigencia_codigo_arquivo

**Combustível - Tanques - Vigência - Código do tanque no arquivo** — tabela `EFCOMBUSTIVEL_TANQUE_VIGENCIA_CODIGO_ARQUIVO` (1 linhas)

Combustível - Tanques - Vigência - Código do tanque no arquivo. 1 linhas no catálogo; chave: CODI_EMP, I_TANQUE, I_VIGENCIA_TANQUE, I_CODIGO_ARQUIVO.

- **Chave:** `CODI_EMP, I_TANQUE, I_VIGENCIA_TANQUE, I_CODIGO_ARQUIVO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_TANQUE asc`, `I_VIGENCIA_TANQUE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_tanque | `i_tanque` | integer(4) |  |  | Sequencial tanque |
| sequencial_da_vigencia | `i_vigencia_tanque` | integer(4) |  |  | Sequencial da vigência |
| sequencial_codigo_do_tanque_no_arquivo | `i_codigo_arquivo` | integer(4) |  |  | Sequencial código do tanque no arquivo |
| codigo_do_tanque_no_arquivo | `codigo_arquivo` | varchar(7) |  |  | Código do tanque no arquivo |

**Filtros:** `sequencial_tanque` (eq/in), `sequencial_da_vigencia` (eq/in), `sequencial_codigo_do_tanque_no_arquivo` (eq/in), `codigo_do_tanque_no_arquivo` (eq/in)

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

