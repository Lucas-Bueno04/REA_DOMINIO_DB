# Modelo — Histórico da folha (salário, contrato, eventos, situação mensal)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/folha_historico.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [alteracao_salarial](#alteracao_salarial) | `foaltesal` | 27.782 | medio | empresa; um de: empregado_codigo, periodo |
| [alteracao_contratual](#alteracao_contratual) | `foempregados_alteracao_contratual` | 33.276 | medio | empresa; um de: empregado_codigo, periodo |
| [lancamento_evento_folha](#lancamento_evento_folha) | `folancamentos_eventos` | 226.043 | medio | empresa; um de: empregado_codigo, periodo |
| [situacao_mensal_empregado](#situacao_mensal_empregado) | `foafastamentos_competencia` | 429.060 | medio | empresa; um de: empregado_codigo, periodo |

## alteracao_salarial

**Alterações salariais do empregado** — tabela `foaltesal` (27.782 linhas)

Cada reajuste ou alteração de salário de um empregado: salário anterior e novo, forma da alteração, motivo, retroatividade e período. 27.825 linhas, 974 empresas, 10.976 empregados. Datas anteriores a 2000 (707 linhas) são provavelmente o valor padrão 1900-01-01.

- **Chave:** `codi_emp, i_empregados, competencia, tipo_alt_grade`
- **Empresa:** `codi_emp`
- **Período:** `competencia` · exige um de: `empregado_codigo, periodo`
- **Ordem padrão:** `competencia desc`, `i_empregados asc`

**Regras de negócio validadas:**

- Percentual: em 3.727 de 3.731 alterações de forma 3 (percentual), novo salário = salário anterior × (1 + %) com tolerância de 5 centavos. Adicionar valor: novo = anterior + valor adicionado em 107 de 107 (forma 2).
- Continuidade: nas 40 empresas com mais alterações, o salário anterior de uma alteração é igual ao novo salário da alteração anterior do mesmo empregado em 8.915 de 8.955 pares (99,6%).
- Formas de alteração: 1 (novo salário) 23.651 · 3 (percentual) 3.731 · 7 (sem legenda) 335 · 2 (adicionar valor) 107 · 6 (sem legenda) 1. Só existe o tipo 1 (normal).
- Dados suspeitos: 707 alterações têm data anterior a 2000 (valor padrão 1900-01-01), 6 têm data futura (até 2026-10-20) e 2.225 têm novo salário zero. 4.430 são retroativas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empregado_codigo | `i_empregados` | integer(4) |  |  | Empregado |
| competencia | `competencia` | date(4) |  |  | Data |
| tipo | `tipo_alt_grade` | smallint(2) |  | tipo_alteracao_salarial | Tipo da alteração salarial: (1=Normal, 2=Valor hora-aula, 3=Grade salarial, 4=Resilição Professor) |
| forma_alteracao | `forma_alteracao` | tinyint(1) |  | forma_alteracao_salarial | Forma de alteração: (1=Novo salário/2=Adicionar valor/3=Percentual de aumento/4=Nível/5=Percentual CCT/6=Valor antecipação/7=Percentual CCT/8=Percentual variável/9=Conforme índice) |
| salario_anterior 🔒 | `salario_anterior` | numeric(30) |  |  | Salario anterior |
| novo_salario 🔒 | `novo_salario` | numeric(30) |  |  | Valor |
| valor_adicionado 🔒 | `valor_adicionado` | numeric(30) |  |  | Valor adicionado |
| percentual_aumento | `perc_aumento` | numeric(30) |  |  | Percentual de aumento |
| motivo | `motivo` | integer(4) |  |  | Motivo |
| retroativo | `retroativo` | tinyint(1) |  | sim_nao_numerico | Aumento retroativo |
| retroativo_a_partir_de | `retroativo_data` | date(4) |  |  | Data retroativa |
| forma_ajuste_retroativo | `retroativo_ajuste` | tinyint(1) |  |  | Forma do ajuste: (0-4) |
| periodo_inicio | `periodo_inicio` | date(4) |  |  | Periodo inicial |
| periodo_fim | `periodo_fim` | date(4) |  |  | Periodo final |
| origem_registro | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| novo_pelo_percentual (calculada) | `salario_anterior * (1 + perc_aumento / 100)` | — | — | | Calculada pelo modelo: salario_anterior * (1 + perc_aumento / 100) |
| novo_pela_soma (calculada) | `salario_anterior + valor_adicionado` | — | — | | Calculada pelo modelo: salario_anterior + valor_adicionado |

> 🔒 **Privacidade:** Salário por empregado identificável (financeiro).

**Filtros:** `empregado_codigo` (eq/in), `competencia` (eq/entre/gte/lte), `forma_alteracao` (eq/in), `retroativo` (eq)

## alteracao_contratual

**Alterações contratuais do empregado** — tabela `foempregados_alteracao_contratual` (33.276 linhas)

Histórico das condições do contrato de cada empregado a partir de uma data: serviço, cargo, função, convenção coletiva, categoria, vínculo, salário, jornada e horas semanais. 33.339 linhas, 977 empresas, todas com salário. Usa 23 das 55 colunas (as demais são de estágio, contrato por prazo determinado e controle do eSocial).

- **Chave:** `CODI_EMP, I_EMPREGADOS, DATA_ALTERACAO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ALTERACAO` · exige um de: `empregado_codigo, periodo`
- **Ordem padrão:** `DATA_ALTERACAO desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- 33.339 linhas e todas têm salário preenchido; a data mais antiga é 1900-01-01 (valor padrão) e a mais recente 2026-10-20.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empregado_codigo | `i_empregados` | integer(4) |  |  | Código do empregado. |
| data_alteracao | `data_alteracao` | date(4) |  |  | Data da alteração. |
| servico_codigo | `i_servicos` | integer(4) |  |  | Código do serviço. |
| cargo_codigo | `i_cargos` | integer(4) |  |  | Código do cargo. |
| funcao_codigo | `i_funcao` | integer(4) |  |  | Código da função. |
| sindicato_codigo | `i_sindicatos` | integer(4) |  |  | Código da convenção coletiva |
| categoria | `categoria` | smallint(2) |  |  | Categoria. |
| vinculo | `vinculo` | smallint(2) |  |  | Vínculo empregatício. |
| tipo_horario | `tipo_horario` | smallint(2) |  |  | Tipo de horário. |
| salario 🔒 | `salario` | numeric(30) |  |  | Salário. |
| horas_semana | `horas_semana` | numeric(5) |  |  | Total de horas trabalhadas por semana. |
| carga_horaria_variavel | `carga_horaria_variavel` | smallint(2) |  | sim_nao_numerico | Carga horário variável. (0=Não/1=Sim) |
| jornada_codigo | `i_jornada` | integer(4) |  |  | Código da jornada. |
| local_trabalho_codigo | `i_local_trabalho` | integer(4) |  |  | Código do local de trabalho. |
| remuneracao_variavel_codigo | `i_remuneracao_variavel` | integer(4) |  |  | Código da remuneração variável. |
| sindicalizado | `sindicalizado` | smallint(2) |  | sim_nao_numerico | Sindicalizado. (0=Não/1=Sim) |
| categoria_esocial | `categoria_esocial_empregado` | integer(4) |  |  | Categoria eSocial do Empregado. |
| tipo_contribuinte | `tipo_contribuinte` | char(1) |  |  | Tipo contribuinte |
| fim_contrato_prazo_determinado | `data_fim_contrato_prazo_determinado` | date(4) |  |  | Data fim do contrato por prazo determinado. |
| dias_contrato_prazo_determinado | `quantidade_dias_contrato_prazo_determinado` | integer(4) |  |  | Quantidade de dias de contrato de prazo determinado |
| alvara_judicial | `alvara_judicial` | smallint(2) |  | sim_nao_numerico | Possui alvará judicial. (0=Não/1=Sim) |
| modalidade_contratacao | `modalidade_contratacao` | integer(4) |  |  | Modalidade da Contratação. |
| numero_processo | `numero_processo` | varchar(20) |  |  | Numero do processo - menor de 16 anos. |

> 🔒 **Privacidade:** Salário e cargo por empregado identificável (financeiro).

**Filtros:** `empregado_codigo` (eq/in), `data_alteracao` (eq/entre/gte/lte), `cargo_codigo` (eq/in)

## lancamento_evento_folha

**Lançamentos de eventos da folha (variáveis e fixos)** — tabela `folancamentos_eventos` (226.043 linhas)

Eventos lançados para um empregado (horas extras, faltas, comissões, descontos fixos...) com a competência inicial e final, o tipo de folha, o valor informado e a origem do lançamento. 226.061 linhas, 805 empresas. 213.860 não têm competência final (valem sem prazo).

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_EVENTOS, TIPO_PROCESSO, TIPO_LANCAMENTO, COMPETENCIA_INICIAL, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA_INICIAL` · exige um de: `empregado_codigo, periodo`
- **Ordem padrão:** `COMPETENCIA_INICIAL desc`, `I_EMPREGADOS asc`, `I_EVENTOS asc`

**Regras de negócio validadas:**

- Tipo de lançamento: mensal (1) em 203.673 e fixo (2) em 22.388. Origem: lançamento de eventos 169.827 · importação 25.772 · origem 4 (sem legenda) 17.300 · alterar cálculo 10.612 · origem 6 (sem legenda) 2.477 · origem 5 (sem legenda) 73.
- 213.860 lançamentos não têm competência final (valem até serem encerrados) e 15.291 têm valor informado zero. Dado suspeito: há competência inicial no ano 2400.
- Por tipo de folha: mensal (11) 216.286 · participação nos lucros (70) 4.323 · adiantamento (41) 3.197 · 13º (52) 1.027 · adiantamento de 13º (51) 648 · complementar (42) 580.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empregado_codigo | `i_empregados` | integer(4) |  |  | Código do empregado |
| evento_codigo | `i_eventos` | integer(4) |  |  | Código do evento |
| tipo_folha | `tipo_processo` | smallint(2) |  | tipo_folha_lancamento | Tipo do processo: 11=Mensal/31=1ª semana/32=2ª semana/33=3ª semana/34=4ª semana/35=Última semana/36=Todas as semanas/41=Adiantamento/42=Complementar/51=Adiantamento 13º salário/52=13º salário |
| tipo_lancamento | `tipo_lancamento` | smallint(2) |  | tipo_lancamento_evento | Tipo do lançamento: 1=Mensal/2=Fixo |
| competencia_inicial | `competencia_inicial` | date(4) |  |  | Competência inicial |
| competencia_final | `competencia_final` | date(4) |  |  | Competência final |
| meses_aplicaveis | `meses` | smallint(2) |  |  | Meses (Soma binária) |
| prioridade | `prioridade` | integer(4) |  |  | Prioridade do lançamento (Utilizado para definir a prioridade de lançamentos temporários originados na versão 7.4A03 ou anterior) |
| valor_informado 🔒 | `valor_informado` | numeric(13) |  |  | Valor informado |
| valor_calculado 🔒 | `valor_calculado` | numeric(13) |  |  | Valor calculado (Alterar Cálculo) |
| origem_lancamento | `origem_lancamento` | smallint(2) |  | origem_lancamento_evento | Origem do lançamento: 1=Lançamento de eventos/2=Alterar Cálculo/3=Importação de lançamentos/4=Domínio Atendimento/5=Alteração retroativa de rubricas/6=Cadastro de empregados/7=Beneficios Digital Banking/8=RPA/9=Importação API |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| competencia_alteracao | `competencia_alteracao` | date(4) |  |  | Competência da alteração. |
| data_pagamento_alteracao_calculo | `data_pagamento_altera_calculo` | date(4) |  |  | Data de pagamento gerada no altera cálculo |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `evento` → `foeventos` por `CODI_EMP` = `codi_emp` e `I_EVENTOS` = `i_eventos`; colunas: `evento_nome`

> 🔒 **Privacidade:** Valores lançados por empregado identificável (financeiro).

**Filtros:** `empregado_codigo` (eq/in), `evento_codigo` (eq/in), `tipo_folha` (eq/in), `competencia_inicial` (eq/entre/gte/lte)

## situacao_mensal_empregado

**Situação mensal do empregado (trabalhando, férias, afastado...)** — tabela `foafastamentos_competencia` (429.060 linhas)

Registra, para cada empregado e competência, em que situação ele estava (código de afastamento) e o período correspondente. ATENÇÃO: o código 1 é "Trabalhando": 400.581 de 429.093 linhas (93%) são o empregado trabalhando; os afastamentos (férias, doença, maternidade, demitido...) são a minoria. 429.093 linhas, 969 empresas.

- **Chave:** `CODI_EMP, I_EMPREGADOS, COMPETENCIA, DATA_REAL_DN, DATA_INICIO_DN`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA` · exige um de: `empregado_codigo, periodo`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`

**Regras de negócio validadas:**

- Situação 1 'Trabalhando' em 400.581 linhas; 9 'Férias' 13.319; 8 'Demitido' 10.418; 6 'Doença período superior a 15 dias' 1.130; 18 'Doença até 15 dias' 1.092; 5 'Licença maternidade' 741. Para listar só afastamentos filtre situacao_codigo diferente de 1.
- O número de dias é igual a (data fim − data início + 1) em 427.267 de 429.093 linhas.
- Dados suspeitos: competências de 1968-01 até 2028-11 (futuras) aparecem; use filtro de período.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empregado_codigo | `i_empregados` | integer(4) |  |  | CODIGO |
| competencia | `competencia` | date(4) |  |  | Competência |
| situacao_codigo | `i_afastamentos` | integer(4) |  |  | Código do afastamento referente ao tipo de afastamento da FOAFASTAMENTOS_TIPO |
| data_real | `data_real` | date(4) |  |  | Data real |
| data_inicio | `data_inicio` | date(4) |  |  | Data de início |
| data_fim | `data_fim` | date(4) |  |  | Data fim |
| numero_dias | `numero_dias` | numeric(10) |  |  | Número de dias |
| origem_registro | `origem_reg` | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `tipo` → `foafastamentos_tipos` por `I_AFASTAMENTOS` = `i_afastamentos`; colunas: `situacao_descricao`

> 🔒 **Privacidade:** A situação de afastamento pode revelar condição de saúde do empregado.

**Filtros:** `empregado_codigo` (eq/in), `competencia` (eq/entre/gte/lte), `situacao_codigo` (eq/in)

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

### tipo_alteracao_salarial

Tipo da alteração salarial (foaltesal.tipo_alt_grade)

Confirmado: parcial

> O comentário lista 1 (normal), 2 (valor hora-aula), 3 (grade salarial) e 4 (resilição de professor, truncado). Nos dados só existe 1 (27.825 linhas).

| Código | Significado |
|---|---|
| 1 | Normal |
| 2 | Valor hora-aula |
| 3 | Grade salarial |
| 4 | Resilição de professor |

### forma_alteracao_salarial

Como o novo salário foi obtido (foaltesal.forma_alteracao)

Confirmado: parcial

> O comentário está truncado depois do 3. Confirmados pelos dados: 1 = novo salário informado (23.651 linhas), 2 = adicionar valor (novo = anterior + valor adicionado, 107 de 107 linhas) e 3 = percentual de aumento (novo = anterior × (1 + %), 3.727 de 3.731). Os códigos 6 (1 linha) e 7 (335) existem nos dados e não têm legenda no banco.

| Código | Significado |
|---|---|
| 1 | Novo salário |
| 2 | Adicionar valor |
| 3 | Percentual de aumento |
| 6 | Sem legenda (1 linha) |
| 7 | Sem legenda (335 linhas) |

### tipo_lancamento_evento

Tipo do lançamento de evento (folancamentos_eventos.tipo_lancamento)

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Mensal |
| 2 | Fixo |

### origem_lancamento_evento

Origem do lançamento de evento (folancamentos_eventos.origem_lancamento)

Confirmado: parcial

> O comentário está truncado ("1=Lançamento de eventos/2=Alterar Cálculo/3=Importação de lançame..."). Em uso 1 (169.827), 3 (25.772), 4 (17.300), 2 (10.612), 6 (2.477) e 5 (73); 4, 5 e 6 sem legenda.

| Código | Significado |
|---|---|
| 1 | Lançamento de eventos |
| 2 | Alterar cálculo |
| 3 | Importação de lançamentos |
| 4 | Sem legenda |
| 5 | Sem legenda |
| 6 | Sem legenda |

### tipo_folha_lancamento

Tipo do processo (folancamentos_eventos.tipo_processo)

Confirmado: parcial

> Mesmos códigos do domínio tipo_folha do módulo folha (11 mensal, 41 adiantamento, 42 complementar, 51/52 13º, 70 PLR). Em uso 11 (216.286), 70 (4.323), 41 (3.197), 52 (1.027), 51 (648) e 42 (580).

| Código | Significado |
|---|---|
| 11 | Mensal |
| 41 | Adiantamento |
| 42 | Complementar |
| 51 | Adiantamento de 13º salário |
| 52 | 13º salário |
| 70 | Participação nos lucros |

