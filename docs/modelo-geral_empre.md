# Modelo — Geral - empre (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_empre.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

9 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geempre_alteracao](#geempre_alteracao) | `GEEMPRE_ALTERACAO` | 4.910 | pequeno | empresa |
| [geempre_vigencia](#geempre_vigencia) | `geempre_vigencia` | 1.969 | pequeno | empresa |
| [geempre_centralizadora](#geempre_centralizadora) | `GEEMPRE_CENTRALIZADORA` | 1.419 | pequeno | empresa |
| [geempre_historico](#geempre_historico) | `GEEMPRE_HISTORICO` | 1.068 | pequeno | empresa |
| [geempre_informacoes](#geempre_informacoes) | `geempre_informacoes` | 1 | pequeno | empresa |
| [geempre_bens](#geempre_bens) | `geempre_bens` | 1 | pequeno | empresa |
| [geempre_seguros](#geempre_seguros) | `geempre_seguros` | 1 | pequeno | empresa |
| [geempre_participacoes](#geempre_participacoes) | `geempre_participacoes` | 1 | pequeno | empresa |
| [geempre_comerciais](#geempre_comerciais) | `geempre_comerciais` | 1 | pequeno | empresa |

## geempre_alteracao

**Empresa - Alterações** — tabela `GEEMPRE_ALTERACAO` (4.910 linhas)

Empresa - Alterações. 4.910 linhas no catálogo; chave: CODI_EMP, DATA_ALTERACAO, CAMPO.

- **Chave:** `CODI_EMP, DATA_ALTERACAO, CAMPO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ALTERACAO`
- **Ordem padrão:** `DATA_ALTERACAO desc`, `CAMPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.910 linhas, 582 empresa(s), DATA_ALTERACAO de 2016-09-08 a 2202-11-28.
- origem_da_alteracao_1_cadastro_de_empres: todos os valores reais estão no comentário do banco (1=4.907, 2=3).
- enviar_para_o_esocial_0_nao_1_sim: todos os valores reais estão no comentário do banco (1=4.910).
- gerar_retificacao_esocial: todos os valores reais estão no comentário do banco (0=4.910).
- marcacao_do_evento_para_gerar_o_evento_d: todos os valores reais estão no comentário do banco (0=4.910).
- Vínculo geempre (geempre): 0 de 7 linhas sem registro relacionado (empresa 1070).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| data_da_alteracao | `data_alteracao` | date(4) |  |  | Data da alteração |
| campo_alterado | `campo` | tinyint(1) |  |  | Campo alterado |
| valor_anterior_a_alteracao | `de` | varchar(255) |  |  | Valor anterior a alteracao |
| valor_posterior_a_aleracao | `para` | varchar(255) |  |  | Valor posterior a aleracao |
| origem_da_alteracao_1_cadastro_de_empres | `origem` | tinyint(1) |  | geempre_alteracao_origem_da_alteracao_1_cadastro_ | Origem da alteração (1=Cadastro de empresa/ 2=Alteração contratual) |
| enviar_para_o_esocial_0_nao_1_sim | `enviar_esocial` | smallint(2) |  | geempre_alteracao_enviar_para_o_esocial_0_nao_1_s | Enviar para o eSocial. (0=Não/1=Sim) |
| gerar_retificacao_esocial | `gerar_retificacao_esocial` | smallint(2) |  | geempre_alteracao_gerar_retificacao_para_o_esocia | Gerar retificação para o eSocial. (0=Não/1=Sim) |
| marcacao_do_evento_para_gerar_o_evento_d | `processar_exclusao_esocial` | smallint(2) |  | geempre_alteracao_marcacao_do_evento_para_gerar_o | Marcação do evento para gerar o evento de exclusão no eSocial. (0=Não/1=Sim) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `data_da_alteracao` (eq/in), `campo_alterado` (eq/in), `valor_anterior_a_alteracao` (contem/prefixo), `valor_posterior_a_aleracao` (contem/prefixo)

## geempre_vigencia

**Empresa - Cadastro Vigencia** — tabela `geempre_vigencia` (1.969 linhas)

Empresa - Cadastro Vigencia. 1.969 linhas no catálogo; chave: codi_emp, data.

- **Chave:** `codi_emp, data`
- **Empresa:** `codi_emp`
- **Período:** `data`
- **Ordem padrão:** `data desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.969 linhas, 1.968 empresa(s), data de 1990-01-01 a 2018-03-07.
- Colunas expostas nulas em 100% das linhas (6): cidade, codigo_da_classificacao, codigo_do_municipio, inscricao_subst_tributario, valor_dos_honorarios, codigo_do_municipio_do_responsavel_legal.
- tipo_da_inscricao_1_cnpj_2_cpf_3_cei_6_c: todos os valores reais estão no comentário do banco (1=1.827, 2=141, 6=1).
- situacao_a_ativa_i_inativa_c_em_constitu: todos os valores reais estão no comentário do banco (I=1.226, A=743).
- selecionada_1_sim_0_nao: todos os valores reais estão no comentário do banco (0=1.638, 1=331).
- usa_contabilidade_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.383, 0=586).
- usa_livro_caixa_1_sim_0_nao: todos os valores reais estão no comentário do banco (0=1.969).
- usa_honorarios_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.466, 0=503).
- usa_escrita_fiscal_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.384, 0=585).
- usa_patrimonio_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.372, 0=597).
- usa_lalur_1_sim_0_nao: todos os valores reais estão no comentário do banco (0=1.460, 1=509).
- usa_atualizar_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.395, 0=574).
- usa_protocolo_1_sim_0_nao: todos os valores reais estão no comentário do banco (0=1.964, nulo=5).
- usa_registro_1_sim_0_nao: todos os valores reais estão no comentário do banco (1=1.477, 0=492).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codi_emp` | integer(4) |  |  | Codigo |
| data_da_vigencia | `data` | date(4) |  |  | Data da vigencia |
| nome | `nome_emp` | char(40) |  |  | Nome |
| endereco 🔒 | `ende_emp` | char(40) |  |  | Endereco |
| cep 🔒 | `cepe_emp` | char(8) |  |  | CEP |
| cidade | `cida_emp` | char(25) |  |  | Cidade |
| cnpj 🔒 | `cgce_emp` | char(14) |  |  | CNPJ |
| inscricao_estadual 🔒 | `iest_emp` | char(22) |  |  | Inscricao estadual |
| inscricao_municipal 🔒 | `imun_emp` | char(20) |  |  | Inscricao municipal |
| inscricao_na_junta_comercial 🔒 | `ijuc_emp` | char(30) |  |  | Inscricao na junta comercial |
| bairro 🔒 | `bair_emp` | char(60) |  |  | Bairro |
| ramo_de_atividade | `ramo_emp` | char(180) |  |  | Ramo de atividade |
| codigo_da_classificacao | `i_classificacoes` | integer(4) |  |  | Codigo da classificacao |
| apelido | `apel_emp` | char(20) |  |  | Apelido |
| codigo_do_municipio | `codi_mun` | integer(4) |  |  | Codigo do municipio |
| numero | `nume_emp` | integer(4) |  |  | Numero |
| data_de_inscricao_na_junta_comercial | `djuc_emp` | date(4) |  |  | Data de inscricao na junta comercial |
| telefone 🔒 | `fone_emp` | char(14) |  |  | Telefone |
| responsavel_legal | `rleg_emp` | char(60) |  |  | Responsavel legal |
| estado | `esta_emp` | char(2) |  |  | Estado |
| tipo_da_inscricao_1_cnpj_2_cpf_3_cei_6_c 🔒 | `tins_emp` | integer(4) |  | geempre_vigencia_tipo_da_inscricao_1_cnpj | Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| situacao_a_ativa_i_inativa_c_em_constitu | `stat_emp` | char(1) |  | geempre_vigencia_situacao_a_ativa_i_inati | Situacao (A - Ativa/ I - Inativa/C - Em Constituicao/ M - Ativo sem movimento/ B - Em processo de baixa) |
| data_que_ficou_inativo | `dina_emp` | date(4) |  |  | Data que ficou inativo |
| data_do_cadastramento | `dcad_emp` | date(4) |  |  | Data do cadastramento |
| selecionada_1_sim_0_nao | `sele_emp` | tinyint(1) |  | geempre_vigencia_selecionada_1_sim_0_nao | Selecionada (1 - Sim/0 - Nao) |
| este_campo_nao_e_mais_usado_a_partir_da | `codi_cla` | tinyint(1) |  |  | Este campo nao e mais usado a partir da versao 6.1A-01 do Contabil |
| usa_contabilidade_1_sim_0_nao | `ucta_emp` | tinyint(1) |  | geempre_vigencia_usa_contabilidade_1_sim_ | Usa contabilidade (1 - Sim/0 - Nao) |
| usa_livro_caixa_1_sim_0_nao | `ucxa_emp` | tinyint(1) |  | geempre_vigencia_usa_livro_caixa_1_sim_0_ | Usa livro caixa (1 - Sim/0 - Nao) |
| usa_honorarios_1_sim_0_nao | `uhon_emp` | tinyint(1) |  | geempre_vigencia_usa_honorarios_1_sim_0_n | Usa honorarios (1 - Sim/0 - Nao) |
| usa_escrita_fiscal_1_sim_0_nao | `uefi_emp` | tinyint(1) |  | geempre_vigencia_usa_escrita_fiscal_1_sim | Usa escrita fiscal (1 - Sim/0 - Nao) |
| usa_patrimonio_1_sim_0_nao | `upat_emp` | tinyint(1) |  | geempre_vigencia_usa_patrimonio_1_sim_0_n | Usa patrimonio (1 - Sim/0 - Nao) |
| usa_lalur_1_sim_0_nao | `ulal_emp` | tinyint(1) |  | geempre_vigencia_usa_lalur_1_sim_0_nao | Usa lalur (1 - Sim/0 - Nao) |
| usa_atualizar_1_sim_0_nao | `uatu_emp` | tinyint(1) |  | geempre_vigencia_usa_atualizar_1_sim_0_na | Usa atualizar (1 - Sim/0 - Nao) |
| usa_protocolo_1_sim_0_nao | `upro_emp` | tinyint(1) |  | geempre_vigencia_usa_protocolo_1_sim_0_na | Usa protocolo (1 - Sim/0 - Nao) |
| usa_registro_1_sim_0_nao | `ureg_emp` | tinyint(1) |  | geempre_vigencia_usa_registro_1_sim_0_nao | Usa registro (1 - Sim/0 - Nao) |
| cae | `ccae_emp` | double(8) |  |  | CAE |
| inscricao_subst_tributario 🔒 | `isub_emp` | char(20) |  |  | Inscricao Subst. Tributario |
| nro_de_empregados_da_empresa | `empreg_emp` | integer(4) |  |  | Nro de empregados da empresa |
| valor_medio_do_faturamento | `vlfat_emp` | numeric(13) |  |  | Valor Medio do Faturamento |
| valor_dos_honorarios | `vlhon_emp` | numeric(13) |  |  | Valor dos honorarios |
| complemento_do_responsavel_legal | `comp_leg_emp` | char(30) |  |  | Complemento do responsavel legal |
| cpf_do_responsavel_legal 🔒 | `cpf_leg_emp` | char(14) |  |  | CPF do responsavel legal |
| endereco_do_responsavel_legal 🔒 | `end_leg_emp` | char(40) |  |  | Endereco do responsavel legal |
| municipio_do_responsavel_legal | `mun_leg_emp` | char(25) |  |  | Municipio do responsavel legal |
| estado_do_responsavel_legal | `uf_leg_emp` | char(2) |  |  | Estado do responsavel legal |
| cep_do_responsavel_legal 🔒 | `cep_leg_emp` | char(8) |  |  | CEP do responsavel legal |
| natureza_juridica | `njud_emp` | integer(4) |  |  | Natureza juridica |
| complemento | `comp_emp` | char(30) |  |  | Complemento |
| numero_do_responsavel_legal | `nume_leg_emp` | integer(4) |  |  | Numero do responsavel legal |
| bairro_do_responsavel_legal 🔒 | `bair_leg_emp` | char(15) |  |  | Bairro do responsavel legal |
| codigo_do_municipio_do_responsavel_legal | `codm_leg_emp` | integer(4) |  |  | Codigo do municipio do responsavel legal |
| telefone_do_responsavel_legal 🔒 | `fone_leg_emp` | char(14) |  |  | Telefone do responsavel legal |
| cnae | `cnae_emp` | double(8) |  |  | CNAE |
| ddd | `dddf_emp` | integer(4) |  |  | DDD |
| contador | `codi_con` | integer(4) |  |  | Contador |
| cargo_do_responsavel_legal | `cargo_leg_emp` | char(30) |  |  | Cargo do responsavel legal |
| ddd_do_responsavel_legal | `dddf_leg_emp` | integer(4) |  |  | DDD do responsavel legal |
| nro_do_livro_no_cartorio_de_registros_es | `livro_cart_emp` | char(10) |  |  | Nro do livro no cartorio de registros Especiais |
| folha_do_livro_no_cartorio_de_registros | `folha_cart_emp` | char(10) |  |  | Folha do livro no cartorio de registros Especiais |
| nro_na_folha_do_livro_no_cartorio_de_reg | `nliv_cart_emp` | char(10) |  |  | Nro na folha do livro no cartorio de registros Especiais |

**Filtros:** `data_da_vigencia` (eq/in), `data_de_inscricao_na_junta_comercial` (entre/gte/lte), `data_que_ficou_inativo` (entre/gte/lte), `data_do_cadastramento` (entre/gte/lte), `nome` (contem/prefixo), `endereco` (contem/prefixo), `cep` (eq/in), `cidade` (contem/prefixo), `cnpj` (eq/in), `inscricao_estadual` (contem/prefixo), `inscricao_municipal` (eq/in), `inscricao_na_junta_comercial` (contem/prefixo), `bairro` (contem/prefixo), `ramo_de_atividade` (contem/prefixo)

## geempre_centralizadora

**Tabela Empresa Centralizadora** — tabela `GEEMPRE_CENTRALIZADORA` (1.419 linhas)

Tabela Empresa Centralizadora. 1.419 linhas no catálogo; chave: VIGENCIA, RAIZ_CNPJ_CAEPF, TINS_EMP, CODI_EMP.

- **Chave:** `VIGENCIA, RAIZ_CNPJ_CAEPF, TINS_EMP, CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `VIGENCIA`
- **Ordem padrão:** `VIGENCIA desc`, `RAIZ_CNPJ_CAEPF asc`, `TINS_EMP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.419 linhas, 1.419 empresa(s), VIGENCIA de 1900-01-01 a 1900-01-01.
- tipo_de_inscricao_1_cnpj_6_caepf: todos os valores reais estão no comentário do banco (1=1.418, 6=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1665).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| vigencia | `vigencia` | date(4) |  |  | Vigencia |
| raiz_do_cnpj_caepf 🔒 | `raiz_cnpj_caepf` | varchar(9) |  |  | Raiz do CNPJ / CAEPF |
| tipo_de_inscricao_1_cnpj_6_caepf 🔒 | `tins_emp` | integer(4) |  | geempre_centralizadora_tipo_de_inscricao_1_ | Tipo de Inscrição (1-CNPJ/6-CAEPF) |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da Empresa |
| centralizacao | `centralizacao` | integer(4) |  |  |  |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `vigencia` (eq/in), `raiz_do_cnpj_caepf` (eq/in), `tipo_de_inscricao_1_cnpj_6_caepf` (eq/in)

## geempre_historico

**Tabela de histórico de mudança da tabela GEEMPRE** — tabela `GEEMPRE_HISTORICO` (1.068 linhas)

Tabela de histórico de mudança da tabela GEEMPRE. 1.068 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.068 linhas, 1.068 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `sequencial` | integer(4) |  |  |  |
| codi_emp | `codi_emp` | integer(4) |  |  |  |
| usa_portal_empregado | `usa_portal_empregado` | integer(4) |  |  |  |

**Filtros:** `sequencial` (eq/in)

## geempre_informacoes

**Empresa - Outras Informacoes** — tabela `geempre_informacoes` (1 linhas)

Empresa - Outras Informacoes. 1 linhas no catálogo; chave: codi_emp.

- **Chave:** `codi_emp`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** 

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): esfera_poder, franqueadora.
- setor_de_atuacao_1_industria_2_comercio: todos os valores reais estão no comentário do banco (1=1).
- tipo_de_empresa_1_privada_2_publica_3_es: todos os valores reais estão no comentário do banco (1=1).
- origem_do_capital_1_nacional_2_estrangei: todos os valores reais estão no comentário do banco (1=1).
- esfera_poder: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- tipo_do_imovel_1_proprio_quitado_2_propr: todos os valores reais estão no comentário do banco (1=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| setor_de_atuacao_1_industria_2_comercio | `setor` | tinyint(1) |  | geempre_informacoes_setor_de_atuacao_1_indu | Setor de Atuacao(1 - Industria/2 - Comercio Varejista/3 - Comercio Atacadista/4 - Servicos/5 - Agricola/6 - Pecuaria/7 - Outros) |
| capital_aberto_s_n | `capital_aberto` | char(1) |  |  | Capital Aberto (S/N) |
| tipo_de_empresa_1_privada_2_publica_3_es | `tipo` | tinyint(1) |  | geempre_informacoes_tipo_de_empresa_1_priva | Tipo de Empresa (1 - Privada/2 - Publica/3 - Estatal/4 - Mista/5 - Autarquia/6 - Sem Fins Lucrativos/7 - Estrangeira Domiciliada no Exterior/8 - Estrangeira Domiciliada no Brasil) |
| origem_do_capital_1_nacional_2_estrangei | `origem_capital` | tinyint(1) |  | geempre_informacoes_origem_do_capital_1_nac | Origem do Capital (1 - Nacional/2 - Estrangeiro/3 - Ambos) |
| esfera_poder | `esfera_poder` | tinyint(1) |  | geempre_informacoes_esfera_de_poder_1_munic | Esfera de Poder (1 - Municipal/2 - Estatual/3 - Federal/4 - Distrital) |
| tipo_do_imovel_1_proprio_quitado_2_propr | `tipo_imovel` | tinyint(1) |  | geempre_informacoes_tipo_do_imovel_1_propri | Tipo do imovel (1 - Proprio Quitado/2 - Proprio Fianciado/3 - Alugado/4 - Familiar/5 - Cedido) |
| franquia | `franquia` | char(1) |  |  | Franquia |
| franqueadora | `franqueadora` | varchar(30) |  |  | Franqueadora |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `capital_aberto_s_n` (eq/in), `tipo_de_empresa_1_privada_2_publica_3_es` (eq/in), `tipo_do_imovel_1_proprio_quitado_2_propr` (eq/in), `franquia` (eq/in), `franqueadora` (contem/prefixo)

## geempre_bens

**Empresa - Bens** — tabela `geempre_bens` (1 linhas)

Empresa - Bens. 1 linhas no catálogo; chave: codi_emp, sequencial.

- **Chave:** `codi_emp, sequencial`
- **Empresa:** `codi_emp`
- **Período:** `data_matricula`
- **Ordem padrão:** `data_matricula desc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), data_matricula de 1994-10-10 a 1994-10-10.
- Colunas expostas nulas em 100% das linhas (7): valor_do_onus, credor, marca, ano, vencimento_final, empresa_do_leasing, data_do_contrato_de_leasing.
- tipo_u_urbano_r_rural: todos os valores reais estão no comentário do banco (U=1).
- tipo_de_onus_p_penhora_h_hipoteca: todos os valores reais estão no comentário do banco (H=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| classificacao | `classificacao` | char(1) |  |  | Classificacao |
| tipo_u_urbano_r_rural | `tipo` | char(1) |  | geempre_bens_tipo_u_urbano_r_rural | Tipo (U - Urbano/R - Rural) |
| descricao | `descricao` | char(100) |  |  | Descricao |
| localizacao | `localizacao` | char(100) |  |  | Localizacao |
| valor_do_bem | `valor` | numeric(13) |  |  | Valor do bem |
| area_em_m2_ou_ha | `area` | numeric(13) |  |  | Area (em m2 ou HA) |
| area_construida_em_m2 | `area_construida` | numeric(13) |  |  | Area construida em m2 |
| onus_s_n | `onus` | char(1) |  |  | Onus (S/N) |
| tipo_de_onus_p_penhora_h_hipoteca | `tipo_onus` | char(1) |  | geempre_bens_tipo_de_onus_p_penhora_h_hipoteca | Tipo de Onus ( P - Penhora/H - Hipoteca) |
| valor_do_onus | `valor_onus` | numeric(13) |  |  | Valor do onus |
| credor | `credor` | char(40) |  |  | Credor |
| matricula | `matricula` | char(20) |  |  | Matricula |
| cartorio | `cartorio` | char(30) |  |  | Cartorio |
| data_da_matricula | `data_matricula` | date(4) |  |  | Data da matricula |
| numero_do_livro | `livro` | char(10) |  |  | Numero do livro |
| numero_da_folha | `folha` | char(10) |  |  | Numero da folha |
| cessao_s_n | `cessao` | char(1) |  |  | Cessao (S/N) |
| bem_impenhoravel_s_n | `impenhoravel` | char(1) |  |  | Bem impenhoravel (S/N) |
| imovel_rural_enquadrado_s_n | `rural_enquadrado` | char(1) |  |  | Imovel rural enquadrado(S/N) |
| marca | `marca` | char(30) |  |  | Marca |
| ano | `ano` | integer(4) |  |  | Ano |
| alienado_s_n | `alienado` | char(1) |  |  | Alienado(S/N) |
| vencimento_final | `vencimento` | date(4) |  |  | Vencimento final |
| leasing_s_n | `leasing` | char(1) |  |  | Leasing (S/N) |
| empresa_do_leasing | `empresa` | char(30) |  |  | Empresa do leasing |
| data_do_contrato_de_leasing | `data_contrato` | date(4) |  |  | Data do contrato de leasing |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `data_da_matricula` (entre/gte/lte), `vencimento_final` (entre/gte/lte), `data_do_contrato_de_leasing` (entre/gte/lte), `classificacao` (eq/in), `tipo_u_urbano_r_rural` (eq/in), `descricao` (contem/prefixo), `localizacao` (contem/prefixo), `onus_s_n` (eq/in), `tipo_de_onus_p_penhora_h_hipoteca` (eq/in), `credor` (contem/prefixo), `matricula` (eq/in), `cartorio` (contem/prefixo), `numero_do_livro` (eq/in)

## geempre_seguros

**Empresa - Seguros** — tabela `geempre_seguros` (1 linhas)

Empresa - Seguros. 1 linhas no catálogo; chave: codi_emp, sequencial.

- **Chave:** `codi_emp, sequencial`
- **Empresa:** `codi_emp`
- **Período:** `vencimento`
- **Ordem padrão:** `vencimento desc`, `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), vencimento de 2005-07-10 a 2005-07-10.
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| modalidade_do_seguro | `modalidade` | char(30) |  |  | Modalidade do seguro |
| bem_segurado | `bem` | char(40) |  |  | Bem segurado |
| nome_da_seguradora | `seguradora` | char(40) |  |  | Nome da seguradora |
| valor_do_seguro | `valor` | numeric(13) |  |  | Valor do seguro |
| data_de_vencimento | `vencimento` | date(4) |  |  | Data de vencimento |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `data_de_vencimento` (entre/gte/lte), `modalidade_do_seguro` (contem/prefixo), `bem_segurado` (contem/prefixo), `nome_da_seguradora` (contem/prefixo)

## geempre_participacoes

**Empresa - Participacoes em outras empresas** — tabela `geempre_participacoes` (1 linhas)

Empresa - Participacoes em outras empresas. 1 linhas no catálogo; chave: codi_emp, cnpj.

- **Chave:** `codi_emp, cnpj`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `cnpj asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| cnpj 🔒 | `cnpj` | char(14) |  |  | CNPJ |
| razao_social 🔒 | `razao_social` | char(40) |  |  | Razao Social |
| participacao | `participacao` | numeric(5) |  |  | Participacao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `cnpj` (eq/in), `razao_social` (contem/prefixo)

## geempre_comerciais

**Empresa - Referencias Comerciais** — tabela `geempre_comerciais` (1 linhas)

Empresa - Referencias Comerciais. 1 linhas no catálogo; chave: codi_emp, sequencial.

- **Chave:** `codi_emp, sequencial`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `sequencial asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Colunas expostas nulas em 100% das linhas (2): complemento, pessoa_para_contato.
- tipo_c_cliente_f_fornecedor_a_ambos: todos os valores reais estão no comentário do banco (A=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 9999).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| tipo_c_cliente_f_fornecedor_a_ambos | `tipo` | char(1) |  | geempre_comerciais_tipo_c_cliente_f_fo | Tipo (C - Cliente/F - Fornecedor/A - Ambos) |
| nome_da_empresa | `empresa` | char(40) |  |  | Nome da empresa |
| endereco 🔒 | `endereco` | char(40) |  |  | Endereco |
| bairro 🔒 | `bairro` | char(40) |  |  | Bairro |
| cidade | `cidade` | char(40) |  |  | Cidade |
| uf | `uf` | char(2) |  |  | UF |
| numero | `numero` | integer(4) |  |  | Numero |
| cep 🔒 | `cep` | char(8) |  |  | CEP |
| complemento | `complemento` | char(30) |  |  | Complemento |
| ddd | `ddd` | integer(4) |  |  | DDD |
| fone 🔒 | `fone` | char(14) |  |  | Fone |
| pessoa_para_contato | `pessoa_contato` | varchar(50) |  |  | Pessoa para contato |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `tipo_c_cliente_f_fornecedor_a_ambos` (eq/in), `nome_da_empresa` (contem/prefixo), `endereco` (contem/prefixo), `bairro` (contem/prefixo), `cidade` (contem/prefixo), `uf` (eq/in), `cep` (eq/in), `complemento` (contem/prefixo), `fone` (eq/in), `pessoa_para_contato` (contem/prefixo)

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

### geempre_alteracao_origem_da_alteracao_1_cadastro_

Confirmado: sim

> Todos os valores observados em GEEMPRE_ALTERACAO.ORIGEM estão no comentário do banco (2026-10-18). Distribuição: 1=4.907, 2=3.

| Código | Significado |
|---|---|
| 1 | Cadastro de empresa |
| 2 | Alteração contratual |

### geempre_alteracao_enviar_para_o_esocial_0_nao_1_s

Confirmado: sim

> Todos os valores observados em GEEMPRE_ALTERACAO.ENVIAR_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 1=4.910.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### geempre_alteracao_gerar_retificacao_para_o_esocia

Confirmado: sim

> Todos os valores observados em GEEMPRE_ALTERACAO.GERAR_RETIFICACAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=4.910.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### geempre_alteracao_marcacao_do_evento_para_gerar_o

Confirmado: sim

> Todos os valores observados em GEEMPRE_ALTERACAO.PROCESSAR_EXCLUSAO_ESOCIAL estão no comentário do banco (2026-10-18). Distribuição: 0=4.910.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### geempre_vigencia_tipo_da_inscricao_1_cnpj

Confirmado: sim

> Todos os valores observados em geempre_vigencia.tins_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.827, 2=141, 6=1.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 2 | CPF |
| 3 | CEI |
| 6 | CAEPF |

### geempre_vigencia_situacao_a_ativa_i_inati

Confirmado: sim

> Todos os valores observados em geempre_vigencia.stat_emp estão no comentário do banco (2026-10-18). Distribuição: I=1.226, A=743.

| Código | Significado |
|---|---|
| A | Ativa |
| I | Inativa |
| C | Em Constituicao |
| M | Ativo sem movimento |
| B | Em processo de baixa |

### geempre_vigencia_selecionada_1_sim_0_nao

Confirmado: sim

> Todos os valores observados em geempre_vigencia.sele_emp estão no comentário do banco (2026-10-18). Distribuição: 0=1.638, 1=331.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_contabilidade_1_sim_

Confirmado: sim

> Todos os valores observados em geempre_vigencia.ucta_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.383, 0=586.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_livro_caixa_1_sim_0_

Confirmado: sim

> Todos os valores observados em geempre_vigencia.ucxa_emp estão no comentário do banco (2026-10-18). Distribuição: 0=1.969.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_honorarios_1_sim_0_n

Confirmado: sim

> Todos os valores observados em geempre_vigencia.uhon_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.466, 0=503.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_escrita_fiscal_1_sim

Confirmado: sim

> Todos os valores observados em geempre_vigencia.uefi_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.384, 0=585.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_patrimonio_1_sim_0_n

Confirmado: sim

> Todos os valores observados em geempre_vigencia.upat_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.372, 0=597.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_lalur_1_sim_0_nao

Confirmado: sim

> Todos os valores observados em geempre_vigencia.ulal_emp estão no comentário do banco (2026-10-18). Distribuição: 0=1.460, 1=509.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_atualizar_1_sim_0_na

Confirmado: sim

> Todos os valores observados em geempre_vigencia.uatu_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.395, 0=574.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_protocolo_1_sim_0_na

Confirmado: sim

> Todos os valores observados em geempre_vigencia.upro_emp estão no comentário do banco (2026-10-18). Distribuição: 0=1.964, nulo=5.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_vigencia_usa_registro_1_sim_0_nao

Confirmado: sim

> Todos os valores observados em geempre_vigencia.ureg_emp estão no comentário do banco (2026-10-18). Distribuição: 1=1.477, 0=492.

| Código | Significado |
|---|---|
| 1 | Sim |
| 0 | Nao |

### geempre_centralizadora_tipo_de_inscricao_1_

Confirmado: sim

> Todos os valores observados em GEEMPRE_CENTRALIZADORA.TINS_EMP estão no comentário do banco (2026-10-18). Distribuição: 1=1.418, 6=1.

| Código | Significado |
|---|---|
| 1 | CNPJ |
| 6 | CAEPF |

### geempre_informacoes_setor_de_atuacao_1_indu

Confirmado: sim

> Todos os valores observados em geempre_informacoes.setor estão no comentário do banco (2026-10-18). Distribuição: 1=1.

| Código | Significado |
|---|---|
| 1 | Industria |
| 2 | Comercio Varejista |
| 3 | Comercio Atacadista |
| 4 | Servicos |
| 5 | Agricola |
| 6 | Pecuaria |
| 7 | Outros |

### geempre_informacoes_tipo_de_empresa_1_priva

Confirmado: sim

> Todos os valores observados em geempre_informacoes.tipo estão no comentário do banco (2026-10-18). Distribuição: 1=1.

| Código | Significado |
|---|---|
| 1 | Privada |
| 2 | Publica |
| 3 | Estatal |
| 4 | Mista |
| 5 | Autarquia |
| 6 | Sem Fins Lucrativos |
| 7 | Estrangeira Domiciliada no Exterior |
| 8 | Estrangeira Domiciliada no Brasil |

### geempre_informacoes_origem_do_capital_1_nac

Confirmado: sim

> Todos os valores observados em geempre_informacoes.origem_capital estão no comentário do banco (2026-10-18). Distribuição: 1=1.

| Código | Significado |
|---|---|
| 1 | Nacional |
| 2 | Estrangeiro |
| 3 | Ambos |

### geempre_informacoes_esfera_de_poder_1_munic

Confirmado: parcial

> Coluna geempre_informacoes.esfera_poder só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| 1 | Municipal |
| 2 | Estatual |
| 3 | Federal |
| 4 | Distrital |

### geempre_informacoes_tipo_do_imovel_1_propri

Confirmado: sim

> Todos os valores observados em geempre_informacoes.tipo_imovel estão no comentário do banco (2026-10-18). Distribuição: 1=1.

| Código | Significado |
|---|---|
| 1 | Proprio Quitado |
| 2 | Proprio Fianciado |
| 3 | Alugado |
| 4 | Familiar |
| 5 | Cedido |

### geempre_bens_tipo_u_urbano_r_rural

Confirmado: sim

> Todos os valores observados em geempre_bens.tipo estão no comentário do banco (2026-10-18). Distribuição: U=1.

| Código | Significado |
|---|---|
| U | Urbano |
| R | Rural |

### geempre_bens_tipo_de_onus_p_penhora_h_hipoteca

Confirmado: sim

> Todos os valores observados em geempre_bens.tipo_onus estão no comentário do banco (2026-10-18). Distribuição: H=1.

| Código | Significado |
|---|---|
| P | Penhora |
| H | Hipoteca |

### geempre_comerciais_tipo_c_cliente_f_fo

Confirmado: sim

> Todos os valores observados em geempre_comerciais.tipo estão no comentário do banco (2026-10-18). Distribuição: A=1.

| Código | Significado |
|---|---|
| C | Cliente |
| F | Fornecedor |
| A | Ambos |

