# Modelo — Pessoal - memoria (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_memoria.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fomemoria_calculo_inss](#fomemoria_calculo_inss) | `FOMEMORIA_CALCULO_INSS` | 1.167.319 | grande | empresa; um de: codigo_do_empregado |
| [fomemoria_calculo_diferenca_salario_bases](#fomemoria_calculo_diferenca_salario_bases) | `FOMEMORIA_CALCULO_DIFERENCA_SALARIO_BASES` | 419.415 | medio | um de: codigo_do_calculo_da_diferenca, codigo_do_calculo_ajustado |
| [fomemoria_calculo_salario_proporcional](#fomemoria_calculo_salario_proporcional) | `FOMEMORIA_CALCULO_SALARIO_PROPORCIONAL` | 129.546 | medio | empresa |
| [fomemoria_calculo_diferenca_salario](#fomemoria_calculo_diferenca_salario) | `FOMEMORIA_CALCULO_DIFERENCA_SALARIO` | 53.380 | medio | empresa |
| [fomemoria_calculo_diferenca](#fomemoria_calculo_diferenca) | `FOMEMORIA_CALCULO_DIFERENCA` | 26.117 | medio | — |
| [fomemoria_calculo_diferenca_salarial_cct_esocial](#fomemoria_calculo_diferenca_salarial_cct_esocial) | `FOMEMORIA_CALCULO_DIFERENCA_SALARIAL_CCT_ESOCIAL` | 1.678 | pequeno | empresa |
| [fomemoria_calculo_salario_indenizacao_mp_936](#fomemoria_calculo_salario_indenizacao_mp_936) | `FOMEMORIA_CALCULO_SALARIO_INDENIZACAO_MP_936` | 7 | pequeno | empresa |

## fomemoria_calculo_inss

**Memória de cálculo do INSS** — tabela `FOMEMORIA_CALCULO_INSS` (1.167.319 linhas)

Memória de cálculo do INSS. 1.167.319 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, SEQUENCIAL, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_EVENTOS, RATEIO, I_SERVICOS, SEQUENCIAL, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA` · exige um de: `codigo_do_empregado`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.167.365 linhas, 352 empresa(s), COMPETENCIA de 2020-03-01 a 2026-11-30.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_de_processo | `tipo_processo` | integer(4) |  |  | Tipo de processo. |
| codigo_da_rubrica | `i_eventos` | integer(4) |  |  | Código da rubrica. |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| tipo_de_descricao_valor | `tipo` | integer(4) |  |  | Tipo de descrição/valor. |
| descricao | `descricao` | varchar(255) |  |  | Descrição. |
| valor | `valor` | numeric(15) |  |  | Valor. |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_processo` (eq/in), `codigo_da_rubrica` (eq/in), `rateio` (eq/in), `codigo_do_servico` (eq/in), `sequencial` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in), `tipo_de_descricao_valor` (eq/in), `descricao` (contem/prefixo)

## fomemoria_calculo_diferenca_salario_bases

**Memória de cálculo de diferença de salário - Bases de cálculo** — tabela `FOMEMORIA_CALCULO_DIFERENCA_SALARIO_BASES` (419.415 linhas)

Memória de cálculo de diferença de salário - Bases de cálculo. 419.415 linhas no catálogo; chave: I_CADBASES, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA.

- **Chave:** `I_CADBASES, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—` · exige um de: `codigo_do_calculo_da_diferenca, codigo_do_calculo_ajustado`
- **Ordem padrão:** `I_CADBASES asc`, `I_SERVICOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 419.415 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_base_de_calculo | `i_cadbases` | integer(4) |  |  | Código da base de cálculo |
| servico | `i_servicos` | integer(4) |  |  | Serviço. |
| rateio | `rateio` | smallint(2) |  |  | Rateio. |
| codigo_do_calculo_ajustado | `i_calculos_ajustado` | uniqueidentifier(16) |  |  | Código do cálculo ajustado |
| codigo_do_calculo_da_diferenca | `i_calculos_diferenca` | uniqueidentifier(16) |  |  | Código do cálculo da diferença |
| codigo_do_calculo_da_diferenca_renomeado | `i_calculos_diferenca_old` | integer(4) |  |  | Código do cálculo da diferença - Renomeado |
| codigo_do_calculo_ajustado_renomeado | `i_calculos_ajustado_old` | integer(4) |  |  | Código do cálculo ajustado - Renomeado |
| base_ajustada | `base` | numeric(13) |  |  | Base ajustada. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_da_base_ajustada | `valor` | numeric(17) |  |  | Valor da base ajustada. |
| codigo_da_forma_de_ajuste_conforme_parce | `i_forma_ajuste_parcelamento` | integer(4) |  |  | Código da forma de ajuste conforme parcelamento. |

**Filtros:** `codigo_da_base_de_calculo` (eq/in), `servico` (eq/in), `rateio` (eq/in), `codigo_do_calculo_ajustado` (eq/in), `codigo_do_calculo_da_diferenca` (eq/in), `codigo_do_calculo_da_diferenca_renomeado` (eq/in), `codigo_do_calculo_ajustado_renomeado` (eq/in), `codigo_da_forma_de_ajuste_conforme_parce` (eq/in)

## fomemoria_calculo_salario_proporcional

**Memória de cálculo do salário proporcional.** — tabela `FOMEMORIA_CALCULO_SALARIO_PROPORCIONAL` (129.546 linhas)

Memória de cálculo do salário proporcional.. 129.546 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_SERVICOS, RATEIO, SEQUENCIAL, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_SERVICOS, RATEIO, SEQUENCIAL, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_INICIO_REDUCAO`
- **Ordem padrão:** `DATA_INICIO_REDUCAO desc`, `I_EMPREGADOS asc`, `COMPETENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 129.576 linhas, 541 empresa(s), DATA_INICIO_REDUCAO de 2020-04-01 a 2021-07-17.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_da_folha | `tipo_processo` | integer(4) |  |  | Tipo da folha |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| rateio_do_servico | `rateio` | integer(4) |  |  | Rateio do serviço |
| codigo_sequencial | `sequencial` | integer(4) |  |  | Código sequencial |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo. |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| data_de_inicio_do_periodo | `periodo_inicio` | date(4) |  |  | Data de início do período |
| data_de_fim_do_periodo | `periodo_fim` | date(4) |  |  | Data de fim do período |
| quantidade_de_dias_no_mes | `dias_mes` | integer(4) |  |  | Quantidade de dias no mês |
| quantidade_de_dias_proporcionais | `dias_proporcional` | integer(4) |  |  | Quantidade de dias proporcionais |
| valor_do_salario_base_para_calculo 🔒 | `salario_base_calculo` | numeric(15) |  |  | Valor do salário base para cálculo |
| valor_proporcional | `valor_proporcional` | numeric(15) |  |  | Valor proporcional |
| valor_do_percentual_de_reducao | `reducao` | numeric(5) |  |  | Valor do percentual de redução |
| data_de_inicio_da_reducao | `data_inicio_reducao` | date(4) |  |  | Data de início da redução |
| data_final_da_reducao | `data_fim_reducao` | date(4) |  |  | Data final da redução |
| tipo_de_calculo_1_integral_2_com_reducao | `tipo_calculo` | integer(4) |  |  | Tipo de cálculo 1=Integral/2=Com redução. |
| tipo_de_memoria_de_calculo_1_salario_2_s 🔒 | `tipo_salario` | integer(4) |  |  | Tipo de memória de cálculo 1=Salário/2=Sindicato. |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_da_folha` (eq/in), `codigo_do_servico` (eq/in), `rateio_do_servico` (eq/in), `codigo_sequencial` (eq/in), `codigo_do_calculo` (eq/in), `data_de_inicio_do_periodo` (entre/gte/lte), `data_de_fim_do_periodo` (entre/gte/lte), `data_de_inicio_da_reducao` (entre/gte/lte), `data_final_da_reducao` (entre/gte/lte), `codigo_do_calculo_renomeado` (eq/in), `tipo_de_calculo_1_integral_2_com_reducao` (eq/in), `tipo_de_memoria_de_calculo_1_salario_2_s` (eq/in)

## fomemoria_calculo_diferenca_salario

**MEMÓRIA DE CÁLCULO DE DIFERENÇA DE SALÁRIO** — tabela `FOMEMORIA_CALCULO_DIFERENCA_SALARIO` (53.380 linhas)

MEMÓRIA DE CÁLCULO DE DIFERENÇA DE SALÁRIO. 53.380 linhas no catálogo; chave: I_EVENTOS, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA.

- **Chave:** `I_EVENTOS, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EVENTOS asc`, `I_SERVICOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 53.380 linhas, 206 empresa(s).
- considerar_para_a_remuneracao_do_esocial: todos os valores reais estão no comentário do banco (0=38.331, 1=15.049).
- considerar_para_a_retencao_de_pagamentos: todos os valores reais estão no comentário do banco (0=53.380).
- considerar_para_a_remuneracao_para_compo: todos os valores reais estão no comentário do banco (0=43.542, 1=9.838).
- rubrica_referente_a_convencao_coletiva_d: todos os valores reais estão no comentário do banco (0=46.187, 1=7.193).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_evento | `i_eventos` | integer(4) |  |  | CÓDIGO DO EVENTO |
| servico | `i_servicos` | integer(4) |  |  | Serviço. |
| rateio | `rateio` | smallint(2) |  |  | Rateio. |
| codigo_do_calculo_ajustado | `i_calculos_ajustado` | uniqueidentifier(16) |  |  | CÓDIGO DO CÁLCULO AJUSTADO |
| codigo_do_calculo_da_diferenca | `i_calculos_diferenca` | uniqueidentifier(16) |  |  | CÓDIGO DO CÁLCULO DA DIFERENÇA |
| codigo_do_calculo_da_diferenca_renomeado | `i_calculos_diferenca_old` | integer(4) |  |  | CÓDIGO DO CÁLCULO DA DIFERENÇA - Renomeado |
| codigo_do_calculo_ajustado_renomeado | `i_calculos_ajustado_old` | integer(4) |  |  | CÓDIGO DO CÁLCULO AJUSTADO - Renomeado |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | CÓDIGO DA EMPRESA |
| valor_do_evento_ajustado 🔒 | `valor` | numeric(13) |  |  | VALOR DO EVENTO AJUSTADO |
| codigo_da_forma_de_ajuste_conforme_parce | `i_forma_ajuste_parcelamento` | integer(4) |  |  | Código da forma de ajuste conforme parcelamento. |
| considerar_para_a_remuneracao_do_esocial | `considerar_remuneracao_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salario_considerar_ | Considerar para a remuneração do eSocial. (0=Não/1=Sim) |
| considerar_para_a_retencao_de_pagamentos | `considerar_retencao_pagamento_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salario_considerar_ | Considerar para a retenção de pagamentos do eSocial. (0=Não/1=Sim) |
| considerar_para_a_remuneracao_para_compo | `considerar_remuneracao_s_1210_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salario_considerar_ | Considerar para a remuneração para compor liquido evento S-1210 do eSocial. (0=Não/1=Sim) |
| rubrica_referente_a_convencao_coletiva_d | `diferenca_cct_esocial` | integer(4) |  | fomemoria_calculo_diferenca_salario_rubrica_ref | Rubrica referente a Convenção Coletiva de Trabalho para o eSocial (0-Não/1-Sim) |
| codigo_do_calculo_do_pagamento_do_adicio | `i_calculos_pagamento_adicional_mp_927_old` | integer(4) |  |  | Código do cálculo do pagamento do adicional MP 927 - Renomeado |

**Filtros:** `codigo_do_evento` (eq/in), `servico` (eq/in), `rateio` (eq/in), `codigo_do_calculo_ajustado` (eq/in), `codigo_do_calculo_da_diferenca` (eq/in), `codigo_do_calculo_da_diferenca_renomeado` (eq/in), `codigo_do_calculo_ajustado_renomeado` (eq/in), `codigo_da_forma_de_ajuste_conforme_parce` (eq/in), `codigo_do_calculo_do_pagamento_do_adicio` (eq/in)

## fomemoria_calculo_diferenca

**Memória de cálculo do cálculo da diferença** — tabela `FOMEMORIA_CALCULO_DIFERENCA` (26.117 linhas)

Memória de cálculo do cálculo da diferença. 26.117 linhas no catálogo; chave: I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA.

- **Chave:** `I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CALCULOS_AJUSTADO asc`, `I_CALCULOS_DIFERENCA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 26.117 linhas.
- calculo_de_diferenca_cct_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=24.123, 1=1.994).
- diferenca_referente_a_antecipacao_salari: todos os valores reais estão no comentário do banco (0=26.117).
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=26.117).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_calculo_ajustado | `i_calculos_ajustado` | uniqueidentifier(16) |  |  | Código do cálculo ajustado |
| codigo_do_calculo_da_diferenca | `i_calculos_diferenca` | uniqueidentifier(16) |  |  | Código do cálculo da diferença |
| codigo_do_calculo_da_diferenca_renomeado | `i_calculos_diferenca_old` | integer(4) |  |  | Código do cálculo da diferença - Renomeado |
| codigo_do_calculo_ajustado_renomeado | `i_calculos_ajustado_old` | integer(4) |  |  | Código do cálculo ajustado - Renomeado |
| calculo_de_diferenca_cct_0_nao_1_sim | `diferenca_cct` | smallint(2) |  | fomemoria_calculo_diferenca_calculo_de_ | Cálculo de diferença CCT.(0=Não/1=Sim) |
| diferenca_referente_a_antecipacao_salari | `antecipacao_salarial` | smallint(2) |  | fomemoria_calculo_diferenca_diferenca_r | Diferença referente a antecipação salarial.(0=Não/1=Sim) |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | fomemoria_calculo_diferenca_origem_do_r | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de leiaute/3=Conversão) |

**Filtros:** `codigo_do_calculo_ajustado` (eq/in), `codigo_do_calculo_da_diferenca` (eq/in), `codigo_do_calculo_da_diferenca_renomeado` (eq/in), `codigo_do_calculo_ajustado_renomeado` (eq/in)

## fomemoria_calculo_diferenca_salarial_cct_esocial

**Memória de cálculo do cálculo de diferença salarial CCT com algumas considerações do eSocial** — tabela `FOMEMORIA_CALCULO_DIFERENCA_SALARIAL_CCT_ESOCIAL` (1.678 linhas)

Memória de cálculo do cálculo de diferença salarial CCT com algumas considerações do eSocial. 1.678 linhas no catálogo; chave: I_EVENTOS, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA.

- **Chave:** `I_EVENTOS, I_SERVICOS, RATEIO, I_CALCULOS_AJUSTADO, I_CALCULOS_DIFERENCA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EVENTOS asc`, `I_SERVICOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.678 linhas, 65 empresa(s).
- considerar_para_a_remuneracao_do_esocial: todos os valores reais estão no comentário do banco (1=1.678).
- considerar_para_a_retencao_de_pagamentos: todos os valores reais estão no comentário do banco (0=1.678).
- considerar_para_a_remuneracao_para_compo: todos os valores reais estão no comentário do banco (1=1.678).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| servico | `i_servicos` | integer(4) |  |  | Serviço. |
| rateio | `rateio` | smallint(2) |  |  | Rateio. |
| codigo_do_calculo_ajustado | `i_calculos_ajustado` | uniqueidentifier(16) |  |  | Código do cálculo ajustado |
| codigo_do_calculo_da_diferenca | `i_calculos_diferenca` | uniqueidentifier(16) |  |  | Código do cálculo da diferença |
| codigo_do_calculo_da_diferenca_renomeado | `i_calculos_diferenca_old` | integer(4) |  |  | Código do cálculo da diferença - Renomeado |
| codigo_do_calculo_ajustado_renomeado | `i_calculos_ajustado_old` | integer(4) |  |  | Código do cálculo ajustado - Renomeado |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| valor_do_evento_ajustado 🔒 | `valor` | numeric(30) |  |  | Valor do evento ajustado |
| considerar_para_a_remuneracao_do_esocial | `considerar_remuneracao_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salarial_cct_esocial_considerar_ | Considerar para a remuneração do esocial. (0=Não/1=Sim) |
| considerar_para_a_retencao_de_pagamentos | `considerar_retencao_pagamento_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salarial_cct_esocial_considerar_ | Considerar para a retenção de pagamentos do esocial. (0=Não/1=Sim) |
| considerar_para_a_remuneracao_para_compo | `considerar_remuneracao_s_1210_esocial` | smallint(2) |  | fomemoria_calculo_diferenca_salarial_cct_esocial_considerar_ | Considerar para a remuneração para compor liquido evento s-1210 do esocial. (0=Não/1=Sim) |

**Filtros:** `codigo_do_evento` (eq/in), `servico` (eq/in), `rateio` (eq/in), `codigo_do_calculo_ajustado` (eq/in), `codigo_do_calculo_da_diferenca` (eq/in), `codigo_do_calculo_da_diferenca_renomeado` (eq/in), `codigo_do_calculo_ajustado_renomeado` (eq/in)

## fomemoria_calculo_salario_indenizacao_mp_936

**Memória de cálculo da indenização MP 936.** — tabela `FOMEMORIA_CALCULO_SALARIO_INDENIZACAO_MP_936` (7 linhas)

Memória de cálculo da indenização MP 936.. 7 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_SERVICOS, RATEIO, SEQUENCIAL, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESSO, I_SERVICOS, RATEIO, SEQUENCIAL, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_INICIO_REDUCAO`
- **Ordem padrão:** `DATA_INICIO_REDUCAO desc`, `I_EMPREGADOS asc`, `COMPETENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 4 empresa(s), DATA_INICIO_REDUCAO de 2020-07-14 a 2021-05-03.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_da_folha | `tipo_processo` | integer(4) |  |  | Tipo da folha |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| rateio_do_servico | `rateio` | integer(4) |  |  | Rateio do serviço |
| codigo_sequencial | `sequencial` | integer(4) |  |  | Código sequencial |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo. |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| data_de_inicio_do_periodo_de_estabilidad | `periodo_inicio_estabilidade` | date(4) |  |  | Data de início do período de estabilidade |
| data_de_fim_do_periodo_de_estabilidade | `periodo_fim_estabilidade` | date(4) |  |  | Data de fim do período de estabilidade |
| dias_de_estabilidade | `dias_estabilidade` | integer(4) |  |  | Dias de estabilidade |
| tipo_de_medida | `tipo_medida` | integer(4) |  |  | Tipo de medida |
| quantidade_de_dias_no_mes | `dias_mes` | integer(4) |  |  | Quantidade de dias no mês |
| valor_do_percentual_de_reducao | `percentual_reducao` | numeric(5) |  |  | Valor do percentual de redução |
| valor_do_percentual_de_indenizacao | `percentual_indenizacao` | numeric(5) |  |  | Valor do percentual de indenização |
| valor_do_salario_base_para_calculo 🔒 | `salario_base_calculo` | numeric(13) |  |  | Valor do salário base para cálculo |
| valor_da_indenizacao | `valor_indenizacao` | numeric(13) |  |  | Valor da indenização |
| data_de_inicio_da_reducao | `data_inicio_reducao` | date(4) |  |  | Data de início da redução |
| data_final_da_reducao | `data_fim_reducao` | date(4) |  |  | Data final da redução |

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_da_folha` (eq/in), `codigo_do_servico` (eq/in), `rateio_do_servico` (eq/in), `codigo_sequencial` (eq/in), `codigo_do_calculo` (eq/in), `data_de_inicio_do_periodo_de_estabilidad` (entre/gte/lte), `data_de_fim_do_periodo_de_estabilidade` (entre/gte/lte), `data_de_inicio_da_reducao` (entre/gte/lte), `data_final_da_reducao` (entre/gte/lte), `codigo_do_calculo_renomeado` (eq/in), `tipo_de_medida` (eq/in)

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

### fomemoria_calculo_diferenca_salario_considerar_

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA_SALARIO.CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=43.542, 1=9.838.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomemoria_calculo_diferenca_salario_rubrica_ref

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA_SALARIO.DIFERENCA_CCT_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=46.187, 1=7.193.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomemoria_calculo_diferenca_calculo_de_

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA.DIFERENCA_CCT estão no comentário do banco (2026-10-18). Distribuição: 0=24.123, 1=1.994.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomemoria_calculo_diferenca_diferenca_r

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA.ANTECIPACAO_SALARIAL estão no comentário do banco (2026-10-18). Distribuição: 0=26.117.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fomemoria_calculo_diferenca_origem_do_r

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=26.117.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Importação de tabelas |
| 2 | Importação de leiaute |
| 3 | Conversão |

### fomemoria_calculo_diferenca_salarial_cct_esocial_considerar_

Confirmado: sim

> Todos os valores observados em FOMEMORIA_CALCULO_DIFERENCA_SALARIAL_CCT_ESOCIAL.CONSIDERAR_REMUNERACAO_S_1210_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=1.678.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

