# Modelo — Pessoal - afastamentos (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_afastamentos.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [foafastamentos_envios_esocial](#foafastamentos_envios_esocial) | `FOAFASTAMENTOS_ENVIOS_ESOCIAL` | 16.173 | medio | empresa |
| [foafastamentos_estabilidade](#foafastamentos_estabilidade) | `FOAFASTAMENTOS_ESTABILIDADE` | 1.565 | pequeno | empresa |
| [foafastamentos_periodo_aquisitivo](#foafastamentos_periodo_aquisitivo) | `FOAFASTAMENTOS_PERIODO_AQUISITIVO` | 480 | pequeno | empresa |
| [foafastamentos_dados_eventos_esocial](#foafastamentos_dados_eventos_esocial) | `FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL` | 42 | pequeno | empresa |
| [foafastamentos_somar_dias](#foafastamentos_somar_dias) | `FOAFASTAMENTOS_SOMAR_DIAS` | 23 | pequeno | empresa |

## foafastamentos_envios_esocial

**Envios de afastamentos ao eSocial** — tabela `FOAFASTAMENTOS_ENVIOS_ESOCIAL` (16.173 linhas)

Envios de afastamentos ao eSocial. 16.173 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `DATA_REAL_DN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 16.176 linhas, 216 empresa(s).
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 24 linhas sem registro relacionado (empresa 961).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| data_numerica_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data numérica do afastamento |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_referente_a_foesocial_dados_event | `i_dados_eventos` | integer(4) |  |  | Código referente a FOESOCIAL_DADOS_EVENTOS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp_dados_eventos` = `codi_emp` e `i_dados_eventos` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_numerica_do_afastamento` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_referente_a_foesocial_dados_event` (eq/in)

## foafastamentos_estabilidade

**Estabilidades do empregado geradas pelo afastamento.** — tabela `FOAFASTAMENTOS_ESTABILIDADE` (1.565 linhas)

Estabilidades do empregado geradas pelo afastamento.. 1.565 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, I_ESTABILIDADE, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, I_ESTABILIDADE, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `DATA_REAL_DN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.568 linhas, 99 empresa(s).
- estabilidade_gerada_pela_convencao_colet: todos os valores reais estão no comentário do banco (1=1.532, 0=36).
- Vínculo foafastamentos (FOAFASTAMENTOS): 0 de 4 linhas sem registro relacionado (empresa 291).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_real_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data real do afastamento. |
| codigo_do_tipo_de_estabilidade | `i_estabilidade` | integer(4) |  |  | Código do tipo de estabilidade. |
| codigo_sequencial_da_estabilidade | `sequencial` | integer(4) |  |  | Código sequencial da estabilidade. |
| estabilidade_gerada_pela_convencao_colet | `estabilidade_cct` | smallint(2) |  | foafastamentos_estabilidade_estabilidad | Estabilidade gerada pela Convenção Coletiva de Trabalho (0=Não/1=Sim ). |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foafastamentos` → `FOAFASTAMENTOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `data_real_dn` = `data_real_dn`; colunas: `foafastamentos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_real_do_afastamento` (eq/in), `codigo_do_tipo_de_estabilidade` (eq/in), `codigo_sequencial_da_estabilidade` (eq/in)

## foafastamentos_periodo_aquisitivo

**AFASTAMENTOS SEPARADOS POR PERIODO AQUISITIVO** — tabela `FOAFASTAMENTOS_PERIODO_AQUISITIVO` (480 linhas)

AFASTAMENTOS SEPARADOS POR PERIODO AQUISITIVO. 480 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_FERIAS_AQUISITIVOS, DATA_INICIO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_FERIAS_AQUISITIVOS, DATA_INICIO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_FIM`
- **Ordem padrão:** `DATA_FIM desc`, `I_EMPREGADOS asc`, `I_FERIAS_AQUISITIVOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 480 linhas, 88 empresa(s), DATA_FIM de 2012-02-25 a 2027-01-27.
- onus_da_remuneracao_do_exercicio_do_mand: todos os valores reais estão no comentário do banco (2=409, nulo=71).
- Vínculo foafastamentos (FOAFASTAMENTOS): 0 de 2 linhas sem registro relacionado (empresa 9090).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | CODIGO EMPRESA |
| codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| sequencia_de_periodos_aquisitivos | `i_ferias_aquisitivos` | integer(4) |  |  | SEQUENCIA DE PERIODOS AQUISITIVOS |
| data_de_inicio_do_afastamento | `data_inicio` | date(4) |  |  | Data de início do afastamento |
| data_final_do_afastamento | `data_fim` | date(4) |  |  | Data final do afastamento |
| data_real_do_afastamento | `data_real` | date(4) |  |  | Data real do afastamento |
| codigo_do_afastamento | `i_afastamentos` | integer(4) |  |  | Código do afastamento |
| numero_de_dias | `numero_dias` | numeric(10) |  |  | Número de dias |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| data_numerica_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data numérica do afastamento |
| onus_da_remuneracao_do_exercicio_do_mand | `onus_remuneracao_mandato_sindical` | smallint(2) |  | foafastamentos_periodo_aquisitivo_onus_da_rem | Ônus da remuneração do exercício do mandato sindical. (1=Empregador/2=Sindicato/3=Diferença salarial paga pelo sindicato/null=Sem dados informado, conversao) |
| dilatar_periodo_aquisitivo_0_nao_1_sim | `dilatar_periodo_aquisitivo` | smallint(2) |  |  | Dilatar período aquisitivo. 0=Não/1=Sim |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foafastamentos` → `FOAFASTAMENTOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `data_real_dn` = `data_real_dn`; colunas: `foafastamentos_nome`

**Filtros:** `codigo` (eq/in), `sequencia_de_periodos_aquisitivos` (eq/in), `data_de_inicio_do_afastamento` (eq/in), `data_final_do_afastamento` (entre/gte/lte), `data_real_do_afastamento` (entre/gte/lte), `codigo_do_afastamento` (eq/in)

## foafastamentos_dados_eventos_esocial

**Dados de envio do afastamento para o eSocial.** — tabela `FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL` (42 linhas)

Dados de envio do afastamento para o eSocial.. 42 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_EMPREGADOS asc`, `DATA_REAL_DN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 42 linhas, 10 empresa(s).
- evento_de_inclusao_de_afastamento_0_nao: todos os valores reais estão no comentário do banco (1=30, 0=12).
- evento_de_inclusao_de_data_fim_de_afasta: todos os valores reais estão no comentário do banco (0=30, 1=12).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=42).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=42).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=42).
- Vínculo foafastamentos (FOAFASTAMENTOS): 0 de 4 linhas sem registro relacionado (empresa 147).
- Vínculo foesocial_dados_eventos (FOESOCIAL_DADOS_EVENTOS): 0 de 4 linhas sem registro relacionado (empresa 147).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data do afastamento. |
| codigo_sequencial | `sequencial` | integer(4) |  |  | Código sequencial |
| evento_de_inclusao_de_afastamento_0_nao | `evento_inclusao_afastamento` | smallint(2) |  | foafastamentos_dados_eventos_esocial_evento_de_i | Evento de inclusão de afastamento (0 = Não/1 = Sim) |
| evento_de_inclusao_de_data_fim_de_afasta | `evento_inclusao_data_fim_afastamento` | smallint(2) |  | foafastamentos_dados_eventos_esocial_evento_de_i | Evento de inclusão de data fim de afastamento (0 = Não/1 = Sim) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | foafastamentos_dados_eventos_esocial_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | foafastamentos_dados_eventos_esocial_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | foafastamentos_dados_eventos_esocial_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foafastamentos` → `FOAFASTAMENTOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `data_real_dn` = `data_real_dn`; colunas: `foafastamentos_nome`
- `foesocial_dados_eventos` → `FOESOCIAL_DADOS_EVENTOS` por `codi_emp` = `codi_emp` e `i_dados_eventos_esocial` = `i_dados_eventos`; colunas: `foesocial_dados_eventos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_do_afastamento` (eq/in), `codigo_sequencial` (eq/in)

## foafastamentos_somar_dias

**Informações sobre os afastamentos que devem somar para calcular a data folha.** — tabela `FOAFASTAMENTOS_SOMAR_DIAS` (23 linhas)

Informações sobre os afastamentos que devem somar para calcular a data folha.. 23 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, DATA_REAL_DN_AFASTAMENTO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_REAL_DN, DATA_REAL_DN_AFASTAMENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_REAL`
- **Ordem padrão:** `DATA_REAL desc`, `I_EMPREGADOS asc`, `DATA_REAL_DN asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 23 linhas, 11 empresa(s), DATA_REAL de 2020-11-11 a 2026-05-05.
- afastamento_decorrente_de_contaminacao_p: todos os valores reais estão no comentário do banco (0=23).
- Vínculo foafastamentos (FOAFASTAMENTOS): 0 de 1 linhas sem registro relacionado (empresa 147).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| data_numerica_do_afastamento | `data_real_dn` | numeric(10) |  |  | Data numérica do afastamento |
| data_real_dn_afastamento | `data_real_dn_afastamento` | numeric(10) |  |  | Data numérica do afastamento |
| codigo_do_afastamento | `i_afastamentos` | integer(4) |  |  | Código do afastamento |
| data_do_afastamento | `data_real` | date(4) |  |  | Data do afastamento |
| data_final_do_afastamento | `data_fim` | date(4) |  |  | Data final do afastamento |
| linha_selecionada | `selecionado` | integer(4) |  |  | Linha selecionada |
| afastamento_decorrente_de_contaminacao_p | `afastamento_decorrente_contaminacao_coronavirus` | integer(4) |  | foafastamentos_somar_dias_afastamento_ | Afastamento decorrente de contaminação pelo coronavírus (Covid-19) (0 = Não/ 1 = Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foafastamentos` → `FOAFASTAMENTOS` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados` e `data_real_dn` = `data_real_dn`; colunas: `foafastamentos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_numerica_do_afastamento` (eq/in), `data_real_dn_afastamento` (eq/in), `data_do_afastamento` (entre/gte/lte), `data_final_do_afastamento` (entre/gte/lte), `codigo_do_afastamento` (eq/in)

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

### foafastamentos_estabilidade_estabilidad

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_ESTABILIDADE.ESTABILIDADE_CCT estão no comentário do banco (2026-10-18). Distribuição: 1=1.532, 0=36.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foafastamentos_periodo_aquisitivo_onus_da_rem

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_PERIODO_AQUISITIVO.ONUS_REMUNERACAO_MANDATO_SINDICAL estão no comentário do banco (2026-10-18). Distribuição: 2=409, nulo=71.

| Código | Significado |
|---|---|
| 1 | Empregador |
| 2 | Sindicato |
| 3 | Diferença salarial paga pelo sindicato |
| null | Sem dados informado, conversao |

### foafastamentos_dados_eventos_esocial_evento_de_i

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL.EVENTO_INCLUSAO_DATA_FIM_AFASTAMENTO estão no comentário do banco (2026-10-18). Distribuição: 0=30, 1=12.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foafastamentos_dados_eventos_esocial_enviar_para

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=42.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foafastamentos_dados_eventos_esocial_gerar_retif

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=42.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foafastamentos_dados_eventos_esocial_marcacao_do

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_DADOS_EVENTOS_ESOCIAL.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=42.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### foafastamentos_somar_dias_afastamento_

Confirmado: sim

> Todos os valores observados em FOAFASTAMENTOS_SOMAR_DIAS.AFASTAMENTO_DECORRENTE_CONTAMINACAO_CORONAVIRUS estão no comentário do banco (2026-10-18). Distribuição: 0=23.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

