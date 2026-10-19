# Modelo — Pessoal - movtoserv (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_movtoserv.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

6 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fomovtoserv_planosaude](#fomovtoserv_planosaude) | `FOMOVTOSERV_PLANOSAUDE` | 115.080 | medio | empresa |
| [fomovtoserv_simulacao](#fomovtoserv_simulacao) | `FOMOVTOSERV_SIMULACAO` | 106.705 | medio | empresa |
| [fomovtoserv_pensao_alimenticia](#fomovtoserv_pensao_alimenticia) | `FOMOVTOSERV_PENSAO_ALIMENTICIA` | 2.205 | pequeno | empresa |
| [fomovtoserv_salario_familia](#fomovtoserv_salario_familia) | `FOMOVTOSERV_SALARIO_FAMILIA` | 1.689 | pequeno | empresa |
| [fomovtoserv_dados_formula](#fomovtoserv_dados_formula) | `FOMOVTOSERV_DADOS_FORMULA` | 725 | pequeno | empresa |
| [fomovtoserv_dados_per_dcomp](#fomovtoserv_dados_per_dcomp) | `FOMOVTOSERV_DADOS_PER_DCOMP` | 9 | pequeno | empresa |

## fomovtoserv_planosaude

**Movimentação - Cálculo - Plano de saúde** — tabela `FOMOVTOSERV_PLANOSAUDE` (115.080 linhas)

Movimentação - Cálculo - Plano de saúde. 115.080 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_BENEFICIARIO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_BENEFICIARIO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_EMPREGADOS asc`, `TIPO_PROCES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 115.082 linhas, 87 empresa(s), DATA de 2014-01-01 a 2026-10-01.
- Vínculo fofilhos (fofilhos): 82 de 218 linhas sem registro relacionado (empresa 734).
- Vínculo fooperadoraplanosaude (FOOPERADORAPLANOSAUDE): 0 de 218 linhas sem registro relacionado (empresa 734).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `data` | date(4) |  |  | Competência |
| tipo_de_calculo | `tipo_proces` | integer(4) |  |  | Tipo de cálculo |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| rateio | `rateio` | integer(4) |  |  | Rateio |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| sequencial_de_beneficiario | `i_beneficiario` | integer(4) |  |  | Sequencial de beneficiário |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente |
| valor | `valor` | numeric(13) |  |  | Valor |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigo_da_operadora_de_plano_de_saude | `i_operadoraplanosaude` | integer(4) |  |  | Código da operadora de plano de saúde |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`
- `fooperadoraplanosaude` → `FOOPERADORAPLANOSAUDE` por `i_operadoraplanosaude` = `i_operadoraplanosaude`; colunas: `fooperadoraplanosaude_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_calculo` (eq/in), `codigo_do_evento` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `sequencial_de_beneficiario` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_dependente` (eq/in), `codigo_da_operadora_de_plano_de_saude` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fomovtoserv_simulacao

**Movimentação do cálculo de simulação de rescisão/férias** — tabela `FOMOVTOSERV_SIMULACAO` (106.705 linhas)

Movimentação do cálculo de simulação de rescisão/férias. 106.705 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_EMPREGADOS asc`, `TIPO_PROCES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 106.705 linhas, 192 empresa(s), DATA de 2018-06-01 a 2027-02-01.
- e_simulacao_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=101.062, 0=5.643).
- considerar_para_a_remuneracao_do_esocial: todos os valores reais estão no comentário do banco (1=89.718, 0=16.987).
- considerar_para_a_retencao_de_pagamentos: todos os valores reais estão no comentário do banco (0=104.548, 1=2.157).
- considerar_para_a_remuneracao_para_compo: todos os valores reais estão no comentário do banco (0=86.128, 1=20.577).
- Vínculo foservicos (foservicos): 0 de 156 linhas sem registro relacionado (empresa 9067).
- Vínculo foempregados (foempregados): 0 de 156 linhas sem registro relacionado (empresa 9067).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo empresa |
| empregado | `i_empregados` | integer(4) |  |  | Empregado |
| competencia | `data` | date(4) |  |  | Competencia |
| tipo_folha | `tipo_proces` | integer(4) |  |  | Tipo folha |
| evento | `i_eventos` | integer(4) |  |  | Evento |
| rateio | `rateio` | integer(4) |  |  | Rateio |
| servico | `i_servicos` | integer(4) |  |  | Servico |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| valor_informado | `valor_inf` | numeric(15) |  |  | Valor informado |
| valor_calculado | `valor_cal` | numeric(15) |  |  | Valor Calculado |
| provento_desconto | `prov_desc` | varchar(2) |  |  | Provento/Desconto |
| origem_calculo_origem_calculo_c_mensal_f | `origem` | char(1) |  |  | Origem Calculo (Origem calculo C = mensal / F = férias / I = convocacao intermitente |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_informado_da_folha_complementar | `valor_inf_compl` | numeric(15) |  |  | Valor informado da folha complementar |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| e_simulacao_0_nao_1_sim | `simulacao` | smallint(2) |  | fomovtoserv_simulacao_e_simulacao | É simulação (0=Não/1=Sim) |
| valor_calculado_integral | `valor_calculado_integral` | numeric(15) |  |  | Valor calculado integral. |
| valor_informado_real_utilizado_no_calcul | `valor_informado_real` | numeric(17) |  |  | Valor informado real utilizado no cálculo da rubrica. |
| considerar_para_a_remuneracao_do_esocial | `considerar_remuneracao_esocial` | smallint(2) |  | fomovtoserv_simulacao_considerar_ | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| considerar_para_a_retencao_de_pagamentos | `considerar_retencao_pagamento_esocial` | smallint(2) |  | fomovtoserv_simulacao_considerar_ | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| considerar_para_a_remuneracao_para_compo | `considerar_remuneracao_s_1210_esocial` | smallint(2) |  | fomovtoserv_simulacao_considerar_ | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foservicos` → `foservicos` por `codi_emp` = `codi_emp` e `i_servicos` = `i_servicos`; colunas: `foservicos_nome`
- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `empregado` (eq/in), `competencia` (eq/in), `tipo_folha` (eq/in), `evento` (eq/in), `rateio` (eq/in), `servico` (eq/in), `codigo_do_calculo` (eq/in), `provento_desconto` (eq/in), `origem_calculo_origem_calculo_c_mensal_f` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fomovtoserv_pensao_alimenticia

**Valores de pensão alimentícia nas férias por dependente.** — tabela `FOMOVTOSERV_PENSAO_ALIMENTICIA` (2.205 linhas)

Valores de pensão alimentícia nas férias por dependente.. 2.205 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, I_FILHOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, I_FILHOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.205 linhas, 34 empresa(s), DATA de 2017-09-01 a 2026-11-09.
- Colunas expostas nulas em 100% das linhas (2): codigo_da_convocacao_intermitente_relaci, numero_do_rpa.
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=2.205).
- Vínculo fofilhos (fofilhos): 0 de 45 linhas sem registro relacionado (empresa 364).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia | `data` | date(4) |  |  | Competência. |
| tipo_de_processo | `tipo_processo` | integer(4) |  |  | Tipo de processo. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| valor | `valor` | numeric(13) |  |  | Valor. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | fomovtoserv_pensao_alimenticia_origem_do_r | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| codigo_da_convocacao_intermitente_relaci | `i_convocacao` | numeric(10) |  |  | Código da Convocacao Intermitente Relacionada |
| numero_do_rpa | `numero` | numeric(10) |  |  | Número do RPA |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_processo` (eq/in), `codigo_do_evento` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `codigo_do_dependente` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fomovtoserv_salario_familia

**Dependentes que foram considerados para o cálculo do salário família na rubrica.** — tabela `FOMOVTOSERV_SALARIO_FAMILIA` (1.689 linhas)

Dependentes que foram considerados para o cálculo do salário família na rubrica.. 1.689 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_FILHOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA, TIPO_PROCES, I_EVENTOS, RATEIO, I_SERVICOS, I_FILHOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA`
- **Ordem padrão:** `DATA desc`, `I_EMPREGADOS asc`, `TIPO_PROCES asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.689 linhas, 75 empresa(s), DATA de 2015-01-01 a 2026-09-01.
- Vínculo fofilhos (fofilhos): 0 de 14 linhas sem registro relacionado (empresa 981).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia | `data` | date(4) |  |  | Competência |
| tipo_de_folha | `tipo_proces` | integer(4) |  |  | Tipo de folha. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_folha` (eq/in), `codigo_do_evento` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `codigo_do_dependente` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fomovtoserv_dados_formula

**Informações do cálculo da fórmula.** — tabela `FOMOVTOSERV_DADOS_FORMULA` (725 linhas)

Informações do cálculo da fórmula.. 725 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 725 linhas, 9 empresa(s), COMPETENCIA de 2016-04-01 a 2026-09-01.
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=725).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia_do_calculo | `competencia` | date(4) |  |  | Competência do cálculo. |
| tipo_de_calculo | `tipo_processo` | integer(4) |  |  | Tipo de cálculo. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| base_de_calculo_utilizada | `base_calculo` | numeric(13) |  |  | Base de cálculo utilizada. |
| percentual_utilizado_para_o_calculo | `percentual` | numeric(13) |  |  | Percentual utilizado para o cálculo. |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | fomovtoserv_dados_formula_origem_do_regist | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| dias_dsr_utilizados_no_calculo_da_formul | `dias_dsr` | smallint(2) |  |  | Dias DSR utilizados no cálculo da fórmula do evento. |
| dias_trabalhados_utilizados_no_calculo_d | `dias_trabalhados` | smallint(2) |  |  | Dias trabalhados utilizados no cálculo da fórmula do evento. |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia_do_calculo` (eq/in), `tipo_de_calculo` (eq/in), `codigo_do_evento` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fomovtoserv_dados_per_dcomp

**Informações do cálculo da fórmula.** — tabela `FOMOVTOSERV_DADOS_PER_DCOMP` (9 linhas)

Informações do cálculo da fórmula.. 9 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, SEQUENCIAL, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, SEQUENCIAL, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas, 1 empresa(s), COMPETENCIA de 2022-10-01 a 2023-01-01.
- Colunas expostas nulas em 100% das linhas (1): codigo_do_filho.
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=9).
- tipo: todos os valores reais estão no comentário do banco (2=8, 3=1).
- Vínculo fofilhos (fofilhos): 9 de 9 linhas sem registro relacionado (empresa 911).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia_do_calculo | `competencia` | date(4) |  |  | Competência do cálculo. |
| tipo_de_calculo | `tipo_processo` | integer(4) |  |  | Tipo de cálculo. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| codigo_do_filho | `i_filhos` | integer(4) |  |  | Código do filho. |
| valor_calculado | `valor_calculado` | numeric(13) |  |  | Valor calculado. |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | fomovtoserv_dados_per_dcomp_origem_do_regist | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| tipo | `tipo` | smallint(2) |  | fomovtoserv_dados_per_dcomp_tipo_do_calculo_ | Tipo do calculo que a rubrica pertence (1=Salário Familia/2=Maternidade/3=Maternidade 13o) |
| provento_desconto | `prov_desc` | varchar(2) |  |  | Provento/Desconto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia_do_calculo` (eq/in), `tipo_de_calculo` (eq/in), `codigo_do_evento` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `sequencial` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in), `codigo_do_filho` (eq/in), `tipo` (eq/in), `provento_desconto` (eq/in)

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

### fomovtoserv_simulacao_e_simulacao

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_SIMULACAO.SIMULACAO estão no comentário do banco (2026-10-18). Distribuição: 1=101.062, 0=5.643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomovtoserv_simulacao_considerar_

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_SIMULACAO.CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=86.128, 1=20.577.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomovtoserv_pensao_alimenticia_origem_do_r

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_PENSAO_ALIMENTICIA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=2.205.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

### fomovtoserv_dados_formula_origem_do_regist

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_DADOS_FORMULA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=725.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Importação de tabelas |
| 2 | Importação de layout |

### fomovtoserv_dados_per_dcomp_origem_do_regist

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_DADOS_PER_DCOMP.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=9.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Importação de tabelas |
| 2 | Importação de layout |

### fomovtoserv_dados_per_dcomp_tipo_do_calculo_

Confirmado: sim

> Todos os valores observados em FOMOVTOSERV_DADOS_PER_DCOMP.TIPO estão no comentário do banco (2026-10-18). Distribuição: 2=8, 3=1.

| Código | Significado |
|---|---|
| 1 | Salário Familia |
| 2 | Maternidade |
| 3 | Maternidade 13o |

