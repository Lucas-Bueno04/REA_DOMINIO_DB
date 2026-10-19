# Modelo — Fiscal - outrosdados (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_outrosdados.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

20 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efoutrosdados_efd_contas](#efoutrosdados_efd_contas) | `EFOUTROSDADOS_EFD_CONTAS` | 3.369 | pequeno | empresa |
| [efoutrosdados_efd_contas_cfop](#efoutrosdados_efd_contas_cfop) | `EFOUTROSDADOS_EFD_CONTAS_CFOP` | 1.787 | pequeno | empresa |
| [efoutrosdados_reinf_rendimentos_isentos](#efoutrosdados_reinf_rendimentos_isentos) | `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS` | 1.181 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_cfops_considerados](#efoutrosdados_planejamento_tributario_cfops_considerados) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CFOPS_CONSIDERADOS` | 658 | pequeno | empresa |
| [efoutrosdados_efd_contas_acumulador](#efoutrosdados_efd_contas_acumulador) | `EFOUTROSDADOS_EFD_CONTAS_ACUMULADOR` | 444 | pequeno | empresa |
| [efoutrosdados_efd_reinf_servicos_tomados](#efoutrosdados_efd_reinf_servicos_tomados) | `EFOUTROSDADOS_EFD_REINF_SERVICOS_TOMADOS` | 79 | pequeno | empresa |
| [efoutrosdados_efd_contas_cst](#efoutrosdados_efd_contas_cst) | `EFOUTROSDADOS_EFD_CONTAS_CST` | 28 | pequeno | empresa |
| [efoutrosdados_efd_reinf_servicos_prestados](#efoutrosdados_efd_reinf_servicos_prestados) | `EFOUTROSDADOS_EFD_REINF_SERVICOS_PRESTADOS` | 20 | pequeno | empresa |
| [efoutrosdados_reinf_rendimentos_isentos_contas_param](#efoutrosdados_reinf_rendimentos_isentos_contas_param) | `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS_CONTAS_PARAM` | 8 | pequeno | empresa |
| [efoutrosdados_efd_recibo_scp](#efoutrosdados_efd_recibo_scp) | `EFOUTROSDADOS_EFD_RECIBO_SCP` | 7 | pequeno | empresa |
| [efoutrosdados_reinf_rendimentos_isentos_contas](#efoutrosdados_reinf_rendimentos_isentos_contas) | `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS_CONTAS` | 7 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_presuncao](#efoutrosdados_planejamento_tributario_presuncao) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_PRESUNCAO` | 3 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_custos_despesas_lucro](#efoutrosdados_planejamento_tributario_custos_despesas_lucro) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_EMPRESAS_CONTAS` | 3 | pequeno | empresa |
| [efoutrosdados_efd_evento_scp](#efoutrosdados_efd_evento_scp) | `EFOUTROSDADOS_EFD_EVENTO_SCP` | 2 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_aliquota_impostos](#efoutrosdados_planejamento_tributario_aliquota_impostos) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_ALIQUOTA_IMPOSTOS` | 2 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_custos_despesas_lucro_x](#efoutrosdados_planejamento_tributario_custos_despesas_lucro_x) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL` | 2 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x](#efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_EMPRESAS` | 2 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_percentual_rb_simples](#efoutrosdados_planejamento_tributario_percentual_rb_simples) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_PERCENTUAL_RB_SIMPLES_NACIONAL` | 2 | pequeno | empresa |
| [efoutrosdados_dirf_scp](#efoutrosdados_dirf_scp) | `EFOUTROSDADOS_DIRF_SCP` | 1 | pequeno | empresa |
| [efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x_x](#efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x_x) | `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_SALDO_CONTA_ACUMULADOR_EMPRESAS` | 1 | pequeno | empresa |

## efoutrosdados_efd_contas

**EFD Contribuições - Outros Dados - Contas** — tabela `EFOUTROSDADOS_EFD_CONTAS` (3.369 linhas)

EFD Contribuições - Outros Dados - Contas. 3.369 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `REGISTRO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.369 linhas, 32 empresa(s), COMPETENCIA de 2017-07-01 a 2026-07-01.
- tipo_do_cst_1_todos_os_csts_2_selecionar: todos os valores reais estão no comentário do banco (1=3.237, 2=132).
- tipo_do_natureza_receita_1_todas_as_natu: todos os valores reais estão no comentário do banco (1=3.369).
- tipo_do_acumulador_1_todos_os_acumulador: todos os valores reais estão no comentário do banco (1=3.187, 2=182).
- tipo_do_cfop_1_todos_os_cfops_2_selecion: todos os valores reais estão no comentário do banco (1=2.384, 2=985).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| registro_1_c481_c485_2_m400_m800_3_f500 | `registro` | integer(4) |  |  | REGISTRO (1-C481/C485/2-M400/M800/3-F500/F510/4-F550/F560/5-C181/C185/6-C191/C195/7-C491/C495/8-M410/M810/9-C870/C880/10-F100SAI/11-F100ENT) |
| sequencial_da_conta | `sequencial_cta` | integer(4) |  |  | Sequencial da Conta |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta Contábil |
| tipo_do_cst_1_todos_os_csts_2_selecionar | `tipo_cst` | integer(4) |  | efoutrosdados_efd_contas_tipo_do_cst_ | Tipo do CST (1 - Todos os CSTs / 2 - Selecionar os CSTs) |
| tipo_do_natureza_receita_1_todas_as_natu | `tipo_natureza_receita` | integer(4) |  | efoutrosdados_efd_contas_tipo_do_natu | Tipo do Natureza Receita (1 - Todas as Naturezas / 2 - Selecionar as Naturezas) |
| tipo_do_acumulador_1_todos_os_acumulador | `tipo_acumulador` | integer(4) |  | efoutrosdados_efd_contas_tipo_do_acum | Tipo do Acumulador (1 - Todos os acumuladores / 2 - Selecioanr os acumuladores) |
| tipo_do_cfop_1_todos_os_cfops_2_selecion | `tipo_cfop` | integer(4) |  | efoutrosdados_efd_contas_tipo_do_cfop | Tipo do CFOP (1 - Todos os CFOPs / 2 - Selecionar os CFOPs) |
| tipo_lancamento_d_demais_lancamentos_c_c | `tipo_lancamento` | char(1) |  |  | TIPO LANÇAMENTO - D(DEMAIS LANÇAMENTOS)/C(CONTRATOS DE FOMENTO MERCANTIL)/E(Empreendimentos Imobiliários) |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `registro_1_c481_c485_2_m400_m800_3_f500` (eq/in), `sequencial_da_conta` (eq/in), `conta_contabil` (eq/in), `tipo_do_cst_1_todos_os_csts_2_selecionar` (eq/in), `tipo_do_natureza_receita_1_todas_as_natu` (eq/in), `tipo_do_acumulador_1_todos_os_acumulador` (eq/in), `tipo_do_cfop_1_todos_os_cfops_2_selecion` (eq/in), `tipo_lancamento_d_demais_lancamentos_c_c` (eq/in)

## efoutrosdados_efd_contas_cfop

**EFD Contribuições - Outros Dados - Contas - CFOP** — tabela `EFOUTROSDADOS_EFD_CONTAS_CFOP` (1.787 linhas)

EFD Contribuições - Outros Dados - Contas - CFOP. 1.787 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_NAT.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_NAT`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `REGISTRO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.787 linhas, 22 empresa(s), COMPETENCIA de 2020-01-01 a 2025-03-01.
- Vínculo efnatureza (efnatureza): 0 de 114 linhas sem registro relacionado (empresa 1026).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| registro_1_c481_c485_2_m400_m800_3_f500 | `registro` | integer(4) |  |  | Registro (1-C481/C485/2-M400/M800/3-F500/F510/4-F550/F560/5-C181/C185/6-C191/C195/7-C491/C495/8-M410/M810/9-C870/C880/10-F100Sai/11-F100Ent) |
| sequencial_da_conta | `sequencial_cta` | integer(4) |  |  | Sequencial da Conta |
| sequencial_do_cfop | `sequencial_nat` | integer(4) |  |  | Sequencial do CFOP |
| codigo_do_cfop | `codi_nat` | integer(4) |  |  | Código do CFOP |
| versao_do_cfop | `versao_nat` | smallint(2) |  |  | Versão do CFOP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efnatureza` → `efnatureza` por `codi_nat` = `codi_nat` e `versao_nat` = `versao_nat`; colunas: `efnatureza_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `registro_1_c481_c485_2_m400_m800_3_f500` (eq/in), `sequencial_da_conta` (eq/in), `sequencial_do_cfop` (eq/in), `codigo_do_cfop` (eq/in)

## efoutrosdados_reinf_rendimentos_isentos

**REINF - Outros Dados - Rendimentos Isentos** — tabela `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS` (1.181 linhas)

REINF - Outros Dados - Rendimentos Isentos. 1.181 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_RENDIMENTO`
- **Ordem padrão:** `DATA_RENDIMENTO desc`, `COMPETENCIA asc`, `I_INFORMATIVOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.201 linhas, 27 empresa(s), DATA_RENDIMENTO de 2024-10-31 a 2026-10-02.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial_rendimento | `i_rendimento_isento` | integer(4) |  |  | Sequencial rendimento |
| cpf_cnpj_do_beneficiario 🔒 | `beneficiario` | char(14) |  |  | CPF/CNPJ DO BENEFICIÁRIO |
| pais | `codigo_pais` | integer(4) |  |  | País |
| codigo_natureza_de_rendimento | `codi_nat_rendimento` | integer(4) |  |  | Código natureza de rendimento |
| valor | `valor` | numeric(13) |  |  | Valor |
| controle_de_informacoes_importadas_da_fo | `importado_folha` | char(1) |  |  | Controle de informações importadas da folha |
| data_do_rendimento_isento | `data_rendimento` | date(4) |  |  | Data do rendimento isento |
| beneficiario_importado_pela_contabilidad | `origem_contabilidade` | char(1) |  |  | Beneficiário importado pela contabilidade (S/N) |
| lucro_apurado_ate_2025_s_n | `lucro_apurado_ate_2025` | char(1) |  |  | Lucro apurado ate 2025 (S/N) |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial_rendimento` (eq/in), `data_do_rendimento_isento` (entre/gte/lte), `cpf_cnpj_do_beneficiario` (eq/in), `pais` (eq/in), `codigo_natureza_de_rendimento` (eq/in), `controle_de_informacoes_importadas_da_fo` (eq/in), `beneficiario_importado_pela_contabilidad` (eq/in), `lucro_apurado_ate_2025_s_n` (eq/in)

## efoutrosdados_planejamento_tributario_cfops_considerados

**Outros Dados - Planejamento Tributário - CFOPs considerados para o cálculo (debito e credito)** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CFOPS_CONSIDERADOS` (658 linhas)

Outros Dados - Planejamento Tributário - CFOPs considerados para o cálculo (debito e credito). 658 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, TIPO, I_SEQUENCIAL, ATIVIDADE.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, TIPO, I_SEQUENCIAL, ATIVIDADE`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 658 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- tipo_d_debito_c_credito: todos os valores reais estão no comentário do banco (C=418, D=240).
- atividade_1_comercio_2_industria_3_servi: todos os valores reais estão no comentário do banco (1=512, 2=142, 3=4).
- Vínculo efinformativos (efinformativos): 0 de 329 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 329 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| tipo_d_debito_c_credito | `tipo` | char(1) |  | efoutrosdados_planejamento_tributario_cfops_considerados_tipo_d_debi | Tipo (D - Débito / C- Crédito) |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| atividade_1_comercio_2_industria_3_servi | `atividade` | integer(4) |  | efoutrosdados_planejamento_tributario_cfops_considerados_atividade_1 | Atividade (1 - Comercio / 2 - Industria / 3 - Serviço) |
| cfop_considerado | `cfop_considerado` | integer(4) |  |  | CFOP_CONSIDERADO |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `tipo_d_debito_c_credito` (eq/in), `sequencial` (eq/in), `atividade_1_comercio_2_industria_3_servi` (eq/in)

## efoutrosdados_efd_contas_acumulador

**EFD Contribuições - Outros Dados - Contas - Acumulador** — tabela `EFOUTROSDADOS_EFD_CONTAS_ACUMULADOR` (444 linhas)

EFD Contribuições - Outros Dados - Contas - Acumulador. 444 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_ACUMULADOR.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_ACUMULADOR`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `REGISTRO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 444 linhas, 20 empresa(s), COMPETENCIA de 2024-01-01 a 2026-07-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| registro_1_c481_c485_2_m400_m800_3_f500 | `registro` | integer(4) |  |  | Registro (1-C481/C485/2-M400/M800/3-F500/F510/4-F550/F560/5-C181/C185/6-C191/C195/7-C491/C495/8-M410/M810/9-C870/C880/10-F100Sai/11-F100Ent) |
| sequencial_da_conta | `sequencial_cta` | integer(4) |  |  | Sequencial da Conta |
| sequencial_do_acumulador | `sequencial_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| codigo_do_acumulador | `codi_acu` | integer(4) |  |  | Código do Acumulador |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `registro_1_c481_c485_2_m400_m800_3_f500` (eq/in), `sequencial_da_conta` (eq/in), `sequencial_do_acumulador` (eq/in), `codigo_do_acumulador` (eq/in)

## efoutrosdados_efd_reinf_servicos_tomados

**EFD-Reinf - Outros Dados - Serviçoes Tomados** — tabela `EFOUTROSDADOS_EFD_REINF_SERVICOS_TOMADOS` (79 linhas)

EFD-Reinf - Outros Dados - Serviçoes Tomados. 79 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, CODI_EMP_TOMADOR, TIPO_INSCRICAO_TOMADOR, INSCRICAO_TOMADOR, CODIGO_RECOLHIMENTO_VALOR_APURADO, TIPO_INSCRICAO_VALOR_APURADO, INSCRICAO_VALOR_APURADO, NUMERO_DOCUMENTO, INDICATIVO_PRESTACAO_SERVICOS.

- **Chave:** `CODI_EMP, COMPETENCIA, CODI_EMP_TOMADOR, TIPO_INSCRICAO_TOMADOR, INSCRICAO_TOMADOR, CODIGO_RECOLHIMENTO_VALOR_APURADO, TIPO_INSCRICAO_VALOR_APURADO, INSCRICAO_VALOR_APURADO, NUMERO_DOCUMENTO, INDICATIVO_PRESTACAO_SERVICOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_EMP_TOMADOR asc`, `TIPO_INSCRICAO_TOMADOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 79 linhas, 4 empresa(s), COMPETENCIA de 2021-02-01 a 2026-02-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| empresa_tomador | `codi_emp_tomador` | integer(4) |  |  | Empresa Tomador |
| tipo_inscricao_tomador 🔒 | `tipo_inscricao_tomador` | integer(4) |  |  | Tipo inscrição tomador |
| inscricao_tomador 🔒 | `inscricao_tomador` | varchar(14) |  |  | Inscrição tomador |
| codigo_de_recolhimento | `codigo_recolhimento_valor_apurado` | varchar(6) |  |  | Código de recolhimento |
| tipo_inscricao_valor_apurado 🔒 | `tipo_inscricao_valor_apurado` | integer(4) |  |  | Tipo inscrição valor apurado |
| inscricao_valor_apurado 🔒 | `inscricao_valor_apurado` | varchar(14) |  |  | Inscrição valor apurado |
| numero_do_documento | `numero_documento` | numeric(15) |  |  | Número do documento |
| indicativo_de_prestacao_de_servicos | `indicativo_prestacao_servicos` | integer(4) |  |  | Indicativo de Prestação de Serviços |
| valor_debito | `valor_debito` | numeric(13) |  |  | Valor débito |
| numero_cno | `numero_cno` | varchar(14) |  |  | Número CNO |

**Filtros:** `competencia` (eq/in), `empresa_tomador` (eq/in), `tipo_inscricao_tomador` (eq/in), `inscricao_tomador` (eq/in), `codigo_de_recolhimento` (eq/in), `tipo_inscricao_valor_apurado` (eq/in), `inscricao_valor_apurado` (eq/in), `numero_do_documento` (eq/in), `indicativo_de_prestacao_de_servicos` (eq/in), `numero_cno` (eq/in)

## efoutrosdados_efd_contas_cst

**EFD Contribuições - Outros Dados - Contas - CST** — tabela `EFOUTROSDADOS_EFD_CONTAS_CST` (28 linhas)

EFD Contribuições - Outros Dados - Contas - CST. 28 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_CST.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, REGISTRO, SEQUENCIAL_CTA, SEQUENCIAL_CST`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `REGISTRO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 28 linhas, 7 empresa(s), COMPETENCIA de 2017-07-01 a 2026-07-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| registro_1_c481_c485_2_m400_m800_3_f500 | `registro` | integer(4) |  |  | REGISTRO (1-C481/C485/2-M400/M800/3-F500/F510/4-F550/F560/5-C181/C185/6-C191/C195/7-C491/C495/8-M410/M810/9-C870/C880/10-F100SAI/11-F100ENT) |
| sequencial_da_conta | `sequencial_cta` | integer(4) |  |  | Sequencial da Conta |
| sequencial_do_cst | `sequencial_cst` | integer(4) |  |  | Sequencial do CST |
| codigo_da_situacao_tributaria | `codi_cst` | integer(4) |  |  | Código da Situação Tributária |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `registro_1_c481_c485_2_m400_m800_3_f500` (eq/in), `sequencial_da_conta` (eq/in), `sequencial_do_cst` (eq/in), `codigo_da_situacao_tributaria` (eq/in)

## efoutrosdados_efd_reinf_servicos_prestados

**EFD-Reinf - Outros Dados - Serviçoes Tomados** — tabela `EFOUTROSDADOS_EFD_REINF_SERVICOS_PRESTADOS` (20 linhas)

EFD-Reinf - Outros Dados - Serviçoes Tomados. 20 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, CODI_EMP_PRESTADOS, TIPO_INSCRICAO_PRESTADOS, INSCRICAO_PRESTADOS, CODIGO_RECOLHIMENTO_VALOR_APURADO, TIPO_INSCRICAO_VALOR_APURADO, INSCRICAO_VALOR_APURADO, NUMERO_DOCUMENTO, TIPO_NOTA, INDICATIVO_PRESTACAO_SERVICOS.

- **Chave:** `CODI_EMP, COMPETENCIA, CODI_EMP_PRESTADOS, TIPO_INSCRICAO_PRESTADOS, INSCRICAO_PRESTADOS, CODIGO_RECOLHIMENTO_VALOR_APURADO, TIPO_INSCRICAO_VALOR_APURADO, INSCRICAO_VALOR_APURADO, NUMERO_DOCUMENTO, TIPO_NOTA, INDICATIVO_PRESTACAO_SERVICOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `CODI_EMP_PRESTADOS asc`, `TIPO_INSCRICAO_PRESTADOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 20 linhas, 1 empresa(s), COMPETENCIA de 2021-09-01 a 2023-11-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| codi_emp_prestados | `codi_emp_prestados` | integer(4) |  |  |  |
| tipo_inscricao_prestados 🔒 | `tipo_inscricao_prestados` | integer(4) |  |  |  |
| inscricao_prestados 🔒 | `inscricao_prestados` | varchar(14) |  |  |  |
| codigo_de_recolhimento | `codigo_recolhimento_valor_apurado` | varchar(6) |  |  | Código de recolhimento |
| tipo_inscricao_valor_apurado 🔒 | `tipo_inscricao_valor_apurado` | integer(4) |  |  | Tipo inscrição valor apurado |
| inscricao_valor_apurado 🔒 | `inscricao_valor_apurado` | varchar(14) |  |  | Inscrição valor apurado |
| numero_do_documento | `numero_documento` | numeric(15) |  |  | Número do documento |
| tipo_da_nota_s_saida_v_servico | `tipo_nota` | char(1) |  |  | Tipo da nota S-Saída/V-Serviço |
| indicativo_de_prestacao_de_servicos | `indicativo_prestacao_servicos` | integer(4) |  |  | Indicativo de Prestação de Serviços |
| valor_debito | `valor_debito` | numeric(13) |  |  | Valor débito |
| numero_cno | `numero_cno` | varchar(14) |  |  | Número CNO |

**Filtros:** `competencia` (eq/in), `codi_emp_prestados` (eq/in), `tipo_inscricao_prestados` (eq/in), `inscricao_prestados` (eq/in), `codigo_de_recolhimento` (eq/in), `tipo_inscricao_valor_apurado` (eq/in), `inscricao_valor_apurado` (eq/in), `numero_do_documento` (eq/in), `tipo_da_nota_s_saida_v_servico` (eq/in), `indicativo_de_prestacao_de_servicos` (eq/in), `numero_cno` (eq/in)

## efoutrosdados_reinf_rendimentos_isentos_contas_param

**REINF - Outros Dados - Rendimentos Isentos - Contas parâmetros** — tabela `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS_CONTAS_PARAM` (8 linhas)

REINF - Outros Dados - Rendimentos Isentos - Contas parâmetros. 8 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO`
- **Empresa:** `CODI_EMP`
- **Período:** `PERIODO_INICIAL`
- **Ordem padrão:** `PERIODO_INICIAL desc`, `COMPETENCIA asc`, `I_INFORMATIVOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 2 empresa(s), PERIODO_INICIAL de 2025-05-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial_rendimento | `i_rendimento_isento` | integer(4) |  |  | Sequencial rendimento |
| periodo_inicial | `periodo_inicial` | date(4) |  |  | Período inicial |
| periodo_final | `periodo_final` | date(4) |  |  | Período final |
| determinar_a_forma_de_importar_o_saldo_d | `forma_importar_saldo` | integer(4) |  |  | Determinar a forma de importar o saldo das contas contábeis |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial_rendimento` (eq/in), `periodo_inicial` (entre/gte/lte), `periodo_final` (entre/gte/lte)

## efoutrosdados_efd_recibo_scp

**EFD Contribuições - Outros Dados - Recibo - SCP** — tabela `EFOUTROSDADOS_EFD_RECIBO_SCP` (7 linhas)

EFD Contribuições - Outros Dados - Recibo - SCP. 7 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SCP.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 1 empresa(s), COMPETENCIA de 2025-03-01 a 2025-04-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| scp | `i_scp` | integer(4) |  |  | SCP |
| numero_do_recibo | `numero_recibo` | varchar(41) |  |  | Número do recibo |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `scp` (eq/in), `numero_do_recibo` (contem/prefixo)

## efoutrosdados_reinf_rendimentos_isentos_contas

**REINF - Outros Dados - Rendimentos Isentos - Contas** — tabela `EFOUTROSDADOS_REINF_RENDIMENTOS_ISENTOS_CONTAS` (7 linhas)

REINF - Outros Dados - Rendimentos Isentos - Contas. 7 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO, CONTA.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_RENDIMENTO_ISENTO, CONTA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_RENDIMENTO_ISENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 1 empresa(s), COMPETENCIA de 2026-01-01 a 2026-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial_rendimento | `i_rendimento_isento` | integer(4) |  |  | Sequencial rendimento |
| conta | `conta` | integer(4) |  |  | Conta |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial_rendimento` (eq/in), `conta` (eq/in)

## efoutrosdados_planejamento_tributario_presuncao

**Outros Dados - Planejamento Tributário - Percentual Receita Bruta por Presunção de CSLL e IRPJ** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_PRESUNCAO` (3 linhas)

Outros Dados - Planejamento Tributário - Percentual Receita Bruta por Presunção de CSLL e IRPJ. 3 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 2 linhas sem registro relacionado (empresa 1).
- Vínculo geempre (geempre): 0 de 2 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| percentual_csll | `percentual_csll` | numeric(5) |  |  | Percentual CSLL |
| percentual_irpj | `percentual_irpj` | numeric(5) |  |  | Percentual IRPJ |
| percentual_receita_bruta | `percentual_receita_bruta` | numeric(5) |  |  | Percentual Receita Bruta |
| considerar_cfops_de | `considerar_cfop` | integer(4) |  |  | Considerar CFOPS de: |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial` (eq/in)

## efoutrosdados_planejamento_tributario_custos_despesas_lucro

**Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real)** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_EMPRESAS_CONTAS` (3 linhas)

Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real). 3 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA, CODI_CTA.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA, CODI_CTA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `EMPRESA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 2 linhas sem registro relacionado (empresa 1).
- Vínculo geempre (geempre): 0 de 2 linhas sem registro relacionado (empresa 1).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| empresa_importar_saldo_das_contas_contab | `empresa` | integer(4) |  |  | Empresa - Importar saldo das contas contábeis |
| conta_contabil | `codi_cta` | integer(4) |  |  | Conta contábil |
| empresa_do_plano_de_contas | `codi_emp_plano` | integer(4) |  |  | Empresa do plano de contas |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `empresa_importar_saldo_das_contas_contab` (eq/in), `conta_contabil` (eq/in), `empresa_do_plano_de_contas` (eq/in)

## efoutrosdados_efd_evento_scp

**EFD Contribuições - Outros Dados - SCP** — tabela `EFOUTROSDADOS_EFD_EVENTO_SCP` (2 linhas)

EFD Contribuições - Outros Dados - SCP. 2 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SCP.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 1 empresa(s), COMPETENCIA de 2022-03-01 a 2022-03-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competaancia | `competencia` | date(4) |  |  | CompetÃªncia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| scp | `i_scp` | integer(4) |  |  | SCP |
| evento | `evento` | integer(4) |  |  | Evento |

**Filtros:** `competaancia` (eq/in), `informativo` (eq/in), `scp` (eq/in)

## efoutrosdados_planejamento_tributario_aliquota_impostos

**Outros Dados - Planejamento Tributário - Aliquota dos Impostos** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_ALIQUOTA_IMPOSTOS` (2 linhas)

Outros Dados - Planejamento Tributário - Aliquota dos Impostos. 2 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 1 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| aliquota_iss | `aliquota_iss` | numeric(5) |  |  | Aliquota ISS |
| aliquota_ipi | `aliquota_ipi` | numeric(5) |  |  | Aliquota IPI |
| aliquota_csll | `aliquota_csll` | numeric(5) |  |  | Aliquota CSLL |
| aliquota_irpj | `aliquota_irpj` | numeric(5) |  |  | Aliquota IRPJ |
| alqiuota_pis_cumulativo | `aliquota_pis` | numeric(5) |  |  | Alqiuota PIS Cumulativo |
| aliquota_cofins_cumulativo | `aliquota_cofins` | numeric(5) |  |  | Aliquota COFINS Cumulativo |
| aliquota_pis_nao_cumulativo | `aliquota_pis_nc` | numeric(5) |  |  | Aliquota PIS Não Cumulativo |
| aliquota_cofins_nao_cumulativo | `aliquota_cofins_nc` | numeric(5) |  |  | Aliquota COFINS Não Cumulativo |
| aliquota_pis_importacao | `aliquota_pis_importacao` | numeric(5) |  |  | Aliquota PIS Importação |
| aliquota_cofins_importacao | `aliquota_cofins_importacao` | numeric(5) |  |  | Aliquota COFINS Importação |
| aliquota_icms_importacao | `aliquota_icms_importacao` | numeric(5) |  |  | Aliquota ICMS Importação |
| tabela_de_icms | `i_tabela_icms` | integer(4) |  |  | Tabela de ICMS |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `tabela_de_icms` (eq/in)

## efoutrosdados_planejamento_tributario_custos_despesas_lucro_x

**Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real)** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL` (2 linhas)

Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real). 2 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 1 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| considerar_os_valores_da_folha_mensal_do | `considerar_valores_folha_mensal` | char(1) |  |  | Considerar os valores da folha mensal do módulo folha |
| forma_de_importacao_do_saldo_das_contas | `forma_importacao_saldo_contas` | char(1) |  |  | Forma de importação do saldo das contas contábeis |
| considerar_o_saldo_das_contas_contabeis | `considerar_saldo_contas_acumuladores` | char(1) |  |  | Considerar o saldo das contas contábeis informadas nos acumuladores |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `considerar_os_valores_da_folha_mensal_do` (eq/in), `forma_de_importacao_do_saldo_das_contas` (eq/in), `considerar_o_saldo_das_contas_contabeis` (eq/in)

## efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x

**Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real)** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_EMPRESAS` (2 linhas)

Outros Dados - Planejamento Tributário - Custos e Despesas (Lucro Real). 2 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `EMPRESA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 1 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| empresa_importar_saldo_das_contas_contab | `empresa` | integer(4) |  |  | Empresa - Importar saldo das contas contábeis |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `empresa_importar_saldo_das_contas_contab` (eq/in)

## efoutrosdados_planejamento_tributario_percentual_rb_simples

**Outros Dados - Planejamento Tributario - Percentual de Receita Bruta calculo Simples Nacional** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_PERCENTUAL_RB_SIMPLES_NACIONAL` (2 linhas)

Outros Dados - Planejamento Tributario - Percentual de Receita Bruta calculo Simples Nacional. 2 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s), COMPETENCIA de 2026-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 1 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| anexo | `anexo` | integer(4) |  |  | Anexo |
| secao | `secao` | integer(4) |  |  | Secao |
| tabela | `tabela` | integer(4) |  |  | Tabela |
| considerar_cfops_de | `considerar_cfop` | integer(4) |  |  | Considerar CFOPS de: |
| percentual_receita_bruta | `percentual_receita_bruta` | numeric(5) |  |  | Percentual receita bruta |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial` (eq/in)

## efoutrosdados_dirf_scp

**DIRF - Outros Dados - SCP** — tabela `EFOUTROSDADOS_DIRF_SCP` (1 linhas)

DIRF - Outros Dados - SCP. 1 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_DIRF_SCP.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, I_DIRF_SCP`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `I_DIRF_SCP asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), COMPETENCIA de 2021-01-01 a 2021-01-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competencia |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| sequencial | `i_dirf_scp` | integer(4) |  |  | Sequencial |
| cnpj 🔒 | `cnpj` | char(14) |  |  | CNPJ |
| nome | `nome` | char(150) |  |  | Nome |
| filial | `codigo_filial` | integer(4) |  |  | Filial |

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `sequencial` (eq/in), `cnpj` (eq/in), `nome` (contem/prefixo), `filial` (eq/in)

## efoutrosdados_planejamento_tributario_custos_despesas_lucro_x_x_x

**Outros Dados - Planejamento Tributário - Custos e Despesas Saldo Conta Acumulador (Lucro Real)** — tabela `EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CUSTOS_DESPESAS_LUCRO_REAL_SALDO_CONTA_ACUMULADOR_EMPRESAS` (1 linhas)

Outros Dados - Planejamento Tributário - Custos e Despesas Saldo Conta Acumulador (Lucro Real). 1 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA.

- **Chave:** `CODI_EMP, COMPETENCIA, I_INFORMATIVOS, EMPRESA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_INFORMATIVOS asc`, `EMPRESA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s), COMPETENCIA de 2027-01-01 a 2027-01-01.
- Vínculo efinformativos (efinformativos): 0 de 1 linhas sem registro relacionado (empresa 1649).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1649).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| competencia | `competencia` | date(4) |  |  | Competência |
| informativo | `i_informativos` | integer(4) |  |  | Informativo |
| empresa_importar_saldo_das_contas_contab | `empresa` | integer(4) |  |  | Empresa - Importar saldo das contas contábeis |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efinformativos` → `efinformativos` por `i_informativos` = `i_informativos`; colunas: `efinformativos_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `informativo` (eq/in), `empresa_importar_saldo_das_contas_contab` (eq/in)

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

### efoutrosdados_efd_contas_tipo_do_cst_

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_EFD_CONTAS.TIPO_CST estão no comentário do banco (2026-10-18). Distribuição: 1=3.237, 2=132.

| Código | Significado |
|---|---|
| 1 | Todos os CSTs |
| 2 | Selecionar os CSTs |

### efoutrosdados_efd_contas_tipo_do_natu

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_EFD_CONTAS.TIPO_NATUREZA_RECEITA estão no comentário do banco (2026-10-18). Distribuição: 1=3.369.

| Código | Significado |
|---|---|
| 1 | Todas as Naturezas |
| 2 | Selecionar as Naturezas |

### efoutrosdados_efd_contas_tipo_do_acum

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_EFD_CONTAS.TIPO_ACUMULADOR estão no comentário do banco (2026-10-18). Distribuição: 1=3.187, 2=182.

| Código | Significado |
|---|---|
| 1 | Todos os acumuladores |
| 2 | Selecioanr os acumuladores |

### efoutrosdados_efd_contas_tipo_do_cfop

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_EFD_CONTAS.TIPO_CFOP estão no comentário do banco (2026-10-18). Distribuição: 1=2.384, 2=985.

| Código | Significado |
|---|---|
| 1 | Todos os CFOPs |
| 2 | Selecionar os CFOPs |

### efoutrosdados_planejamento_tributario_cfops_considerados_tipo_d_debi

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CFOPS_CONSIDERADOS.TIPO estão no comentário do banco (2026-10-18). Distribuição: C=418, D=240.

| Código | Significado |
|---|---|
| D | Débito |
| C | Crédito |

### efoutrosdados_planejamento_tributario_cfops_considerados_atividade_1

Confirmado: sim

> Todos os valores observados em EFOUTROSDADOS_PLANEJAMENTO_TRIBUTARIO_CFOPS_CONSIDERADOS.ATIVIDADE estão no comentário do banco (2026-10-18). Distribuição: 1=512, 2=142, 3=4.

| Código | Significado |
|---|---|
| 1 | Comercio |
| 2 | Industria |
| 3 | Serviço |

