# Modelo — Pessoal - parmto (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_parmto.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foparmto_configuracao_data_pagamento](#foparmto_configuracao_data_pagamento) | `FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO` | 20.325 | medio | empresa |
| [foparmto_natureza_desconto_comp](#foparmto_natureza_desconto_comp) | `FOPARMTO_NATUREZA_DESCONTO_COMP` | 11.812 | medio | empresa |
| [foparmto_alteracao_envios_esocial](#foparmto_alteracao_envios_esocial) | `FOPARMTO_ALTERACAO_ENVIOS_ESOCIAL` | 1.829 | pequeno | empresa |
| [foparmto_alteracao](#foparmto_alteracao) | `FOPARMTO_ALTERACAO` | 1.457 | pequeno | empresa |

## foparmto_configuracao_data_pagamento

**Configurações para as datas de pagamento dos cálculos da folha.** — tabela `FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO` (20.325 linhas)

Configurações para as datas de pagamento dos cálculos da folha.. 20.325 linhas no catálogo; chave: CODI_EMP, TIPO_EMPREGADO, TIPO_PROCESSO, DECIMO_INTEGRAL_COMPETENCIA_DIFERENTE_DEZEMBRO.

- **Chave:** `CODI_EMP, TIPO_EMPREGADO, TIPO_PROCESSO, DECIMO_INTEGRAL_COMPETENCIA_DIFERENTE_DEZEMBRO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `TIPO_EMPREGADO asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20.340 linhas, 1.356 empresa(s).
- tipo_de_empregado_1_empregado_2_contribu: todos os valores reais estão no comentário do banco (3=8.136, 1=8.136, 2=4.068).
- configuracao_para_o_13o_integral_pago_em: todos os valores reais estão no comentário do banco (0=17.628, 1=2.712).
- mes_paga_pagamento_1_1o_mes_subsequente: todos os valores reais estão no comentário do banco (2=16.429, 1=3.908, 3=2, 4=1).
- forma_de_vencimento_1_dias_corridos_dire: todos os valores reais estão no comentário do banco (5=9.189, 3=6.708, 4=3.703, 2=740).
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=20.340).
- antecipar_pagamento_quando_a_data_do_pag: todos os valores reais estão no comentário do banco (0=20.297, 1=43).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| tipo_de_empregado_1_empregado_2_contribu | `tipo_empregado` | smallint(2) |  | foparmto_configuracao_data_pagamento_tipo_de_emp | Tipo de empregado. (1=Empregado/2=Contribuinte/3=Estagiário) |
| tipo_de_calculo | `tipo_processo` | integer(4) |  |  | Tipo de cálculo. |
| configuracao_para_o_13o_integral_pago_em | `decimo_integral_competencia_diferente_dezembro` | smallint(2) |  | foparmto_configuracao_data_pagamento_configuraca | Configuração para o 13º integral pago em competência diferente de dezembro. (0=Não/1=Sim) |
| mes_paga_pagamento_1_1o_mes_subsequente | `mes_pagamento` | smallint(2) |  | foparmto_configuracao_data_pagamento_mes_paga_pa | Mês paga pagamento. (1=1º Mês subsequente/2=No mesmo mês/3=2º Mês subsequente/4=1ª Quinzena/5=2ª Quinzena) |
| forma_de_vencimento_1_dias_corridos_dire | `forma_vencimento` | smallint(2) |  | foparmto_configuracao_data_pagamento_forma_de_ve | Forma de vencimento. (1=Dias corridos direto/2=Dias corridos adiados/3=Dias corridos antecipados/4=Dias úteis/5=Último dia útil) |
| total_de_dias_para_o_calculo_da_data_de | `total_dias` | smallint(2) |  |  | Total de dias para o cálculo da data de pagamento. |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | foparmto_configuracao_data_pagamento_origem_do_r | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout/3=Importação tabelas concorrentes ) |
| antecipar_pagamento_quando_a_data_do_pag | `antecipar_data_pagamento_sabado` | smallint(2) |  | foparmto_configuracao_data_pagamento_antecipar_p | Antecipar pagamento quando a data do pagamento cair no sábado. (0=Não/1=Sim) |

**Filtros:** `tipo_de_empregado_1_empregado_2_contribu` (eq/in), `tipo_de_calculo` (eq/in), `configuracao_para_o_13o_integral_pago_em` (eq/in)

## foparmto_natureza_desconto_comp

**Tabela de naturezas das rubricas de desconto compulsório** — tabela `FOPARMTO_NATUREZA_DESCONTO_COMP` (11.812 linhas)

Tabela de naturezas das rubricas de desconto compulsório. 11.812 linhas no catálogo; chave: CODI_EMP, NATUREZA_FOLHA_MENSAL.

- **Chave:** `CODI_EMP, NATUREZA_FOLHA_MENSAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `NATUREZA_FOLHA_MENSAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.812 linhas, 1.969 empresa(s).
- Vínculo geempre (geempre): 0 de 6 linhas sem registro relacionado (empresa 9082).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| natureza_da_rubrica | `natureza_folha_mensal` | integer(4) |  |  | Natureza da rubrica |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `natureza_da_rubrica` (eq/in)

## foparmto_alteracao_envios_esocial

**Envios das alterações dos parâmetros ao eSocial** — tabela `FOPARMTO_ALTERACAO_ENVIOS_ESOCIAL` (1.829 linhas)

Envios das alterações dos parâmetros ao eSocial. 1.829 linhas no catálogo; chave: CODI_EMP, VIGENCIA, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS.

- **Chave:** `CODI_EMP, VIGENCIA, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `CODI_EMP_DADOS_EVENTOS asc`, `I_DADOS_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.831 linhas, 862 empresa(s), VIGENCIA de 1900-01-01 a 2026-09-01.
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 2 linhas sem registro relacionado (empresa 856).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_evento_referente_a_foesocial_d | `i_dados_eventos` | integer(4) |  |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp_dados_eventos` = `codi_emp` e `i_dados_eventos` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `vigencia` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_do_evento_referente_a_foesocial_d` (eq/in)

## foparmto_alteracao

**Tabela de alterações de parâmetros.** — tabela `FOPARMTO_ALTERACAO` (1.457 linhas)

Tabela de alterações de parâmetros.. 1.457 linhas no catálogo; chave: CODI_EMP, VIGENCIA.

- **Chave:** `CODI_EMP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_EMISSAO_ENTIDADE_BENEFICENTE`
- **Ordem padrão:** `DATA_EMISSAO_ENTIDADE_BENEFICENTE desc`, `VIGENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.459 linhas, 1.356 empresa(s).
- Colunas expostas nulas em 100% das linhas (12): situacao_especial_1_extincao_2_fusao_3_c, sigla_do_ministerio_que_concedeu_a_class, data_de_emissao_da_classificacao_de_enti, data_de_vencimento_da_classificacao_de_e, numero_do_protocolo_de_renovacao_da_clas, data_do_protocolo_de_renovacao_da_entida, data_do_diario_oficial_da_uniao_da_class, pagina_do_diario_oficial_da_uniao_da_cla, codigo_do_processo_judicial_para_contrat, utiliza_forma_unificada_a_orgaos_publico, cnpj_do_ente_federativo_responsavel_a_or, numero_do_processo_para_contratacao_de_d.
- cooperativa_0_nao_1_sim_cooperativa_de_t: todos os valores reais estão no comentário do banco (0=1.459).
- construtora_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=1.456, 1=3).
- optante_pelo_registro_eletronico_de_empr: todos os valores reais estão no comentário do banco (0=1.267, 1=192).
- possui_acordo_internacional_para_isencao: todos os valores reais estão no comentário do banco (0=1.458, 1=1).
- situacao_especial_1_extincao_2_fusao_3_c: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- sigla_do_ministerio_que_concedeu_a_class: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- contratacao_pessoa_com_deficiencia: todos os valores reais estão no comentário do banco (1=1.372, 4=87).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=869, 0=590).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=1.433, 1=26).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=1.459).
- origem_do_registro_1_sistema_2_alteracao: todos os valores reais estão no comentário do banco (1=1.455, 2=4).
- calcular_funrural_sobre_a_de_folha_pagam: todos os valores reais estão no comentário do banco (0=1.459).
- utiliza_modulo_web_simplificado_me_e_epp: todos os valores reais estão no comentário do banco (0=1.459).
- utiliza_forma_unificada_a_orgaos_publico: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| vigencia_da_alteracao | `vigencia` | date(4) |  |  | Vigência da alteração. |
| classificacao_tributaria | `classificacao_tributaria` | smallint(2) |  |  | Classificação tributária. |
| cooperativa_0_nao_1_sim_cooperativa_de_t | `cooperativa` | smallint(2) |  | foparmto_alteracao_cooperativa_0_n | Cooperativa. (0=Não/1=Sim, cooperativa de trabalho/2=Sim, cooperativa de produção/3=Sim, outras cooperativas) |
| construtora_0_nao_1_sim | `construtora` | smallint(2) |  | foparmto_alteracao_construtora_0_n | Construtora. (0=Não/1=Sim) |
| optante_pelo_registro_eletronico_de_empr | `optante_registro_eletronico_empregados` | smallint(2) |  | foparmto_alteracao_optante_pelo_re | Optante pelo registro eletrônico de empregados. (0=Não/1=Sim) |
| possui_acordo_internacional_para_isencao | `possui_acordo_internacional_isencao_multa` | smallint(2) |  | foparmto_alteracao_possui_acordo_i | Possui acordo internacional para isenção de multa. (0=Não/1=Sim) |
| situacao_especial_1_extincao_2_fusao_3_c | `possui_situacao_especial_situacao` | smallint(2) |  | foparmto_alteracao_situacao_especi | Situação especial. (1=Extinção/2=Fusão/3=Cisão/4=Incorporação) |
| sigla_do_ministerio_que_concedeu_a_class | `sigla_ministerio_concedeu_entidade_beneficente` | smallint(2) |  | foparmto_alteracao_sigla_do_minist | Sigla do ministério que concedeu a classificação de Entidade Beneficente. (1=CNAS/2=MEC/3=MS/4=MDS/5=Lei) |
| data_de_emissao_da_classificacao_de_enti | `data_emissao_entidade_beneficente` | date(4) |  |  | Data de emissão da classificação de Entidade Beneficente. |
| data_de_vencimento_da_classificacao_de_e | `data_vencimento_entidade_beneficente` | date(4) |  |  | Data de vencimento da classificação de Entidade Beneficente. |
| numero_do_protocolo_de_renovacao_da_clas | `numero_protocolo_renovacao_entidade_beneficente` | varchar(40) |  |  | Número do protocolo de renovação da classificação de Entidade Beneficente. |
| data_do_protocolo_de_renovacao_da_entida | `data_protocolo_renovacao_entidade_beneficente` | date(4) |  |  | Data do protocolo de renovação da Entidade Beneficente. |
| data_do_diario_oficial_da_uniao_da_class | `data_diario_oficial_uniao_entidade_beneficente` | date(4) |  |  | Data do diário oficial da união da classificação de Entidade Beneficente. |
| pagina_do_diario_oficial_da_uniao_da_cla | `paginal_diario_oficial_uniao_entidade_beneficente` | varchar(5) |  |  | Página do diário oficial da união da classificação de Entidade Beneficente. |
| contratacao_pessoa_com_deficiencia | `contratacao_pessoa_com_deficiencia` | smallint(2) |  | foparmto_alteracao_contratacao_de_ | Contratação de pessoa com deficiência. (1=Dispensado de acordo com a lei/2=Dispensado, mesmo que parcialmente/3=Com a exigibilidade suspensa/4=Obrigado) |
| codigo_do_processo_judicial_para_contrat | `i_processo_pessoa_deficiencia` | integer(4) |  |  | Código do processo judicial para contratação de pessoa com deficiência. |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | foparmto_alteracao_enviar_para_o_e | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | foparmto_alteracao_gerar_retificac | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | foparmto_alteracao_marcacao_do_eve | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| origem_do_registro_1_sistema_2_alteracao | `origem_alteracao` | smallint(2) |  | foparmto_alteracao_origem_do_regis | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| calcular_funrural_sobre_a_de_folha_pagam | `calcular_funrural_sobre_folha_pagamento` | smallint(2) |  | foparmto_alteracao_calcular_funrur | Calcular FUNRURAL sobre a de folha pagamento. (0=Não/1=Sim) |
| utiliza_modulo_web_simplificado_me_e_epp | `utiliza_modulo_web_simplificado_me_epp_esocial` | smallint(2) |  | foparmto_alteracao_utiliza_modulo_ | Utiliza módulo Web Simplificado ME e EPP. (0=Não/1=Sim) |
| utiliza_forma_unificada_a_orgaos_publico | `utiliza_forma_unificada_esocial` | smallint(2) |  | foparmto_alteracao_utiliza_forma_u | Utiliza forma unificada a orgãos públicos. (0=Não/1=Sim) |
| cnpj_do_ente_federativo_responsavel_a_or 🔒 | `cnpj_ente_federativo_responsavel` | varchar(14) |  |  | CNPJ do Ente Federativo Responsável a orgãos públicos. |
| numero_do_processo_para_contratacao_de_d 🔒 | `numero_processo_deficiente` | varchar(20) |  |  | Numero do processo para contratação de deficiente. |
| entidade_beneficiente_informacoes_comple | `gera_dados_isencao_entidade_beneficiente` | char(1) |  |  | Entidade Beneficiente - Informações Complementares - Dados da Isenção |

**Filtros:** `vigencia_da_alteracao` (eq/in), `data_de_emissao_da_classificacao_de_enti` (entre/gte/lte), `data_de_vencimento_da_classificacao_de_e` (entre/gte/lte), `data_do_protocolo_de_renovacao_da_entida` (entre/gte/lte), `data_do_diario_oficial_da_uniao_da_class` (entre/gte/lte), `situacao_especial_1_extincao_2_fusao_3_c` (eq/in), `numero_do_protocolo_de_renovacao_da_clas` (contem/prefixo), `pagina_do_diario_oficial_da_uniao_da_cla` (eq/in), `codigo_do_processo_judicial_para_contrat` (eq/in), `cnpj_do_ente_federativo_responsavel_a_or` (eq/in), `numero_do_processo_para_contratacao_de_d` (eq/in), `entidade_beneficiente_informacoes_comple` (eq/in)

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

### foparmto_configuracao_data_pagamento_tipo_de_emp

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.TIPO_EMPREGADO estão no comentário do banco (2026-10-18). Distribuição: 3=8.136, 1=8.136, 2=4.068.

| Código | Significado |
|---|---|
| 1 | Empregado |
| 2 | Contribuinte |
| 3 | Estagiário |

### foparmto_configuracao_data_pagamento_configuraca

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.DECIMO_INTEGRAL_COMPETENCIA_DIFERENTE_DEZEMBRO estão no comentário do banco (2026-10-18). Distribuição: 0=17.628, 1=2.712.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_configuracao_data_pagamento_mes_paga_pa

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.MES_PAGAMENTO estão no comentário do banco (2026-10-18). Distribuição: 2=16.429, 1=3.908, 3=2, 4=1.

| Código | Significado |
|---|---|
| 1 | 1º Mês subsequente |
| 2 | No mesmo mês |
| 3 | 2º Mês subsequente |
| 4 | 1ª Quinzena |
| 5 | 2ª Quinzena |

### foparmto_configuracao_data_pagamento_forma_de_ve

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.FORMA_VENCIMENTO estão no comentário do banco (2026-10-18). Distribuição: 5=9.189, 3=6.708, 4=3.703, 2=740.

| Código | Significado |
|---|---|
| 1 | Dias corridos direto |
| 2 | Dias corridos adiados |
| 3 | Dias corridos antecipados |
| 4 | Dias úteis |
| 5 | Último dia útil |

### foparmto_configuracao_data_pagamento_origem_do_r

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=20.340.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Importação de tabelas |
| 2 | Importação de layout |
| 3 | Importação tabelas concorrentes |

### foparmto_configuracao_data_pagamento_antecipar_p

Confirmado: sim

> Todos os valores observados em FOPARMTO_CONFIGURACAO_DATA_PAGAMENTO.ANTECIPAR_DATA_PAGAMENTO_SABADO estão no comentário do banco (2026-10-18). Distribuição: 0=20.297, 1=43.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_cooperativa_0_n

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.COOPERATIVA estão no comentário do banco (2026-10-18). Distribuição: 0=1.459.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim, cooperativa de trabalho |
| 2 | Sim, cooperativa de produção |
| 3 | Sim, outras cooperativas |

### foparmto_alteracao_construtora_0_n

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.CONSTRUTORA estão no comentário do banco (2026-10-18). Distribuição: 0=1.456, 1=3.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_optante_pelo_re

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.OPTANTE_REGISTRO_ELETRONICO_EMPREGADOS estão no comentário do banco (2026-10-18). Distribuição: 0=1.267, 1=192.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_possui_acordo_i

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.POSSUI_ACORDO_INTERNACIONAL_ISENCAO_MULTA estão no comentário do banco (2026-10-18). Distribuição: 0=1.458, 1=1.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_situacao_especi

Confirmado: parcial

> Coluna FOPARMTO_ALTERACAO.POSSUI_SITUACAO_ESPECIAL_SITUACAO só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 1 | Extinção |
| 2 | Fusão |
| 3 | Cisão |
| 4 | Incorporação |

### foparmto_alteracao_sigla_do_minist

Confirmado: parcial

> Coluna FOPARMTO_ALTERACAO.SIGLA_MINISTERIO_CONCEDEU_ENTIDADE_BENEFICENTE só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 1 | CNAS |
| 2 | MEC |
| 3 | MS |
| 4 | MDS |
| 5 | Lei |

### foparmto_alteracao_contratacao_de_

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.CONTRATACAO_PESSOA_COM_DEFICIENCIA estão no comentário do banco (2026-10-18). Distribuição: 1=1.372, 4=87.

| Código | Significado |
|---|---|
| 1 | Dispensado de acordo com a lei |
| 2 | Dispensado, mesmo que parcialmente |
| 3 | Com a exigibilidade suspensa |
| 4 | Obrigado |

### foparmto_alteracao_enviar_para_o_e

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=869, 0=590.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_gerar_retificac

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=1.433, 1=26.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_marcacao_do_eve

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=1.459.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_origem_do_regis

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.ORIGEM_ALTERACAO estão no comentário do banco (2026-10-18). Distribuição: 1=1.455, 2=4.

| Código | Significado |
|---|---|
| 1 | Sistema |
| 2 | Alteração de Faseamento do eSocial |

### foparmto_alteracao_calcular_funrur

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.CALCULAR_FUNRURAL_SOBRE_FOLHA_PAGAMENTO estão no comentário do banco (2026-10-18). Distribuição: 0=1.459.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_utiliza_modulo_

Confirmado: sim

> Todos os valores observados em FOPARMTO_ALTERACAO.UTILIZA_MODULO_WEB_SIMPLIFICADO_ME_EPP_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=1.459.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foparmto_alteracao_utiliza_forma_u

Confirmado: parcial

> Coluna FOPARMTO_ALTERACAO.UTILIZA_FORMA_UNIFICADA_ESOCIAL só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

