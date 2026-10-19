# Modelo — Pessoal - calculos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_calculos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [focalculos_bases_inss_terceiros](#focalculos_bases_inss_terceiros) | `FOCALCULOS_BASES_INSS_TERCEIROS` | 879.775 | medio | um de: codigo_da_base_de_calculo, codigo_do_convenio_de_terceiros |
| [focalculos_alteracao_salarial](#focalculos_alteracao_salarial) | `FOCALCULOS_ALTERACAO_SALARIAL` | 236.299 | medio | empresa |
| [focalculos_diferenca_rais](#focalculos_diferenca_rais) | `FOCALCULOS_DIFERENCA_RAIS` | 228.569 | medio | empresa |
| [focalculos_eventos_bases](#focalculos_eventos_bases) | `FOCALCULOS_EVENTOS_BASES` | 11.488 | medio | empresa |
| [focalculos_complementos](#focalculos_complementos) | `FOCALCULOS_COMPLEMENTOS` | 232 | pequeno | empresa |

## focalculos_bases_inss_terceiros

**Bases de cálculo do INSS** — tabela `FOCALCULOS_BASES_INSS_TERCEIROS` (879.775 linhas)

Bases de cálculo do INSS. 879.775 linhas no catálogo; chave: CODIGO_CONVENIO, I_CALCULOSBASES.

- **Chave:** `CODIGO_CONVENIO, I_CALCULOSBASES`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—` · exige um de: `codigo_da_base_de_calculo, codigo_do_convenio_de_terceiros`
- **Ordem padrão:** `CODIGO_CONVENIO asc`, `I_CALCULOSBASES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 879.820 linhas.
- Vínculo foconvenios_terceiros (FOCONVENIOS_TERCEIROS): 0 de 879.820 linhas sem registro relacionado.
- Vínculo focalculosbases (focalculosbases): 0 de 879.820 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_convenio_de_terceiros | `codigo_convenio` | smallint(2) |  |  | Código do convênio de terceiros. |
| codigo_da_base_de_calculo | `i_calculosbases` | uniqueidentifier(16) |  |  | CÓDIGO DA BASE DE CÁLCULO. |
| sequencial_da_base_de_calculo | `i_calculosbases_old` | integer(4) |  |  | Sequencial da base de cálculo. |
| i_cadbases | `i_cadbases` | integer(4) |  |  | Código da base de cálculo. |
| base | `base` | numeric(17) |  |  | Base |
| taxa | `taxa` | numeric(11) |  |  | Taxa |
| valor | `valor` | numeric(20) |  |  | Valor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foconvenios_terceiros` → `FOCONVENIOS_TERCEIROS` por `codigo_convenio` = `codigo_convenio`; colunas: `foconvenios_terceiros_nome`
- `focalculosbases` → `focalculosbases` por `i_calculosbases` = `i_calculosbases`; colunas: `focalculosbases_nome`

**Filtros:** `codigo_do_convenio_de_terceiros` (eq/in), `codigo_da_base_de_calculo` (eq/in), `sequencial_da_base_de_calculo` (eq/in), `i_cadbases` (eq/in)

## focalculos_alteracao_salarial

**Cálculos que pagaram alterações salariais** — tabela `FOCALCULOS_ALTERACAO_SALARIAL` (236.299 linhas)

Cálculos que pagaram alterações salariais. 236.299 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_ALTERACAO, TIPO_GRADE, TIPO_SALARIO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_ALTERACAO, TIPO_GRADE, TIPO_SALARIO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ALTERACAO`
- **Ordem padrão:** `DATA_ALTERACAO desc`, `I_EMPREGADOS asc`, `TIPO_GRADE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 236.333 linhas, 862 empresa(s), DATA_ALTERACAO de 1900-01-01 a 2026-10-13.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| data_da_alteracao_salarial 🔒 | `data_alteracao` | date(4) |  |  | Data da alteração salarial |
| tipo_da_alteracao_salarial_1_normal_2_va | `tipo_grade` | smallint(2) |  |  | Tipo da alteração salarial: (1=Normal, 2=Valor hora-aula, 3=Grade salarial, 4=Resilição Professor) |
| tipo_da_utilizacao_da_alteracao_no_calcu | `tipo_salario` | smallint(2) |  |  | Tipo da utilização da alteração no cálculo. (1=Cálculo do salário no mês, 2=Cálculo do período retroativo) |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_alteracao_salarial` (eq/in), `tipo_da_alteracao_salarial_1_normal_2_va` (eq/in), `tipo_da_utilizacao_da_alteracao_no_calcu` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## focalculos_diferenca_rais

**Todos os calculos com diferença de salario por competência.** — tabela `FOCALCULOS_DIFERENCA_RAIS` (228.569 linhas)

Todos os calculos com diferença de salario por competência.. 228.569 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `I_CALCULOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 228.579 linhas, 807 empresa(s), COMPETENCIA de 2013-01-01 a 2026-11-16.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia_do_calculo | `competencia` | date(4) |  |  | Competência do cálculo. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo. |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia_do_calculo` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## focalculos_eventos_bases

**Contém as bases que não estão vinculadas a eventos para o consulta recibo** — tabela `FOCALCULOS_EVENTOS_BASES` (11.488 linhas)

Contém as bases que não estão vinculadas a eventos para o consulta recibo. 11.488 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_CALCULOS, I_EVENTOS, I_CADBASES, I_EMPRESTIMO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_CALCULOS, I_EVENTOS, I_CADBASES, I_EMPRESTIMO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_CALCULOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.492 linhas, 67 empresa(s).
- Vínculo geempre (geempre): 0 de 49 linhas sem registro relacionado (empresa 1263).
- Vínculo foempregados (foempregados): 0 de 49 linhas sem registro relacionado (empresa 1263).
- Vínculo foeventos (foeventos): 0 de 49 linhas sem registro relacionado (empresa 1263).
- Vínculo foemprestimos_consignado (FOEMPRESTIMOS_CONSIGNADOS): 0 de 49 linhas sem registro relacionado (empresa 1263).
- Vínculo focadbases (focadbases): 0 de 49 linhas sem registro relacionado (empresa 1263).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| identificacao_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Identificação do cálculo |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| codigo_da_base | `i_cadbases` | integer(4) |  |  | Código da base |
| codigo_do_emprestimo | `i_emprestimo` | integer(4) |  |  | Código do empréstimo |
| codigo_da_empresa_dos_eventos | `codi_emp_eve` | integer(4) |  |  | Código da empresa dos eventos |
| valor_do_evento 🔒 | `valor` | numeric(20) |  |  | Valor do evento |
| valor_da_base | `base` | numeric(17) |  |  | Valor da base |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `foeventos` → `foeventos` por `codi_emp_eve` = `codi_emp` e `i_eventos` = `i_eventos`; colunas: `foeventos_nome`
- `foemprestimos_consignado` → `FOEMPRESTIMOS_CONSIGNADOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_emprestimo` = `i_emprestimo`; colunas: `foemprestimos_consignado_nome`
- `focadbases` → `focadbases` por `i_cadbases` = `i_cadbases`; colunas: `focadbases_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `identificacao_do_calculo` (eq/in), `codigo_do_evento` (eq/in), `codigo_da_base` (eq/in), `codigo_do_emprestimo` (eq/in), `codigo_da_empresa_dos_eventos` (eq/in)

## focalculos_complementos

**Complementos de cálculo** — tabela `FOCALCULOS_COMPLEMENTOS` (232 linhas)

Complementos de cálculo. 232 linhas no catálogo; chave: I_CALCULOS_COMPLEMENTOS.

- **Chave:** `I_CALCULOS_COMPLEMENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_CALCULOS_COMPLEMENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 232 linhas, 104 empresa(s), DATA de 2014-10-07 a 3024-04-30.
- origem_do_complemento_1_lancamento_de_ev: todos os valores reais estão no comentário do banco (3=108, 2=88, 1=36).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 710).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_calculos_complementos` | uniqueidentifier(16) |  |  | Código |
| codigo_renomeado | `i_calculos_complementos_old` | integer(4) |  |  | Código - Renomeado |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| competencia_do_calculo | `competencia` | date(4) |  |  | Competência do cálculo |
| data_do_complemento | `data` | date(4) |  |  | Data do complemento |
| origem_do_complemento_1_lancamento_de_ev | `origem` | smallint(2) |  | focalculos_complementos_origem_do_complemento_1_la | Origem do complemento. (1=Lançamento de eventos/2=Alteração salarial/3=Rescisão/4=Alteração salarial CCT) |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  |  | Origem do registro: (0=Sistema, 1=Importação de tabelas, 2=Importação de leiaute, 3=Conversão) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo` (eq/in), `competencia_do_calculo` (entre/gte/lte), `data_do_complemento` (entre/gte/lte), `codigo_renomeado` (eq/in)

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

### focalculos_complementos_origem_do_complemento_1_la

Confirmado: sim

> Todos os valores observados em FOCALCULOS_COMPLEMENTOS.ORIGEM estão no comentário do banco (2026-10-18). Distribuição: 3=108, 2=88, 1=36.

| Código | Significado |
|---|---|
| 1 | Lançamento de eventos |
| 2 | Alteração salarial |
| 3 | Rescisão |
| 4 | Alteração salarial CCT |

