# Modelo — Contábil - parmto (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/contabil_parmto.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

11 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [ctparmto_sped_vigencia](#ctparmto_sped_vigencia) | `CTPARMTO_SPED_VIGENCIA` | 1.484 | pequeno | empresa |
| [ctparmto_dere_vigencia](#ctparmto_dere_vigencia) | `CTPARMTO_DERE_VIGENCIA` | 1.427 | pequeno | empresa |
| [ctparmto_dados_sped_contabil_signatario](#ctparmto_dados_sped_contabil_signatario) | `CTPARMTO_DADOS_SPED_CONTABIL_SIGNATARIO` | 1.203 | pequeno | empresa |
| [ctparmto_periodo_trabalho_usuario](#ctparmto_periodo_trabalho_usuario) | `CTPARMTO_PERIODO_TRABALHO_USUARIO` | 213 | pequeno | empresa |
| [ctparmto_cmv_estoque](#ctparmto_cmv_estoque) | `CTPARMTO_CMV_ESTOQUE` | 62 | pequeno | empresa |
| [ctparmto_cmv_estoque_grupo](#ctparmto_cmv_estoque_grupo) | `CTPARMTO_CMV_ESTOQUE_GRUPO` | 8 | pequeno | empresa |
| [ctparmto_filial_api_conta_azul](#ctparmto_filial_api_conta_azul) | `CTPARMTO_FILIAL_API_CONTA_AZUL` | 6 | pequeno | empresa |
| [ctparmto_contas_iceberg](#ctparmto_contas_iceberg) | `CTPARMTO_CONTAS_ICEBERG` | 4 | pequeno | empresa |
| [ctparmto_cpv_estoque](#ctparmto_cpv_estoque) | `CTPARMTO_CPV_ESTOQUE` | 3 | pequeno | empresa |
| [ctparmto_permitir_mesma_classificacao](#ctparmto_permitir_mesma_classificacao) | `CTPARMTO_PERMITIR_MESMA_CLASSIFICACAO` | 2 | pequeno | empresa |
| [ctparmto_cmv_estoque_grupo_selecao](#ctparmto_cmv_estoque_grupo_selecao) | `CTPARMTO_CMV_ESTOQUE_GRUPO_SELECAO` | 1 | pequeno | empresa |

## ctparmto_sped_vigencia

**Parâmetros Contabilidade - Vigência da guia Dados SPED** — tabela `CTPARMTO_SPED_VIGENCIA` (1.484 linhas)

Parâmetros Contabilidade - Vigência da guia Dados SPED. 1.484 linhas no catálogo; chave: CODI_EMP, VIGENCIA.

- **Chave:** `CODI_EMP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.484 linhas, 1.358 empresa(s), VIGENCIA de 2014-01-01 a 2025-08-01.
- plano_referencial_sped_ecf: todos os valores reais estão no comentário do banco (5=931, 1=479, 3=74).
- tipo_de_atividade_g_atividade_geral_r_at: todos os valores reais estão no comentário do banco (A=804, G=679, R=1).
- forma_de_tributacao_do_lucro_1_lucro_rea: valores reais fora do comentário do banco (9=70, 8=6); tratar o domínio como hipótese.
- periodo_de_apuracao_do_irpj_e_csll_t_tri: todos os valores reais estão no comentário do banco (T=800, A=684).
- forma_de_tributacao_do_trimestre_1_1_luc: todos os valores reais estão no comentário do banco (1=1.484).
- forma_tributacao_trimestre_2: todos os valores reais estão no comentário do banco (1=1.484).
- forma_tributacao_trimestre_3: todos os valores reais estão no comentário do banco (1=1.484).
- forma_tributacao_trimestre_4: todos os valores reais estão no comentário do banco (1=1.484).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| vigencia | `vigencia` | date(4) |  |  | Vigência |
| descricao | `descricao` | varchar(80) |  |  | Descrição |
| plano_referencial_sped_ecf | `plano_referencial_sped_ecf` | integer(4) |  | ctparmto_sped_vigencia_sped_ecf_sp | SPED ECF/SPED CONTÁBIL - A PARTIR DE 2014 (1-PESSOA JURÍDICA EM GERAL - LUCRO REAL / 2-PESSOA JURÍDICA FINANCEIRA / 3-IMUNES E ISENTAS EM GERAL / 4-PARTIDOS POLÍTICOS / 5-PESSOA JURÍDICA EM GERAL - LUCRO PRESUMIDO / 8-ENTIDADES / 9- SEGURADORAS OU ENTIDADES ABERTAS DE PREVIDÊNCIA COMPLEMENTAR / 10-PESSOA JURÍDICA FINANCEIRA - LUCRO PRESUMIDO / 11-TEF TRIBUTAÇÃO ESPECÍFICA DO FUTEBOL) |
| tipo_de_escrituracao | `tipo_escrituracao` | char(1) |  |  | Tipo de Escrituração |
| data_em_formato_integer_para_otimizar_in | `vigencia_busca` | integer(4) |  |  | DATA EM FORMATO INTEGER PARA OTIMIZAR INFORMATIVO ECF |
| tipo_de_atividade_g_atividade_geral_r_at | `tipo_atividade` | char(1) |  | ctparmto_sped_vigencia_tipo_de_ati | Tipo de atividade(G=Atividade Geral/R=Atividade Rural/A=Ambos) |
| forma_de_tributacao_do_lucro_1_lucro_rea | `forma_tributacao` | integer(4) |  | ctparmto_sped_vigencia_forma_de_tr | FORMA DE TRIBUTAÇÃO DO LUCRO (1 - LUCRO REAL / 2 - LUCRO REAL/ARBITRADO / 3 - LUCRO PRESUMIDO/REAL / 5 - LUCRO PRESUMIDO / 6 - LUCRO ARBITRADO / 7 - LUCRO PRESUMIDO/ARBITRADO / 8 - IMUNE DE IRPJ / 9 - ISENTO DO IRPJ / 10 - TEF - TRIBUTAÇÃO ESPECÍFICA DO FUTEBOL) |
| periodo_de_apuracao_do_irpj_e_csll_t_tri | `periodo_apuracao_irpj_csll` | char(1) |  | ctparmto_sped_vigencia_periodo_de_ | Período de apuração do IRPJ e CSLL (T - Trimestral / A - Anual) |
| forma_de_tributacao_do_trimestre_1_1_luc | `forma_tributacao_trimestre_1` | integer(4) |  | ctparmto_sped_vigencia_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_2 | `forma_tributacao_trimestre_2` | integer(4) |  | ctparmto_sped_vigencia_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_3 | `forma_tributacao_trimestre_3` | integer(4) |  | ctparmto_sped_vigencia_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |
| forma_tributacao_trimestre_4 | `forma_tributacao_trimestre_4` | integer(4) |  | ctparmto_sped_vigencia_forma_de_tr | FORMA DE TRIBUTAÇÃO DO TRIMESTRE 1 (1 - LUCRO REAL / 5 - LUCRO PRESUMIDO / 6 - ARBITRADO) |

**Filtros:** `vigencia` (eq/in), `descricao` (contem/prefixo), `tipo_de_escrituracao` (eq/in), `tipo_de_atividade_g_atividade_geral_r_at` (eq/in), `periodo_de_apuracao_do_irpj_e_csll_t_tri` (eq/in)

## ctparmto_dere_vigencia

**Parametros Contabilidade - Vigencia da guia Informativos/DeRE** — tabela `CTPARMTO_DERE_VIGENCIA` (1.427 linhas)

Parametros Contabilidade - Vigencia da guia Informativos/DeRE. 1.427 linhas no catálogo; chave: CODI_EMP, VIGENCIA.

- **Chave:** `CODI_EMP, VIGENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.427 linhas, 1.427 empresa(s), VIGENCIA de 2026-10-01 a 2026-10-01.
- encerramento_contabil_a_anual_s_semestra: todos os valores reais estão no comentário do banco (A=1.427).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| vigencia | `vigencia` | date(4) |  |  | Vigencia |
| descricao | `descricao` | varchar(80) |  |  | Descricao |
| plano_referencial_1_banco_central_cosif | `plano_referencial` | integer(4) |  |  | Plano referencial (1-Banco Central (COSIF) / 2-ANS - Agencia Nacional de Saude Suplementar / 3-SUSEP - Superintendencia de Seguros Privados / 4-SPED) |
| encerramento_contabil_a_anual_s_semestra | `encerramento_contabil` | char(1) |  | ctparmto_dere_vigencia_encerrament | Encerramento contabil (A-Anual / S-Semestral / Q-Quadrimestral / T-Trimestral / B-Bimestral / M-Mensal) |
| vigencia_no_formato_aaaamm_para_navegaca | `vigencia_busca` | integer(4) |  |  | Vigencia no formato AAAAMM para navegacao entre vigencias sem varredura |

**Filtros:** `vigencia` (eq/in), `descricao` (contem/prefixo), `encerramento_contabil_a_anual_s_semestra` (eq/in)

## ctparmto_dados_sped_contabil_signatario

**Dados da Assinaturas do registro J930 do SPED CONTABIL** — tabela `CTPARMTO_DADOS_SPED_CONTABIL_SIGNATARIO` (1.203 linhas)

Dados da Assinaturas do registro J930 do SPED CONTABIL. 1.203 linhas no catálogo; chave: CODI_EMP, CODI_SIGNATARIO.

- **Chave:** `CODI_EMP, CODI_SIGNATARIO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VALIDADE_CPRC`
- **Ordem padrão:** `DATA_VALIDADE_CPRC desc`, `CODI_SIGNATARIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.203 linhas, 601 empresa(s), DATA_VALIDADE_CPRC de 2026-08-16 a 2026-08-16.
- responsavel_pela_assinatura_s_sim_n_nao: todos os valores reais estão no comentário do banco (N=653, S=550).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `codi_signatario` | integer(4) |  |  | Sequencial |
| cpf_ou_cnpj_do_signatario 🔒 | `cpf_cnpj` | varchar(14) |  |  | CPF ou CNPJ do Signatário |
| nome_do_signatario | `nome_signatario` | varchar(255) |  |  | Nome do signatário |
| codigo_fk_para_a_tabela_ctsped_signatari | `i_qualificacao` | integer(4) |  |  | Código FK para a tabela CTSPED_SIGNATARIO_QUALIFICACAO |
| crc_do_signatario | `crc_contabilista` | varchar(120) |  |  | CRC do signatário |
| data_de_validade_do_crc | `data_validade_cprc` | date(4) |  |  | Data de validade do CRC |
| crc_do_expedidor | `crc_expedidor` | varchar(120) |  |  | CRC do expedidor |
| sequencial_do_crc | `sequencial_crc` | varchar(120) |  |  | Sequencial do CRC |
| telefone_do_signatario 🔒 | `telefone_signatario` | varchar(14) |  |  | Telefone do signatário |
| email_signatario 🔒 | `email_signatario` | varchar(150) |  |  | Email signatário |
| responsavel_pela_assinatura_s_sim_n_nao | `responsavel_assinatura` | char(1) |  | ctparmto_dados_sped_contabil_signatario_responsavel_ | Responsável pela assinatura (S - Sim / N - Não) |

**Filtros:** `sequencial` (eq/in), `data_de_validade_do_crc` (entre/gte/lte), `cpf_ou_cnpj_do_signatario` (eq/in), `nome_do_signatario` (contem/prefixo), `codigo_fk_para_a_tabela_ctsped_signatari` (eq/in), `crc_do_signatario` (contem/prefixo), `crc_do_expedidor` (contem/prefixo), `sequencial_do_crc` (contem/prefixo), `telefone_do_signatario` (eq/in), `email_signatario` (contem/prefixo), `responsavel_pela_assinatura_s_sim_n_nao` (eq/in)

## ctparmto_periodo_trabalho_usuario

**Parametros - Período de trabalho por usuário** — tabela `CTPARMTO_PERIODO_TRABALHO_USUARIO` (213 linhas)

Parametros - Período de trabalho por usuário. 213 linhas no catálogo; chave: CODI_EMP, I_PERIODO.

- **Chave:** `CODI_EMP, I_PERIODO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_PERIODO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 213 linhas, 5 empresa(s).
- Vínculo ctparmto (ctparmto): 0 de 41 linhas sem registro relacionado (empresa 812).
- Vínculo usconfusuario (usConfUsuario): 0 de 41 linhas sem registro relacionado (empresa 812).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_periodo` | integer(4) |  |  | Sequencial |
| codigo_do_responsavel | `i_responsavel` | integer(4) |  |  | Código do responsável |
| responsavel_tipo | `responsavel_tipo` | smallint(2) |  |  | Tipo do responsável (Fixo 1) |
| acao_do_periodo_de_trabalho_l_livre_a_av | `acao` | char(1) |  |  | Ação do período de trabalho (L=Livre, A=Avisar N=Não permitir) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctparmto` → `ctparmto` por `codi_emp` = `codi_emp`; colunas: `ctparmto_nome`
- `usconfusuario` → `usConfUsuario` por `responsavel_tipo` = `tipo` e `i_responsavel` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `sequencial` (eq/in), `codigo_do_responsavel` (eq/in), `responsavel_tipo` (eq/in), `acao_do_periodo_de_trabalho_l_livre_a_av` (eq/in)

## ctparmto_cmv_estoque

**Parametros - CMV Contas de estoque** — tabela `CTPARMTO_CMV_ESTOQUE` (62 linhas)

Parametros - CMV Contas de estoque. 62 linhas no catálogo; chave: CODI_EMP, I_CONTA.

- **Chave:** `CODI_EMP, I_CONTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 62 linhas, 24 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 10111).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_conta` | integer(4) |  |  | Sequencial |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `conta_contabil` (eq/in)

## ctparmto_cmv_estoque_grupo

**Parametros - CMV Contas de estoque - Grupos de produtos** — tabela `CTPARMTO_CMV_ESTOQUE_GRUPO` (8 linhas)

Parametros - CMV Contas de estoque - Grupos de produtos. 8 linhas no catálogo; chave: CODI_EMP, I_CONTA, I_FILIAL.

- **Chave:** `CODI_EMP, I_CONTA, I_FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONTA asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 8 empresa(s).
- grupos_de_produtos_s_selecionar_t_todos: todos os valores reais estão no comentário do banco (T=8).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 10103).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_estoque | `i_conta` | integer(4) |  |  | Código estoque |
| sequencial | `i_filial` | integer(4) |  |  | Sequencial |
| filial | `codi_emp_filial` | integer(4) |  |  | Filial |
| grupos_de_produtos_s_selecionar_t_todos | `grupo_produto` | char(1) |  | ctparmto_cmv_estoque_grupo_grupos_de_p | Grupos de produtos (S=Selecionar/ T=Todos) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp_filial` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `codigo_estoque` (eq/in), `sequencial` (eq/in), `filial` (eq/in), `grupos_de_produtos_s_selecionar_t_todos` (eq/in)

## ctparmto_filial_api_conta_azul

**Seleção de empresas filiais para o envio api conta azul** — tabela `CTPARMTO_FILIAL_API_CONTA_AZUL` (6 linhas)

Seleção de empresas filiais para o envio api conta azul. 6 linhas no catálogo; chave: CODIGO, CODI_EMP.

- **Chave:** `CODIGO, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 6 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| prima_key_com_autoincrement | `codigo` | integer(4) |  |  | Prima key com autoincrement |
| empresa_principal_de_parametro | `codi_emp` | integer(4) |  |  | Empresa principal de parametro |
| verifica_se_a_empresa_e_habilitada | `habilitar` | char(1) |  |  | Verifica se a empresa é habilitada |
| codigo_empresa_filial | `codigo_empresa_filial` | integer(4) |  |  | Verifica se a empresa é habilitada |

**Filtros:** `prima_key_com_autoincrement` (eq/in), `verifica_se_a_empresa_e_habilitada` (eq/in), `codigo_empresa_filial` (eq/in)

## ctparmto_contas_iceberg

**Parâmetrização de contas Contabilidade Digital** — tabela `CTPARMTO_CONTAS_ICEBERG` (4 linhas)

Parâmetrização de contas Contabilidade Digital. 4 linhas no catálogo; chave: CODI_EMP, CODI_FIL, I_BANCO.

- **Chave:** `CODI_EMP, CODI_FIL, I_BANCO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_INICIO_INTEGRACAO`
- **Ordem padrão:** `DATA_INICIO_INTEGRACAO desc`, `CODI_FIL asc`, `I_BANCO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas, 3 empresa(s), DATA_INICIO_INTEGRACAO de 2024-11-25 a 2024-11-25.
- Vínculo ctparmto (ctparmto): 0 de 1 linhas sem registro relacionado (empresa 841).
- Vínculo geatendimento_contas_ice (GEATENDIMENTO_CONTAS_ICEBERG): 0 de 1 linhas sem registro relacionado (empresa 841).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_da_filial | `codi_fil` | integer(4) |  |  | Código da filial |
| codigo_de_identificacao_do_banco | `i_banco` | integer(4) |  |  | Codigo de identificacão do banco |
| codigo_da_conta_contabil | `codi_cta` | integer(4) |  |  | Código da conta contábil |
| data_inicial_para_busca_de_dados_de_extr | `data_inicio_integracao` | date(4) |  |  | DATA INICIAL PARA BUSCA DE DADOS DE EXTRATO BANCÁRIO. |
| saldo_inicial | `saldo_inicial` | decimal(13) |  |  | Saldo Inicial |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctparmto` → `ctparmto` por `codi_emp` = `codi_emp`; colunas: `ctparmto_nome`
- `geatendimento_contas_ice` → `GEATENDIMENTO_CONTAS_ICEBERG` por `codi_fil` = `codi_emp` e `i_banco` = `i_banco`; colunas: `geatendimento_contas_ice_nome`

**Filtros:** `codigo_da_filial` (eq/in), `codigo_de_identificacao_do_banco` (eq/in), `data_inicial_para_busca_de_dados_de_extr` (entre/gte/lte), `codigo_da_conta_contabil` (eq/in)

## ctparmto_cpv_estoque

**Parâmetros - CPV Contas de estoque** — tabela `CTPARMTO_CPV_ESTOQUE` (3 linhas)

Parâmetros - CPV Contas de estoque. 3 linhas no catálogo; chave: CODI_EMP, I_CONTA.

- **Chave:** `CODI_EMP, I_CONTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 3 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9993).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_conta` | integer(4) |  |  | Sequencial |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `conta_contabil` (eq/in)

## ctparmto_permitir_mesma_classificacao

**Parametros - Contas que poderão ter as contas analíticas cadastradas com a mesma classificação** — tabela `CTPARMTO_PERMITIR_MESMA_CLASSIFICACAO` (2 linhas)

Parametros - Contas que poderão ter as contas analíticas cadastradas com a mesma classificação. 2 linhas no catálogo; chave: CODI_EMP, I_CONTA.

- **Chave:** `CODI_EMP, I_CONTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s).
- Vínculo ctparmto (ctparmto): 0 de 2 linhas sem registro relacionado (empresa 10001).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_conta` | integer(4) |  |  | Sequencial |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `ctparmto` → `ctparmto` por `codi_emp` = `codi_emp`; colunas: `ctparmto_nome`

**Filtros:** `sequencial` (eq/in), `conta_contabil` (eq/in)

## ctparmto_cmv_estoque_grupo_selecao

**Parametros - CMV Contas de estoque - Grupos de produtos - Seleção** — tabela `CTPARMTO_CMV_ESTOQUE_GRUPO_SELECAO` (1 linhas)

Parametros - CMV Contas de estoque - Grupos de produtos - Seleção. 1 linhas no catálogo; chave: CODI_EMP, I_CONTA, I_FILIAL, I_GRUPO.

- **Chave:** `CODI_EMP, I_CONTA, I_FILIAL, I_GRUPO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONTA asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo efgrupopdi (efgrupopdi): 0 de 1 linhas sem registro relacionado (empresa 10101).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_estoque | `i_conta` | integer(4) |  |  | Código estoque |
| codigo_filial | `i_filial` | integer(4) |  |  | Código filial |
| sequencial | `i_grupo` | integer(4) |  |  | Sequencial |
| empresa_do_grupo_de_produto | `codi_emp_grupo` | integer(4) |  |  | Empresa do grupo de produto |
| grupo_de_produto | `codi_gru` | integer(4) |  |  | Grupo de produto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efgrupopdi` → `efgrupopdi` por `codi_emp_grupo` = `codi_emp` e `codi_gru` = `codi_gru`; colunas: `efgrupopdi_nome`

**Filtros:** `codigo_estoque` (eq/in), `codigo_filial` (eq/in), `sequencial` (eq/in), `empresa_do_grupo_de_produto` (eq/in), `grupo_de_produto` (eq/in)

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

### ctparmto_sped_vigencia_sped_ecf_sp

Confirmado: sim

> Todos os valores observados em CTPARMTO_SPED_VIGENCIA.PLANO_REFERENCIAL_SPED_ECF estão no comentário do banco (2026-10-18). Distribuição: 5=931, 1=479, 3=74.

| Código | Significado |
|---|---|
| 1 | PESSOA JURÍDICA EM GERAL - LUCRO REAL |
| 2 | PESSOA JURÍDICA FINANCEIRA |
| 3 | IMUNES E ISENTAS EM GERAL |
| 4 | PARTIDOS POLÍTICOS |
| 5 | PESSOA JURÍDICA EM GERAL - LUCRO PRESUMIDO |
| 8 | ENTIDADES |
| 9 | SEGURADORAS OU ENTIDADES ABERTAS DE PREVIDÊNCIA COMPLEMENTAR |
| 10 | PESSOA JURÍDICA FINANCEIRA - LUCRO PRESUMIDO |
| 11 | TEF TRIBUTAÇÃO ESPECÍFICA DO FUTEBOL |

### ctparmto_sped_vigencia_tipo_de_ati

Confirmado: sim

> Todos os valores observados em CTPARMTO_SPED_VIGENCIA.TIPO_ATIVIDADE estão no comentário do banco (2026-10-18). Distribuição: A=804, G=679, R=1.

| Código | Significado |
|---|---|
| G | Atividade Geral |
| R | Atividade Rural |
| A | Ambos |

### ctparmto_sped_vigencia_forma_de_tr

Confirmado: sim

> Todos os valores observados em CTPARMTO_SPED_VIGENCIA.FORMA_TRIBUTACAO_TRIMESTRE_4 estão no comentário do banco (2026-10-18). Distribuição: 1=1.484.

| Código | Significado |
|---|---|
| 1 | LUCRO REAL |
| 5 | LUCRO PRESUMIDO |
| 6 | ARBITRADO |

### ctparmto_sped_vigencia_periodo_de_

Confirmado: sim

> Todos os valores observados em CTPARMTO_SPED_VIGENCIA.PERIODO_APURACAO_IRPJ_CSLL estão no comentário do banco (2026-10-18). Distribuição: T=800, A=684.

| Código | Significado |
|---|---|
| T | Trimestral |
| A | Anual |

### ctparmto_dere_vigencia_encerrament

Confirmado: sim

> Todos os valores observados em CTPARMTO_DERE_VIGENCIA.ENCERRAMENTO_CONTABIL estão no comentário do banco (2026-10-18). Distribuição: A=1.427.

| Código | Significado |
|---|---|
| A | Anual |
| S | Semestral |
| Q | Quadrimestral |
| T | Trimestral |
| B | Bimestral |
| M | Mensal |

### ctparmto_dados_sped_contabil_signatario_responsavel_

Confirmado: sim

> Todos os valores observados em CTPARMTO_DADOS_SPED_CONTABIL_SIGNATARIO.RESPONSAVEL_ASSINATURA estão no comentário do banco (2026-10-18). Distribuição: N=653, S=550.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

### ctparmto_cmv_estoque_grupo_grupos_de_p

Confirmado: sim

> Todos os valores observados em CTPARMTO_CMV_ESTOQUE_GRUPO.GRUPO_PRODUTO estão no comentário do banco (2026-10-18). Distribuição: T=8.

| Código | Significado |
|---|---|
| S | Selecionar |
| T | Todos |

