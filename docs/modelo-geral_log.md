# Modelo — Geral - log (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_log.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [gelog_utilitarios_nota](#gelog_utilitarios_nota) | `GELOG_UTILITARIOS_NOTA` | 253.613 | medio | empresa |
| [gelog_utilitarios](#gelog_utilitarios) | `GELOG_UTILITARIOS` | 9.543 | pequeno | empresa |
| [gelog_erro_atualizacao_banco](#gelog_erro_atualizacao_banco) | `GELOG_ERRO_ATUALIZACAO_BANCO` | 4 | pequeno | — |
| [gelog_geral](#gelog_geral) | `GELOG_GERAL` | 1 | pequeno | — |

## gelog_utilitarios_nota

**Log dos Utilitários - Notas** — tabela `GELOG_UTILITARIOS_NOTA` (253.613 linhas)

Log dos Utilitários - Notas. 253.613 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL, TIPO_NOTA, CODIGO_NOTA.

- **Chave:** `CODI_EMP, SEQUENCIAL, TIPO_NOTA, CODIGO_NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`, `TIPO_NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 253.774 linhas, 458 empresa(s).
- tipo_da_nota_1_entrada_2_saida_3_servico: todos os valores reais estão no comentário do banco (3=154.981, 2=56.668, 1=42.125).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| tipo_da_nota_1_entrada_2_saida_3_servico | `tipo_nota` | integer(4) |  | gelog_utilitarios_nota_tipo_da_nota_1_entrada_2 | Tipo da Nota (1=Entrada / 2=Saída / 3=Serviço) |
| codigo_da_nota | `codigo_nota` | integer(4) |  |  | Código da Nota |

**Filtros:** `sequencial` (eq/in), `tipo_da_nota_1_entrada_2_saida_3_servico` (eq/in), `codigo_da_nota` (eq/in)

## gelog_utilitarios

**Log dos Utilitários** — tabela `GELOG_UTILITARIOS` (9.543 linhas)

Log dos Utilitários. 9.543 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL.

- **Chave:** `CODI_EMP, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9.547 linhas, 458 empresa(s).
- utilitario_1_alterar_notas_2_limpeza_arq: todos os valores reais estão no comentário do banco (1=9.547).
- Vínculo geempre (geempre): 0 de 5 linhas sem registro relacionado (empresa 1759).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| utilitario_1_alterar_notas_2_limpeza_arq | `opcao_menu` | integer(4) |  | gelog_utilitarios_utilitario_1_alterar_notas_2_l | Utilitário (1=Alterar Notas/2=Limpeza Arquivos) |
| usuario | `usuario` | varchar(128) |  |  | Usuário |
| versao | `versao` | varchar(10) |  |  | Versão |
| arquivo_de_atualizacao | `arquivo` | integer(4) |  |  | Arquivo de atualização |
| opcoes_utilizadas_na_tela | `opcoes_tela` | varchar(2000) |  |  | Opções utilizadas na tela |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `usuario` (contem/prefixo), `versao` (eq/in), `opcoes_utilizadas_na_tela` (contem/prefixo)

## gelog_erro_atualizacao_banco

**LOG DE ERRO NA ATUALIZAÇÃO DO BANCO** — tabela `GELOG_ERRO_ATUALIZACAO_BANCO` (4 linhas)

LOG DE ERRO NA ATUALIZAÇÃO DO BANCO. 4 linhas no catálogo; chave: I_NUMERO_ERRO.

- **Chave:** `I_NUMERO_ERRO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_NUMERO_ERRO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_numero_erro | `i_numero_erro` | integer(4) |  |  |  |
| versao_sistema | `versao_sistema` | varchar(40) |  |  |  |
| atualizacao | `atualizacao` | integer(4) |  |  |  |
| versao_banco | `versao_banco` | integer(4) |  |  |  |
| comando | `comando` | varchar(1024) |  |  |  |
| erro_sql | `erro_sql` | varchar(1024) |  |  |  |

**Filtros:** `i_numero_erro` (eq/in), `versao_sistema` (contem/prefixo), `comando` (contem/prefixo), `erro_sql` (contem/prefixo)

## gelog_geral

**Tabela de logs gerais do contÃ¡bil.** — tabela `GELOG_GERAL` (1 linhas)

Tabela de logs gerais do contÃ¡bil.. 1 linhas no catálogo; chave: GUID_LOG.

- **Chave:** `GUID_LOG`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `GUID_LOG asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| guid_do_registro | `guid_log` | uniqueidentifier(16) |  |  | Guid do registro. |
| c_1_erro_copiando_dll_relatorios_dw_2_ex | `tipo` | integer(4) |  |  | 1: Erro copiando dll relatorios DW. / 2: Exclusão Controle Brclient. / 3: Erro ao coletar dados de observabilidade. |
| usuario_logado | `usuario` | varchar(20) |  |  | UsuÃ¡rio logado. |
| mensagem_do_log | `mensagem_log` | varchar(5000) |  |  | Mensagem do log. |

**Filtros:** `guid_do_registro` (eq/in), `c_1_erro_copiando_dll_relatorios_dw_2_ex` (eq/in), `usuario_logado` (eq/in), `mensagem_do_log` (contem/prefixo)

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

### gelog_utilitarios_nota_tipo_da_nota_1_entrada_2

Confirmado: sim

> Todos os valores observados em GELOG_UTILITARIOS_NOTA.TIPO_NOTA estão no comentário do banco (2026-10-18). Distribuição: 3=154.981, 2=56.668, 1=42.125.

| Código | Significado |
|---|---|
| 1 | Entrada |
| 2 | Saída |
| 3 | Serviço |

### gelog_utilitarios_utilitario_1_alterar_notas_2_l

Confirmado: sim

> Todos os valores observados em GELOG_UTILITARIOS.OPCAO_MENU estão no comentário do banco (2026-10-18). Distribuição: 1=9.547.

| Código | Significado |
|---|---|
| 1 | Alterar Notas |
| 2 | Limpeza Arquivos |

