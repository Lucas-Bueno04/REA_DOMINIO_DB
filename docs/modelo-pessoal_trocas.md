# Modelo — Pessoal - trocas (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_trocas.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

15 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fotrocas_campos](#fotrocas_campos) | `fotrocas_campos` | 52.536 | medio | empresa |
| [fotrocas_horas](#fotrocas_horas) | `FOTROCAS_HORAS` | 33.110 | medio | empresa |
| [fotrocas_sindpiso](#fotrocas_sindpiso) | `FOTROCAS_SINDPISO` | 14.289 | medio | empresa |
| [fotrocas_cargos](#fotrocas_cargos) | `fotrocas_cargos` | 13.193 | medio | empresa |
| [fotrocas_ccustos](#fotrocas_ccustos) | `fotrocas_ccustos` | 11.812 | medio | empresa |
| [fotrocas_servicos](#fotrocas_servicos) | `fotrocas_servicos` | 11.405 | medio | empresa |
| [fotrocas_depto](#fotrocas_depto) | `fotrocas_depto` | 11.330 | medio | empresa |
| [fotrocas_filiais](#fotrocas_filiais) | `FOTROCAS_FILIAIS` | 10.975 | medio | empresa |
| [fotrocas_jornadas](#fotrocas_jornadas) | `FOTROCAS_JORNADAS` | 8.979 | pequeno | empresa |
| [fotrocas_sindicatos](#fotrocas_sindicatos) | `fotrocas_sindicatos` | 7.476 | pequeno | empresa |
| [fotrocas_informacoes_pessoais](#fotrocas_informacoes_pessoais) | `FOTROCAS_INFORMACOES_PESSOAIS` | 5.527 | pequeno | empresa |
| [fotrocas_informacoes_profissionais](#fotrocas_informacoes_profissionais) | `FOTROCAS_INFORMACOES_PROFISSIONAIS` | 5.351 | pequeno | empresa |
| [fotrocas_funcoes](#fotrocas_funcoes) | `FOTROCAS_FUNCOES` | 2.175 | pequeno | empresa |
| [fotrocas_operadoraplanosaude](#fotrocas_operadoraplanosaude) | `FOTROCAS_OPERADORAPLANOSAUDE` | 5 | pequeno | empresa |
| [fotrocas_turmas](#fotrocas_turmas) | `fotrocas_turmas` | 4 | pequeno | empresa |

## fotrocas_campos

**Trocas de ocorrencia sefip, simples nacional, categoria** — tabela `fotrocas_campos` (52.536 linhas)

Trocas de ocorrencia sefip, simples nacional, categoria. 52.536 linhas no catálogo; chave: codi_emp, i_empregados, data_troca, tipo_troca.

- **Chave:** `codi_emp, i_empregados, data_troca, tipo_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`, `tipo_troca asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 52.608 linhas, 977 empresa(s), data_troca de 1968-01-29 a 2026-10-20.
- tipo_de_troca_1_categoria_2_ocorrencia_s: todos os valores reais estão no comentário do banco (3=11.023, 4=11.003, 2=10.622, 1=10.392, 5=7.007, 6=2.561).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=52.608).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=52.346, 1=262).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=52.608).
- Vínculo foempregados (foempregados): 0 de 10 linhas sem registro relacionado (empresa 883).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| tipo_de_troca_1_categoria_2_ocorrencia_s | `tipo_troca` | integer(4) |  | fotrocas_campos_tipo_de_tro | Tipo de troca. (1=Categoria/2=Ocorrência SEFIP/3=Simples Nacional/4=Vínculo empregatício/5=Sindicalizado/6=Tipo de serviço/7=Agente integração/8=Instituição de ensino/9=Coordenador de Estágio/10=Supervisor de Estágio/11=Categoria eSocial.) |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| preriodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | Preriodo inicial do empregado |
| preriodo_final_do_empregado | `periodo_fim` | date(4) |  |  | Preriodo final do empregado |
| valor_do_campo | `valor_campo` | char(6) |  |  | Valor do campo |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_campos_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_campos_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_campos_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `tipo_de_troca_1_categoria_2_ocorrencia_s` (eq/in), `preriodo_inicial_do_empregado` (entre/gte/lte), `preriodo_final_do_empregado` (entre/gte/lte), `nome_do_usuario_que_fez_a_troca` (eq/in), `valor_do_campo` (eq/in)

## fotrocas_horas

**Trocas da quantidade de horas trabalhadas pelo empregado.** — tabela `FOTROCAS_HORAS` (33.110 linhas)

Trocas da quantidade de horas trabalhadas pelo empregado.. 33.110 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA, CAMPO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA, CAMPO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_GRAVACAO`
- **Ordem padrão:** `DATA_GRAVACAO desc`, `I_EMPREGADOS asc`, `DATA_TROCA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 33.172 linhas, 439 empresa(s), DATA_GRAVACAO de 1900-01-01 a 2026-10-16.
- campo_alterado_1_horas_dia_2_horas_seman: todos os valores reais estão no comentário do banco (3=8.976, 1=8.976, 2=8.816, 4=6.404).
- retificacao_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=31.069, 1=2.103).
- periodo_de_controle_0_inativo_1_ativo: todos os valores reais estão no comentário do banco (1=32.202, 0=970).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=30.580, 1=2.592).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=33.052, 0=120).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=32.757, 1=415).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=33.172).
- Vínculo foempregados (foempregados): 0 de 16 linhas sem registro relacionado (empresa 9054).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_da_alteracao | `data_troca` | date(4) |  |  | Data da alteração. |
| campo_alterado_1_horas_dia_2_horas_seman | `campo` | smallint(2) |  | fotrocas_horas_campo_alter | Campo alterado. (1=Horas dia/2=Horas semana/3=Horas mês/4=Horas compensadas) |
| valor_alterado | `valor` | numeric(5) |  |  | Valor alterado. |
| data_da_gravacao | `data_gravacao` | date(4) |  |  | Data da gravação. |
| horario_da_gravacao | `horario_gravacao` | time(8) |  |  | Horário da gravação. |
| retificacao_0_nao_1_sim | `retificacao` | smallint(2) |  | fotrocas_horas_retificacao | Retificação. (0=Não/1=Sim) |
| periodo_de_controle_0_inativo_1_ativo | `periodo_ctrl` | smallint(2) |  | fotrocas_horas_periodo_de_ | Período de controle. (0=Inativo/1=Ativo) |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | fotrocas_horas_origem_do_r | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_horas_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_horas_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_horas_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_alteracao` (eq/in), `campo_alterado_1_horas_dia_2_horas_seman` (eq/in), `data_da_gravacao` (entre/gte/lte)

## fotrocas_sindpiso

**TROCAS DOS PISOS DOS SINDICATOS** — tabela `FOTROCAS_SINDPISO` (14.289 linhas)

TROCAS DOS PISOS DOS SINDICATOS. 14.289 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA, TIPO_PISO_SALARIAL.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA, TIPO_PISO_SALARIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TROCA`
- **Ordem padrão:** `DATA_TROCA desc`, `I_EMPREGADOS asc`, `TIPO_PISO_SALARIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14.311 linhas, 436 empresa(s), DATA_TROCA de 1988-10-06 a 2026-10-20.
- tipo_de_piso_salarial_1_normal_2_periodo: todos os valores reais estão no comentário do banco (1=8.285, 2=6.026).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=14.311).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=14.311).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=14.311).
- Vínculo foempregados (foempregados): 0 de 7 linhas sem registro relacionado (empresa 1103).
- Vínculo fosindpiso (FOSINDPISO): 3 de 7 linhas sem registro relacionado (empresa 1103).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | CÓDIGO DA EMPRESA |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | CÓDIGO DO EMPREGADO |
| data_da_troca | `data_troca` | date(4) |  |  | DATA DA TROCA |
| tipo_de_piso_salarial_1_normal_2_periodo | `tipo_piso_salarial` | smallint(2) |  | fotrocas_sindpiso_tipo_de_piso_salar | Tipo de piso salarial. (1=Normal/2=Período do contrato de experiência) |
| codigo_do_sindicato | `i_sindicatos` | integer(4) |  |  | CÓDIGO DO SINDICATO |
| codigo_do_piso_do_sindicato | `i_sindpiso` | integer(4) |  |  | CÓDIGO DO PISO DO SINDICATO |
| usiario | `usuario` | char(15) |  |  | USIÁRIO |
| periodo_de_controle | `periodo_ctrl` | integer(4) |  |  | PERIODO DE CONTROLE |
| periodo_inicial | `periodo_inicio` | date(4) |  |  | PERIODO INICIAL |
| periodo_final | `periodo_fim` | date(4) |  |  | PERIODO FINAL |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_sindpiso_enviar_para_o_esoc | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_sindpiso_gerar_retificacao_ | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_sindpiso_marcacao_do_evento | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `fosindpiso` → `FOSINDPISO` por `i_sindicatos` = `i_sindicatos` e `i_sindpiso` = `i_sindpiso`; colunas: `fosindpiso_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `tipo_de_piso_salarial_1_normal_2_periodo` (eq/in), `periodo_inicial` (entre/gte/lte), `periodo_final` (entre/gte/lte), `codigo_do_sindicato` (eq/in), `codigo_do_piso_do_sindicato` (eq/in), `usiario` (eq/in)

## fotrocas_cargos

**Trocas de cargos** — tabela `fotrocas_cargos` (13.193 linhas)

Trocas de cargos. 13.193 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 13.215 linhas, 977 empresa(s), data_troca de 1968-01-29 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=13.215).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=12.646, 1=569).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=13.215).
- Vínculo foempregados (foempregados): 0 de 2 linhas sem registro relacionado (empresa 9092).
- Vínculo focargos (focargos): 0 de 2 linhas sem registro relacionado (empresa 9092).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_do_cargos | `i_cargos` | integer(4) |  |  | Codigo do cargos |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| codigo_da_empresa_do_cargo | `codi_emp_cargos` | integer(4) |  |  | Código da empresa do cargo. |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_cargos_enviar_para_o_esocial_0_nao_1_sim | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_cargos_gerar_retificacao_para_o_esocial_ | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_cargos_marcacao_do_evento_para_gerar_o_e | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `focargos` → `focargos` por `codi_emp_cargos` = `codi_emp` e `i_cargos` = `i_cargos`; colunas: `focargos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_do_cargos` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in), `codigo_da_empresa_do_cargo` (eq/in)

## fotrocas_ccustos

**Trocas de centro de custos** — tabela `fotrocas_ccustos` (11.812 linhas)

Trocas de centro de custos. 11.812 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.828 linhas, 977 empresa(s), data_troca de 1968-01-29 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=11.828).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=11.828).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=11.828).
- Vínculo foempregados (foempregados): 0 de 2 linhas sem registro relacionado (empresa 640).
- Vínculo foccustos (foccustos): 0 de 2 linhas sem registro relacionado (empresa 640).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_do_c_custos | `i_ccustos` | integer(4) |  |  | Codigo do C.Custos |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_ccustos_enviar_para_o_esocial_0 | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_ccustos_gerar_retificacao_para_ | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_ccustos_marcacao_do_evento_para | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `foccustos` → `foccustos` por `codi_emp` = `codi_emp` e `i_ccustos` = `i_ccustos`; colunas: `foccustos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_do_c_custos` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in)

## fotrocas_servicos

**Trocas de servicos** — tabela `fotrocas_servicos` (11.405 linhas)

Trocas de servicos. 11.405 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.421 linhas, 977 empresa(s), data_troca de 1968-01-29 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=11.421).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=11.348, 1=73).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=11.421).
- Vínculo foservicos (foservicos): 0 de 2 linhas sem registro relacionado (empresa 640).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_do_servicos | `i_servicos` | integer(4) |  |  | Codigo do servicos |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| quantidade_de_horas_trabalhadas_no_prime | `horas_trabalhadas_primeiro_dia` | numeric(5) |  |  | Quantidade de horas trabalhadas no primeiro dia no serviço. |
| quantidade_de_horas_trabalhadas_no_ultim | `horas_trabalhadas_ultimo_dia` | numeric(5) |  |  | Quantidade de horas trabalhadas no último dia no serviço. |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_servicos_enviar_para_o_esocial_0_nao_1_s | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_servicos_gerar_retificacao_para_o_esocia | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_servicos_marcacao_do_evento_para_gerar_o | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| endpoint_utilizado_para_a_exclusao_do_re | `endpoint_exclusao` | varchar(1024) |  |  | Endpoint utilizado para a exclusão do registro. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foservicos` → `foservicos` por `codi_emp` = `codi_emp` e `i_servicos` = `i_servicos`; colunas: `foservicos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_do_servicos` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in), `endpoint_utilizado_para_a_exclusao_do_re` (contem/prefixo)

## fotrocas_depto

**Tabela de trocas de departametos** — tabela `fotrocas_depto` (11.330 linhas)

Tabela de trocas de departametos. 11.330 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11.346 linhas, 977 empresa(s), data_troca de 1968-01-29 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=11.346).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=11.346).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=11.346).
- Vínculo foempregados (foempregados): 0 de 2 linhas sem registro relacionado (empresa 640).
- Vínculo fodepto (fodepto): 0 de 2 linhas sem registro relacionado (empresa 640).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_do_departamento | `i_depto` | integer(4) |  |  | Codigo do departamento |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_depto_enviar_para_o_eso | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_depto_gerar_retificacao | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_depto_marcacao_do_event | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `fodepto` → `fodepto` por `codi_emp` = `codi_emp` e `i_depto` = `i_depto`; colunas: `fodepto_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_do_departamento` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in)

## fotrocas_filiais

**Trocas de filiais.** — tabela `FOTROCAS_FILIAIS` (10.975 linhas)

Trocas de filiais.. 10.975 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TROCA`
- **Ordem padrão:** `DATA_TROCA desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10.991 linhas, 977 empresa(s), DATA_TROCA de 1968-01-29 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=10.991).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=10.991).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=10.991).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca. |
| codigo_da_filial | `i_filiais` | integer(4) |  |  | Código da filial. |
| nome_do_usuario_que_fez_a_troca | `usuario` | varchar(15) |  |  | Nome do usuario que fez a troca. |
| controle_do_periodo_0_inativo_1_ativo | `periodo_ctrl` | smallint(2) |  |  | Controle do período. (0=Inativo/1=Ativo |
| periodo_inicial_de_vigencia_da_troca | `periodo_inicio` | date(4) |  |  | Período inicial de vigência da troca |
| periodo_final_de_vigencia_da_troca | `periodo_fim` | date(4) |  |  | Período final de vigência da troca |
| codigo_da_filial_anterior | `i_filiais_anterior` | integer(4) |  |  | Código da filial anterior. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_filiais_enviar_para_o_esocial_0_nao_1_si | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_filiais_gerar_retificacao_para_o_esocial | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_filiais_marcacao_do_evento_para_gerar_o_ | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_de_vigencia_da_troca` (entre/gte/lte), `periodo_final_de_vigencia_da_troca` (entre/gte/lte), `codigo_da_filial` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in), `codigo_da_filial_anterior` (eq/in)

## fotrocas_jornadas

**Trocas de jornada.** — tabela `FOTROCAS_JORNADAS` (8.979 linhas)

Trocas de jornada.. 8.979 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TROCA`
- **Ordem padrão:** `DATA_TROCA desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8.996 linhas, 439 empresa(s), DATA_TROCA de 1988-10-06 a 2026-10-20.
- controle_do_periodo_0_inativo_1_ativo: todos os valores reais estão no comentário do banco (1=8.971, 0=25).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=8.996).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=8.362, 1=634).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=8.996).
- Vínculo fojornadas (FOJORNADAS): 0 de 4 linhas sem registro relacionado (empresa 9108).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca. |
| codigo_da_jornada | `i_jornada` | integer(4) |  |  | Código da jornada. |
| nome_do_usuario_que_fez_a_troca | `usuario` | varchar(128) |  |  | Nome do usuário que fez a troca |
| controle_do_periodo_0_inativo_1_ativo | `periodo_ctrl` | smallint(2) |  | fotrocas_jornadas_controle_do_periodo_0_inativo_1_ | Controle do período. (0=Inativo/1=Ativo) |
| periodo_inicial | `periodo_inicio` | date(4) |  |  | Período inicial. |
| periodo_final | `periodo_fim` | date(4) |  |  | Período final. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_jornadas_enviar_para_o_esocial_0_nao_1_si | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_jornadas_gerar_retificacao_para_o_esocial | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_jornadas_marcacao_do_evento_para_gerar_o_ | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fojornadas` → `FOJORNADAS` por `codi_emp` = `codi_emp` e `i_jornada` = `i_jornada`; colunas: `fojornadas_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial` (entre/gte/lte), `periodo_final` (entre/gte/lte), `codigo_da_jornada` (eq/in), `nome_do_usuario_que_fez_a_troca` (contem/prefixo)

## fotrocas_sindicatos

**Trocas de sindicatos** — tabela `fotrocas_sindicatos` (7.476 linhas)

Trocas de sindicatos. 7.476 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7.487 linhas, 423 empresa(s), data_troca de 1988-10-06 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=7.487).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=6.844, 1=643).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=7.487).
- Vínculo fosindicatos_cadastro (FOSINDICATOS_CADASTRO): 0 de 4 linhas sem registro relacionado (empresa 9034).
- Vínculo foempregados (foempregados): 0 de 4 linhas sem registro relacionado (empresa 9034).
- Vínculo fosindicatos (fosindicatos): 0 de 4 linhas sem registro relacionado (empresa 9034).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_da_convencao_coletiva | `i_sindicatos` | integer(4) |  |  | Código da convenção coletiva |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_sindicatos_enviar_para_o_esocial_0_nao_1 | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_sindicatos_gerar_retificacao_para_o_esoc | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_sindicatos_marcacao_do_evento_para_gerar | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |
| codigo_do_cadastro_do_sindicato | `i_sindicatos_cadastro` | integer(4) |  |  | Código do cadastro do sindicato |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fosindicatos_cadastro` → `FOSINDICATOS_CADASTRO` por `i_sindicatos_cadastro` = `i_sindicatos_cadastro`; colunas: `fosindicatos_cadastro_nome`
- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `fosindicatos` → `fosindicatos` por `i_sindicatos` = `i_sindicatos`; colunas: `fosindicatos_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_da_convencao_coletiva` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in), `codigo_do_cadastro_do_sindicato` (eq/in)

## fotrocas_informacoes_pessoais

**Alterações das informações pessoais do empregado.** — tabela `FOTROCAS_INFORMACOES_PESSOAIS` (5.527 linhas)

Alterações das informações pessoais do empregado.. 5.527 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, CAMPO, DATA_ALTERACAO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, CAMPO, DATA_ALTERACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_GRAVACAO`
- **Ordem padrão:** `DATA_GRAVACAO desc`, `I_EMPREGADOS asc`, `CAMPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.531 linhas, 157 empresa(s), DATA_GRAVACAO de 2015-06-25 a 2026-10-16.
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=5.531).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=5.531).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=5.506, 1=25).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=5.531).
- Vínculo foempregados (foempregados): 0 de 11 linhas sem registro relacionado (empresa 46).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| campo_alterado | `campo` | smallint(2) |  |  | Campo alterado. |
| data_da_alteracao 🔒 | `data_alteracao` | date(4) |  |  | Data da alteração. |
| valor_anterior_a_alteracao | `de` | varchar(255) |  |  | Valor anterior a alteração. |
| valor_posterior_a_alteracao | `para` | varchar(255) |  |  | Valor posterior a alteração. |
| data_de_gravacao_da_alteracao | `data_gravacao` | date(4) |  |  | Data de gravação da alteração. |
| horario_de_gravacao_da_alteracao | `horario_gravacao` | time(8) |  |  | Horário de gravação da alteração. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | fotrocas_informacoes_pessoais_origem_do_r | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_informacoes_pessoais_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_informacoes_pessoais_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_informacoes_pessoais_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `campo_alterado` (eq/in), `data_da_alteracao` (eq/in), `data_de_gravacao_da_alteracao` (entre/gte/lte), `valor_anterior_a_alteracao` (contem/prefixo), `valor_posterior_a_alteracao` (contem/prefixo)

## fotrocas_informacoes_profissionais

**Alterações das informações profissionais do empregado.** — tabela `FOTROCAS_INFORMACOES_PROFISSIONAIS` (5.351 linhas)

Alterações das informações profissionais do empregado.. 5.351 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, CAMPO, DATA_ALTERACAO.

- **Chave:** `CODI_EMP, I_EMPREGADOS, CAMPO, DATA_ALTERACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_GRAVACAO`
- **Ordem padrão:** `DATA_GRAVACAO desc`, `I_EMPREGADOS asc`, `CAMPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.357 linhas, 312 empresa(s), DATA_GRAVACAO de 2015-08-26 a 2026-10-16.
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=5.357).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=5.357).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=5.354, 1=3).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=5.357).
- Vínculo foempregados (foempregados): 0 de 4 linhas sem registro relacionado (empresa 775).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| campo_alterado | `campo` | smallint(2) |  |  | Campo alterado. |
| data_da_alteracao 🔒 | `data_alteracao` | date(4) |  |  | Data da alteração. |
| valor_anterior_a_alteracao | `de` | varchar(255) |  |  | Valor anterior a alteração. |
| valor_posterior_a_alteracao | `para` | varchar(255) |  |  | Valor posterior a alteração. |
| data_de_gravacao_da_alteracao | `data_gravacao` | date(4) |  |  | Data de gravação da alteração. |
| horario_de_gravacao_da_alteracao | `horario_gravacao` | time(8) |  |  | Horário de gravação da alteração. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | fotrocas_informacoes_profissionais_origem_do_r | Origem do registro (0=Sistema/ 1=Imp Tabelas/ 2=Imp Layout) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_informacoes_profissionais_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_informacoes_profissionais_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_informacoes_profissionais_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `campo_alterado` (eq/in), `data_da_alteracao` (eq/in), `data_de_gravacao_da_alteracao` (entre/gte/lte), `valor_anterior_a_alteracao` (contem/prefixo), `valor_posterior_a_alteracao` (contem/prefixo)

## fotrocas_funcoes

**Trocas de funções** — tabela `FOTROCAS_FUNCOES` (2.175 linhas)

Trocas de funções. 2.175 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TROCA`
- **Ordem padrão:** `DATA_TROCA desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.177 linhas, 14 empresa(s), DATA_TROCA de 2010-11-03 a 2026-10-20.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=2.177).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=2.095, 1=82).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=2.177).
- Vínculo fofuncoes (FOFUNCOES): 0 de 3 linhas sem registro relacionado (empresa 650).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_da_funcao | `i_funcao` | integer(4) |  |  | Codigo da função |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | smallint(2) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_funcoes_enviar_para_o_esocial_0_nao_1_si | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_funcoes_gerar_retificacao_para_o_esocial | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_funcoes_marcacao_do_evento_para_gerar_o_ | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `fofuncoes` → `FOFUNCOES` por `codi_emp` = `codi_emp` e `i_funcao` = `i_funcao`; colunas: `fofuncoes_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_da_funcao` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in)

## fotrocas_operadoraplanosaude

**** SEM USO ** Trocas de operadora de plano de saúde** — tabela `FOTROCAS_OPERADORAPLANOSAUDE` (5 linhas)

** SEM USO ** Trocas de operadora de plano de saúde. 5 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, DATA_TROCA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_TROCA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_TROCA`
- **Ordem padrão:** `DATA_TROCA desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5 linhas, 1 empresa(s), DATA_TROCA de 2005-01-02 a 2005-01-25.
- Colunas expostas nulas em 100% das linhas (1): codigo_da_operadora_do_plano_de_saude.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=5).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=5).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=5).
- Vínculo foempregados (foempregados): 0 de 5 linhas sem registro relacionado (empresa 9999).
- Vínculo fooperadoraplanosaude (FOOPERADORAPLANOSAUDE): 0 de 5 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_da_operadora_do_plano_de_saude | `i_operadoraplanosaude` | integer(4) |  |  | Código da operadora do plano de saúde |
| usuario_que_realizou_a_troca | `usuario` | char(15) |  |  | Usuário que realizou a troca |
| controle_0_inativo_1_ativo | `periodo_ctrl` | smallint(2) |  |  | Controle: 0=Inativo/1=Ativo |
| periodo_inicial | `periodo_inicio` | date(4) |  |  | Período inicial |
| periodo_final | `periodo_fim` | date(4) |  |  | Período final |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | smallint(2) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_operadoraplanosaude_enviar_para | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_operadoraplanosaude_gerar_retif | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_operadoraplanosaude_marcacao_do | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `fooperadoraplanosaude` → `FOOPERADORAPLANOSAUDE` por `i_operadoraplanosaude` = `i_operadoraplanosaude`; colunas: `fooperadoraplanosaude_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial` (entre/gte/lte), `periodo_final` (entre/gte/lte), `codigo_da_operadora_do_plano_de_saude` (eq/in), `usuario_que_realizou_a_troca` (eq/in)

## fotrocas_turmas

**Trocas de cargos** — tabela `fotrocas_turmas` (4 linhas)

Trocas de cargos. 4 linhas no catálogo; chave: codi_emp, i_empregados, data_troca.

- **Chave:** `codi_emp, i_empregados, data_troca`
- **Empresa:** `codi_emp`
- **Período:** `data_troca`
- **Ordem padrão:** `data_troca desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 1 empresa(s), data_troca de 2012-06-01 a 2019-03-18.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=4).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=4).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=4).
- Vínculo foempregados (foempregados): 0 de 4 linhas sem registro relacionado (empresa 9999).
- Vínculo poturmas (poturmas): 0 de 4 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | codigo da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Codigo do empregado |
| data_da_troca | `data_troca` | date(4) |  |  | Data da troca |
| codigo_de_turmas | `i_turmas` | integer(4) |  |  | Codigo de turmas |
| nome_do_usuario_que_fez_a_troca | `usuario` | char(15) |  |  | Nome do usuario que fez a troca |
| controle_do_1_ativo_0_inativo | `periodo_ctrl` | tinyint(1) |  |  | Controle do 1=ativo 0 = inativo |
| periodo_inicial_do_empregado | `periodo_inicio` | date(4) |  |  | periodo inicial do empregado |
| periodo_final_do_empregado | `periodo_fim` | date(4) |  |  | periodo final do empregado |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fotrocas_turmas_enviar_para_o_esocial_0_nao_1_sim | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fotrocas_turmas_gerar_retificacao_para_o_esocial_ | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fotrocas_turmas_marcacao_do_evento_para_gerar_o_e | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `poturmas` → `poturmas` por `codi_emp` = `codi_emp` e `i_turmas` = `i_turmas`; colunas: `poturmas_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `data_da_troca` (eq/in), `periodo_inicial_do_empregado` (entre/gte/lte), `periodo_final_do_empregado` (entre/gte/lte), `codigo_de_turmas` (eq/in), `nome_do_usuario_que_fez_a_troca` (eq/in)

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

### fotrocas_campos_tipo_de_tro

Confirmado: sim

> Todos os valores observados em fotrocas_campos.tipo_troca estão no comentário do banco (2026-10-18). Distribuição: 3=11.023, 4=11.003, 2=10.622, 1=10.392, 5=7.007, 6=2.561.

| Código | Significado |
|---|---|
| 1 | Categoria |
| 2 | Ocorrência SEFIP |
| 3 | Simples Nacional |
| 4 | Vínculo empregatício |
| 5 | Sindicalizado |
| 6 | Tipo de serviço |
| 7 | Agente integração |
| 8 | Instituição de ensino |
| 9 | Coordenador de Estágio |
| 10 | Supervisor de Estágio |
| 11 | Categoria eSocial. |

### fotrocas_campos_enviar_para

Confirmado: sim

> Todos os valores observados em fotrocas_campos.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=52.608.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_campos_gerar_retif

Confirmado: sim

> Todos os valores observados em fotrocas_campos.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=52.346, 1=262.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_campos_marcacao_do

Confirmado: sim

> Todos os valores observados em fotrocas_campos.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=52.608.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_horas_campo_alter

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.CAMPO estão no comentário do banco (2026-10-18). Distribuição: 3=8.976, 1=8.976, 2=8.816, 4=6.404.

| Código | Significado |
|---|---|
| 1 | Horas dia |
| 2 | Horas semana |
| 3 | Horas mês |
| 4 | Horas compensadas |

### fotrocas_horas_retificacao

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.RETIFICACAO estão no comentário do banco (2026-10-18). Distribuição: 0=31.069, 1=2.103.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_horas_periodo_de_

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.PERIODO_CTRL estão no comentário do banco (2026-10-18). Distribuição: 1=32.202, 0=970.

| Código | Significado |
|---|---|
| 0 | Inativo |
| 1 | Ativo |

### fotrocas_horas_origem_do_r

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=30.580, 1=2.592.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

### fotrocas_horas_enviar_para

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=33.052, 0=120.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_horas_gerar_retif

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=32.757, 1=415.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_horas_marcacao_do

Confirmado: sim

> Todos os valores observados em FOTROCAS_HORAS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=33.172.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindpiso_tipo_de_piso_salar

Confirmado: sim

> Todos os valores observados em FOTROCAS_SINDPISO.TIPO_PISO_SALARIAL estão no comentário do banco (2026-10-18). Distribuição: 1=8.285, 2=6.026.

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Período do contrato de experiência |

### fotrocas_sindpiso_enviar_para_o_esoc

Confirmado: sim

> Todos os valores observados em FOTROCAS_SINDPISO.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=14.311.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindpiso_gerar_retificacao_

Confirmado: sim

> Todos os valores observados em FOTROCAS_SINDPISO.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=14.311.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindpiso_marcacao_do_evento

Confirmado: sim

> Todos os valores observados em FOTROCAS_SINDPISO.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=14.311.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_cargos_enviar_para_o_esocial_0_nao_1_sim

Confirmado: sim

> Todos os valores observados em fotrocas_cargos.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=13.215.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_cargos_gerar_retificacao_para_o_esocial_

Confirmado: sim

> Todos os valores observados em fotrocas_cargos.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=12.646, 1=569.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_cargos_marcacao_do_evento_para_gerar_o_e

Confirmado: sim

> Todos os valores observados em fotrocas_cargos.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=13.215.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_ccustos_enviar_para_o_esocial_0

Confirmado: sim

> Todos os valores observados em fotrocas_ccustos.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=11.828.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_ccustos_gerar_retificacao_para_

Confirmado: sim

> Todos os valores observados em fotrocas_ccustos.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.828.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_ccustos_marcacao_do_evento_para

Confirmado: sim

> Todos os valores observados em fotrocas_ccustos.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.828.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_servicos_enviar_para_o_esocial_0_nao_1_s

Confirmado: sim

> Todos os valores observados em fotrocas_servicos.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=11.421.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_servicos_gerar_retificacao_para_o_esocia

Confirmado: sim

> Todos os valores observados em fotrocas_servicos.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.348, 1=73.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_servicos_marcacao_do_evento_para_gerar_o

Confirmado: sim

> Todos os valores observados em fotrocas_servicos.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.421.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_depto_enviar_para_o_eso

Confirmado: sim

> Todos os valores observados em fotrocas_depto.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=11.346.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_depto_gerar_retificacao

Confirmado: sim

> Todos os valores observados em fotrocas_depto.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.346.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_depto_marcacao_do_event

Confirmado: sim

> Todos os valores observados em fotrocas_depto.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=11.346.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_filiais_enviar_para_o_esocial_0_nao_1_si

Confirmado: sim

> Todos os valores observados em FOTROCAS_FILIAIS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=10.991.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_filiais_gerar_retificacao_para_o_esocial

Confirmado: sim

> Todos os valores observados em FOTROCAS_FILIAIS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=10.991.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_filiais_marcacao_do_evento_para_gerar_o_

Confirmado: sim

> Todos os valores observados em FOTROCAS_FILIAIS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=10.991.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_jornadas_controle_do_periodo_0_inativo_1_

Confirmado: sim

> Todos os valores observados em FOTROCAS_JORNADAS.PERIODO_CTRL estão no comentário do banco (2026-10-18). Distribuição: 1=8.971, 0=25.

| Código | Significado |
|---|---|
| 0 | Inativo |
| 1 | Ativo |

### fotrocas_jornadas_enviar_para_o_esocial_0_nao_1_si

Confirmado: sim

> Todos os valores observados em FOTROCAS_JORNADAS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=8.996.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_jornadas_gerar_retificacao_para_o_esocial

Confirmado: sim

> Todos os valores observados em FOTROCAS_JORNADAS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=8.362, 1=634.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_jornadas_marcacao_do_evento_para_gerar_o_

Confirmado: sim

> Todos os valores observados em FOTROCAS_JORNADAS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=8.996.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindicatos_enviar_para_o_esocial_0_nao_1

Confirmado: sim

> Todos os valores observados em fotrocas_sindicatos.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=7.487.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindicatos_gerar_retificacao_para_o_esoc

Confirmado: sim

> Todos os valores observados em fotrocas_sindicatos.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=6.844, 1=643.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_sindicatos_marcacao_do_evento_para_gerar

Confirmado: sim

> Todos os valores observados em fotrocas_sindicatos.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=7.487.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_pessoais_origem_do_r

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PESSOAIS.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=5.531.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

### fotrocas_informacoes_pessoais_enviar_para

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PESSOAIS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=5.531.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_pessoais_gerar_retif

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PESSOAIS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.506, 1=25.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_pessoais_marcacao_do

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PESSOAIS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.531.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_profissionais_origem_do_r

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PROFISSIONAIS.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=5.357.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp Tabelas |
| 2 | Imp Layout |

### fotrocas_informacoes_profissionais_enviar_para

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PROFISSIONAIS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=5.357.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_profissionais_gerar_retif

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PROFISSIONAIS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.354, 1=3.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_informacoes_profissionais_marcacao_do

Confirmado: sim

> Todos os valores observados em FOTROCAS_INFORMACOES_PROFISSIONAIS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.357.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_funcoes_enviar_para_o_esocial_0_nao_1_si

Confirmado: sim

> Todos os valores observados em FOTROCAS_FUNCOES.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=2.177.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_funcoes_gerar_retificacao_para_o_esocial

Confirmado: sim

> Todos os valores observados em FOTROCAS_FUNCOES.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=2.095, 1=82.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_funcoes_marcacao_do_evento_para_gerar_o_

Confirmado: sim

> Todos os valores observados em FOTROCAS_FUNCOES.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=2.177.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_operadoraplanosaude_enviar_para

Confirmado: sim

> Todos os valores observados em FOTROCAS_OPERADORAPLANOSAUDE.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=5.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_operadoraplanosaude_gerar_retif

Confirmado: sim

> Todos os valores observados em FOTROCAS_OPERADORAPLANOSAUDE.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_operadoraplanosaude_marcacao_do

Confirmado: sim

> Todos os valores observados em FOTROCAS_OPERADORAPLANOSAUDE.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=5.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_turmas_enviar_para_o_esocial_0_nao_1_sim

Confirmado: sim

> Todos os valores observados em fotrocas_turmas.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=4.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_turmas_gerar_retificacao_para_o_esocial_

Confirmado: sim

> Todos os valores observados em fotrocas_turmas.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=4.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fotrocas_turmas_marcacao_do_evento_para_gerar_o_e

Confirmado: sim

> Todos os valores observados em fotrocas_turmas.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=4.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

