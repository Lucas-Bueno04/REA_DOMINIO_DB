# Modelo — Pessoal - ferias (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_ferias.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

15 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foferias_gozo_tipo](#foferias_gozo_tipo) | `FOFERIAS_GOZO_TIPO` | 61.403 | medio | empresa |
| [foferias_programacao](#foferias_programacao) | `FOFERIAS_PROGRAMACAO` | 17.449 | medio | empresa |
| [foferias_gozo_tipo_simulacao](#foferias_gozo_tipo_simulacao) | `FOFERIAS_GOZO_TIPO_SIMULACAO` | 12.062 | medio | empresa |
| [foferias_gozo_medias](#foferias_gozo_medias) | `FOFERIAS_GOZO_MEDIAS` | 8.578 | pequeno | empresa |
| [foferias_gozo_afastamentos](#foferias_gozo_afastamentos) | `FOFERIAS_GOZO_AFASTAMENTOS` | 7.381 | pequeno | empresa |
| [foferias_gozo_simulacao](#foferias_gozo_simulacao) | `FOFERIAS_GOZO_SIMULACAO` | 3.643 | pequeno | empresa |
| [foferias_gozo_medias_simulacao](#foferias_gozo_medias_simulacao) | `FOFERIAS_GOZO_MEDIAS_SIMULACAO` | 2.122 | pequeno | empresa |
| [foferias_gozo_vantagens](#foferias_gozo_vantagens) | `FOFERIAS_GOZO_VANTAGENS` | 1.939 | pequeno | empresa |
| [foferias_gozo_diasdesconsiderar](#foferias_gozo_diasdesconsiderar) | `FOFERIAS_GOZO_DIASDESCONSIDERAR` | 1.732 | pequeno | empresa |
| [foferias_lancamentos](#foferias_lancamentos) | `FOFERIAS_LANCAMENTOS` | 1.134 | pequeno | empresa |
| [foferias_coletivas](#foferias_coletivas) | `FOFERIAS_COLETIVAS` | 345 | pequeno | empresa |
| [foferias_gozo_vantagens_simulacao](#foferias_gozo_vantagens_simulacao) | `FOFERIAS_GOZO_VANTAGENS_SIMULACAO` | 243 | pequeno | empresa |
| [foferias_gozo_diasdesconsiderar_simulacao](#foferias_gozo_diasdesconsiderar_simulacao) | `FOFERIAS_GOZO_DIASDESCONSIDERAR_SIMULACAO` | 36 | pequeno | empresa |
| [foferias_lancamentos_pensao_alimenticia](#foferias_lancamentos_pensao_alimenticia) | `FOFERIAS_LANCAMENTOS_PENSAO_ALIMENTICIA` | 20 | pequeno | empresa |
| [foferias_lancamentos_planosaude](#foferias_lancamentos_planosaude) | `FOFERIAS_LANCAMENTOS_PLANOSAUDE` | 2 | pequeno | empresa |

## foferias_gozo_tipo

**GOZO DAS FERIAS SEPARADOS POR TIPO** — tabela `FOFERIAS_GOZO_TIPO` (61.403 linhas)

GOZO DAS FERIAS SEPARADOS POR TIPO. 61.403 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_FERIAS_GOZO_TIPO, COMPETENCIA, INICIO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_FERIAS_GOZO_TIPO, COMPETENCIA, INICIO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 61.413 linhas, 410 empresa(s), COMPETENCIA de 1994-12-01 a 2026-12-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| tipo_de_gozo_gozo_abono_lic_remum | `i_ferias_gozo_tipo` | integer(4) |  |  | TIPO DE GOZO (GOZO,ABONO,LIC.REMUM) |
| competencia | `competencia` | date(4) |  |  | COMPETENCIA |
| data_numerica_inicial | `inicio` | numeric(10) |  |  | Data numérica inicial |
| data_numerica_final | `fim` | numeric(10) |  |  | Data numérica final |
| numero_de_dias | `numero_dias` | numeric(10) |  |  | NUMERO DE DIAS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `tipo_de_gozo_gozo_abono_lic_remum` (eq/in), `competencia` (eq/in), `data_numerica_inicial` (eq/in)

## foferias_programacao

**PROGRAMAÇÃO E AVISO DE FERIAS** — tabela `FOFERIAS_PROGRAMACAO` (17.449 linhas)

PROGRAMAÇÃO E AVISO DE FERIAS. 17.449 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_PROGRAMACAO, TIPO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_PROGRAMACAO, TIPO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_AVISO`
- **Ordem padrão:** `DATA_AVISO desc`, `I_EMPREGADOS asc`, `I_FERIAS_PROGRAMACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 17.455 linhas, 320 empresa(s), DATA_AVISO de 1900-01-01 a 2026-10-30.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| codigo_da_programacao_de_ferias | `i_ferias_programacao` | integer(4) |  |  | Código da programação de férias |
| c_1_programacao_2_aviso | `tipo` | integer(4) |  |  | 1=PROGRAMACAO, 2=AVISO |
| sequencia_de_periodos_aquisitivos | `i_ferias_aquisitivos` | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| data_de_inicio_do_gozo_de_ferias | `gozo_inicio` | date(4) |  |  | Data de início do gozo de férias |
| data_numerica_para_a_quantidade_de_dias | `dias_gozo` | numeric(10) |  |  | Data numérica para a quantidade de dias de gozo de férias |
| dias_abono | `dias_abono` | numeric(10) |  |  | Data numérica para a quantidade de dias de abono |
| data_do_aviso_de_ferias | `data_aviso` | date(4) |  |  | Data do aviso de férias |
| data_do_pagamento_das_ferias | `data_pagto` | date(4) |  |  | Data do pagamento das férias |
| indica_se_o_abono_foi_pago | `paga_abono` | char(1) |  |  | Indica se o abono foi pago |
| indica_se_a_antecipacao_do_13o_salario_f | `paga_ad13` | char(1) |  |  | Indica se a antecipação do 13º salário foi paga |
| dias_direito | `dias_direito` | numeric(10) |  |  | Data numérica para a quantidade de dias de direito às férias |
| dias_gozados | `dias_gozados` | numeric(10) |  |  | Data numérica para a quantidade de dias de férias já gozados |
| data_limite_para_inicio_do_gozo_de_feria | `limite_inicio_gozo` | date(4) |  |  | Data limite para início do gozo de férias |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| inicio_do_abono | `abono_inicio` | date(4) |  |  | Início do abono |
| final_do_abono | `abono_fim` | date(4) |  |  | Final do abono |
| data_da_solicitacao_do_abono_pecuniario | `data_solicitacao_abono` | date(4) |  |  | Data da solicitação do abono pecuniário. |
| indica_se_as_ferias_foram_pagas | `paga_ferias` | char(1) |  |  | Indica se as férias foram pagas |

**Filtros:** `codigo` (eq/in), `codigo_da_programacao_de_ferias` (eq/in), `c_1_programacao_2_aviso` (eq/in), `data_de_inicio_do_gozo_de_ferias` (entre/gte/lte), `data_do_aviso_de_ferias` (entre/gte/lte), `data_do_pagamento_das_ferias` (entre/gte/lte), `data_limite_para_inicio_do_gozo_de_feria` (entre/gte/lte), `inicio_do_abono` (entre/gte/lte), `final_do_abono` (entre/gte/lte), `data_da_solicitacao_do_abono_pecuniario` (entre/gte/lte), `sequencia_de_periodos_aquisitivos` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `indica_se_o_abono_foi_pago` (eq/in), `indica_se_a_antecipacao_do_13o_salario_f` (eq/in)

## foferias_gozo_tipo_simulacao

**Simulação do tipo de gozo de férias** — tabela `FOFERIAS_GOZO_TIPO_SIMULACAO` (12.062 linhas)

Simulação do tipo de gozo de férias. 12.062 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_FERIAS_GOZO_TIPO, COMPETENCIA, INICIO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_FERIAS_GOZO_TIPO, COMPETENCIA, INICIO`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 12.062 linhas, 192 empresa(s), COMPETENCIA de 2018-06-01 a 2027-02-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| tipo_de_gozo_gozo_abono_lic_remum | `i_ferias_gozo_tipo` | integer(4) |  |  | TIPO DE GOZO (GOZO,ABONO,LIC.REMUM) |
| competencia | `competencia` | date(4) |  |  | COMPETENCIA |
| data_numerica_inicial | `inicio` | numeric(10) |  |  | Data numérica inicial |
| data_numerica_final | `fim` | numeric(10) |  |  | Data numérica final |
| numero_de_dias | `numero_dias` | numeric(10) |  |  | NUMERO DE DIAS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `tipo_de_gozo_gozo_abono_lic_remum` (eq/in), `competencia` (eq/in), `data_numerica_inicial` (eq/in)

## foferias_gozo_medias

**MEDIAS DE FERIAS CALCULADAS NO GOZO** — tabela `FOFERIAS_GOZO_MEDIAS` (8.578 linhas)

MEDIAS DE FERIAS CALCULADAS NO GOZO. 8.578 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, TIPO_INF, TIPO_CALCULO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, TIPO_INF, TIPO_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8.580 linhas, 193 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| horas_valor_vantagem_ou_hora_aula | `tipo_inf` | smallint(2) |  |  | HORAS, VALOR, VANTAGEM OU HORA-AULA |
| ferias_vencidas_ou_13o_salario | `tipo_calculo` | smallint(2) |  |  | FERIAS VENCIDAS OU 13O. SALARIO |
| valor_da_media | `valor` | decimal(17) |  |  | VALOR DA MEDIA |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `horas_valor_vantagem_ou_hora_aula` (eq/in), `ferias_vencidas_ou_13o_salario` (eq/in)

## foferias_gozo_afastamentos

**Tabela de relacionamento entre o cálculo de férias e o afastamento de férias.** — tabela `FOFERIAS_GOZO_AFASTAMENTOS` (7.381 linhas)

Tabela de relacionamento entre o cálculo de férias e o afastamento de férias.. 7.381 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7.384 linhas, 319 empresa(s).
- Vínculo foafastamentos (FOAFASTAMENTOS): 0 de 8 linhas sem registro relacionado (empresa 9021).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| sequencial_do_calculo_de_ferias | `i_ferias_gozo` | integer(4) |  |  | Sequencial do cálculo de férias. |
| sequencial | `sequencial` | smallint(2) |  |  | Sequencial. |
| data_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data do afastamento. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foafastamentos` → `FOAFASTAMENTOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `data_real_dn` = `data_real_dn`; colunas: `foafastamentos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `sequencial_do_calculo_de_ferias` (eq/in), `sequencial` (eq/in)

## foferias_gozo_simulacao

**Simulação do gozo de férias** — tabela `FOFERIAS_GOZO_SIMULACAO` (3.643 linhas)

Simulação do gozo de férias. 3.643 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_PAGTO`
- **Ordem padrão:** `DATA_PAGTO desc`, `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.643 linhas, 192 empresa(s), DATA_PAGTO de 2018-07-06 a 9022-01-09.
- Colunas expostas nulas em 100% das linhas (2): sequencia_de_pagamento, sequencial_de_ferias_coletivas.
- tipo_de_calculo_das_ferias_1_individual: todos os valores reais estão no comentário do banco (7=3.643).
- descontar_faltas_noturnas_s_sim_n_nao: todos os valores reais estão no comentário do banco (N=3.643).
- descontar_faltas_por_suspensao_s_sim_n_n: todos os valores reais estão no comentário do banco (N=3.643).
- descontar_faltas_parciais_s_sim_n_nao: todos os valores reais estão no comentário do banco (N=3.637, S=6).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=3.643).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=3.643).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=3.643).
- parcelar_o_valor_do_1_3_das_ferias_0_nao: todos os valores reais estão no comentário do banco (0=3.643).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| sequencia_de_periodos_aquisitivos | `i_ferias_aquisitivos` | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| inicio_do_gozo | `gozo_inicio` | date(4) |  |  | INICIO DO GOZO |
| fim_do_gozo | `gozo_fim` | date(4) |  |  | FIM DO GOZO |
| paga_abono_s_n | `abono_paga` | char(1) |  |  | PAGA ABONO (S/N) |
| inicio_abono | `abono_inicio` | date(4) |  |  | INICIO ABONO |
| fim_abono | `abono_fim` | date(4) |  |  | FIM ABONO |
| data_do_pagamento | `data_pagto` | date(4) |  |  | DATA DO PAGAMENTO |
| paga_13o_s_n | `paga_ad13` | char(1) |  |  | PAGA 13O (S/N) |
| medias_informadas_manualmente_s_n | `medias_manual` | char(1) |  |  | MEDIAS INFORMADAS MANUALMENTE (S/N) |
| numero_de_dias_de_faltas_no_momento_do_c | `dias_faltas` | integer(4) |  |  | NUMERO DE DIAS DE FALTAS NO MOMENTO DO CALCULO DE FERIAS |
| valor_de_ferias_baixado_da_provisao_pelo | `baixa_prov_ferias` | numeric(13) |  |  | VALOR DE FERIAS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| valor_de_adicional_de_ferias_1_3_baixado | `baixa_prov_adicferias` | numeric(13) |  |  | VALOR DE ADICIONAL DE FERIAS (1/3) BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| valor_de_inss_baixado_da_provisao_pelo_c | `baixa_prov_inss` | numeric(13) |  |  | VALOR DE INSS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| valor_de_fgts_baixado_da_provisao_pelo_c | `baixa_prov_fgts` | numeric(13) |  |  | VALOR DE FGTS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| valor_de_pis_baixado_da_provisao_pelo_ca | `baixa_prov_pis` | numeric(13) |  |  | VALOR DE PIS BAIXADO DA PROVISÃO PELO CALCULO DE FERIAS |
| sequencia_de_pagamento | `i_pagto` | integer(4) |  |  | SEQUENCIA DE PAGAMENTO |
| descontar_faltas | `descontar_faltas` | char(1) |  |  | DESCONTAR FALTAS |
| sequencial_de_ferias_coletivas | `i_ferias_coletivas` | integer(4) |  |  | SEQUENCIAL DE FERIAS COLETIVAS |
| indica_se_o_empregado_foi_transferido | `transferido` | smallint(2) |  |  | INDICA SE O EMPREGADO FOI TRANSFERIDO |
| tipo_de_calculo_das_ferias_1_individual | `tipo` | smallint(2) |  | foferias_gozo_simulacao_tipo_de_calculo_das_fe | Tipo de cálculo das férias. (1=Individual/2=Coletiva/3=Rescisão/4=Manual/5=Provisão/6=Acerto/7=Simulação férias/8=Simulação rescisão) |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| inicio_do_gozo_numerico | `gozo_inicio_dn` | numeric(10) |  |  | INICIO DO GOZO NUMERICO |
| fim_do_gozo_numerico | `gozo_fim_dn` | numeric(10) |  |  | FIM DO GOZO NUMERICO |
| inicio_abono_numerico | `abono_inicio_dn` | numeric(10) |  |  | INICIO ABONO NUMERICO |
| fim_abono_numerico | `abono_fim_dn` | numeric(10) |  |  | FIM ABONO NUMERICO |
| data_inicial_do_periodo_aquisitivo | `inicio_aquisitivo` | date(4) |  |  | Data inicial do período aquisitivo |
| data_final_do_periodo_aquisitivo | `fim_aquisitivo` | date(4) |  |  | Data final do período aquisitivo |
| descontar_faltas_noturnas_s_sim_n_nao | `descontar_faltas_noturnas` | char(1) |  | foferias_gozo_simulacao_descontar_faltas_notur | Descontar faltas noturnas. (S=Sim/N=Não) |
| descontar_faltas_por_suspensao_s_sim_n_n | `descontar_faltas_suspensao` | char(1) |  | foferias_gozo_simulacao_descontar_faltas_por_s | Descontar faltas por suspensão (S=Sim/N=Não) |
| descontar_faltas_parciais_s_sim_n_nao | `descontar_faltas_parciais` | char(1) |  | foferias_gozo_simulacao_descontar_faltas_parci | Descontar faltas parciais. (S=Sim/N=Não) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | foferias_gozo_simulacao_enviar_para_o_esocial_ | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | foferias_gozo_simulacao_gerar_retificacao_para | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | foferias_gozo_simulacao_marcacao_do_evento_par | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| nao_calcular_adicional_mp_927 | `nao_calcular_adicional_mp_927` | char(1) |  |  | Não calcular 1/3 férias MP 927 |
| iniciou_novo_periodo_aquisitivo_por_feri | `iniciou_novo_periodo_aquisitivo_ferias_coletivas_ano_admissao` | smallint(2) |  |  | Iniciou novo período aquisitivo por férias coletivas no ano da admissão |
| parcelar_o_valor_do_1_3_das_ferias_0_nao | `parcelar_um_terco_ferias` | smallint(2) |  | foferias_gozo_simulacao_parcelar_o_valor_do_1_ | Parcelar o valor do 1/3 das férias (0=Não/1=Sim) |
| indica_se_as_ferias_foram_pagas | `paga_ferias` | char(1) |  |  | Indica se as férias foram pagas |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `inicio_do_gozo` (entre/gte/lte), `fim_do_gozo` (entre/gte/lte), `inicio_abono` (entre/gte/lte), `fim_abono` (entre/gte/lte), `data_do_pagamento` (entre/gte/lte), `data_inicial_do_periodo_aquisitivo` (entre/gte/lte), `data_final_do_periodo_aquisitivo` (entre/gte/lte), `sequencia_de_periodos_aquisitivos` (eq/in), `paga_abono_s_n` (eq/in), `paga_13o_s_n` (eq/in), `medias_informadas_manualmente_s_n` (eq/in), `sequencia_de_pagamento` (eq/in)

## foferias_gozo_medias_simulacao

**Simulação das médias do gozo de férias** — tabela `FOFERIAS_GOZO_MEDIAS_SIMULACAO` (2.122 linhas)

Simulação das médias do gozo de férias. 2.122 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, TIPO_INF, TIPO_CALCULO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, TIPO_INF, TIPO_CALCULO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.122 linhas, 68 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| horas_valor_vantagem_ou_hora_aula | `tipo_inf` | smallint(2) |  |  | HORAS, VALOR, VANTAGEM OU HORA-AULA |
| ferias_vencidas_ou_13o_salario | `tipo_calculo` | smallint(2) |  |  | FERIAS VENCIDAS OU 13O. SALARIO |
| valor_da_media | `valor` | numeric(13) |  |  | VALOR DA MEDIA |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `horas_valor_vantagem_ou_hora_aula` (eq/in), `ferias_vencidas_ou_13o_salario` (eq/in)

## foferias_gozo_vantagens

**VANTAGENS CALCULADAS NAS FERIAS** — tabela `FOFERIAS_GOZO_VANTAGENS` (1.939 linhas)

VANTAGENS CALCULADAS NAS FERIAS. 1.939 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.939 linhas, 79 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | CODIGO DO EVENTO |
| valor_informado | `valor_inf` | numeric(13) |  |  | VALOR INFORMADO |
| valor_calculado | `valor_calc` | numeric(13) |  |  | VALOR CALCULADO |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `codigo_do_evento` (eq/in)

## foferias_gozo_diasdesconsiderar

**DIAS A DESCONSIDERAR NO PERÍODO DO GOZO** — tabela `FOFERIAS_GOZO_DIASDESCONSIDERAR` (1.732 linhas)

DIAS A DESCONSIDERAR NO PERÍODO DO GOZO. 1.732 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, DIA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, DIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DIA`
- **Ordem padrão:** `DIA desc`, `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.732 linhas, 46 empresa(s), DIA de 2012-12-25 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| dia_a_ser_desconsiderado | `dia` | date(4) |  |  | DIA A SER DESCONSIDERADO |
| origem_do_dia_1_sindicato_2_domingo_feri | `origem` | tinyint(1) |  |  | ORIGEM DO DIA (1=SINDICATO, 2=DOMINGO/FERIADO) |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `dia_a_ser_desconsiderado` (eq/in)

## foferias_lancamentos

**TABELA DE LANÇAMENTOS DE FÉRIAS** — tabela `FOFERIAS_LANCAMENTOS` (1.134 linhas)

TABELA DE LANÇAMENTOS DE FÉRIAS. 1.134 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.134 linhas, 144 empresa(s).
- frm_de_rateio_da_pensao_alimenticia_0_na: todos os valores reais estão no comentário do banco (0=1.120, 1=10, 2=4).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | CÓDIGO DA EMPRESA |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | CÓDIGO DO EMPREGADO |
| codigo_do_gozo | `i_ferias_gozo` | integer(4) |  |  | CÓDIGO DO GOZO |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | CÓDIGO DO EVENTO |
| valor_informado | `valor_informado` | numeric(13) |  |  | VALOR INFORMADO |
| valor_calculado | `valor_calculado` | numeric(13) |  |  | VALOR CALCULADO |
| origem | `origem` | tinyint(1) |  |  | ORIGEM |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| forma_do_rateio_0_nao_ratear_1_quantidad | `plano_saude_rateio` | smallint(2) |  |  | Forma do rateio: 0=Não ratear/1=Quantidade de beneficiários/2=Percentual definido/3=Todo para o empregado |
| frm_de_rateio_da_pensao_alimenticia_0_na | `forma_rateio_pensao_alimenticia` | smallint(2) |  | foferias_lancamentos_frm_de_rateio_da_p | Frm de rateio da pensão alimentícia. (0=Não rateado/1=Rateio pela qtd de ben/2=Rat do valor da rubrica por percentual definido) |

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_gozo` (eq/in), `codigo_do_evento` (eq/in)

## foferias_coletivas

**CALCULOS DE FERIAS COLETIVAS** — tabela `FOFERIAS_COLETIVAS` (345 linhas)

CALCULOS DE FERIAS COLETIVAS. 345 linhas no catálogo; chave: CODI_EMP, I_FERIAS_COLETIVAS.

- **Chave:** `CODI_EMP, I_FERIAS_COLETIVAS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_PAGTO`
- **Ordem padrão:** `DATA_PAGTO desc`, `I_FERIAS_COLETIVAS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 345 linhas, 57 empresa(s), DATA_PAGTO de 2007-12-31 a 2026-01-02.
- descontar_faltas_noturnas_s_sim_n_nao: todos os valores reais estão no comentário do banco (N=345).
- descontar_faltas_por_suspensao_s_sim_n_n: todos os valores reais estão no comentário do banco (N=345).
- descontar_faltas_parciais_s_sim_n_nao: todos os valores reais estão no comentário do banco (N=345).
- parcelar_o_valor_do_1_3_das_ferias_0_nao: todos os valores reais estão no comentário do banco (0=345).
- Vínculo geempre (geempre): 0 de 3 linhas sem registro relacionado (empresa 583).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codi_emp` | integer(4) |  |  | CODIGO |
| sequencial_de_ferias_coletivas | `i_ferias_coletivas` | integer(4) |  |  | SEQUENCIAL DE FERIAS COLETIVAS |
| inicio_do_gozo | `gozo_inicio` | date(4) |  |  | INICIO DO GOZO |
| fim_do_gozo | `gozo_fim` | date(4) |  |  | FIM DO GOZO |
| paga_abono | `abono_paga` | char(1) |  |  | PAGA ABONO |
| inicio_do_abono | `abono_inicio` | date(4) |  |  | INICIO DO ABONO |
| fim_do_abono | `abono_fim` | date(4) |  |  | FIM DO ABONO |
| data_do_pagamento | `data_pagto` | date(4) |  |  | DATA DO PAGAMENTO |
| pagar_adiantamento_de_decimo_terceiro | `paga_ad13` | char(1) |  |  | PAGAR ADIANTAMENTO DE DECIMO TERCEIRO |
| descontar_faltas | `descontar_faltas` | char(1) |  |  | DESCONTAR FALTAS |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| descontar_faltas_noturnas_s_sim_n_nao | `descontar_faltas_noturnas` | char(1) |  | foferias_coletivas_descontar_faltas_notu | Descontar faltas noturnas. (S=Sim/N=Não) |
| descontar_faltas_por_suspensao_s_sim_n_n | `descontar_faltas_suspensao` | char(1) |  | foferias_coletivas_descontar_faltas_por_ | Descontar faltas por suspensão (S=Sim/N=Não) |
| descontar_faltas_parciais_s_sim_n_nao | `descontar_faltas_parciais` | char(1) |  | foferias_coletivas_descontar_faltas_parc | Descontar faltas parciais. (S=Sim/N=Não) |
| nao_calcular_adicional_mp_927 | `nao_calcular_adicional_mp_927` | char(1) |  |  | Não calcular 1/3 férias MP 927 |
| parcelar_o_valor_do_1_3_das_ferias_0_nao | `parcelar_um_terco_ferias` | smallint(2) |  | foferias_coletivas_parcelar_o_valor_do_1 | Parcelar o valor do 1/3 das férias (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_de_ferias_coletivas` (eq/in), `inicio_do_gozo` (entre/gte/lte), `fim_do_gozo` (entre/gte/lte), `inicio_do_abono` (entre/gte/lte), `fim_do_abono` (entre/gte/lte), `data_do_pagamento` (entre/gte/lte), `paga_abono` (eq/in), `pagar_adiantamento_de_decimo_terceiro` (eq/in), `descontar_faltas` (eq/in), `descontar_faltas_noturnas_s_sim_n_nao` (eq/in), `descontar_faltas_por_suspensao_s_sim_n_n` (eq/in), `descontar_faltas_parciais_s_sim_n_nao` (eq/in), `nao_calcular_adicional_mp_927` (eq/in)

## foferias_gozo_vantagens_simulacao

**Simulação das vantagens do gozo de férias** — tabela `FOFERIAS_GOZO_VANTAGENS_SIMULACAO` (243 linhas)

Simulação das vantagens do gozo de férias. 243 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 243 linhas, 27 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | CODIGO DO EVENTO |
| valor_informado | `valor_inf` | numeric(13) |  |  | VALOR INFORMADO |
| valor_calculado | `valor_calc` | numeric(13) |  |  | VALOR CALCULADO |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `codigo_do_evento` (eq/in)

## foferias_gozo_diasdesconsiderar_simulacao

**Simulação dos dias a desconsiderar no gozo de férias** — tabela `FOFERIAS_GOZO_DIASDESCONSIDERAR_SIMULACAO` (36 linhas)

Simulação dos dias a desconsiderar no gozo de férias. 36 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, DIA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, DIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DIA`
- **Ordem padrão:** `DIA desc`, `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 36 linhas, 4 empresa(s), DIA de 2018-12-25 a 2025-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencial_de_periodos_de_gozo | `i_ferias_gozo` | integer(4) |  |  | SEQUENCIAL DE PERIODOS DE GOZO |
| dia_a_ser_desconsiderado | `dia` | date(4) |  |  | DIA A SER DESCONSIDERADO |
| origem_do_dia_1_sindicato_2_domingo_feri | `origem` | tinyint(1) |  |  | ORIGEM DO DIA (1=SINDICATO, 2=DOMINGO/FERIADO) |

**Filtros:** `codigo` (eq/in), `sequencial_de_periodos_de_gozo` (eq/in), `dia_a_ser_desconsiderado` (eq/in)

## foferias_lancamentos_pensao_alimenticia

**Valores de pensão alimentícia nas férias por dependente.** — tabela `FOFERIAS_LANCAMENTOS_PENSAO_ALIMENTICIA` (20 linhas)

Valores de pensão alimentícia nas férias por dependente.. 20 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS, I_FILHOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS, I_FILHOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20 linhas, 11 empresa(s).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=20).
- Vínculo fofilhos (fofilhos): 0 de 2 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| codigo_do_periodo_de_gozo | `i_ferias_gozo` | integer(4) |  |  | Código do período de gozo. |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento. |
| codigo_do_dependente | `i_filhos` | integer(4) |  |  | Código do dependente. |
| valor | `valor` | numeric(13) |  |  | Valor. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | foferias_lancamentos_pensao_alimenticia_origem_do_r | Origem do registro. (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_periodo_de_gozo` (eq/in), `codigo_do_evento` (eq/in), `codigo_do_dependente` (eq/in)

## foferias_lancamentos_planosaude

**Lançamentos de férias - Processos - Plano de saúde** — tabela `FOFERIAS_LANCAMENTOS_PLANOSAUDE` (2 linhas)

Lançamentos de férias - Processos - Plano de saúde. 2 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS, I_BENEFICIARIO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_GOZO, I_EVENTOS, I_BENEFICIARIO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `I_FERIAS_GOZO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s).
- Colunas expostas nulas em 100% das linhas (1): coigo_do_dependente.
- Vínculo fooperadoraplanosaude (FOOPERADORAPLANOSAUDE): 0 de 1 linhas sem registro relacionado (empresa 978).
- Vínculo fofilhos (fofilhos): 1 de 1 linhas sem registro relacionado (empresa 978).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| codigo_do_gozo | `i_ferias_gozo` | integer(4) |  |  | Código do gozo |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| sequencial_de_beneficiario | `i_beneficiario` | integer(4) |  |  | Sequencial de beneficiário |
| coigo_do_dependente | `i_filhos` | integer(4) |  |  | Cóigo do dependente |
| valor | `valor` | numeric(13) |  |  | Valor |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigo_da_operadora_de_plano_de_saude | `i_operadoraplanosaude` | integer(4) |  |  | Código da operadora de plano de saúde |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fooperadoraplanosaude` → `FOOPERADORAPLANOSAUDE` por `i_operadoraplanosaude` = `i_operadoraplanosaude`; colunas: `fooperadoraplanosaude_nome`
- `fofilhos` → `fofilhos` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `i_filhos` = `i_filhos`; colunas: `fofilhos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_gozo` (eq/in), `codigo_do_evento` (eq/in), `sequencial_de_beneficiario` (eq/in), `coigo_do_dependente` (eq/in), `codigo_da_operadora_de_plano_de_saude` (eq/in)

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

### foferias_gozo_simulacao_tipo_de_calculo_das_fe

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.TIPO estão no comentário do banco (2026-10-18). Distribuição: 7=3.643.

| Código | Significado |
|---|---|
| 1 | Individual |
| 2 | Coletiva |
| 3 | Rescisão |
| 4 | Manual |
| 5 | Provisão |
| 6 | Acerto |
| 7 | Simulação férias |
| 8 | Simulação rescisão |

### foferias_gozo_simulacao_descontar_faltas_notur

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.DESCONTAR_FALTAS_NOTURNAS estão no comentário do banco (2026-10-18). Distribuição: N=3.643.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_gozo_simulacao_descontar_faltas_por_s

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.DESCONTAR_FALTAS_SUSPENSAO estão no comentário do banco (2026-10-18). Distribuição: N=3.643.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_gozo_simulacao_descontar_faltas_parci

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.DESCONTAR_FALTAS_PARCIAIS estão no comentário do banco (2026-10-18). Distribuição: N=3.637, S=6.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_gozo_simulacao_enviar_para_o_esocial_

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=3.643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foferias_gozo_simulacao_gerar_retificacao_para

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=3.643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foferias_gozo_simulacao_marcacao_do_evento_par

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=3.643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foferias_gozo_simulacao_parcelar_o_valor_do_1_

Confirmado: sim

> Todos os valores observados em FOFERIAS_GOZO_SIMULACAO.PARCELAR_UM_TERCO_FERIAS estão no comentário do banco (2026-10-18). Distribuição: 0=3.643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foferias_lancamentos_frm_de_rateio_da_p

Confirmado: sim

> Todos os valores observados em FOFERIAS_LANCAMENTOS.FORMA_RATEIO_PENSAO_ALIMENTICIA estão no comentário do banco (2026-10-18). Distribuição: 0=1.120, 1=10, 2=4.

| Código | Significado |
|---|---|
| 0 | Não rateado |
| 1 | Rateio pela qtd de ben |
| 2 | Rat do valor da rubrica por percentual definido |

### foferias_coletivas_descontar_faltas_notu

Confirmado: sim

> Todos os valores observados em FOFERIAS_COLETIVAS.DESCONTAR_FALTAS_NOTURNAS estão no comentário do banco (2026-10-18). Distribuição: N=345.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_coletivas_descontar_faltas_por_

Confirmado: sim

> Todos os valores observados em FOFERIAS_COLETIVAS.DESCONTAR_FALTAS_SUSPENSAO estão no comentário do banco (2026-10-18). Distribuição: N=345.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_coletivas_descontar_faltas_parc

Confirmado: sim

> Todos os valores observados em FOFERIAS_COLETIVAS.DESCONTAR_FALTAS_PARCIAIS estão no comentário do banco (2026-10-18). Distribuição: N=345.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### foferias_coletivas_parcelar_o_valor_do_1

Confirmado: sim

> Todos os valores observados em FOFERIAS_COLETIVAS.PARCELAR_UM_TERCO_FERIAS estão no comentário do banco (2026-10-18). Distribuição: 0=345.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foferias_lancamentos_pensao_alimenticia_origem_do_r

Confirmado: sim

> Todos os valores observados em FOFERIAS_LANCAMENTOS_PENSAO_ALIMENTICIA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=20.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

