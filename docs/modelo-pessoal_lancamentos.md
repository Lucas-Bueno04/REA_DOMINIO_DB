# Modelo — Pessoal - lancamentos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_lancamentos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [folancamentos_eventos_servicos](#folancamentos_eventos_servicos) | `FOLANCAMENTOS_EVENTOS_SERVICOS` | 642 | pequeno | empresa |
| [folancamentos_eventos_vale_alimentacao](#folancamentos_eventos_vale_alimentacao) | `FOLANCAMENTOS_EVENTOS_VALE_ALIMENTACAO` | 528 | pequeno | empresa |
| [folancamentos_eventos_complementos](#folancamentos_eventos_complementos) | `FOLANCAMENTOS_EVENTOS_COMPLEMENTOS` | 446 | pequeno | empresa |
| [folancamentos_eventos_pensao_alimenticia](#folancamentos_eventos_pensao_alimenticia) | `FOLANCAMENTOS_EVENTOS_PENSAO_ALIMENTICIA` | 270 | pequeno | empresa |
| [folancamentos_automaticos_complementos](#folancamentos_automaticos_complementos) | `FOLANCAMENTOS_AUTOMATICOS_COMPLEMENTOS` | 115 | pequeno | empresa |

## folancamentos_eventos_servicos

**Lançamento de evento por serviço.** — tabela `FOLANCAMENTOS_EVENTOS_SERVICOS` (642 linhas)

Lançamento de evento por serviço.. 642 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_SERVICOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_SERVICOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIAL`
- **Ordem padrão:** `COMPETENCIA_INICIAL desc`, `I_EMPREGADOS asc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 642 linhas, 58 empresa(s), COMPETENCIA_INICIAL de 2017-05-01 a 2020-02-01.
- tipo_do_processo_11_mensal_31_1a_semana: todos os valores reais estão no comentário do banco (11=641, 41=1).
- tipo_de_lancamento_1_mensal_2_fixo: todos os valores reais estão no comentário do banco (1=642).
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=642).
- Vínculo foservicos (foservicos): 0 de 2 linhas sem registro relacionado (empresa 1023).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| tipo_do_processo_11_mensal_31_1a_semana | `tipo_processo` | smallint(2) |  | folancamentos_eventos_servicos_tipo_do_processo_ | Tipo do processo. (11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento de 13º salário/52=13º salário integral) |
| tipo_de_lancamento_1_mensal_2_fixo | `tipo_lancamento` | smallint(2) |  | folancamentos_eventos_servicos_tipo_de_lancament | Tipo de lançamento. (1=Mensal/2=Fixo) |
| competencia_inicial | `competencia_inicial` | date(4) |  |  | Competência inicial. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| valor_informado | `valor_informado` | numeric(30) |  |  | Valor informado. |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | folancamentos_eventos_servicos_origem_do_registr | Origem do registro. (0=Sistema/1=importação de tabelas/2=importação de leiaute/3=conversão) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foservicos` → `foservicos` por `codi_emp` = `codi_emp` e `i_servicos` = `i_servicos`; colunas: `foservicos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_evento` (eq/in), `tipo_do_processo_11_mensal_31_1a_semana` (eq/in), `tipo_de_lancamento_1_mensal_2_fixo` (eq/in), `competencia_inicial` (eq/in), `sequencial` (eq/in), `codigo_do_servico` (eq/in)

## folancamentos_eventos_vale_alimentacao

**Lançamentos de vale alimentação.** — tabela `FOLANCAMENTOS_EVENTOS_VALE_ALIMENTACAO` (528 linhas)

Lançamentos de vale alimentação.. 528 linhas no catálogo; chave: CODI_EMP, I_VALE_ALIMENTACAO, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, TIPO_LANCAMENTO, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_VALE_ALIMENTACAO, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, TIPO_LANCAMENTO, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_VALE_ALIMENTACAO asc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 530 linhas, 5 empresa(s), COMPETENCIA de 2018-11-01 a 2026-11-01.
- Vínculo fovale_alimentacao (FOVALE_ALIMENTACAO): 0 de 62 linhas sem registro relacionado (empresa 1713).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_vale_alimentacao | `i_vale_alimentacao` | integer(4) |  |  | Código do vale alimentação. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia_do_lancamento | `competencia` | date(4) |  |  | Competência do lançamento. |
| tipo_de_processo_do_lancamento | `tipo_processo` | smallint(2) |  |  | Tipo de processo do lançamento. |
| tipo_do_lancamento | `tipo_lancamento` | smallint(2) |  |  | Tipo do lançamento |
| sequencial_do_lancamento | `sequencial` | integer(4) |  |  | Sequencial do lançamento. |
| codigo_da_rubrica_do_lancamento | `i_eventos` | integer(4) |  |  | Código da rubrica do lançamento. |
| numero_de_dias | `numero_dias` | integer(4) |  |  | Número de dias. |
| numero_de_vales | `numero_vales` | integer(4) |  |  | Número de vales. |
| valor_a_pagar | `valor_pagar` | numeric(13) |  |  | Valor a pagar. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fovale_alimentacao` → `FOVALE_ALIMENTACAO` por `codi_emp` = `codi_emp` e `i_vale_alimentacao` = `i_vale_alimentacao`; colunas: `fovale_alimentacao_nome`

**Filtros:** `codigo_do_vale_alimentacao` (eq/in), `codigo_do_empregado` (eq/in), `competencia_do_lancamento` (eq/in), `tipo_de_processo_do_lancamento` (eq/in), `tipo_do_lancamento` (eq/in), `sequencial_do_lancamento` (eq/in), `codigo_da_rubrica_do_lancamento` (eq/in)

## folancamentos_eventos_complementos

**Lançamentos de eventos para complementos de cálculos** — tabela `FOLANCAMENTOS_EVENTOS_COMPLEMENTOS` (446 linhas)

Lançamentos de eventos para complementos de cálculos. 446 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_CALCULOS_COMPLEMENTOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_CALCULOS_COMPLEMENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIAL`
- **Ordem padrão:** `COMPETENCIA_INICIAL desc`, `I_EMPREGADOS asc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 446 linhas, 48 empresa(s), COMPETENCIA_INICIAL de 2014-10-01 a 2026-10-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| tipo_do_processo_42_complementar | `tipo_processo` | smallint(2) |  |  | Tipo do processo: (42=Complementar) |
| tipo_do_lancamento_1_mensal_2_fixo | `tipo_lancamento` | smallint(2) |  |  | Tipo do lançamento: (1=Mensal, 2=Fixo) |
| competencia_inicial_do_lancamento | `competencia_inicial` | date(4) |  |  | Competência inicial do lançamento |
| sequencial_do_lancamento | `sequencial` | integer(4) |  |  | Sequencial do lançamento |
| codigo_do_complemento_de_calculo | `i_calculos_complementos` | uniqueidentifier(16) |  |  | Código do complemento de cálculo |
| codigo_do_complemento_de_calculo_renomea | `i_calculos_complementos_old` | integer(4) |  |  | Código do complemento de cálculo - Renomeado |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_evento` (eq/in), `tipo_do_processo_42_complementar` (eq/in), `tipo_do_lancamento_1_mensal_2_fixo` (eq/in), `competencia_inicial_do_lancamento` (eq/in), `sequencial_do_lancamento` (eq/in), `codigo_do_complemento_de_calculo` (eq/in), `codigo_do_complemento_de_calculo_renomea` (eq/in)

## folancamentos_eventos_pensao_alimenticia

**Valores de pensão alimentícia por dependente.** — tabela `FOLANCAMENTOS_EVENTOS_PENSAO_ALIMENTICIA` (270 linhas)

Valores de pensão alimentícia por dependente.. 270 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_FILHOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL, I_FILHOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIAL`
- **Ordem padrão:** `COMPETENCIA_INICIAL desc`, `I_EMPREGADOS asc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 270 linhas, 34 empresa(s), COMPETENCIA_INICIAL de 2017-09-01 a 2026-09-01.
- tipo_de_lancamento_1_mensal_2_fixo: todos os valores reais estão no comentário do banco (1=198, 2=72).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=270).
- Vínculo fofilhos (fofilhos): 0 de 5 linhas sem registro relacionado (empresa 603).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| tipo_de_processo | `tipo_processo` | smallint(2) |  |  | Tipo de processo. |
| tipo_de_lancamento_1_mensal_2_fixo | `tipo_lancamento` | smallint(2) |  | folancamentos_eventos_pensao_alimenticia_tipo_de_lan | Tipo de lançamento. (1=Mensal/2=Fixo) |
| competencia_do_lancamento | `competencia_inicial` | date(4) |  |  | Competência do lançamento. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente. |
| valor | `valor` | numeric(13) |  |  | Valor. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | folancamentos_eventos_pensao_alimenticia_origem_do_r | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_evento` (eq/in), `tipo_de_processo` (eq/in), `tipo_de_lancamento_1_mensal_2_fixo` (eq/in), `competencia_do_lancamento` (eq/in), `sequencial` (eq/in), `codigo_do_dependente` (eq/in)

## folancamentos_automaticos_complementos

**Lançamentos automáticos de eventos para complementos de cálculos** — tabela `FOLANCAMENTOS_AUTOMATICOS_COMPLEMENTOS` (115 linhas)

Lançamentos automáticos de eventos para complementos de cálculos. 115 linhas no catálogo; chave: CODI_EMP, I_LANCTOSAUTO, I_CALCULOS_COMPLEMENTOS.

- **Chave:** `CODI_EMP, I_LANCTOSAUTO, I_CALCULOS_COMPLEMENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_LANCTOSAUTO asc`, `I_CALCULOS_COMPLEMENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 115 linhas, 40 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_lancamento_automatico | `i_lanctosauto` | integer(4) |  |  | Código do lançamento automático |
| codigo_do_complemento_de_calculo | `i_calculos_complementos` | uniqueidentifier(16) |  |  | Código do complemento de cálculo |
| codigo_do_complemento_de_calculo_renomea | `i_calculos_complementos_old` | integer(4) |  |  | Código do complemento de cálculo - Renomeado |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |

**Filtros:** `codigo_do_lancamento_automatico` (eq/in), `codigo_do_complemento_de_calculo` (eq/in), `codigo_do_complemento_de_calculo_renomea` (eq/in)

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

### folancamentos_eventos_servicos_tipo_do_processo_

Confirmado: sim

> Todos os valores observados em FOLANCAMENTOS_EVENTOS_SERVICOS.TIPO_PROCESSO estão no comentário do banco (2026-10-18). Distribuição: 11=641, 41=1.

| Código | Significado |
|---|---|
| 11 | Mensal |
| 31 | 1ª semana |
| 32 | 2ª semana |
| 33 | 3ª semana |
| 34 | 4ª semana |
| 35 | Última semana |
| 36 | Todas as semanas |
| 41 | Adiantamento |
| 42 | Complementar |
| 51 | Adiantamento de 13º salário |
| 52 | 13º salário integral |

### folancamentos_eventos_servicos_tipo_de_lancament

Confirmado: sim

> Todos os valores observados em FOLANCAMENTOS_EVENTOS_SERVICOS.TIPO_LANCAMENTO estão no comentário do banco (2026-10-18). Distribuição: 1=642.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | Fixo |

### folancamentos_eventos_servicos_origem_do_registr

Confirmado: sim

> Todos os valores observados em FOLANCAMENTOS_EVENTOS_SERVICOS.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=642.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | importação de tabelas |
| 2 | importação de leiaute |
| 3 | conversão |

### folancamentos_eventos_pensao_alimenticia_tipo_de_lan

Confirmado: sim

> Todos os valores observados em FOLANCAMENTOS_EVENTOS_PENSAO_ALIMENTICIA.TIPO_LANCAMENTO estão no comentário do banco (2026-10-18). Distribuição: 1=198, 2=72.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | Fixo |

### folancamentos_eventos_pensao_alimenticia_origem_do_r

Confirmado: sim

> Todos os valores observados em FOLANCAMENTOS_EVENTOS_PENSAO_ALIMENTICIA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=270.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

