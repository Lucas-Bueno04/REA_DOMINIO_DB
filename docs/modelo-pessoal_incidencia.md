# Modelo — Pessoal - incidencia (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_incidencia.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foincidencia_irrf_rubrica_esocial](#foincidencia_irrf_rubrica_esocial) | `FOINCIDENCIA_IRRF_RUBRICA_ESOCIAL` | 90 | pequeno | — |
| [foincidencia_inss_rubrica_esocial](#foincidencia_inss_rubrica_esocial) | `FOINCIDENCIA_INSS_RUBRICA_ESOCIAL` | 28 | pequeno | — |
| [foincidencia_fgts_rubrica_esocial](#foincidencia_fgts_rubrica_esocial) | `FOINCIDENCIA_FGTS_RUBRICA_ESOCIAL` | 8 | pequeno | — |
| [foincidencia_rpps_rubrica_esocial](#foincidencia_rpps_rubrica_esocial) | `FOINCIDENCIA_RPPS_RUBRICA_ESOCIAL` | 7 | pequeno | — |
| [foincidencia_pis_rubrica_esocial](#foincidencia_pis_rubrica_esocial) | `FOINCIDENCIA_PIS_RUBRICA_ESOCIAL` | 5 | pequeno | — |
| [foincidencia_sindical_rubrica_esocial](#foincidencia_sindical_rubrica_esocial) | `FOINCIDENCIA_SINDICAL_RUBRICA_ESOCIAL` | 4 | pequeno | — |

## foincidencia_irrf_rubrica_esocial

**Tabela de códigos de incidência de IRRF para o eSocial.** — tabela `FOINCIDENCIA_IRRF_RUBRICA_ESOCIAL` (90 linhas)

Tabela de códigos de incidência de IRRF para o eSocial.. 90 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `COMPETENCIA_INICIO`
- **Ordem padrão:** `COMPETENCIA_INICIO desc`, `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 90 linhas, COMPETENCIA_INICIO de 2015-10-01 a 2015-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| descricao | `descricao` | char(120) |  |  | Descrição |
| competencia_inicio_para_incidencia_tribu | `competencia_inicio` | date(4) |  |  | Competência inicio para Incidência Tributária da Rubrica para o IRRF. |
| competencia_termino_para_incidencia_trib | `competencia_termino` | date(4) |  |  | Competência termino para Incidência Tributária da Rubrica para o IRRF. |

**Filtros:** `codigo` (eq/in), `competencia_inicio_para_incidencia_tribu` (entre/gte/lte), `competencia_termino_para_incidencia_trib` (entre/gte/lte), `descricao` (contem/prefixo)

## foincidencia_inss_rubrica_esocial

**Tabela de códigos de incidência de INSS para o eSocial.** — tabela `FOINCIDENCIA_INSS_RUBRICA_ESOCIAL` (28 linhas)

Tabela de códigos de incidência de INSS para o eSocial.. 28 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 28 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| descricao | `descricao` | varchar(80) |  |  | Descrição |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## foincidencia_fgts_rubrica_esocial

**Incidência de FGTS da rubrica para o eSocial.** — tabela `FOINCIDENCIA_FGTS_RUBRICA_ESOCIAL` (8 linhas)

Incidência de FGTS da rubrica para o eSocial.. 8 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| descricao | `descricao` | char(100) |  |  | Descrição |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## foincidencia_rpps_rubrica_esocial

**Incidência de RPPS da rubrica para o eSocial.** — tabela `FOINCIDENCIA_RPPS_RUBRICA_ESOCIAL` (7 linhas)

Incidência de RPPS da rubrica para o eSocial.. 7 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| descricao | `descricao` | varchar(80) |  |  | Descrição |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## foincidencia_pis_rubrica_esocial

**Tabela de códigos de incidência de PIS para o eSocial.** — tabela `FOINCIDENCIA_PIS_RUBRICA_ESOCIAL` (5 linhas)

Tabela de códigos de incidência de PIS para o eSocial.. 5 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| descricao | `descricao` | varchar(80) |  |  | Descrição |

**Filtros:** `codigo` (eq/in), `descricao` (contem/prefixo)

## foincidencia_sindical_rubrica_esocial

**Códigos de incidência sindical das rubricas para o eSocial.** — tabela `FOINCIDENCIA_SINDICAL_RUBRICA_ESOCIAL` (4 linhas)

Códigos de incidência sindical das rubricas para o eSocial.. 4 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_incidencia | `codigo` | integer(4) |  |  | Código da incidência. |
| descricao_da_incidencia | `descricao` | varchar(80) |  |  | Descrição da incidência. |

**Filtros:** `codigo_da_incidencia` (eq/in), `descricao_da_incidencia` (contem/prefixo)

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

