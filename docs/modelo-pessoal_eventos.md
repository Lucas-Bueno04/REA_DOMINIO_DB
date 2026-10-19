# Modelo — Pessoal - eventos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_eventos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foeventos_alteracao_controle_envio_esocial](#foeventos_alteracao_controle_envio_esocial) | `FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL` | 3.750.710 | grande | empresa; um de: codigo_da_rubrica |
| [foeventos_alteracao](#foeventos_alteracao) | `FOEVENTOS_ALTERACAO` | 1.331.191 | grande | empresa; um de: codigo_da_rubrica |
| [foeventos_alteracao_dados_cadastrais](#foeventos_alteracao_dados_cadastrais) | `FOEVENTOS_ALTERACAO_DADOS_CADASTRAIS` | 1.310.502 | grande | empresa; um de: codigo_da_rubrica |
| [foeventos_ordem_calculo](#foeventos_ordem_calculo) | `FOEVENTOS_ORDEM_CALCULO` | 1.051.318 | grande | empresa; um de: codigo_dos_eventos |
| [foeventos_alteracao_controle_envio_esocial_envios_esocial](#foeventos_alteracao_controle_envio_esocial_envios_esocial) | `FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL_ENVIOS_ESOCIAL` | 570.241 | medio | empresa |
| [foeventos_afast](#foeventos_afast) | `foeventos_afast` | 214.085 | medio | empresa |
| [foeventos_afastdef](#foeventos_afastdef) | `foeventos_afastdef` | 275 | pequeno | — |

## foeventos_alteracao_controle_envio_esocial

**Tabela de controle de envio da rubrica ao eSocial.** — tabela `FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL` (3.750.710 linhas)

Tabela de controle de envio da rubrica ao eSocial.. 3.750.710 linhas no catálogo; chave: CODI_EMP, I_EVENTOS, VIGENCIA, CODI_EMP_ENVIO.

- **Chave:** `CODI_EMP, I_EVENTOS, VIGENCIA, CODI_EMP_ENVIO`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA` · exige um de: `codigo_da_rubrica`
- **Ordem padrão:** `VIGENCIA desc`, `I_EVENTOS asc`, `CODI_EMP_ENVIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.752.407 linhas, 711 empresa(s), VIGENCIA de 1900-01-01 a 2026-07-01.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=3.608.952, 1=143.455).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (1=1.886.981, 0=1.865.426).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=3.752.407).
- Vínculo geempre (geempre): 0 de 1.888 linhas sem registro relacionado (empresa 571).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa_do_evento | `codi_emp` | integer(4) |  |  | Código da empresa do evento. |
| codigo_da_rubrica | `i_eventos` | integer(4) |  |  | Código da rubrica. |
| vigencia_da_alteracao | `vigencia` | date(4) |  |  | Vigência da alteração. |
| codigo_da_empresa_de_envio_do_evento_ao | `codi_emp_envio` | integer(4) |  |  | Codigo da empresa de envio do evento ao eSocial. |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | foeventos_alteracao_controle_envio_esocial_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | foeventos_alteracao_controle_envio_esocial_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | foeventos_alteracao_controle_envio_esocial_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp_envio` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo_da_rubrica` (eq/in), `vigencia_da_alteracao` (eq/in), `codigo_da_empresa_de_envio_do_evento_ao` (eq/in)

## foeventos_alteracao

**Tabela de alterações.** — tabela `FOEVENTOS_ALTERACAO` (1.331.191 linhas)

Tabela de alterações.. 1.331.191 linhas no catálogo; chave: CODI_EMP, I_EVENTOS, VIGENCIA.

- **Chave:** `CODI_EMP, I_EVENTOS, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA` · exige um de: `codigo_da_rubrica`
- **Ordem padrão:** `VIGENCIA desc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.332.888 linhas, 732 empresa(s), VIGENCIA de 1900-01-01 a 2026-07-01.
- origem_do_registro_1_sistema_2_alteracao: todos os valores reais estão no comentário do banco (1=1.317.230, 2=15.658).
- Vínculo foincidencia_pis_rubrica (FOINCIDENCIA_PIS_RUBRICA_ESOCIAL): 0 de 1.886 linhas sem registro relacionado (empresa 220).
- Vínculo foeventos (foeventos): 0 de 1.886 linhas sem registro relacionado (empresa 220).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa_do_evento | `codi_emp` | integer(4) |  |  | Código da empresa do evento. |
| codigo_da_rubrica | `i_eventos` | integer(4) |  |  | Código da rubrica. |
| vigencia_da_alteracao | `vigencia` | date(4) |  |  | Vigência da alteração. |
| nome_da_rubrica | `nome` | varchar(50) |  |  | Nome da rubrica. |
| tipo_rubrica | `prov_desc` | char(2) |  |  | Tipo rubrica. |
| natureza_do_evento_para_folha_mensal | `natureza_folha_mensal` | integer(4) |  |  | Natureza do evento para folha mensal. |
| natureza_do_evento_para_13_integral | `natureza_13_integral` | integer(4) |  |  | Natureza do evento para 13° integral. |
| codigo_da_incidencias_do_irrf_para_o_eso | `codigo_incidencia_irrf_esocial` | integer(4) |  |  | Código da incidências do IRRF para o eSocial. |
| codigo_da_incidencias_do_inss_para_o_eso | `codigo_incidencia_inss_esocial` | integer(4) |  |  | Código da incidências do INSS para o eSocial. |
| codigo_da_incidencias_do_fgts_para_o_eso | `codigo_incidencia_fgts_esocial` | integer(4) |  |  | Código da incidências do FGTS para o eSocial. |
| codigo_da_incidencias_sindical_para_o_es | `codigo_incidencia_sindical_esocial` | integer(4) |  |  | Código da incidências sindical para o eSocial. |
| alteracao_de_informacoes_que_devem_ser_e | `enviar_alteracao_esocial` | smallint(2) |  |  | Alteração de informações que devem ser enviadas ao eSocial. |
| alteracao_inserida_pela_troca_de_faseame | `alteracao_faseamento_esocial` | smallint(2) |  |  | Alteração inserida pela troca de faseamento do eSocial. |
| origem_do_registro_1_sistema_2_alteracao | `origem_alteracao` | smallint(2) |  | foeventos_alteracao_origem_do_registro_1_sistema_ | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| codigo_de_incidencia_do_rpps_para_o_esoc | `codigo_incidencia_rpps_esocial` | integer(4) |  |  | Código de incidência do RPPS para o eSocial. |
| codigo_de_incidencia_do_pis_para_o_esoci | `codigo_incidencia_pis_esocial` | integer(4) |  |  | Código de incidência do PIS para o eSocial |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foincidencia_pis_rubrica` → `FOINCIDENCIA_PIS_RUBRICA_ESOCIAL` por `codigo_incidencia_pis_esocial` = `codigo`; colunas: `foincidencia_pis_rubrica_nome`
- `foeventos` → `foeventos` por `codi_emp` = `codi_emp` e `i_eventos` = `i_eventos`; colunas: `foeventos_nome`

**Filtros:** `codigo_da_rubrica` (eq/in), `vigencia_da_alteracao` (eq/in), `nome_da_rubrica` (contem/prefixo), `tipo_rubrica` (eq/in), `codigo_da_incidencias_do_irrf_para_o_eso` (eq/in), `codigo_da_incidencias_do_inss_para_o_eso` (eq/in), `codigo_da_incidencias_do_fgts_para_o_eso` (eq/in), `codigo_da_incidencias_sindical_para_o_es` (eq/in), `codigo_de_incidencia_do_rpps_para_o_esoc` (eq/in), `codigo_de_incidencia_do_pis_para_o_esoci` (eq/in)

## foeventos_alteracao_dados_cadastrais

**Alteração de dados cadastrais do histórico do cadastro de rubricas** — tabela `FOEVENTOS_ALTERACAO_DADOS_CADASTRAIS` (1.310.502 linhas)

Alteração de dados cadastrais do histórico do cadastro de rubricas. 1.310.502 linhas no catálogo; chave: CODI_EMP, I_EVENTOS, VIGENCIA.

- **Chave:** `CODI_EMP, I_EVENTOS, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA` · exige um de: `codigo_da_rubrica`
- **Ordem padrão:** `VIGENCIA desc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.312.199 linhas, 732 empresa(s), VIGENCIA de 1900-01-01 a 2026-07-01.
- origem_do_registro_1_sistema_2_alteracao: todos os valores reais estão no comentário do banco (1=1.307.271, 2=4.928).
- Vínculo foeventos (foeventos): 0 de 1.886 linhas sem registro relacionado (empresa 638).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa_do_evento | `codi_emp` | integer(4) |  |  | Código da empresa do evento. |
| codigo_da_rubrica | `i_eventos` | integer(4) |  |  | Código da rubrica. |
| vigencia_da_alteracao | `vigencia` | date(4) |  |  | Vigência da alteração. |
| taxa_da_rubrica | `taxa` | numeric(7) |  |  | Taxa da rubrica. |
| soma_adicional_aviso_previo | `soma_adicional_aviso_previo` | smallint(2) |  |  | Soma adicional aviso prévio. |
| computa_13_ferias | `comp_13fer` | char(1) |  |  | Computa 13/Ferias. |
| soma_media_aviso_previo | `soma_media_aviso_previo` | smallint(2) |  |  | Soma média aviso prévio. |
| soma_med_13 | `soma_med_13` | char(1) |  |  | Soma média 13° |
| soma_media_ferias | `soma_med_fer` | char(1) |  |  | Soma média férias. |
| reflexo_dsr | `base_rdsr` | char(1) |  |  | Reflexo DSR. |
| desconta_no_dsr | `desconta_dsr` | smallint(2) |  |  | Desconta no DSR. |
| soma_media_licenca_premio | `soma_media_licenca_premio` | smallint(2) |  |  | Soma média licença prêmio. |
| soma_adicional_licenca_premio | `soma_adicional_licenca_premio` | smallint(2) |  |  | Soma adicional licença prêmio. |
| tipo_de_valor_pra_considerar_no_calculo | `tipo_valor_considerar_calculo_medias` | smallint(2) |  |  | Tipo de valor pra considerar no cálculo de médias. |
| detalhar_lancamento_por_servico | `detalhar_lancamento_por_servico` | smallint(2) |  |  | Detalhar lançamento por serviço. |
| origem_do_registro_1_sistema_2_alteracao | `origem_alteracao` | smallint(2) |  | foeventos_alteracao_dados_cadastrais_origem_do_r | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| utiliza_para_o_esocial_domestico | `utiliza_para_esocial_domestico` | smallint(2) |  |  | Utiliza para o eSocial Doméstico |
| codigo_esocial_domestico | `codigo_esocial_domestico` | varchar(15) |  |  | Código eSocial Doméstico |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foeventos` → `foeventos` por `codi_emp` = `codi_emp` e `i_eventos` = `i_eventos`; colunas: `foeventos_nome`

**Filtros:** `codigo_da_rubrica` (eq/in), `vigencia_da_alteracao` (eq/in), `computa_13_ferias` (eq/in), `soma_med_13` (eq/in), `soma_media_ferias` (eq/in), `reflexo_dsr` (eq/in), `tipo_de_valor_pra_considerar_no_calculo` (eq/in), `codigo_esocial_domestico` (eq/in)

## foeventos_ordem_calculo

**Tabela de controle da ordem de cálculo das rubricas** — tabela `FOEVENTOS_ORDEM_CALCULO` (1.051.318 linhas)

Tabela de controle da ordem de cálculo das rubricas. 1.051.318 linhas no catálogo; chave: CODI_EMP, I_EVENTOS.

- **Chave:** `CODI_EMP, I_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—` · exige um de: `codigo_dos_eventos`
- **Ordem padrão:** `I_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.053.025 linhas, 603 empresa(s).
- Vínculo foeventos (foeventos): 0 de 1.698 linhas sem registro relacionado (empresa 1507).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_dos_eventos | `i_eventos` | integer(4) |  |  | Código dos eventos |
| ordem_do_calculo | `ordem_calculo` | integer(4) |  |  | Ordem do cálculo |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foeventos` → `foeventos` por `codi_emp` = `codi_emp` e `i_eventos` = `i_eventos`; colunas: `foeventos_nome`

**Filtros:** `codigo_dos_eventos` (eq/in)

## foeventos_alteracao_controle_envio_esocial_envios_esocial

**Envios do controle de envio de rubrica ao eSocial** — tabela `FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL_ENVIOS_ESOCIAL` (570.241 linhas)

Envios do controle de envio de rubrica ao eSocial. 570.241 linhas no catálogo; chave: CODI_EMP, I_EVENTOS, VIGENCIA, CODI_EMP_ENVIO, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS.

- **Chave:** `CODI_EMP, I_EVENTOS, VIGENCIA, CODI_EMP_ENVIO, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_EVENTOS asc`, `CODI_EMP_ENVIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 570.249 linhas, 413 empresa(s), VIGENCIA de 1900-01-01 a 2026-05-01.
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 1.503 linhas sem registro relacionado (empresa 802).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| codigo_da_empresa_de_envio_do_evento_ao | `codi_emp_envio` | integer(4) |  |  | Código da empresa de envio do evento ao eSocial |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_evento_referente_a_foesocial_d | `i_dados_eventos` | integer(4) |  |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp_dados_eventos` = `codi_emp` e `i_dados_eventos` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `codigo_do_evento` (eq/in), `vigencia` (eq/in), `codigo_da_empresa_de_envio_do_evento_ao` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_do_evento_referente_a_foesocial_d` (eq/in)

## foeventos_afast

**Eventos pagos em afastamento** — tabela `foeventos_afast` (214.085 linhas)

Eventos pagos em afastamento. 214.085 linhas no catálogo; chave: codi_emp, i_eventos, situacao.

- **Chave:** `codi_emp, i_eventos, situacao`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `i_eventos asc`, `situacao asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 214.360 linhas, 722 empresa(s).
- Vínculo foeventos (foeventos): 0 de 319 linhas sem registro relacionado (empresa 291).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| situacao | `situacao` | integer(4) |  |  | Situacao |
| codigo_do_evento_de_afastamento | `i_eventos_afast` | integer(4) |  |  | Código do evento de afastamento |
| calcular_1_sim_0_nao | `calcular` | tinyint(1) |  |  | Calcular: 1=Sim, 0=Nao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foeventos` → `foeventos` por `codi_emp` = `codi_emp` e `i_eventos` = `i_eventos`; colunas: `foeventos_nome`

**Filtros:** `codigo_do_evento` (eq/in), `situacao` (eq/in), `codigo_do_evento_de_afastamento` (eq/in)

## foeventos_afastdef

**Eventos pagos em afastamento - padrao** — tabela `foeventos_afastdef` (275 linhas)

Eventos pagos em afastamento - padrao. 275 linhas no catálogo; chave: i_eventos, situacao.

- **Chave:** `i_eventos, situacao`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `i_eventos asc`, `situacao asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 275 linhas.
- Vínculo foeventosdef (foeventosdef): 0 de 275 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_evento | `i_eventos` | integer(4) |  |  | Código do evento |
| situacao | `situacao` | integer(4) |  |  | Situacao |
| codigo_do_evento_de_afastamento | `i_eventos_afast` | integer(4) |  |  | Código do evento de afastamento |
| calcular_1_sim_0_nao | `calcular` | tinyint(1) |  |  | Calcular: 1=Sim, 0=Nao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foeventosdef` → `foeventosdef` por `i_eventos` = `i_eventos`; colunas: `foeventosdef_nome`

**Filtros:** `codigo_do_evento` (eq/in), `situacao` (eq/in), `codigo_do_evento_de_afastamento` (eq/in)

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

### foeventos_alteracao_controle_envio_esocial_enviar_para

Confirmado: sim

> Todos os valores observados em FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=3.608.952, 1=143.455.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foeventos_alteracao_controle_envio_esocial_gerar_retif

Confirmado: sim

> Todos os valores observados em FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=1.886.981, 0=1.865.426.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foeventos_alteracao_controle_envio_esocial_marcacao_do

Confirmado: sim

> Todos os valores observados em FOEVENTOS_ALTERACAO_CONTROLE_ENVIO_ESOCIAL.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=3.752.407.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foeventos_alteracao_origem_do_registro_1_sistema_

Confirmado: sim

> Todos os valores observados em FOEVENTOS_ALTERACAO.ORIGEM_ALTERACAO estão no comentário do banco (2026-10-18). Distribuição: 1=1.317.230, 2=15.658.

| Código | Significado |
|---|---|
| 1 | Sistema |
| 2 | Alteração de Faseamento do eSocial |

### foeventos_alteracao_dados_cadastrais_origem_do_r

Confirmado: sim

> Todos os valores observados em FOEVENTOS_ALTERACAO_DADOS_CADASTRAIS.ORIGEM_ALTERACAO estão no comentário do banco (2026-10-18). Distribuição: 1=1.307.271, 2=4.928.

| Código | Significado |
|---|---|
| 1 | Sistema |
| 2 | Alteração de Faseamento do eSocial |

