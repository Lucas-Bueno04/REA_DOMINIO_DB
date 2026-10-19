# Modelo — Pessoal - provisoes (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_provisoes.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foprovisoes_valores](#foprovisoes_valores) | `FOPROVISOES_VALORES` | 782.189 | medio | empresa |
| [foprovisoes_periodos_valores](#foprovisoes_periodos_valores) | `FOPROVISOES_PERIODOS_VALORES` | 526.302 | medio | empresa |
| [foprovisoes_periodos](#foprovisoes_periodos) | `FOPROVISOES_PERIODOS` | 115.036 | medio | empresa |
| [foprovisoes_valores_tipos](#foprovisoes_valores_tipos) | `FOPROVISOES_VALORES_TIPOS` | 35 | pequeno | — |

## foprovisoes_valores

**Valores da provisão.** — tabela `FOPROVISOES_VALORES` (782.189 linhas)

Valores da provisão.. 782.189 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, TIPO_VALOR.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, TIPO_VALOR`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 782.189 linhas, 321 empresa(s), COMPETENCIA de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_de_provisao | `tipo` | tinyint(1) |  |  | Tipo de provisão |
| tipo_de_valor | `tipo_valor` | smallint(2) |  |  | Tipo de valor |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_do_1_3_de_ferias | `valor_adicional_ferias` | numeric(13) |  |  | Valor do 1/3 de férias |
| valor_de_medias_e_vantagens | `valor_medias_vantagens` | numeric(13) |  |  | Valor de médias e vantagens |
| valor_do_inss_empresa | `valor_inss_empresa` | numeric(13) |  |  | Valor do INSS Empresa |
| valor_do_inss_rat | `valor_inss_rat` | numeric(13) |  |  | Valor do INSS RAT |
| valor_do_inss_terceiros | `valor_inss_terceiros` | numeric(13) |  |  | Valor do INSS Terceiros |
| valor_do_fgts | `valor_fgts` | numeric(13) |  |  | Valor do FGTS |
| valor_do_pis | `valor_pis` | numeric(13) |  |  | Valor do PIS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_do_adicional_de_ferias_sem_conside | `valor_adicional_ferias_sem_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias sem considerar as médias/vantagens. |
| valor_do_adicional_de_ferias_das_medias | `valor_adicional_ferias_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias das médias/vantagens. |
| valor_adicional_ferias_mp_927 | `valor_adicional_ferias_mp_927` | numeric(13) |  |  | Valor do 1/3 de férias MP 927 |
| valor_adicional_ferias_sem_medias_vantag | `valor_adicional_ferias_sem_medias_vantagens_mp_927` | numeric(13) |  |  | Valor do adicional de férias sem considerar as médias/vantagens  MP 927. |
| valor_adicional_ferias_medias_vantagens | `valor_adicional_ferias_medias_vantagens_mp_927` | numeric(13) |  |  | Valor do adicional de férias das médias/vantagens  MP 927. |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_provisao` (eq/in), `tipo_de_valor` (eq/in)

## foprovisoes_periodos_valores

**Valores do período da provisão** — tabela `FOPROVISOES_PERIODOS_VALORES` (526.302 linhas)

Valores do período da provisão. 526.302 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, I_FERIAS_AQUISITIVOS, TIPO_VALOR.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, I_FERIAS_AQUISITIVOS, TIPO_VALOR`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 526.302 linhas, 320 empresa(s), COMPETENCIA de 2013-01-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_de_provisao | `tipo` | tinyint(1) |  |  | Tipo de provisão |
| sequencia_de_periodos_aquisitivos | `i_ferias_aquisitivos` | integer(4) |  |  | Sequência de períodos aquisitivos |
| tipo_de_valor_da_provisao | `tipo_valor` | smallint(2) |  |  | Tipo de valor da provisão |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_do_1_3_de_ferias | `valor_adicional_ferias` | numeric(13) |  |  | Valor do 1/3 de férias |
| valor_de_medias_e_vantagens | `valor_medias_vantagens` | numeric(13) |  |  | Valor de médias e vantagens |
| valor_do_inss_empresa | `valor_inss_empresa` | numeric(13) |  |  | Valor do INSS Empresa |
| valor_do_inss_rat | `valor_inss_rat` | numeric(13) |  |  | Valor do INSS RAT |
| valor_do_inss_terceiros | `valor_inss_terceiros` | numeric(13) |  |  | Valor do INSS Terceiros |
| valor_do_fgts | `valor_fgts` | numeric(13) |  |  | Valor do FGTS |
| valor_do_pis | `valor_pis` | numeric(13) |  |  | Valor do PIS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_do_adicional_de_ferias_sem_conside | `valor_adicional_ferias_sem_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias sem considerar as médias/vantagens. |
| valor_do_adicional_de_ferias_das_medias | `valor_adicional_ferias_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias das médias/vantagens. |
| valor_adicional_ferias_mp_927 | `valor_adicional_ferias_mp_927` | numeric(13) |  |  | Valor do 1/3 de férias MP 927 |
| valor_adicional_ferias_sem_medias_vantag | `valor_adicional_ferias_sem_medias_vantagens_mp_927` | numeric(13) |  |  | Valor do adicional de férias sem considerar as médias/vantagens  MP 927. |
| valor_adicional_ferias_medias_vantagens | `valor_adicional_ferias_medias_vantagens_mp_927` | numeric(13) |  |  | Valor do adicional de férias das médias/vantagens  MP 927. |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_provisao` (eq/in), `sequencia_de_periodos_aquisitivos` (eq/in), `tipo_de_valor_da_provisao` (eq/in)

## foprovisoes_periodos

**PROVISOES CALCULADAS - PERIODOS DE FERIAS** — tabela `FOPROVISOES_PERIODOS` (115.036 linhas)

PROVISOES CALCULADAS - PERIODOS DE FERIAS. 115.036 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, I_FERIAS_AQUISITIVOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO, I_FERIAS_AQUISITIVOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 115.036 linhas, 320 empresa(s), COMPETENCIA de 2013-01-01 a 2026-09-01.
- considerar_na_provisao_do_mes_0_nao_1_si: todos os valores reais estão no comentário do banco (1=112.955, 0=2.081).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | CODIGO DA EMPRESA |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | CÓDIGO DO EMPREGADO |
| competencia | `competencia` | date(4) |  |  | COMPETÊNCIA |
| tipo_da_provisao | `tipo` | tinyint(1) |  |  | TIPO DA PROVISAO |
| sequencia_de_periodos_aquisitivos | `i_ferias_aquisitivos` | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| numero_de_dias_de_direito_no_periodo | `qtde_dias` | numeric(13) |  |  | NUMERO DE DIAS DE DIREITO NO PERIODO |
| numero_de_avos_adquiridos | `no_avos` | integer(4) |  |  | NUMERO DE AVOS ADQUIRIDOS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| considerar_na_provisao_do_mes_0_nao_1_si | `considerar_provisao_mes` | smallint(2) |  | foprovisoes_periodos_considerar_ | Considerar na provisão do mês: (0=Não/1=Sim) |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_da_provisao` (eq/in), `sequencia_de_periodos_aquisitivos` (eq/in)

## foprovisoes_valores_tipos

**Descrição dos tipos de valores gerados no calculo da provisão.** — tabela `FOPROVISOES_VALORES_TIPOS` (35 linhas)

Descrição dos tipos de valores gerados no calculo da provisão.. 35 linhas no catálogo; chave: TIPO_VALOR.

- **Chave:** `TIPO_VALOR`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `TIPO_VALOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 35 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| tipo_de_valor | `tipo_valor` | integer(4) |  |  | TIPO DE VALOR |
| descricao | `descricao` | varchar(100) |  |  | DESCRICAO |

**Filtros:** `tipo_de_valor` (eq/in), `descricao` (contem/prefixo)

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

### foprovisoes_periodos_considerar_

Confirmado: sim

> Todos os valores observados em FOPROVISOES_PERIODOS.CONSIDERAR_PROVISAO_MES estão no comentário do banco (2026-10-18). Distribuição: 1=112.955, 0=2.081.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

