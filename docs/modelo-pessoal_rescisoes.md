# Modelo — Pessoal - rescisoes (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_rescisoes.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

8 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [forescisoes_termo_configuracao_campos](#forescisoes_termo_configuracao_campos) | `FORESCISOES_TERMO_CONFIGURACAO_CAMPOS` | 11.351 | medio | empresa |
| [forescisoes_termo](#forescisoes_termo) | `FORESCISOES_TERMO` | 5.750 | pequeno | empresa |
| [forescisoes_envios_esocial](#forescisoes_envios_esocial) | `FORESCISOES_ENVIOS_ESOCIAL` | 5.230 | pequeno | empresa |
| [forescisoes_simulacao](#forescisoes_simulacao) | `FORESCISOES_SIMULACAO` | 1.902 | pequeno | empresa |
| [forescisoes_termo_simulacao](#forescisoes_termo_simulacao) | `FORESCISOES_TERMO_SIMULACAO` | 1.902 | pequeno | empresa |
| [forescisoes_termo_ferias_vencidas](#forescisoes_termo_ferias_vencidas) | `FORESCISOES_TERMO_FERIAS_VENCIDAS` | 1.888 | pequeno | empresa |
| [forescisoes_termo_ferias_vencidas_simulacao](#forescisoes_termo_ferias_vencidas_simulacao) | `FORESCISOES_TERMO_FERIAS_VENCIDAS_SIMULACAO` | 1.020 | pequeno | empresa |
| [forescisoes_termo_configuracao](#forescisoes_termo_configuracao) | `FORESCISOES_TERMO_CONFIGURACAO` | 378 | pequeno | empresa |

## forescisoes_termo_configuracao_campos

**Recibo de Rescisão - Configuração de Campos sem Valor** — tabela `FORESCISOES_TERMO_CONFIGURACAO_CAMPOS` (11.351 linhas)

Recibo de Rescisão - Configuração de Campos sem Valor. 11.351 linhas no catálogo; chave: CODI_EMP, CAMPO, MODELO.

- **Chave:** `CODI_EMP, CAMPO, MODELO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CAMPO asc`, `MODELO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.351 linhas, 367 empresa(s).
- modelo_1_trct_portaria_mte_1621_2010_ane: todos os valores reais estão no comentário do banco (2=11.010, 1=341).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| nome_codigo_do_campo | `campo` | char(5) |  |  | Nome/código do campo |
| modelo_1_trct_portaria_mte_1621_2010_ane | `modelo` | smallint(2) |  | forescisoes_termo_configuracao_campos_modelo_1_tr | Modelo: (1=TRCT Portaria MTE 1621/2010 - Anexo I/2=TRCT Portaria MTE 1621/2010 - Alterado) |

**Filtros:** `nome_codigo_do_campo` (eq/in), `modelo_1_trct_portaria_mte_1621_2010_ane` (eq/in)

## forescisoes_termo

**Discriminação das verbas rescisórias do TRCT - (13º salário e férias)** — tabela `FORESCISOES_TERMO` (5.750 linhas)

Discriminação das verbas rescisórias do TRCT - (13º salário e férias). 5.750 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.752 linhas, 360 empresa(s).
- tipo_de_calculo_de_rescisao_1_normal_2_c: todos os valores reais estão no comentário do banco (1=5.520, 2=232).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_de_calculo_de_rescisao_1_normal_2_c 🔒 | `tipo` | integer(4) |  | forescisoes_termo_tipo_de_cal | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| quantidade_de_avos_de_13o_salario_pagos | `avos_13` | smallint(2) |  |  | Quantidade de avos de 13º salário pagos |
| quantidade_de_avos_de_ferias_pagos | `avos_ferias` | smallint(2) |  |  | Quantidade de avos de férias pagos |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_das_ferias_vencidas_valor_lancado | `valor_ferias_vencidas` | numeric(13) |  |  | Valor das férias vencidas (Valor lançado/alterado) |
| valor_das_ferias_em_dobro_valor_lancado | `valor_ferias_dobro` | numeric(13) |  |  | Valor das férias em dobro (Valor lançado/alterado) |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_de_calculo_de_rescisao_1_normal_2_c` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## forescisoes_envios_esocial

**Envios das rescisões ao eSocial** — tabela `FORESCISOES_ENVIOS_ESOCIAL` (5.230 linhas)

Envios das rescisões ao eSocial. 5.230 linhas no catálogo; chave: codi_emp, i_empregados, tipo, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS, I_CALCULOS.

- **Chave:** `codi_emp, i_empregados, tipo, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS, I_CALCULOS`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `i_empregados asc`, `tipo asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.237 linhas, 249 empresa(s).
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 6 linhas sem registro relacionado (empresa 1448).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_de_rescisao 🔒 | `tipo` | integer(4) |  |  | Tipo de rescisão |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_evento_referente_a_foesocial_d | `i_dados_eventos` | integer(4) |  |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo. |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp_dados_eventos` = `codi_emp` e `i_dados_eventos` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_de_rescisao` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_do_evento_referente_a_foesocial_d` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## forescisoes_simulacao

**Simulação da rescisão** — tabela `FORESCISOES_SIMULACAO` (1.902 linhas)

Simulação da rescisão. 1.902 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_AVISO`
- **Ordem padrão:** `DATA_AVISO desc`, `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.902 linhas, 183 empresa(s), DATA_AVISO de 2018-05-30 a 2026-12-31.
- Colunas expostas nulas em 100% das linhas (9): desconto_outro_motivo, desconto_faltas, valor_media_do_aviso, data_acordo_dissidio, inss_empresa_13_c, acid_trab_13, inss_terc_13, valor_pis_13_c, sequencial_de_pagamento.
- tipo_de_calculo_de_rescisao_1_normal_2_c: todos os valores reais estão no comentário do banco (4=1.902).
- Vínculo foempregados (foempregados): 0 de 4 linhas sem registro relacionado (empresa 886).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo empresa |
| empregado | `i_empregados` | integer(4) |  |  | Empregado |
| tipo_de_calculo_de_rescisao_1_normal_2_c 🔒 | `tipo` | integer(4) |  | forescisoes_simulacao_tipo_de_calculo_de_rescisao_ | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| data_demissao | `demissao` | date(4) |  |  | Data Demissao |
| motivo | `motivo` | integer(4) |  |  | Motivo |
| data_aviso | `data_aviso` | date(4) |  |  | Data aviso |
| aviso_indenizado | `aviso_indenizado` | char(1) |  |  | Aviso indenizado |
| avos_pago_13_c | `avos_pago_13` | smallint(2) |  |  | Avos pago 13 |
| no_ferias_vencidas | `num_fer_venc` | smallint(2) |  |  | No. ferias vencidas |
| meses_ferias_prop | `meses_fer_prop` | smallint(2) |  |  | Meses ferias prop. |
| codigo_saque_fgts | `codigo_saque_fgts` | char(2) |  |  | Codigo saque FGTS |
| saldo_fgts | `saldo_fgts` | numeric(15) |  |  | Saldo FGTS |
| fgts_mes_anterior_depositado | `fgts_mes_ant_dep` | char(1) |  |  | FGTS mes anterior depositado |
| salario 🔒 | `salario` | numeric(13) |  |  | Salario |
| provento 🔒 | `proventos` | numeric(13) |  |  | Provento |
| desconto | `descontos` | numeric(13) |  |  | Desconto |
| media_ferias_vencidas | `med_fer_ven_i` | numeric(13) |  |  | Media ferias vencidas |
| media_ferias_prop | `med_fer_pro_i` | numeric(13) |  |  | Media ferias prop. |
| med_13_i | `med_13_i` | numeric(13) |  |  | Media 13 |
| valor_fgts_anteriro | `val_fgts_ant` | numeric(13) |  |  | Valor FGTS anteriro |
| valor_fgts_rescisao 🔒 | `val_fgts_res` | numeric(13) |  |  | Valor FGTS rescisao |
| pago_medias | `pago_medias` | char(1) |  |  | Pago medias |
| pago_adicionais | `pago_adicionais` | char(1) |  |  | Pago adicionais |
| desconto_outro_motivo | `desc_outr_motivo` | char(30) |  |  | Desconto outro motivo |
| minimo_mes_rescisao 🔒 | `min_mes_res` | integer(4) |  |  | Minimo mes rescisao |
| data_pagamento | `data_pagto` | date(4) |  |  | Data pagamento |
| recolher_grfc | `recolher_grfp` | char(1) |  |  | Recolher GRFC |
| desconto_faltas | `desc_falta` | char(1) |  |  | Desconto faltas |
| base_fgts_13_c | `base_fgts_13` | numeric(13) |  |  | Base FGTS 13 |
| maior_remuneracao 🔒 | `maior_remuneracao` | numeric(13) |  |  | Maior remuneracao |
| base_irrf_ferias | `base_irrf_fer` | numeric(13) |  |  | Base IRRF ferias |
| abatimento_irrf_ferias | `abat_irrf_fer` | numeric(13) |  |  | Abatimento IRRF ferias |
| taxa_irrf_ferias | `taxa_irrf_fer` | numeric(5) |  |  | Taxa IRRF ferias |
| base_irrf_13_c | `base_irrf_13` | numeric(13) |  |  | Base IRRF 13 |
| abat_irrf_13 | `abat_irrf_13` | numeric(13) |  |  | Abatimento IRRF 13 |
| taxa_irrf_13_c | `taxa_irrf_13` | numeric(5) |  |  | Taxa IRRF 13 |
| valor_irrf_ferias | `valor_irrf_fer` | numeric(13) |  |  | Valor IRRF ferias |
| deducao_irrf_ferias | `ded_irrf_fer` | numeric(13) |  |  | Deducao IRRF ferias |
| valor_irrf_13_c | `valor_irrf_13` | numeric(13) |  |  | Valor IRRF 13 |
| ded_irrf_13 | `ded_irrf_13` | numeric(13) |  |  | Deducao IRRF 13 |
| dias_estabilidade | `dias_estab` | integer(4) |  |  | Dias estabilidade |
| media_informada | `media_informada` | tinyint(1) |  |  | Media informada |
| dias_aviso | `dias_aviso` | numeric(5) |  |  | Dias aviso |
| valor_media_do_aviso | `valor_med_aviso` | numeric(13) |  |  | Valor media do aviso |
| data_acordo_dissidio | `dissidio_acordo_data` | date(4) |  |  | Data acordo dissidio |
| inss_empresa_13_c | `inss_empresa_13` | numeric(13) |  |  | INSS empresa 13 |
| acid_trab_13 | `acid_trab_13` | numeric(13) |  |  | Acid. trabalho 13 |
| inss_terc_13 | `inss_terc_13` | numeric(13) |  |  | INSS terceiro 13 |
| valor_pis_13_c | `valor_pis_13` | numeric(13) |  |  | Valor PIS 13 |
| desc_lei_irrf_13 | `desc_lei_irrf_13` | numeric(13) |  |  | Desconto IRRF 13 |
| desconto_irrf_ferias | `desc_lei_irrf_fer` | numeric(13) |  |  | Desconto IRRF ferias |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| sequencial_de_pagamento | `i_pagto` | integer(4) |  |  | Sequencial de pagamento |
| indica_se_e_para_calcular_dsr_na_semana | `dsr_semana_resc` | tinyint(1) |  |  | Indica se é para calcular DSR na semana da rescisao |
| aviso_previo_1_trab_2_indeizado_3_ausenc | `aviso_previo` | tinyint(1) |  |  | Aviso Previo (1=trab,2=indeizado,3=ausencia/dispensa) |
| a_vaga_sera_reposta_1_sim_0_nao | `reposicao_vaga` | tinyint(1) |  |  | A vaga sera reposta (1=sim, 0=nao) |
| complemento_do_saldo_do_fgts | `complemento_saldo_fgts` | numeric(15) |  |  | Complemento do saldo do fgts |
| competencia_da_rescisao | `competencia` | date(4) |  |  | Competência da rescisão |
| tipo_de_processo_da_rescisao 🔒 | `tipo_process` | integer(4) |  |  | Tipo de processo da rescisão |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `empregado` (eq/in), `tipo_de_calculo_de_rescisao_1_normal_2_c` (eq/in), `codigo_do_calculo` (eq/in), `data_demissao` (entre/gte/lte), `data_aviso` (entre/gte/lte), `data_pagamento` (entre/gte/lte), `data_acordo_dissidio` (entre/gte/lte), `competencia_da_rescisao` (entre/gte/lte), `aviso_indenizado` (eq/in), `codigo_saque_fgts` (eq/in), `fgts_mes_anterior_depositado` (eq/in), `pago_medias` (eq/in), `pago_adicionais` (eq/in), `desconto_outro_motivo` (contem/prefixo)

## forescisoes_termo_simulacao

**Simulação do termo rescisão** — tabela `FORESCISOES_TERMO_SIMULACAO` (1.902 linhas)

Simulação do termo rescisão. 1.902 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.902 linhas, 183 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): valor_das_ferias_vencidas_valor_lancado, valor_das_ferias_em_dobro_valor_lancado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_da_rescisao 🔒 | `tipo` | integer(4) |  |  | Tipo da rescisão |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| quantidade_de_avos_de_13o_salario_pagos | `avos_13` | smallint(2) |  |  | Quantidade de avos de 13º salário pagos |
| quantidade_de_avos_de_ferias_pagos | `avos_ferias` | smallint(2) |  |  | Quantidade de avos de férias pagos |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_das_ferias_vencidas_valor_lancado | `valor_ferias_vencidas` | numeric(13) |  |  | Valor das férias vencidas (Valor lançado/alterado) |
| valor_das_ferias_em_dobro_valor_lancado | `valor_ferias_dobro` | numeric(13) |  |  | Valor das férias em dobro (Valor lançado/alterado) |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_da_rescisao` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## forescisoes_termo_ferias_vencidas

**Discriminação das verbas rescisórias do TRCT - (férias vencidas)** — tabela `FORESCISOES_TERMO_FERIAS_VENCIDAS` (1.888 linhas)

Discriminação das verbas rescisórias do TRCT - (férias vencidas). 1.888 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO, I_FERIAS_AQUISITIVOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO, I_FERIAS_AQUISITIVOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.888 linhas, 247 empresa(s).
- tipo_de_calculo_de_rescisao_1_normal_2_c: todos os valores reais estão no comentário do banco (1=1.794, 2=94).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_de_calculo_de_rescisao_1_normal_2_c 🔒 | `tipo` | integer(4) |  | forescisoes_termo_ferias_vencidas_tipo_de_cal | Tipo de cálculo de rescisão. (1=Normal/2=Complementar/3=Parcial/4=Simulação) |
| codigo_do_periodo_aquisitivo | `i_ferias_aquisitivos` | integer(4) |  |  | Código do período aquisitivo |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_em_dobro | `valor_dobro` | numeric(13) |  |  | Valor em dobro |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_das_ferias | `valor_ferias` | decimal(13) |  |  | Valor das férias. |
| valor_do_1_3_de_ferias | `valor_adicional` | decimal(13) |  |  | Valor do 1/3 de férias. |
| valor_de_medias_e_vantagens | `valor_medias_vantagens` | decimal(13) |  |  | Valor de médias e vantagens. |
| valor_do_pis | `valor_pis` | decimal(13) |  |  | Valor do Pis. |
| valor_do_1_3_de_ferias_em_dobro | `valor_adicional_dobro` | numeric(13) |  |  | Valor do 1/3 de férias em dobro |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| valor_do_adicional_de_ferias_sem_conside | `valor_adicional_sem_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias sem considerar as médias/vantagens. |
| valor_do_adicional_de_ferias_das_medias | `valor_adicional_medias_vantagens` | numeric(13) |  |  | Valor do adicional de férias das médias/vantagens. |
| valor_de_ferias_vencidas_do_dirigente_si | `valor_dirigente_sindical` | numeric(13) |  |  | Valor de férias vencidas do dirigente sindical. |
| base_de_ferias_vencidas_do_dirigente_sin | `base_dirigente_sindical` | numeric(13) |  |  | Base de férias vencidas do dirigente sindical. |
| base_de_ferias_vencidas | `base_ferias` | numeric(13) |  |  | Base de férias vencidas. |

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_de_calculo_de_rescisao_1_normal_2_c` (eq/in), `codigo_do_periodo_aquisitivo` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## forescisoes_termo_ferias_vencidas_simulacao

**Simulação do termo de férias vencidas da rescisão** — tabela `FORESCISOES_TERMO_FERIAS_VENCIDAS_SIMULACAO` (1.020 linhas)

Simulação do termo de férias vencidas da rescisão. 1.020 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO, I_FERIAS_AQUISITIVOS, I_CALCULOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO, I_FERIAS_AQUISITIVOS, I_CALCULOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.020 linhas, 142 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_da_rescisao 🔒 | `tipo` | integer(4) |  |  | Tipo da rescisão |
| codigo_do_periodo_aquisitivo | `i_ferias_aquisitivos` | integer(4) |  |  | Código do período aquisitivo |
| codigo_do_calculo | `i_calculos` | uniqueidentifier(16) |  |  | Código do cálculo |
| valor | `valor` | numeric(13) |  |  | Valor |
| valor_em_dobro | `valor_dobro` | numeric(13) |  |  | Valor em dobro |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| valor_das_ferias | `valor_ferias` | decimal(13) |  |  | Valor das férias. |
| valor_do_1_3_de_ferias | `valor_adicional` | decimal(13) |  |  | Valor do 1/3 de férias. |
| valor_de_medias_e_vantagens | `valor_medias_vantagens` | decimal(13) |  |  | Valor de médias e vantagens. |
| valor_do_pis | `valor_pis` | decimal(13) |  |  | Valor do Pis. |
| valor_do_1_3_de_ferias_em_dobro | `valor_adicional_dobro` | numeric(13) |  |  | Valor do 1/3 de férias em dobro |
| codigo_do_calculo_renomeado | `i_calculos_old` | integer(4) |  |  | Código do cálculo - Renomeado |
| valor_adicional_sem_medias_vantagens | `valor_adicional_sem_medias_vantagens` | numeric(13) |  |  | Valor adicional sem médias/vantagens |
| valor_adicional_de_medias_vantagens | `valor_adicional_medias_vantagens` | numeric(13) |  |  | Valor adicional de médias/vantagens |
| valor_de_ferias_vencidas_do_dirigente_si | `valor_dirigente_sindical` | numeric(13) |  |  | Valor de férias vencidas do dirigente sindical. |
| base_de_ferias_vencidas_do_dirigente_sin | `base_dirigente_sindical` | numeric(13) |  |  | Base de férias vencidas do dirigente sindical. |
| base_de_ferias_vencidas | `base_ferias` | numeric(13) |  |  | Base de férias vencidas. |

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_da_rescisao` (eq/in), `codigo_do_periodo_aquisitivo` (eq/in), `codigo_do_calculo` (eq/in), `codigo_do_calculo_renomeado` (eq/in)

## forescisoes_termo_configuracao

**Recibo de Rescisão - Configuração** — tabela `FORESCISOES_TERMO_CONFIGURACAO` (378 linhas)

Recibo de Rescisão - Configuração. 378 linhas no catálogo; chave: CODI_EMP, MODELO.

- **Chave:** `CODI_EMP, MODELO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `MODELO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 378 linhas, 367 empresa(s).
- modelo_1_trct_portaria_mte_1621_2010_ane: todos os valores reais estão no comentário do banco (2=367, 1=11).
- tipo_demonstracao: todos os valores reais estão no comentário do banco (3=375, 2=2, 1=1).
- tipo_do_codigo_do_campo_27_0_todos_1_cod: todos os valores reais estão no comentário do banco (1=376, 0=2).
- configuracao_para_emissao_do_campo_2_do: todos os valores reais estão no comentário do banco (1=375, 3=2, 2=1).
- demonstrar_em_branco_os_campos_sem_valor: todos os valores reais estão no comentário do banco (0=236, 1=142).
- demonstrar_no_campo_50_a_quantidade_de_d: todos os valores reais estão no comentário do banco (0=377, 1=1).
- considerar_para_o_campo_23_remuneracao_m: todos os valores reais estão no comentário do banco (0=378).
- demonstrar_codigo_da_entidade_sindical_n: todos os valores reais estão no comentário do banco (0=377, 1=1).
- demonstrar_nos_outros_descontos_o_valor: todos os valores reais estão no comentário do banco (0=377, 1=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1664).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| modelo_1_trct_portaria_mte_1621_2010_ane | `modelo` | smallint(2) |  | forescisoes_termo_configuracao_modelo_1_trct_port | Modelo: (1=TRCT Portaria MTE 1621/2010 - Anexo I/2=TRCT Portaria MTE 1621/2010 - Alterado) |
| tipo_demonstracao | `tipo_demonstracao` | smallint(2) |  | forescisoes_termo_configuracao_tipo_de_demonstrac | Tipo de demonstração: (1=Todos/2=Nenhum/3=Seleção) |
| tipo_do_codigo_do_campo_27_0_todos_1_cod | `tipo_codigo_campo_27` | smallint(2) |  | forescisoes_termo_configuracao_tipo_do_codigo_do_ | Tipo do código do campo 27: (0=Todos/1=Código afastamento homolognet/2=Código do saque FGTS) |
| imprimir_a_identificacao_do_empregador_t | `imprimir_identificacao` | smallint(2) |  |  | Imprimir a identificação do empregador/trabalhador a partir da segunda página: 0=Não/1=Sim |
| imprimir_as_deducoes_na_sequencia_das_ve | `imprimir_deducoes_sequencia` | smallint(2) |  |  | Imprimir as deduções na sequência das verbas rescisórias: 0=Não/1=Sim |
| configuracao_para_emissao_do_campo_2_do | `configuracao_campo_23` | smallint(2) |  | forescisoes_termo_configuracao_configuracao_para_ | Configuração para emissão do campo 2 do recibo de rescisão (1=De acordo com a configuração das rubricas/2=Salário contratual e adicionais/3=Zerado) |
| demonstrar_em_branco_os_campos_sem_valor | `demonstrar_branco_campos_sem_valor` | smallint(2) |  | forescisoes_termo_configuracao_demonstrar_em_bran | Demonstrar em branco os campos sem valor. (0=Não/1=Sim) |
| demonstrar_no_campo_50_a_quantidade_de_d | `demonstrar_quantidade_dias_ferias_gozados_mes_rescisao_campo_50` | smallint(2) |  | forescisoes_termo_configuracao_demonstrar_no_camp | Demonstrar no campo 50 a quantidade de dias de férias que o empregado gozou no mês da rescisão. (0=Não/1=Sim) |
| considerar_para_o_campo_23_remuneracao_m | `considerar_folha_complementar_campo_23` | smallint(2) |  | forescisoes_termo_configuracao_considerar_para_o_ | Considerar para o campo 23-Remuneração Mes Ant. as folhas complementares calculadas. (0=Não/1=Sim) |
| demonstrar_codigo_da_entidade_sindical_n | `demonstrar_codigo_entidade_sindical_campo_31_trabalhador_rural` | smallint(2) |  | forescisoes_termo_configuracao_demonstrar_codigo_ | Demonstrar código da entidade sindical no campo 31 quando trabalhador rural. (0=Não/1=Sim) |
| demonstrar_nos_outros_descontos_o_valor | `demonstrar_valor_informado_outros_descontos` | smallint(2) |  | forescisoes_termo_configuracao_demonstrar_nos_out | Demonstrar nos outros descontos o valor informado da rubrica. (0=Não/1=Sim) |
| imprimir_dados_da_conta_bancaria_do_cola | `emitir_dados_conta_bancaria_colaborador` | smallint(2) |  |  | Imprimir dados da conta bancaria do colaborador no relatorio "TRCT Portaria MTE 1621/2010 - Alterado": 0=Não/1=Sim |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `modelo_1_trct_portaria_mte_1621_2010_ane` (eq/in), `tipo_demonstracao` (eq/in), `tipo_do_codigo_do_campo_27_0_todos_1_cod` (eq/in), `demonstrar_codigo_da_entidade_sindical_n` (eq/in)

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

### forescisoes_termo_configuracao_campos_modelo_1_tr

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO_CAMPOS.MODELO estão no comentário do banco (2026-10-18). Distribuição: 2=11.010, 1=341.

| Código | Significado |
|---|---|
| 1 | TRCT Portaria MTE 1621 |
| 2010 | Alterado |
| 2 | TRCT Portaria MTE 1621 |

### forescisoes_termo_tipo_de_cal

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO.TIPO estão no comentário do banco (2026-10-18). Distribuição: 1=5.520, 2=232.

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Complementar |
| 3 | Parcial |
| 4 | Simulação |

### forescisoes_simulacao_tipo_de_calculo_de_rescisao_

Confirmado: sim

> Todos os valores observados em FORESCISOES_SIMULACAO.TIPO estão no comentário do banco (2026-10-18). Distribuição: 4=1.902.

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Complementar |
| 3 | Parcial |
| 4 | Simulação |

### forescisoes_termo_ferias_vencidas_tipo_de_cal

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_FERIAS_VENCIDAS.TIPO estão no comentário do banco (2026-10-18). Distribuição: 1=1.794, 2=94.

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Complementar |
| 3 | Parcial |
| 4 | Simulação |

### forescisoes_termo_configuracao_modelo_1_trct_port

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.MODELO estão no comentário do banco (2026-10-18). Distribuição: 2=367, 1=11.

| Código | Significado |
|---|---|
| 1 | TRCT Portaria MTE 1621 |
| 2010 | Alterado |
| 2 | TRCT Portaria MTE 1621 |

### forescisoes_termo_configuracao_tipo_de_demonstrac

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.TIPO_DEMONSTRACAO estão no comentário do banco (2026-10-18). Distribuição: 3=375, 2=2, 1=1.

| Código | Significado |
|---|---|
| 1 | Todos |
| 2 | Nenhum |
| 3 | Seleção |

### forescisoes_termo_configuracao_tipo_do_codigo_do_

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.TIPO_CODIGO_CAMPO_27 estão no comentário do banco (2026-10-18). Distribuição: 1=376, 0=2.

| Código | Significado |
|---|---|
| 0 | Todos |
| 1 | Código afastamento homolognet |
| 2 | Código do saque FGTS |

### forescisoes_termo_configuracao_configuracao_para_

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.CONFIGURACAO_CAMPO_23 estão no comentário do banco (2026-10-18). Distribuição: 1=375, 3=2, 2=1.

| Código | Significado |
|---|---|
| 1 | De acordo com a configuração das rubricas |
| 2 | Salário contratual e adicionais |
| 3 | Zerado |

### forescisoes_termo_configuracao_demonstrar_em_bran

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.DEMONSTRAR_BRANCO_CAMPOS_SEM_VALOR estão no comentário do banco (2026-10-18). Distribuição: 0=236, 1=142.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### forescisoes_termo_configuracao_demonstrar_no_camp

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.DEMONSTRAR_QUANTIDADE_DIAS_FERIAS_GOZADOS_MES_RESCISAO_CAMPO_50 estão no comentário do banco (2026-10-18). Distribuição: 0=377, 1=1.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### forescisoes_termo_configuracao_considerar_para_o_

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.CONSIDERAR_FOLHA_COMPLEMENTAR_CAMPO_23 estão no comentário do banco (2026-10-18). Distribuição: 0=378.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### forescisoes_termo_configuracao_demonstrar_codigo_

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.DEMONSTRAR_CODIGO_ENTIDADE_SINDICAL_CAMPO_31_TRABALHADOR_RURAL estão no comentário do banco (2026-10-18). Distribuição: 0=377, 1=1.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### forescisoes_termo_configuracao_demonstrar_nos_out

Confirmado: sim

> Todos os valores observados em FORESCISOES_TERMO_CONFIGURACAO.DEMONSTRAR_VALOR_INFORMADO_OUTROS_DESCONTOS estão no comentário do banco (2026-10-18). Distribuição: 0=377, 1=1.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

