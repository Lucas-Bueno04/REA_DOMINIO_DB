# Modelo — Pessoal - controle (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/pessoal_controle.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

5 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [focontrole_atualiza_dados_rais](#focontrole_atualiza_dados_rais) | `FOCONTROLE_ATUALIZA_DADOS_RAIS` | 119.726 | medio | empresa; um de: codigo_do_controle |
| [focontrole_recalculo](#focontrole_recalculo) | `FOCONTROLE_RECALCULO` | 52.082 | medio | empresa |
| [focontrole_busca_tabelas_calculo_sgd](#focontrole_busca_tabelas_calculo_sgd) | `FOCONTROLE_BUSCA_TABELAS_CALCULO_SGD` | 15.280 | medio | — |
| [focontrole_entrega_equipamentos_protecao_individual](#focontrole_entrega_equipamentos_protecao_individual) | `FOCONTROLE_ENTREGA_EQUIPAMENTOS_PROTECAO_INDIVIDUAL` | 8 | pequeno | empresa |
| [focontrole_atualizacao_tabelas_calculo_sgd](#focontrole_atualizacao_tabelas_calculo_sgd) | `FOCONTROLE_ATUALIZACAO_TABELAS_CALCULO_SGD` | 4 | pequeno | — |

## focontrole_atualiza_dados_rais

**Controle para atualizar as tabelas da RAIS de acordo com o cálculo.** — tabela `FOCONTROLE_ATUALIZA_DADOS_RAIS` (119.726 linhas)

Controle para atualizar as tabelas da RAIS de acordo com o cálculo.. 119.726 linhas no catálogo; chave: I_CONTROLE_ATUALIZA_DADOS_RAIS.

- **Chave:** `I_CONTROLE_ATUALIZA_DADOS_RAIS`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA` · exige um de: `codigo_do_controle`
- **Ordem padrão:** `COMPETENCIA desc`, `I_CONTROLE_ATUALIZA_DADOS_RAIS asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 119.738 linhas, 866 empresa(s), COMPETENCIA de 2012-12-01 a 2026-11-01.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_controle | `i_controle_atualiza_dados_rais` | integer(4) |  |  | Código do controle. |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| competencia_do_calculo | `competencia` | date(4) |  |  | Competência do cálculo. |
| status | `status` | integer(4) |  |  | Status |

**Filtros:** `codigo_do_controle` (eq/in), `competencia_do_calculo` (entre/gte/lte)

## focontrole_recalculo

**Controle de alteração nos cálculos para recálculo** — tabela `FOCONTROLE_RECALCULO` (52.082 linhas)

Controle de alteração nos cálculos para recálculo. 52.082 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, TIPO_PROCESSO, COMPETENCIA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, TIPO_PROCESSO, COMPETENCIA`
- **Empresa:** `CODI_EMP`
- **Período:** `COMPETENCIA`
- **Ordem padrão:** `COMPETENCIA desc`, `I_EMPREGADOS asc`, `TIPO_PROCESSO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 52.112 linhas, 337 empresa(s), COMPETENCIA de 2021-05-01 a 2026-11-01.
- status_calculo: todos os valores reais estão no comentário do banco (3=46.056, 2=6.056).
- Vínculo geempre (geempre): 0 de 46 linhas sem registro relacionado (empresa 1095).
- Vínculo foempregados (foempregados): 0 de 46 linhas sem registro relacionado (empresa 1095).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado |
| tipo_de_calculo | `tipo_processo` | integer(4) |  |  | Tipo de cálculo |
| competencia | `competencia` | date(4) |  |  | Competência |
| versao_do_calculo | `versao_calculo` | integer(4) |  |  | Versão do cálculo |
| versao_do_recalculo | `versao_recalculo` | integer(4) |  |  | Versão do recálculo |
| status_calculo | `status_calculo` | smallint(2) |  | focontrole_recalculo_status_do_c | Status do cálculo (1=NOVO/2=MODIFICADO/3=PENDENTE) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `tipo_de_calculo` (eq/in), `competencia` (eq/in)

## focontrole_busca_tabelas_calculo_sgd

**Tabela de controle para buscar atualizações das tabelas de cálculo da Folha no SGD por dia.** — tabela `FOCONTROLE_BUSCA_TABELAS_CALCULO_SGD` (15.280 linhas)

Tabela de controle para buscar atualizações das tabelas de cálculo da Folha no SGD por dia.. 15.280 linhas no catálogo; chave: DATA_BUSCA, HORARIO_BUSCA, TIPO_TABELA_CALCULO.

- **Chave:** `DATA_BUSCA, HORARIO_BUSCA, TIPO_TABELA_CALCULO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_BUSCA`
- **Ordem padrão:** `DATA_BUSCA desc`, `HORARIO_BUSCA asc`, `TIPO_TABELA_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 15.284 linhas, DATA_BUSCA de 2016-05-16 a 2026-10-16.
- tipo_da_tabela_de_calculo_1_irrf_progres: todos os valores reais estão no comentário do banco (2=3.824, 1=3.823, 3=3.821, 4=3.816).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| data_da_busca | `data_busca` | date(4) |  |  | Data da busca. |
| horario_da_busca | `horario_busca` | time(8) |  |  | Horário da busca. |
| tipo_da_tabela_de_calculo_1_irrf_progres | `tipo_tabela_calculo` | smallint(2) |  | focontrole_busca_tabelas_calculo_sgd_tipo_da_tab | Tipo da tabela de cálculo. (1=IRRF Progressiva/2=INSS e Salário Família/3=Salário Mínimo/4=IRRF PLR) |

**Filtros:** `data_da_busca` (eq/in), `horario_da_busca` (eq/in), `tipo_da_tabela_de_calculo_1_irrf_progres` (eq/in)

## focontrole_entrega_equipamentos_protecao_individual

**Equipamento de proteção individual - Empregado** — tabela `FOCONTROLE_ENTREGA_EQUIPAMENTOS_PROTECAO_INDIVIDUAL` (8 linhas)

Equipamento de proteção individual - Empregado. 8 linhas no catálogo; chave: CODI_EMP, I_EMPREGADOS, I_EPI, DATA_ENTREGA.

- **Chave:** `CODI_EMP, I_EMPREGADOS, I_EPI, DATA_ENTREGA`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_VENCIMENTO`
- **Ordem padrão:** `DATA_VENCIMENTO desc`, `I_EMPREGADOS asc`, `I_EPI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 8 linhas, 1 empresa(s), DATA_VENCIMENTO de 2017-01-16 a 2017-01-16.
- Colunas expostas nulas em 100% das linhas (1): observacao.
- origem_do_registro_0_sistema_1_importaca: todos os valores reais estão no comentário do banco (0=8).
- Vínculo foempregados (foempregados): 0 de 8 linhas sem registro relacionado (empresa 603).
- Vínculo foequipamentos_protecao (FOEQUIPAMENTOS_PROTECAO_INDIVIDUAL): 0 de 8 linhas sem registro relacionado (empresa 603).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa. |
| codigo_do_empregado | `i_empregados` | integer(4) |  |  | Código do empregado. |
| codigo_do_epi | `i_epi` | integer(4) |  |  | Código do EPI. |
| data_da_entrega | `data_entrega` | date(4) |  |  | Data da entrega. |
| quantidade | `quantidade` | integer(4) |  |  | Quantidade. |
| observacao | `observacao` | varchar(150) |  |  | Observação. |
| origem_do_registro_0_sistema_1_importaca | `origem_registro` | smallint(2) |  | focontrole_entrega_equipamentos_protecao_individual_origem_do_r | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| data_de_vencimento | `data_vencimento` | date(4) |  |  | Data de vencimento. |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `foempregados` → `foempregados` por `codi_emp` = `codi_emp` e `i_empregados` = `i_empregados`; colunas: `foempregados_nome`
- `foequipamentos_protecao` → `FOEQUIPAMENTOS_PROTECAO_INDIVIDUAL` por `codi_emp` = `codi_emp` e `i_epi` = `i_epi`; colunas: `foequipamentos_protecao_nome`

**Filtros:** `codigo_do_empregado` (eq/in), `codigo_do_epi` (eq/in), `data_da_entrega` (eq/in), `data_de_vencimento` (entre/gte/lte), `observacao` (contem/prefixo)

## focontrole_atualizacao_tabelas_calculo_sgd

**Tabela de controle para verificação de novas versões das tabelas de cálculo da folha no SGD.** — tabela `FOCONTROLE_ATUALIZACAO_TABELAS_CALCULO_SGD` (4 linhas)

Tabela de controle para verificação de novas versões das tabelas de cálculo da folha no SGD.. 4 linhas no catálogo; chave: TIPO_TABELA_CALCULO.

- **Chave:** `TIPO_TABELA_CALCULO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `TIPO_TABELA_CALCULO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas.
- tipo_da_tabela_de_calculo_1_irrf_progres: todos os valores reais estão no comentário do banco (2=1, 1=1, 4=1, 3=1).
- atualizar_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=4).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| tipo_da_tabela_de_calculo_1_irrf_progres | `tipo_tabela_calculo` | smallint(2) |  | focontrole_atualizacao_tabelas_calculo_sgd_tipo_da_tab | Tipo da tabela de cálculo. (1=IRRF Progressiva/2=INSS e Salário Família/3=Salário Mínimo/4=IRRF PLR) |
| atualizar_0_nao_1_sim | `atualizar` | smallint(2) |  | focontrole_atualizacao_tabelas_calculo_sgd_atualizar_0 | Atualizar. (0=Não/1=Sim) |

**Filtros:** `tipo_da_tabela_de_calculo_1_irrf_progres` (eq/in)

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

### focontrole_recalculo_status_do_c

Confirmado: sim

> Todos os valores observados em FOCONTROLE_RECALCULO.STATUS_CALCULO estão no comentário do banco (2026-10-18). Distribuição: 3=46.056, 2=6.056.

| Código | Significado |
|---|---|
| 1 | NOVO |
| 2 | MODIFICADO |
| 3 | PENDENTE |

### focontrole_busca_tabelas_calculo_sgd_tipo_da_tab

Confirmado: sim

> Todos os valores observados em FOCONTROLE_BUSCA_TABELAS_CALCULO_SGD.TIPO_TABELA_CALCULO estão no comentário do banco (2026-10-18). Distribuição: 2=3.824, 1=3.823, 3=3.821, 4=3.816.

| Código | Significado |
|---|---|
| 1 | IRRF Progressiva |
| 2 | INSS e Salário Família |
| 3 | Salário Mínimo |
| 4 | IRRF PLR |

### focontrole_entrega_equipamentos_protecao_individual_origem_do_r

Confirmado: sim

> Todos os valores observados em FOCONTROLE_ENTREGA_EQUIPAMENTOS_PROTECAO_INDIVIDUAL.ORIGEM_REGISTRO estão no comentário do banco (2026-10-18). Distribuição: 0=8.

| Código | Significado |
|---|---|
| 0 | Sistema |
| 1 | Importação de tabelas |
| 2 | Importação de layout |

### focontrole_atualizacao_tabelas_calculo_sgd_tipo_da_tab

Confirmado: sim

> Todos os valores observados em FOCONTROLE_ATUALIZACAO_TABELAS_CALCULO_SGD.TIPO_TABELA_CALCULO estão no comentário do banco (2026-10-18). Distribuição: 2=1, 1=1, 4=1, 3=1.

| Código | Significado |
|---|---|
| 1 | IRRF Progressiva |
| 2 | INSS e Salário Família |
| 3 | Salário Mínimo |
| 4 | IRRF PLR |

### focontrole_atualizacao_tabelas_calculo_sgd_atualizar_0

Confirmado: sim

> Todos os valores observados em FOCONTROLE_ATUALIZACAO_TABELAS_CALCULO_SGD.ATUALIZAR estão no comentário do banco (2026-10-18). Distribuição: 0=4.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

