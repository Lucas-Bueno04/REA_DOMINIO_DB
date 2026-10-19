# Modelo — Pessoal - basesserv (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_basesserv.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fobasesserv_calculos_rateio_servico](#fobasesserv_calculos_rateio_servico) | `FOBASESSERV_CALCULOS_RATEIO_SERVICO` | 628.958 | medio | empresa |
| [fobasesserv_envios_esocial](#fobasesserv_envios_esocial) | `FOBASESSERV_ENVIOS_ESOCIAL` | 349.595 | medio | empresa |
| [fobasesserv_fofilhos](#fobasesserv_fofilhos) | `FOBASESSERV_FOFILHOS` | 10.482 | medio | empresa |
| [fobasesserv_simulacao](#fobasesserv_simulacao) | `FOBASESSERV_SIMULACAO` | 6.039 | pequeno | empresa |

## fobasesserv_calculos_rateio_servico

**Relacionamento entre o cálculo principal e os cálculos de rateio por serviço.** — tabela `FOBASESSERV_CALCULOS_RATEIO_SERVICO` (628.958 linhas)

Relacionamento entre o cálculo principal e os cálculos de rateio por serviço.. 628.958 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, CODI_EMP_RELACIONADO, I_EMPREGADOS_RELACIONADO, COMPETENCIA_RELACIONADO, TIPO_PROCESS_RELACIONADO, I_SERVICOS_RELACIONADO, RATEIO_RELACIONADO, I_CALCULOS, I_CALCULOS_RELACIONADO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, CODI_EMP_RELACIONADO, I_EMPREGADOS_RELACIONADO, COMPETENCIA_RELACIONADO, TIPO_PROCESS_RELACIONADO, I_SERVICOS_RELACIONADO, RATEIO_RELACIONADO, I_CALCULOS, I_CALCULOS_RELACIONADO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 628.998 linhas, 865 empresa(s), COMPETENCIA de 2013-01-01 a 2026-11-01.
- existe_registro_de_rateio_para_o_calculo: todos os valores reais estão no comentário do banco (0=620.310, 1=8.688).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa_do_calculo_integral | `codi_emp` | integer(4) |  |  | Código da empresa do cálculo integral. |
| codigo_do_empregado_do_calculo_integral | `i_empregados` | integer(4) |  |  | Código do empregado do cálculo integral. |
| competencia_do_calculo_integral | `competencia` | date(4) |  |  | Competência do cálculo integral. |
| tipo_de_processo_do_calculo_integral | `tipo_process` | integer(4) |  |  | Tipo de processo do cálculo integral. |
| codigo_do_servico_do_calculo_integral | `i_servicos` | integer(4) |  |  | Código do serviço do cálculo integral. |
| rateio_do_calculo_integral | `rateio` | integer(4) |  |  | Rateio do cálculo integral. |
| codigo_da_empresa_do_calculo_relacionado | `codi_emp_relacionado` | integer(4) |  |  | Código da empresa do cálculo relacionado. |
| codigo_do_empregado_do_calculo_relaciona | `i_empregados_relacionado` | integer(4) |  |  | Código do empregado do cálculo relacionado. |
| competencia_do_calculo_relacionado | `competencia_relacionado` | date(4) |  |  | Competência do cálculo relacionado. |
| tipo_de_processo_do_calculo_relacionado | `tipo_process_relacionado` | integer(4) |  |  | Tipo de processo do cálculo relacionado. |
| codigo_do_servico_do_calculo_relacionado | `i_servicos_relacionado` | integer(4) |  |  | Código do serviço do cálculo relacionado. |
| rateio_do_calculo_relacionado | `rateio_relacionado` | integer(4) |  |  | Rateio do cálculo relacionado. |
| codigo_do_calculo_do_calculo_integral | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo do cálculo integral. |
| codigo_do_calculo_do_calculo_relacionado | `i_calculos_relacionado` | uniqueidentifier(16) |  |  | Código do cálculo do cálculo relacionado. |
| codigo_do_calculo_do_calculo_integral_re | `i_calculos_old` | integer(4) |  |  | Código do cálculo do cálculo integral - Renomeado |
| codigo_do_complemento_de_calculo_do_calc | `i_calculos_complementos_old` | integer(4) |  |  | Código do complemento de cálculo do cálculo integral - Renomeado |
| i_calculos_relacionado_old | `i_calculos_relacionado_old` | integer(4) |  |  | Código do cálculo do cálculo relacionado - Renomeado |
| i_calculos_complementos_relacionado_old | `i_calculos_complementos_relacionado_old` | integer(4) |  |  | Código do complemento de cálculo do cálculo relacionado - Renomeado |
| existe_registro_de_rateio_para_o_calculo | `existe_calculo_rateio` | smallint(2) |  | fobasesserv_calculos_rateio_servico_existe_regi | Existe registro de rateio para o cálculo principal.(0=Não/1=Sim) |
| situacao_mes_do_calculo | `situacao_mes` | integer(4) |  |  | Situação mês do cálculo. |

**Filtros:** `codigo_do_empregado_do_calculo_integral` (eq/in), `competencia_do_calculo_integral` (eq/in), `tipo_de_processo_do_calculo_integral` (eq/in), `codigo_do_servico_do_calculo_integral` (eq/in), `rateio_do_calculo_integral` (eq/in), `codigo_da_empresa_do_calculo_relacionado` (eq/in), `codigo_do_empregado_do_calculo_relaciona` (eq/in), `competencia_do_calculo_relacionado` (eq/in), `tipo_de_processo_do_calculo_relacionado` (eq/in), `codigo_do_servico_do_calculo_relacionado` (eq/in), `rateio_do_calculo_relacionado` (eq/in), `codigo_do_calculo_do_calculo_integral` (eq/in), `codigo_do_calculo_do_calculo_relacionado` (eq/in), `codigo_do_calculo_do_calculo_integral_re` (eq/in)

## fobasesserv_envios_esocial

**Envios de bases de cálculo para o esocial** — tabela `FOBASESSERV_ENVIOS_ESOCIAL` (349.595 linhas)

Envios de bases de cálculo para o esocial. 349.595 linhas no catálogo; chave: codi_emp, i_empregados, competencia, tipo_process, i_servicos, rateio, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS, I_CALCULOS.

- **Chave:** `codi_emp, i_empregados, competencia, tipo_process, i_servicos, rateio, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS, I_CALCULOS`
- **Empresa:** `codi_emp`
- **Período:** `competencia`
- **Ordem padrão:** `competencia desc`, `i_empregados asc`, `tipo_process asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 349.606 linhas, 468 empresa(s), competencia de 2018-10-01 a 2026-10-05.
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 94 linhas sem registro relacionado (empresa 1592).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_da_folha | `tipo_process` | integer(4) |  |  | Tipo da folha |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| rateio | `rateio` | integer(4) |  |  | Rateio |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_evento_referente_a_foesocial_d | `i_dados_eventos` | integer(4) |  |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo. |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp_dados_eventos` = `codi_emp` e `i_dados_eventos` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_da_folha` (eq/in), `codigo_do_servico` (eq/in), `rateio` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_do_evento_referente_a_foesocial_d` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fobasesserv_fofilhos

**Dependentes que foram considerados para o cálculo.** — tabela `FOBASESSERV_FOFILHOS` (10.482 linhas)

Dependentes que foram considerados para o cálculo.. 10.482 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, I_FILHOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, I_FILHOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10.484 linhas, 127 empresa(s), COMPETENCIA de 2017-12-15 a 2026-12-01.
- Vínculo fofilhos (fofilhos): 0 de 40 linhas sem registro relacionado (empresa 1161).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| competencia | `competencia` | date(4) |  |  | Competência |
| tipo_de_folha | `tipo_process` | integer(4) |  |  | Tipo de folha. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| rateio | `rateio` | integer(4) |  |  | Rateio. |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente. |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `competencia` (eq/in), `tipo_de_folha` (eq/in), `codigo_do_servico` (eq/in), `rateio` (eq/in), `codigo_do_dependente` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## fobasesserv_simulacao

**Bases da simulação de rescisão/férias** — tabela `FOBASESSERV_SIMULACAO` (6.039 linhas)

Bases da simulação de rescisão/férias. 6.039 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, TIPO_PROCESS, I_SERVICOS, RATEIO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_PAGTO`
- **Ordem padrão:** `DATA_PAGTO desc`, `I_EMPREGADOS asc`, `COMPETENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6.039 linhas, 192 empresa(s), DATA_PAGTO de 2018-07-06 a 9022-01-09.
- Colunas expostas nulas em 100% das linhas (5): competencia_da_alteracao_salarial_cct, indica_no_calculo_do_13o_salario_se_a_fo, codigo_do_calculo_que_descontou_o_arredo, codigo_do_complemento_de_calculo_renomea, codigo_do_periodo_gozo_da_licenca_premio.
- permite_alterar_a_data_de_pagamento_0_na: todos os valores reais estão no comentário do banco (1=6.039).
- gravou_as_bases_de_calculo_das_diferenca: todos os valores reais estão no comentário do banco (1=5.188, 0=851).
- calcular_diferenca_13o_adiantamento_0_na: todos os valores reais estão no comentário do banco (0=6.039).
- calcula_o_13o_adiantamento_folha_mensal: todos os valores reais estão no comentário do banco (0=6.039).
- calcula_o_13o_adiantamento_conforme_avos: todos os valores reais estão no comentário do banco (0=6.039).
- considerou_medias_diferenciadas_para_com: todos os valores reais estão no comentário do banco (0=5.642, 1=397).
- simulacao_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=5.188, 0=851).
- calcular_adiantamento_13o_com_base_no_sa: todos os valores reais estão no comentário do banco (0=6.039).
- gravou_o_valor_integral_das_rubricas_que: todos os valores reais estão no comentário do banco (1=6.039).
- Vínculo foservicos (foservicos): 0 de 9 linhas sem registro relacionado (empresa 735).
- Vínculo foccustos (foccustos): 0 de 9 linhas sem registro relacionado (empresa 735).
- Vínculo focargos (focargos): 0 de 9 linhas sem registro relacionado (empresa 735).
- Vínculo fodepto (fodepto): 0 de 9 linhas sem registro relacionado (empresa 735).
- Vínculo foempregados (foempregados): 0 de 9 linhas sem registro relacionado (empresa 735).
- Vínculo fofiliais (fofiliais): 0 de 9 linhas sem registro relacionado (empresa 735).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo empresa |
| empregado | `i_empregados` | integer(4) |  |  | Empregado |
| competencia | `competencia` | date(4) |  |  | Competencia |
| tipo_de_calculo | `tipo_process` | integer(4) |  |  | TIPO DE CALCULO |
| servico | `i_servicos` | integer(4) |  |  | Servico |
| rateio | `rateio` | integer(4) |  |  | Rateio |
| codigo_sequencial_de_calculos | `i_calculos` | uniqueidentifier(16) |  |  | Código sequencial de calculos |
| departamento | `i_depto` | integer(4) |  |  | Departamento |
| centro_de_custos | `i_ccustos` | integer(4) |  |  | Centro de Custos |
| cargo | `i_cargos` | integer(4) |  |  | Cargo |
| situacao_mes | `situacao_mes` | integer(4) |  |  | Situação: (0~89) |
| no_filhos | `num_filhos` | integer(4) |  |  | No. filhos |
| no_dependentes | `num_dependentes` | integer(4) |  |  | No. Dependentes |
| proventos 🔒 | `proventos` | numeric(13) |  |  | Proventos |
| descontos | `descontos` | numeric(13) |  |  | Descontos |
| salario_maternidade 🔒 | `salario_maternidade` | numeric(13) |  |  | Salario Maternidade |
| salario_mes 🔒 | `salario_mes` | numeric(13) |  |  | Salario Mes |
| valor_sal_familia | `val_sal_fam` | numeric(13) |  |  | Valor Sal. Familia |
| no_cheque | `nume_cheque` | integer(4) |  |  | No. Cheque |
| dedinssmat13 | `dedinssmat13` | numeric(13) |  |  | Deducao INSS 13 |
| data_pagamento | `data_pagto` | date(4) |  |  | Data pagamento |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| numero_de_dias_que_o_empregado_ficou_no | `dias_servico` | integer(4) |  |  | Numero de dias que o empregado ficou no servico |
| c_1_dados_implantados_0_calculado_pelo_s | `implantado` | tinyint(1) |  |  | 1=Dados implantados, 0=Calculado pelo sistema |
| filial | `i_filiais` | integer(4) |  |  | Filial |
| codigo_sequencial_de_calculos_renomeado | `i_calculos_old` | integer(4) |  |  | Código sequencial de calculos - Renomeado |
| categoria | `categoria` | smallint(2) |  |  | Categoria |
| horas_dia | `horas_dia` | numeric(5) |  |  | Horas dia |
| horas_semana | `horas_semana` | numeric(5) |  |  | Horas semana |
| horas_mes | `horas_mes` | numeric(5) |  |  | Horas mes |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| competencia_da_alteracao_salarial_cct | `competencia_cct` | date(4) |  |  | Competência da alteração salarial CCT |
| indica_no_calculo_do_13o_salario_se_a_fo | `folha_mes_paga` | smallint(2) |  |  | Indica no cálculo do 13º salário se a folha do mês já foi paga: 0=Não/1=Sim |
| tipo_do_calculo_proporcional_1_mes_comer | `tipo_calculo_prop` | smallint(2) |  |  | Tipo do cálculo proporcional: 1=Mês comercial/2=Mês civil |
| vinculo_empregaticio | `vinculo` | smallint(2) |  |  | Vínculo empregatício |
| diferenca_de_inss_13o_salario_descontado 🔒 | `dif_inss_13_desc_maior` | numeric(13) |  |  | Diferença de INSS 13º salário descontado a maior |
| percentual_de_adiantamento | `percentual_adiantamento` | numeric(5) |  |  | Percentual de adiantamento |
| permite_alterar_a_data_de_pagamento_0_na | `permite_alterar_data_pagamento` | smallint(2) |  | fobasesserv_simulacao_permite_alte | Permite alterar a data de pagamento: (0=Não/1=sim) |
| codigo_do_calculo_que_descontou_o_arredo | `i_calculos_desconto_arredondamento_old` | integer(4) |  |  | Código do cálculo que descontou o arredondamento - Renomeado |
| gravou_as_bases_de_calculo_das_diferenca | `gravou_bases_calculo_diferenca` | smallint(2) |  | fobasesserv_simulacao_gravou_as_ba | Gravou as bases de cálculo das diferenças pagas.(0=Não/1=Sim) |
| codigo_do_complemento_de_calculo_renomea | `i_calculos_complementos_old` | integer(4) |  |  | Código do complemento de cálculo - Renomeado |
| codigo_da_funcao | `i_funcao` | integer(4) |  |  | Código da função. |
| calcular_diferenca_13o_adiantamento_0_na | `calcular_diferenca_13_adiantamento` | smallint(2) |  | fobasesserv_simulacao_calcular_dif | Calcular diferença 13º adiantamento. (0=Não/1=Sim) |
| calcula_o_13o_adiantamento_folha_mensal | `calcular_13_adiantamento_folha_mensal` | smallint(2) |  | fobasesserv_simulacao_calcula_o_13 | Calcula o 13º adiantamento folha mensal. (0=Não/1=Sim) |
| calcula_o_13o_adiantamento_conforme_avos | `calcular_13_adiantamento_conforme_avos_direito` | smallint(2) |  | fobasesserv_simulacao_calcula_o_13 | Calcula o 13º adiantamento conforme avos direito. (0=Não/1=Sim) |
| base_do_piso_salarial_utilizada_para_o_c | `base_piso_salarial` | numeric(13) |  |  | Base do piso salarial utilizada para o cálculo. |
| quantidade_de_faltas_consideradas_no_cal | `quantidade_faltas` | smallint(2) |  |  | Quantidade de faltas consideradas no cálculo. |
| soma_das_rubricas_com_tipo_informativa | `total_rubricas_informativas` | numeric(15) |  |  | Soma das rubricas com tipo informativa. |
| soma_das_rubricas_com_tipo_informativa_d | `total_rubricas_informativas_dedutoras` | numeric(13) |  |  | Soma das rubricas com tipo informativa dedutora. |
| considerou_medias_diferenciadas_para_com | `media_diferenciada_comissoes` | smallint(2) |  | fobasesserv_simulacao_considerou_m | Considerou médias diferenciadas para comissões. (0=Não/1=Sim) |
| codigo_do_periodo_gozo_da_licenca_premio | `i_periodo_gozo_licenca_premio` | integer(4) |  |  | Código do período gozo da licença prêmio. |
| simulacao_0_nao_1_sim | `simulacao` | smallint(2) |  | fobasesserv_simulacao_simulacao_0_ | Simulação (0=Não/1=Sim) |
| calcular_adiantamento_13o_com_base_no_sa | `calcular_adiantamento_13_salario_mes_anterior` | smallint(2) |  | fobasesserv_simulacao_calcular_adi | Calcular adiantamento 13º com base no salário do mês anterior. (0=Não/1=Sim) |
| gravou_o_valor_integral_das_rubricas_que | `gravou_valor_integral_rubricas` | smallint(2) |  | fobasesserv_simulacao_gravou_o_val | Gravou o valor integral das rubricas que é considerado para algumas bases de cálculo. (0=Não/1=Sim) |
| salario_considerado_no_calculo 🔒 | `salario` | numeric(13) |  |  | Salário considerado no cálculo. |
| salario_mensal_no_sindicato_considerado 🔒 | `salario_mensal_sindicato` | numeric(13) |  |  | Salário mensal no sindicato considerado no cálculo do dirigente sindical. |
| salario_por_semana_considerado_no_calcul 🔒 | `salario_semana` | numeric(13) |  |  | Salário por semana considerado no cálculo. |
| salario_por_semana_no_sindicato_consider 🔒 | `salario_semana_sindicato` | numeric(13) |  |  | Salário por semana no sindicato considerado no cálculo do dirigente sindical. |
| salario_por_dia_considerado_no_calculo 🔒 | `salario_dia` | numeric(30) |  |  | Salário por dia considerado no cálculo. |
| salario_por_dia_no_sindicato_considerado 🔒 | `salario_dia_sindicato` | numeric(30) |  |  | Salário por dia no sindicato considerado no cálculo do dirigente sindical. |
| i_calculos_pagamento_adicional_mp_927 | `i_calculos_pagamento_adicional_mp_927` | uniqueidentifier(16) |  |  | Código do cálculo do pagamento do adicional MP 927 |
| i_calculos_desconto_arredondamento | `i_calculos_desconto_arredondamento` | uniqueidentifier(16) |  |  | Código do cálculo que descontou o arredondamento |
| i_calculos_complementos | `i_calculos_complementos` | uniqueidentifier(16) |  |  | Código do complemento de cálculo |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foservicos` → `foservicos` por `codi_emp` = `codi_emp` e `i_servicos` = `i_servicos`; colunas: `foservicos_nome`
- `foccustos` → `foccustos` por `codi_emp` = `codi_emp` e `i_ccustos` = `i_ccustos`; colunas: `foccustos_nome`
- `focargos` → `focargos` por `codi_emp` = `codi_emp` e `i_cargos` = `i_cargos`; colunas: `focargos_nome`
- `fodepto` → `fodepto` por `codi_emp` = `codi_emp` e `i_depto` = `i_depto`; colunas: `fodepto_nome`
- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `fofiliais` → `fofiliais` por `codi_emp` = `codi_emp` e `i_filiais` = `i_filiais`; colunas: `fofiliais_nome`

**Filtros:** `empregado` (eq/in), `competencia` (eq/in), `tipo_de_calculo` (eq/in), `servico` (eq/in), `rateio` (eq/in), `codigo_sequencial_de_calculos` (eq/in), `data_pagamento` (entre/gte/lte), `competencia_da_alteracao_salarial_cct` (entre/gte/lte), `departamento` (eq/in), `centro_de_custos` (eq/in), `cargo` (eq/in), `situacao_mes` (eq/in), `filial` (eq/in), `codigo_sequencial_de_calculos_renomeado` (eq/in), `i_calculos_pagamento_adicional_mp_927` (eq/in), `i_calculos_desconto_arredondamento` (eq/in), `i_calculos_complementos` (eq/in)

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

### fobasesserv_calculos_rateio_servico_existe_regi

Confirmado: sim

> Todos os valores observados em FOBASESSERV_CALCULOS_RATEIO_SERVICO.EXISTE_CALCULO_RATEIO estão no comentário do banco (2026-10-18). Distribuição: 0=620.310, 1=8.688.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_permite_alte

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.PERMITE_ALTERAR_DATA_PAGAMENTO estão no comentário do banco (2026-10-18). Distribuição: 1=6.039.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | sim |

### fobasesserv_simulacao_gravou_as_ba

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.GRAVOU_BASES_CALCULO_DIFERENCA estão no comentário do banco (2026-10-18). Distribuição: 1=5.188, 0=851.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_calcular_dif

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.CALCULAR_DIFERENCA_13_ADIANTAMENTO estão no comentário do banco (2026-10-18). Distribuição: 0=6.039.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_calcula_o_13

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.CALCULAR_13_ADIANTAMENTO_CONFORME_AVOS_DIREITO estão no comentário do banco (2026-10-18). Distribuição: 0=6.039.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_considerou_m

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.MEDIA_DIFERENCIADA_COMISSOES estão no comentário do banco (2026-10-18). Distribuição: 0=5.642, 1=397.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_simulacao_0_

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.SIMULACAO estão no comentário do banco (2026-10-18). Distribuição: 1=5.188, 0=851.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_calcular_adi

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.CALCULAR_ADIANTAMENTO_13_SALARIO_MES_ANTERIOR estão no comentário do banco (2026-10-18). Distribuição: 0=6.039.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fobasesserv_simulacao_gravou_o_val

Confirmado: sim

> Todos os valores observados em FOBASESSERV_SIMULACAO.GRAVOU_VALOR_INTEGRAL_RUBRICAS estão no comentário do banco (2026-10-18). Distribuição: 1=6.039.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

