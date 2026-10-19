# Modelo — Pessoal - vigencias (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_vigencias.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [fovigencias_servico_envios_esocial](#fovigencias_servico_envios_esocial) | `FOVIGENCIAS_SERVICO_ENVIOS_ESOCIAL` | 5.075 | pequeno | empresa |
| [fovigencias_servico](#fovigencias_servico) | `FOVIGENCIAS_SERVICO` | 4.432 | pequeno | empresa |
| [fovigencias_servico_entidades_educativas](#fovigencias_servico_entidades_educativas) | `FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS` | 9 | pequeno | empresa |
| [fovigencias_servico_fornecedores_aquisicao_producao_rural](#fovigencias_servico_fornecedores_aquisicao_producao_rural) | `FOVIGENCIAS_SERVICO_FORNECEDORES_AQUISICAO_PRODUCAO_RURAL` | 6 | pequeno | empresa |

## fovigencias_servico_envios_esocial

**Envios das vigências do cadastro de serviços ao eSocial** — tabela `FOVIGENCIAS_SERVICO_ENVIOS_ESOCIAL` (5.075 linhas)

Envios das vigências do cadastro de serviços ao eSocial. 5.075 linhas no catálogo; chave: codi_emp, i_servicos, VIGENCIA, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS.

- **Chave:** `codi_emp, i_servicos, VIGENCIA, CODI_EMP_DADOS_EVENTOS, I_DADOS_EVENTOS`
- **Empresa:** `codi_emp`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `i_servicos asc`, `CODI_EMP_DADOS_EVENTOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.077 linhas, 725 empresa(s), VIGENCIA de 1973-03-01 a 2026-09-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço |
| data_de_vigencia | `vigencia` | date(4) |  |  | Data de vigência |
| codigo_da_empresa_referente_a_foesocial | `codi_emp_dados_eventos` | integer(4) |  |  | Código da empresa referente a FOESOCIAL_DADOS_EVENTOS |
| codigo_do_evento_referente_a_foesocial_d | `i_dados_eventos` | integer(4) |  |  | Código do evento referente a FOESOCIAL_DADOS_EVENTOS |

**Filtros:** `codigo_do_servico` (eq/in), `data_de_vigencia` (eq/in), `codigo_da_empresa_referente_a_foesocial` (eq/in), `codigo_do_evento_referente_a_foesocial_d` (eq/in)

## fovigencias_servico

**Vigências serviço - Cadastro** — tabela `FOVIGENCIAS_SERVICO` (4.432 linhas)

Vigências serviço - Cadastro. 4.432 linhas no catálogo; chave: codi_emp, i_servicos, VIGENCIA.

- **Chave:** `codi_emp, i_servicos, VIGENCIA`
- **Empresa:** `codi_emp`
- **Período:** `COMPETENCIA_FIM_VIGENCIA`
- **Ordem padrão:** `COMPETENCIA_FIM_VIGENCIA desc`, `i_servicos asc`, `VIGENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.432 linhas, 1.668 empresa(s), COMPETENCIA_FIM_VIGENCIA de 1973-10-16 a 3000-12-31.
- Colunas expostas nulas em 100% das linhas (5): codigo_do_processo_administravivo_judici, scp, codigo_do_processo_administrativo_judici, codigo_do_processo_para_contratacao_de_a, codigo_de_suspensao_do_processo_do_rat.
- tipo_de_inscricao_1_cnpj_2_cpf_3_cei_6_c: todos os valores reais estão no comentário do banco (1=3.934, 2=250, 3=247, 6=1).
- tipo_de_servico_1_empresa_2_obra_propria: todos os valores reais estão no comentário do banco (1=3.649, 4=703, 5=80).
- calcular_inss_empresa_sobre_a_receita_br: todos os valores reais estão no comentário do banco (0=2.589, nulo=1.261, 1=582).
- tipo_de_inscricao_do_contratante_da_empr: todos os valores reais estão no comentário do banco (nulo=4.037, 1=395).
- tipo_de_inscricao_do_proprietario_do_cei: todos os valores reais estão no comentário do banco (nulo=4.045, 1=366, 2=21).
- tipo_de_informacao_da_aliquota_do_aciden: todos os valores reais estão no comentário do banco (2=2.325, 1=2.107).
- tipo_de_caepf_1_contribuinte_individual: todos os valores reais estão no comentário do banco (nulo=4.383, 1=49).
- registro_ponto: todos os valores reais estão no comentário do banco (0=3.746, 1=515, 3=107, 2=52, 5=12).
- contratacao_de_aprendiz_1_dispensado_de: todos os valores reais estão no comentário do banco (1=4.271, 3=161).
- realiza_contratacao_de_aprendiz_por_inte: todos os valores reais estão no comentário do banco (0=4.423, 1=9).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_empresa | `codi_emp` | integer(4) |  |  | Codigo empresa |
| codigo | `i_servicos` | integer(4) |  |  | Codigo |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao_da_vigencia | `descricao` | char(80) |  |  | Descrição da vigência |
| cnpj_cpf_cei 🔒 | `cgc` | char(14) |  |  | CNPJ/CPF/CEI |
| tipo_de_inscricao_1_cnpj_2_cpf_3_cei_6_c | `tipo_insc` | smallint(2) |  | fovigencias_servico_tipo_de_inscricao_1_cnp | Tipo de inscrição (1=CNPJ/2=CPF/3=CEI/6=CAEPF/7=CNO). |
| codigo_terceiro | `codigo_terceiro` | numeric(4) |  |  | Codigo terceiro |
| terceiro | `perc_terceiro` | numeric(5) |  |  | Terceiro(%) |
| inss_empresa | `perc_inss_empresa` | numeric(5) |  |  | INSS Empresa(%) |
| acid_trabalho | `perc_acid_trabalho` | numeric(5) |  |  | Acid. Trabalho(%) |
| codigo_do_sat | `codigo_sat` | numeric(5) |  |  | Codigo do SAT |
| pro_lab_aut | `perc_autonomos` | numeric(5) |  |  | Pro-Lab./Aut.(%) |
| codigo_fpas | `codigo_fpas` | numeric(3) |  |  | Codigo FPAS |
| cnae | `codigo_atividade` | numeric(7) |  |  | CNAE |
| codigo_sefip | `codigo_gfip` | numeric(3) |  |  | Codigo SEFIP |
| codigo_gps | `codigo_gps` | numeric(4) |  |  | Codigo GPS |
| banco | `i_bancos` | integer(4) |  |  | Banco |
| numero | `numero_fgts` | numeric(14) |  |  | Numero |
| endereco 🔒 | `endereco` | char(31) |  |  | Endereco |
| numero_c | `numero` | integer(4) |  |  | Numero |
| bairro 🔒 | `bairro` | char(20) |  |  | Bairro |
| cep 🔒 | `cep` | char(8) |  |  | CEP |
| cidade | `cidade` | char(20) |  |  | Cidade |
| estado | `estado` | char(2) |  |  | UF |
| filial | `i_filiais` | integer(4) |  |  | Filial |
| sequencia | `sequencia_gps` | integer(4) |  |  | Sequencia |
| isencao_filantropia | `filantropia` | numeric(6) |  |  | Isencao Filantropia(%) |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4-Importação eSocial |
| tipo_de_servico_1_empresa_2_obra_propria | `tipo` | integer(4) |  | fovigencias_servico_tipo_de_servico_1_empre | Tipo de serviço. (1=Empresa/2=Obra Própria/3=Cooperativa de trabalho/4=Tomador de serviço/5=Empreitada parcial/6=Empreitada total) |
| codigo_do_municipio | `codi_mun` | integer(4) |  |  | Codigo do municipio |
| codigo_municipio | `codigo_municipio` | integer(4) |  |  | Codigo do municipio |
| codigo_sequencial_fpas | `i_fpas` | integer(4) |  |  | Código Sequencial FPAS |
| calcular_inss_empresa_sobre_a_receita_br | `calcula_inss_empresa_lei_12546` | smallint(2) |  | fovigencias_servico_calcular_inss_empresa_s | Calcular INSS Empresa sobre a receita bruta conforme Lei 12.546/2011: (0=Não/1=Sim) |
| tipo_de_servico_do_tomador_1_cessao_de_m | `tipo_servico_tomador` | smallint(2) |  |  | Tipo de serviço do tomador. (1=Cessão de Mão de Obra, inclusive contratante de cooperativa de trabalho (PJ)/2=Trabalho temporário - substituição de pessoal/3=Trabalho temporário - serviços extraordinários) |
| tipo_de_endereco | `tipo_endereco` | smallint(2) |  |  | Tipo de endereço. |
| complemento_do_endereco 🔒 | `complemento` | varchar(30) |  |  | Complemento do endereço. |
| tipo_de_inscricao_do_contratante_da_empr | `tipo_inscricao_contratante_empreitada_parcial` | smallint(2) |  | fovigencias_servico_tipo_de_inscricao_do_co | Tipo de inscrição do contratante da empreitada parcial. (1=CNPJ/2=CPF) |
| inscricao_do_contratante_da_empreitada_p 🔒 | `inscricao_contratante_empreitada_parcial` | varchar(14) |  |  | Inscrição do contratante da empreitada parcial. |
| nome_do_contratante_da_empreitada_parcia | `nome_contratante_empreitada_parcial` | varchar(100) |  |  | Nome do contratante da empreitada parcial. |
| tipo_de_inscricao_do_proprietario_do_cei | `tipo_inscricao_proprietario_cei_empreitada_parcial` | smallint(2) |  | fovigencias_servico_tipo_de_inscricao_do_pr | Tipo de inscrição do proprietário do CEI da empreitada parcial. (1=CNPJ/2=CPF) |
| inscricao_do_proprietario_do_cei_da_empr 🔒 | `inscricao_proprietario_cei_empreitada_parcial` | varchar(14) |  |  | Inscrição do proprietário do CEI da empreitada parcial. |
| nome_do_proprietario_do_cei_da_empreitad | `nome_proprietario_cei_empreitada_parcial` | varchar(100) |  |  | Nome do proprietário do CEI da empreitada parcial. |
| i_cnae20 | `i_cnae20` | char(15) |  |  | Código do CNAE 2.0. |
| tipo_de_informacao_da_aliquota_do_aciden | `tipo_informacao_aliquota_acidente_trabalho` | smallint(2) |  | fovigencias_servico_tipo_de_informacao_da_a | Tipo de informação da alíquota do acidente de trabalho. (1=Informado/2=Conforme CNAE) |
| codigo_do_processo_administravivo_judici | `i_processo` | integer(4) |  |  | Código do processo administravivo/judicial. |
| scp | `i_scp` | integer(4) |  |  | SCP. |
| ddd_do_telefone 🔒 | `ddd` | varchar(4) |  |  | DDD do telefone. |
| telefone 🔒 | `telefone` | varchar(14) |  |  | Telefone. |
| competencia_fim_da_vigencia | `competencia_fim_vigencia` | date(4) |  |  | Competência fim da vigência. |
| tipo_de_lotacao_esocial | `tipo_lotacao_esocial` | smallint(2) |  |  | Tipo de lotação eSocial. |
| codigo_do_processo_administrativo_judici | `i_processo_terceiros` | integer(4) |  |  | Código do processo administrativo/judicial de terceiros. |
| codigo_caepf | `caepf` | varchar(15) |  |  | Código CAEPF. |
| tipo_de_caepf_1_contribuinte_individual | `tipo_caepf` | smallint(2) |  | fovigencias_servico_tipo_de_caepf_1_contrib | Tipo de CAEPF. (1=Contribuinte individual/2=Produtor rural/3=Segurado especial) |
| registro_ponto | `registro_ponto` | smallint(2) |  | fovigencias_servico_registro_ponto_0_nao_ut | Registro ponto. (0=Não utiliza/1=Manual/2=Mecânico/3=Eletrônico/4=Não eletrônico/5=Eletrônico alternativo/6=Eletrônico outros) |
| contratacao_de_aprendiz_1_dispensado_de | `contratacao_aprendiz` | smallint(2) |  | fovigencias_servico_contratacao_de_aprendiz | Contratação de aprendiz. (1=Dispensado, de acordo com a lei/2=Dispensado, mesmo que parcialmente, em virtude de processo judicial/3=Obrigado) |
| codigo_do_processo_para_contratacao_de_a | `i_processo_contratacao_aprendiz` | integer(4) |  |  | Código do processo para contratação de aprendiz. |
| realiza_contratacao_de_aprendiz_por_inte | `realiza_contratacao_aprendiz_intermedio_entidade_educativa_sem_fins_lucrativos` | smallint(2) |  | fovigencias_servico_realiza_contratacao_de_ | Realiza contratação de aprendiz por intermédio de entidade educativa sem fins lucrativos. (0=Não/1=Sim) |
| codigo_de_suspensao_do_processo_do_rat | `codigo_suspensao_processo_rat` | varchar(14) |  |  | Código de suspensão do processo do RAT. |
| soma_do_percentual_de_codigos_de_suspens 🔒 | `soma_codigos_suspensao_terceiros` | numeric(5) |  |  | Soma do percentual de códigos de suspensão de terceiros. |
| percentual_bruto_de_terceiros | `percentual_terceiro_bruto` | numeric(5) |  |  | Percentual bruto de terceiros. |

**Filtros:** `codigo` (eq/in), `vigencia` (eq/in), `competencia_fim_da_vigencia` (entre/gte/lte), `descricao_da_vigencia` (contem/prefixo), `cnpj_cpf_cei` (eq/in), `tipo_de_inscricao_1_cnpj_2_cpf_3_cei_6_c` (eq/in), `banco` (eq/in), `endereco` (contem/prefixo), `bairro` (eq/in), `cep` (eq/in), `cidade` (eq/in), `estado` (eq/in), `filial` (eq/in), `tipo_de_servico_1_empresa_2_obra_propria` (eq/in)

## fovigencias_servico_entidades_educativas

**Entidades educativas para contratação de aprendiz no cadastro de serviços.** — tabela `FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS` (9 linhas)

Entidades educativas para contratação de aprendiz no cadastro de serviços.. 9 linhas no catálogo; chave: CODI_EMP, I_SERVICOS, VIGENCIA, SEQUENCIAL.

- **Chave:** `CODI_EMP, I_SERVICOS, VIGENCIA, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `I_SERVICOS asc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas, 2 empresa(s), VIGENCIA de 1989-06-01 a 2019-01-01.
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=9).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=9).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=9).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| vigencia | `vigencia` | date(4) |  |  | Vigência. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| nome_da_entidade_educativa | `nome` | varchar(50) |  |  | Nome da entidade educativa. |
| cnpj_da_entidade_educativa 🔒 | `cnpj` | varchar(14) |  |  | CNPJ da entidade educativa. |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | fovigencias_servico_entidades_educativas_enviar_para_ | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | fovigencias_servico_entidades_educativas_gerar_retifi | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | fovigencias_servico_entidades_educativas_marcacao_do_ | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Filtros:** `codigo_do_servico` (eq/in), `vigencia` (eq/in), `sequencial` (eq/in), `nome_da_entidade_educativa` (contem/prefixo), `cnpj_da_entidade_educativa` (eq/in)

## fovigencias_servico_fornecedores_aquisicao_producao_rural

**Fornecedores para importar notas fiscais de produção rural.** — tabela `FOVIGENCIAS_SERVICO_FORNECEDORES_AQUISICAO_PRODUCAO_RURAL` (6 linhas)

Fornecedores para importar notas fiscais de produção rural.. 6 linhas no catálogo; chave: CODI_EMP, I_SERVICOS, VIGENCIA, CODI_FOR, SEQUENCIAL, CODI_EMP_FOR.

- **Chave:** `CODI_EMP, I_SERVICOS, VIGENCIA, CODI_FOR, SEQUENCIAL, CODI_EMP_FOR`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIO`
- **Ordem padrão:** `COMPETENCIA_INICIO desc`, `I_SERVICOS asc`, `VIGENCIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s), COMPETENCIA_INICIO de 2021-01-01 a 2026-01-01.
- Colunas expostas nulas em 100% das linhas (1): competencia_fim.
- determinar_fim_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=6).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=6).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_servico | `i_servicos` | integer(4) |  |  | Código do serviço. |
| vigencia | `vigencia` | date(4) |  |  | Vigência. |
| codigo_do_fornecedor | `codi_for` | integer(4) |  |  | Código do fornecedor. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial. |
| codigo_empresa_fornecedor | `codi_emp_for` | integer(4) |  |  | Codigo empresa fornecedor. |
| competencia_inicio | `competencia_inicio` | date(4) |  |  | Competência início. |
| determinar_fim_0_nao_1_sim | `determinar_fim` | smallint(2) |  | fovigencias_servico_fornecedores_aquisicao_producao_rural_determinar_ | Determinar fim. (0=Não/1=Sim) |
| competencia_fim | `competencia_fim` | date(4) |  |  | Competência fim. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | fovigencias_servico_fornecedores_aquisicao_producao_rural_origem_do_r | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |

**Filtros:** `codigo_do_servico` (eq/in), `vigencia` (eq/in), `codigo_do_fornecedor` (eq/in), `sequencial` (eq/in), `codigo_empresa_fornecedor` (eq/in), `competencia_inicio` (entre/gte/lte), `competencia_fim` (entre/gte/lte)

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

### fovigencias_servico_tipo_de_inscricao_1_cnp

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.tipo_insc estão no comentário do banco (2026-10-18). Distribuição: 1=3.934, 2=250, 3=247, 6=1.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |
| 3 | CEI |
| 6 | CAEPF |
| 7 | CNO |

### fovigencias_servico_tipo_de_servico_1_empre

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.tipo estão no comentário do banco (2026-10-18). Distribuição: 1=3.649, 4=703, 5=80.

| Código | Significado |
|---|---|
| 1 | Empresa |
| 2 | Obra Própria |
| 3 | Cooperativa de trabalho |
| 4 | Tomador de serviço |
| 5 | Empreitada parcial |
| 6 | Empreitada total |

### fovigencias_servico_calcular_inss_empresa_s

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.CALCULA_INSS_EMPRESA_LEI_12546 estão no comentário do banco (2026-10-18). Distribuição: 0=2.589, nulo=1.261, 1=582.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_tipo_de_inscricao_do_co

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.TIPO_INSCRICAO_CONTRATANTE_EMPREITADA_PARCIAL estão no comentário do banco (2026-10-18). Distribuição: nulo=4.037, 1=395.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |

### fovigencias_servico_tipo_de_inscricao_do_pr

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.TIPO_INSCRICAO_PROPRIETARIO_CEI_EMPREITADA_PARCIAL estão no comentário do banco (2026-10-18). Distribuição: nulo=4.045, 1=366, 2=21.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |

### fovigencias_servico_tipo_de_informacao_da_a

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.TIPO_INFORMACAO_ALIQUOTA_ACIDENTE_TRABALHO estão no comentário do banco (2026-10-18). Distribuição: 2=2.325, 1=2.107.

| Código | Significado |
|---|---|
| 1 | Informado |
| 2 | Conforme CNAE |

### fovigencias_servico_tipo_de_caepf_1_contrib

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.TIPO_CAEPF estão no comentário do banco (2026-10-18). Distribuição: nulo=4.383, 1=49.

| Código | Significado |
|---|---|
| 1 | Contribuinte individual |
| 2 | Produtor rural |
| 3 | Segurado especial |

### fovigencias_servico_registro_ponto_0_nao_ut

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.REGISTRO_PONTO estão no comentário do banco (2026-10-18). Distribuição: 0=3.746, 1=515, 3=107, 2=52, 5=12.

| Código | Significado |
|---|---|
| 0 | Não utiliza |
| 1 | Manual |
| 2 | Mecânico |
| 3 | Eletrônico |
| 4 | Não eletrônico |
| 5 | Eletrônico alternativo |
| 6 | Eletrônico outros |

### fovigencias_servico_contratacao_de_aprendiz

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.CONTRATACAO_APRENDIZ estão no comentário do banco (2026-10-18). Distribuição: 1=4.271, 3=161.

| Código | Significado |
|---|---|
| 1 | Dispensado, de acordo com a lei |
| 2 | Dispensado, mesmo que parcialmente, em virtude de processo judicial |
| 3 | Obrigado |

### fovigencias_servico_realiza_contratacao_de_

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO.REALIZA_CONTRATACAO_APRENDIZ_INTERMEDIO_ENTIDADE_EDUCATIVA_SEM_FINS_LUCRATIVOS estão no comentário do banco (2026-10-18). Distribuição: 0=4.423, 1=9.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_entidades_educativas_enviar_para_

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=9.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_entidades_educativas_gerar_retifi

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=9.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_entidades_educativas_marcacao_do_

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO_ENTIDADES_EDUCATIVAS.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=9.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_fornecedores_aquisicao_producao_rural_determinar_

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO_FORNECEDORES_AQUISICAO_PRODUCAO_RURAL.DETERMINAR_FIM estão no comentário do banco (2026-10-18). Distribuição: 0=6.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### fovigencias_servico_fornecedores_aquisicao_producao_rural_origem_do_r

Confirmado: sim

> Todos os valores observados em FOVIGENCIAS_SERVICO_FORNECEDORES_AQUISICAO_PRODUCAO_RURAL.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=6.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

