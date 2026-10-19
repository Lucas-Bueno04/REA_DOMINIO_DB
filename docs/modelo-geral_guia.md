# Modelo — Geral - guia (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_guia.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geguia_contribuicao_previdenciaria_saldos_recolher_valores_c](#geguia_contribuicao_previdenciaria_saldos_recolher_valores_c) | `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER_VALORES_COMPENSADOS` | 3.219.687 | grande | empresa; um de: competencia |
| [geguia_contribuicao_previdenciaria_saldos_recolher](#geguia_contribuicao_previdenciaria_saldos_recolher) | `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER` | 654.147 | medio | empresa |
| [geguia_contribuicao_previdenciaria_saldos_compensar](#geguia_contribuicao_previdenciaria_saldos_compensar) | `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_COMPENSAR` | 105.054 | medio | empresa |
| [geguia_contribuicao_previdenciaria](#geguia_contribuicao_previdenciaria) | `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA` | 22.483 | medio | empresa |
| [geguia_contribuicao_previdenciaria_compensacoes_dcomp](#geguia_contribuicao_previdenciaria_compensacoes_dcomp) | `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP` | 10 | pequeno | empresa |

## geguia_contribuicao_previdenciaria_saldos_recolher_valores_c

**Guia da contribuição previdenciária - Valores compensados do saldo a recolher.** — tabela `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER_VALORES_COMPENSADOS` (3.219.687 linhas)

Guia da contribuição previdenciária - Valores compensados do saldo a recolher.. 3.219.687 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_RECOLHER, TIPO_SALDO_COMPENSAR, SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_RECOLHER, TIPO_SALDO_COMPENSAR, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA` · exige um de: `competencia`
- **Ordem padrão:** `COMPETENCIA desc`, `TIPO_GUIA asc`, `TIPO_SALDO_RECOLHER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.226.507 linhas, 934 empresa(s), COMPETENCIA de 2011-04-01 a 2026-11-01.
- tipo_de_guia_1_mensal_2_13o_salario_3_tr: todos os valores reais estão no comentário do banco (3=3.134.689, 1=76.482, 2=15.336).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=3.226.507).
- Vínculo geempre (geempre): 0 de 4.125 linhas sem registro relacionado (empresa 1524).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia | `competencia` | date(4) |  |  | Competência. |
| tipo_de_guia_1_mensal_2_13o_salario_3_tr | `tipo_guia` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_recolher_valores_c_tipo_de_gui | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| tipo_de_saldo_a_recolher | `tipo_saldo_recolher` | smallint(2) |  |  | Tipo de saldo a recolher. |
| tipo_de_saldo_a_compensar | `tipo_saldo_compensar` | smallint(2) |  |  | Tipo de saldo a compensar. |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| valor_compensado | `valor_compensado` | numeric(13) |  |  |  |
| codi_emp_escrita_fiscal | `codi_emp_escrita_fiscal` | integer(4) |  |  |  |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_recolher_valores_c_origem_do_r | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp_escrita_fiscal` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `tipo_de_guia_1_mensal_2_13o_salario_3_tr` (eq/in), `tipo_de_saldo_a_recolher` (eq/in), `tipo_de_saldo_a_compensar` (eq/in), `sequencial` (eq/in), `codi_emp_escrita_fiscal` (eq/in)

## geguia_contribuicao_previdenciaria_saldos_recolher

**Guia da contribuição previdenciária - Valores de saldo a recolher.** — tabela `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER` (654.147 linhas)

Guia da contribuição previdenciária - Valores de saldo a recolher.. 654.147 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_RECOLHER, SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_RECOLHER, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `TIPO_GUIA asc`, `TIPO_SALDO_RECOLHER asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 655.511 linhas, 934 empresa(s), COMPETENCIA de 2011-04-01 a 2026-11-01.
- tipo_de_guia_1_mensal_2_13o_salario_3_tr: todos os valores reais estão no comentário do banco (3=633.540, 1=18.558, 2=3.413).
- valor_alterado_manualmente_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=654.154, 1=1.357).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=655.511).
- Vínculo geempre (geempre): 0 de 831 linhas sem registro relacionado (empresa 1071).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia | `competencia` | date(4) |  |  | Competência. |
| tipo_de_guia_1_mensal_2_13o_salario_3_tr | `tipo_guia` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_recolher_tipo_de_gui | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| tipo_saldo_recolher | `tipo_saldo_recolher` | smallint(2) |  |  | Tipo de saldo a recolher. (1=INSS Folha/2=INSS Retido (EF)/3=FUNRURAL (EF)/4=INSS Receita Bruta (EF))/5=INSS Segurado folha/6=INSS Terceiros SEST/SENAT Folha/7=IRRF Folha/8=INSS Empresa e RAT Folha/9=INSS Terceiros Folha/10=IRRF (EF)/11=IRRF PF (EF)/12=IRRF Propaganda (EF)/13=CRF (EF)/14=COFINS Ret. (EF)/15=PIS Ret. (EF)/16=CSLL Ret. (EF)/17=CRF Órgão Públicos/(EF)18=PIS Folha/19=2,30(EF)/20=4,108(EF)/21=5,109(EF)/22=6,110(EF)/23=7,111,33(EF)/24=17,106(EF)/25=19,107(EF)/26=67(EF)/27=68(EF)/28=83,168(EF)/29=84(EF)/30=85(EF)/31=86(EF)/32=87(EF)/33=88,169(EF)/34=89(EF)/35=90(EF)/36=91(EF)/37=92(EF)/38=104(EF)/39=105(EF)/40=117(EF)/41=133(EF)/42=134(EF)/43=138(EF)/44=139(EF)/45=140(EF)/46=141(EF)/47=161(EF)/48=CSLL(LALUR)/49=IRPJ(LALUR)/50=Adicional ao SENAI |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| valor_alterado_manualmente_0_nao_1_sim | `alterado_manualmente` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_recolher_valor_alter | Valor alterado manualmente. (0=Não/1=Sim) |
| valor_devido | `valor_devido` | numeric(13) |  |  |  |
| valor_compensado | `valor_compensado` | numeric(13) |  |  |  |
| saldo_recolher | `saldo_recolher` | numeric(13) |  |  |  |
| codi_emp_escrita_fiscal | `codi_emp_escrita_fiscal` | integer(4) |  |  |  |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_recolher_origem_do_r | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp_escrita_fiscal` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `tipo_de_guia_1_mensal_2_13o_salario_3_tr` (eq/in), `tipo_saldo_recolher` (eq/in), `sequencial` (eq/in), `codi_emp_escrita_fiscal` (eq/in)

## geguia_contribuicao_previdenciaria_saldos_compensar

**Guia da contribuição previdenciária  - Valores de saldo a compensar.** — tabela `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_COMPENSAR` (105.054 linhas)

Guia da contribuição previdenciária  - Valores de saldo a compensar.. 105.054 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_COMPENSAR, SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_SALDO_COMPENSAR, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `TIPO_GUIA asc`, `TIPO_SALDO_COMPENSAR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 105.199 linhas, 934 empresa(s), COMPETENCIA de 2011-04-01 a 2026-11-01.
- tipo_de_guia_1_mensal_2_13o_salario_3_tr: todos os valores reais estão no comentário do banco (3=82.960, 1=19.356, 2=2.883).
- valor_alterado_manualmente_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=105.195, 1=4).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=105.199).
- Vínculo geempre (geempre): 0 de 95 linhas sem registro relacionado (empresa 1512).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia | `competencia` | date(4) |  |  | Competência. |
| tipo_de_guia_1_mensal_2_13o_salario_3_tr | `tipo_guia` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_compensar_tipo_de_gui | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| tipo_de_saldo_a_compensar_1_compensacao | `tipo_saldo_compensar` | smallint(2) |  |  | Tipo de saldo a compensar. (1=Compensação DCOMP/2=Salário família/3=Salário maternidade/4=Retenções/5=Abater Pagamentos Anteriores |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| valor_alterado_manualmente_0_nao_1_sim | `alterado_manualmente` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_compensar_valor_alter | Valor alterado manualmente. (0=Não/1=Sim) |
| valor_compensar | `valor_compensar` | numeric(13) |  |  |  |
| valor_compensado | `valor_compensado` | numeric(13) |  |  |  |
| codi_emp_escrita_fiscal | `codi_emp_escrita_fiscal` | integer(4) |  |  |  |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | geguia_contribuicao_previdenciaria_saldos_compensar_origem_do_r | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp_escrita_fiscal` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `tipo_de_guia_1_mensal_2_13o_salario_3_tr` (eq/in), `tipo_de_saldo_a_compensar_1_compensacao` (eq/in), `sequencial` (eq/in), `codi_emp_escrita_fiscal` (eq/in)

## geguia_contribuicao_previdenciaria

**Guia da contribuição previdenciária.** — tabela `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA` (22.483 linhas)

Guia da contribuição previdenciária.. 22.483 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, TIPO_GUIA, SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, TIPO_GUIA, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `COMPETENCIA asc`, `TIPO_GUIA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 22.512 linhas, 934 empresa(s), DATA_VENCIMENTO de 1900-01-01 a 2026-12-18.
- tipo_de_guia_1_mensal_2_13o_salario_3_tr: todos os valores reais estão no comentário do banco (3=17.166, 1=4.695, 2=651).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=22.512).
- Vínculo geempre (geempre): 0 de 20 linhas sem registro relacionado (empresa 1578).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia | `competencia` | date(4) |  |  | Competência. |
| tipo_de_guia_1_mensal_2_13o_salario_3_tr | `tipo_guia` | smallint(2) |  | geguia_contribuicao_previdenciaria_tipo_de_guia_1 | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| data_vencimento | `data_vencimento` | date(4) |  |  |  |
| valor_recolher | `valor_recolher` | numeric(13) |  |  |  |
| codi_emp_escrita_fiscal | `codi_emp_escrita_fiscal` | integer(4) |  |  |  |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | geguia_contribuicao_previdenciaria_origem_do_regi | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| considerar_saldo_inferior_a_10_reais_s_n | `considerar_saldo_inferior_10_reais` | char(1) |  |  | Considerar saldo inferior a 10 reais (S/N) |
| modulo_origem_5_escrita_fiscal_12_folha | `modulo_origem` | smallint(2) |  |  | Modulo origem (5=Escrita Fiscal, 12=Folha, 0=Indefinido) |
| saldo_devedor | `saldo_devedor` | numeric(13) |  |  | Saldo devedor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `tipo_de_guia_1_mensal_2_13o_salario_3_tr` (eq/in), `sequencial` (eq/in), `data_vencimento` (entre/gte/lte), `codi_emp_escrita_fiscal` (eq/in), `considerar_saldo_inferior_a_10_reais_s_n` (eq/in)

## geguia_contribuicao_previdenciaria_compensacoes_dcomp

**Guia da contribuição previdenciária - Valores compensados do saldo a recolher.** — tabela `GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP` (10 linhas)

Guia da contribuição previdenciária - Valores compensados do saldo a recolher.. 10 linhas no catálogo; chave: CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_CREDITO, SEQUENCIAL.

- **Chave:** `CODI_EMP, COMPETENCIA, TIPO_GUIA, TIPO_CREDITO, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `TIPO_GUIA asc`, `TIPO_CREDITO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10 linhas, 7 empresa(s), COMPETENCIA de 2022-01-01 a 2025-05-01.
- Colunas expostas nulas em 100% das linhas (1): descricao_de_impostos.
- tipo_de_guia_1_mensal_2_13o_salario_3_tr: todos os valores reais estão no comentário do banco (1=10).
- tipo_de_credito_1_pagamento_indevido_ou: todos os valores reais estão no comentário do banco (2=5, 1=4, 3=1).
- origem_do_registro_0_sistema_1_imp_tabel: todos os valores reais estão no comentário do banco (0=10).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 967).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia | `competencia` | date(4) |  |  | Competência. |
| tipo_de_guia_1_mensal_2_13o_salario_3_tr | `tipo_guia` | smallint(2) |  | geguia_contribuicao_previdenciaria_compensacoes_dcomp_tipo_de_gui | Tipo de guia. (1=Mensal/2=13º salário/3=Tributos federais) |
| tipo_de_credito_1_pagamento_indevido_ou | `tipo_credito` | smallint(2) |  | geguia_contribuicao_previdenciaria_compensacoes_dcomp_tipo_de_cre | Tipo de crédito. (1=Pagamento indevido ou a maior/2=Retenções/3=Outros) |
| sequencial_unico | `sequencial` | integer(4) |  |  | sequencial unico |
| numero_da_dcomp | `numero_dcomp` | varchar(50) |  |  | Número da DCOMP. |
| valor_compensado | `valor` | numeric(13) |  |  | Valor compensado. |
| origem_do_registro_0_sistema_1_imp_tabel | `origem_registro` | smallint(2) |  | geguia_contribuicao_previdenciaria_compensacoes_dcomp_origem_do_r | Origem do registro. (0=Sistema/1=Imp. tabelas/2=Imp. layout/3=Imp. tabelas concorrentes) |
| descricao_de_impostos | `imposto_compensar` | varchar(255) |  |  | Descrição de impostos |
| resgistrando_que_salvou_a_coluna_tipo_de | `registro_salvo` | char(1) |  |  | Resgistrando que salvou a coluna Tipo de crédito DCOMP |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `competencia` (eq/in), `tipo_de_guia_1_mensal_2_13o_salario_3_tr` (eq/in), `tipo_de_credito_1_pagamento_indevido_ou` (eq/in), `sequencial_unico` (eq/in), `numero_da_dcomp` (contem/prefixo), `descricao_de_impostos` (contem/prefixo), `resgistrando_que_salvou_a_coluna_tipo_de` (eq/in)

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

### geguia_contribuicao_previdenciaria_saldos_recolher_valores_c_tipo_de_gui

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER_VALORES_COMPENSADOS.TIPO_GUIA estão no comentário do banco (2026-10-18). Distribuição: 3=3.134.689, 1=76.482, 2=15.336.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | 13º salário |
| 3 | Tributos federais |

### geguia_contribuicao_previdenciaria_saldos_recolher_valores_c_origem_do_r

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER_VALORES_COMPENSADOS.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=3.226.507.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

### geguia_contribuicao_previdenciaria_saldos_recolher_tipo_de_gui

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER.TIPO_GUIA estão no comentário do banco (2026-10-18). Distribuição: 3=633.540, 1=18.558, 2=3.413.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | 13º salário |
| 3 | Tributos federais |

### geguia_contribuicao_previdenciaria_saldos_recolher_valor_alter

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER.ALTERADO_MANUALMENTE estão no comentário do banco (2026-10-18). Distribuição: 0=654.154, 1=1.357.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### geguia_contribuicao_previdenciaria_saldos_recolher_origem_do_r

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_RECOLHER.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=655.511.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

### geguia_contribuicao_previdenciaria_saldos_compensar_tipo_de_gui

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_COMPENSAR.TIPO_GUIA estão no comentário do banco (2026-10-18). Distribuição: 3=82.960, 1=19.356, 2=2.883.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | 13º salário |
| 3 | Tributos federais |

### geguia_contribuicao_previdenciaria_saldos_compensar_valor_alter

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_COMPENSAR.ALTERADO_MANUALMENTE estão no comentário do banco (2026-10-18). Distribuição: 0=105.195, 1=4.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### geguia_contribuicao_previdenciaria_saldos_compensar_origem_do_r

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_SALDOS_COMPENSAR.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=105.199.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

### geguia_contribuicao_previdenciaria_tipo_de_guia_1

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA.TIPO_GUIA estão no comentário do banco (2026-10-18). Distribuição: 3=17.166, 1=4.695, 2=651.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | 13º salário |
| 3 | Tributos federais |

### geguia_contribuicao_previdenciaria_origem_do_regi

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=22.512.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

### geguia_contribuicao_previdenciaria_compensacoes_dcomp_tipo_de_gui

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP.TIPO_GUIA estão no comentário do banco (2026-10-18). Distribuição: 1=10.

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | 13º salário |
| 3 | Tributos federais |

### geguia_contribuicao_previdenciaria_compensacoes_dcomp_tipo_de_cre

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP.TIPO_CREDITO estão no comentário do banco (2026-10-18). Distribuição: 2=5, 1=4, 3=1.

| Código | Significado |
|---|---|
| 1 | Pagamento indevido ou a maior |
| 2 | Retenções |
| 3 | Outros |

### geguia_contribuicao_previdenciaria_compensacoes_dcomp_origem_do_r

Confirmado: sim

> Todos os valores observados em GEGUIA_CONTRIBUICAO_PREVIDENCIARIA_COMPENSACOES_DCOMP.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=10.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Imp. tabelas |
| 2 | Imp. layout |
| 3 | Imp. tabelas concorrentes |

