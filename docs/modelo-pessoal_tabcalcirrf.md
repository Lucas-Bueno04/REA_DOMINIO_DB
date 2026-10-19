# Modelo — Pessoal - tabcalcirrf (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_tabcalcirrf.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fotabcalcirrf_faixas](#fotabcalcirrf_faixas) | `FOTABCALCIRRF_FAIXAS` | 235 | pequeno | — |
| [fotabcalcirrf_faixas_complemento](#fotabcalcirrf_faixas_complemento) | `FOTABCALCIRRF_FAIXAS_COMPLEMENTO` | 2 | pequeno | — |
| [fotabcalcirrf_exterior](#fotabcalcirrf_exterior) | `FOTABCALCIRRF_EXTERIOR` | 1 | pequeno | — |
| [fotabcalcirrf_exterior_faixas](#fotabcalcirrf_exterior_faixas) | `FOTABCALCIRRF_EXTERIOR_FAIXAS` | 1 | pequeno | — |

## fotabcalcirrf_faixas

**Tabela de IRRF - Faixas** — tabela `FOTABCALCIRRF_FAIXAS` (235 linhas)

Tabela de IRRF - Faixas. 235 linhas no catálogo; chave: I_TABCALCIRRF, VALOR_ATE.

- **Chave:** `I_TABCALCIRRF, VALOR_ATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `I_TABCALCIRRF`
- **Ordem padrão:** `I_TABCALCIRRF desc`, `VALOR_ATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 235 linhas, I_TABCALCIRRF de 1998-01-01 a 2025-05-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| competencia | `i_tabcalcirrf` | date(4) |  |  | Competência |
| valor_ate | `valor_ate` | numeric(13) |  |  | Valor até |
| taxa | `taxa` | numeric(13) |  |  | Taxa |
| desconto | `desconto` | numeric(13) |  |  | Desconto |

**Filtros:** `competencia` (eq/in), `valor_ate` (eq/in)

## fotabcalcirrf_faixas_complemento

**Tabela de faixas para complementar o IRRF a partir de 01/2026 conforme LEI Nº 1,087 DE 2025** — tabela `FOTABCALCIRRF_FAIXAS_COMPLEMENTO` (2 linhas)

Tabela de faixas para complementar o IRRF a partir de 01/2026 conforme LEI Nº 1,087 DE 2025. 2 linhas no catálogo; chave: DATA, VALOR_ATE.

- **Chave:** `DATA, VALOR_ATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `VALOR_ATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, DATA de 2026-01-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| competencia | `data` | date(4) |  |  | Competência |
| valor_maximo_da_faixa | `valor_ate` | numeric(13) |  |  | Valor máximo da faixa |
| valor_de_reducao_da_faixa | `reducao` | numeric(13) |  |  | Valor de redução da faixa |
| fator_de_correcao_aplicado | `fator_correcao` | numeric(13) |  |  | Fator de correcao aplicado |

**Filtros:** `competencia` (eq/in), `valor_maximo_da_faixa` (eq/in)

## fotabcalcirrf_exterior

**Tabela de IRRF para residentes no exterior.** — tabela `FOTABCALCIRRF_EXTERIOR` (1 linhas)

Tabela de IRRF para residentes no exterior.. 1 linhas no catálogo; chave: I_TABCALCIRRF_EXTERIOR.

- **Chave:** `I_TABCALCIRRF_EXTERIOR`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `I_TABCALCIRRF_EXTERIOR`
- **Ordem padrão:** `I_TABCALCIRRF_EXTERIOR desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, I_TABCALCIRRF_EXTERIOR de 1998-01-01 a 1998-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| competencia | `i_tabcalcirrf_exterior` | date(4) |  |  | Competência |
| desconto_por_dependente | `desc_depend` | numeric(13) |  |  | Desconto por dependente. |
| minimo_para_retencao | `minimo_retencao` | numeric(13) |  |  | Mínimo para retenção. |

**Filtros:** `competencia` (eq/in)

## fotabcalcirrf_exterior_faixas

**Faixas da tabela de IRRF para residentes no exterior.** — tabela `FOTABCALCIRRF_EXTERIOR_FAIXAS` (1 linhas)

Faixas da tabela de IRRF para residentes no exterior.. 1 linhas no catálogo; chave: I_TABCALCIRRF_EXTERIOR, VALOR_ATE.

- **Chave:** `I_TABCALCIRRF_EXTERIOR, VALOR_ATE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `I_TABCALCIRRF_EXTERIOR`
- **Ordem padrão:** `I_TABCALCIRRF_EXTERIOR desc`, `VALOR_ATE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, I_TABCALCIRRF_EXTERIOR de 1998-01-01 a 1998-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| competencia | `i_tabcalcirrf_exterior` | date(4) |  |  | Competência |
| valor_ate | `valor_ate` | numeric(13) |  |  | Valor até |
| taxa | `taxa` | numeric(13) |  |  | Taxa |
| desconto | `desconto` | numeric(13) |  |  | Desconto |

**Filtros:** `competencia` (eq/in), `valor_ate` (eq/in)

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

