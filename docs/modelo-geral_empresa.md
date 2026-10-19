# Modelo — Geral - empresa (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_empresa.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geempresa_bloqueio_historico](#geempresa_bloqueio_historico) | `GEEMPRESA_BLOQUEIO_HISTORICO` | 4.461 | pequeno | empresa |
| [geempresa_bloqueio_restricao](#geempresa_bloqueio_restricao) | `GEEMPRESA_BLOQUEIO_RESTRICAO` | 134 | pequeno | empresa |
| [geempresa_bloqueada](#geempresa_bloqueada) | `GEEMPRESA_BLOQUEADA` | 7 | pequeno | empresa |
| [geempresa_bloqueada_escritorio](#geempresa_bloqueada_escritorio) | `GEEMPRESA_BLOQUEADA_ESCRITORIO` | 7 | pequeno | — |

## geempresa_bloqueio_historico

**Empresas bloqueadas - Históricos** — tabela `GEEMPRESA_BLOQUEIO_HISTORICO` (4.461 linhas)

Empresas bloqueadas - Históricos. 4.461 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_HISTORICO`
- **Ordem padrão:** `DATA_HISTORICO desc`, `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 4.461 linhas, 403 empresa(s), DATA_HISTORICO de 2015-12-11 a 2026-01-15.
- origem_do_historico_s_sistema_u_usuario: todos os valores reais estão no comentário do banco (S=4.389, U=72).
- situacao_b_bloqueado_d_desbloqueado: todos os valores reais estão no comentário do banco (B=2.234, D=2.227).
- Vínculo geempre (geempre): 0 de 6 linhas sem registro relacionado (empresa 1286).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| origem_do_historico_s_sistema_u_usuario | `origem` | char(1) |  | geempresa_bloqueio_historico_origem_do_historico | Origem do histórico (S=Sistema/ U=Usuário) |
| situacao_b_bloqueado_d_desbloqueado | `situacao` | char(1) |  | geempresa_bloqueio_historico_situacao_b_bloquead | Situação (B=Bloqueado/ D=Desbloqueado) |
| data | `data_historico` | date(4) |  |  | Data |
| usuario | `usuario` | varchar(30) |  |  | Usuário |
| dias_desbloquados | `dias_desbloqueados` | integer(4) |  |  | Dias desbloquados |
| data_final_do_desbloqueio | `data_final_desbloqueio` | date(4) |  |  | Data final do desbloqueio |
| obervacao | `obervacao_inadimplente` | varchar(200) |  |  | Obervação |
| historico_para_o_contrato | `historico_contrato` | varchar(200) |  |  | Histórico para o contrato |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in), `data` (entre/gte/lte), `data_final_do_desbloqueio` (entre/gte/lte), `origem_do_historico_s_sistema_u_usuario` (eq/in), `situacao_b_bloqueado_d_desbloqueado` (eq/in), `usuario` (contem/prefixo), `obervacao` (contem/prefixo), `historico_para_o_contrato` (contem/prefixo)

## geempresa_bloqueio_restricao

**Empresas que não serão bloqueadas** — tabela `GEEMPRESA_BLOQUEIO_RESTRICAO` (134 linhas)

Empresas que não serão bloqueadas. 134 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 134 linhas, 134 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1093).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in)

## geempresa_bloqueada

**Empresas bloqueadas** — tabela `GEEMPRESA_BLOQUEADA` (7 linhas)

Empresas bloqueadas. 7 linhas no catálogo; chave: I_SEQUENCIAL.

- **Chave:** `I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas, 7 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1109).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial` (eq/in)

## geempresa_bloqueada_escritorio

**Empresas bloqueadas - Escritório que bloqueou** — tabela `GEEMPRESA_BLOQUEADA_ESCRITORIO` (7 linhas)

Empresas bloqueadas - Escritório que bloqueou. 7 linhas no catálogo; chave: I_SEQUENCIAL, CODI_EMP_ESCRITORIO.

- **Chave:** `I_SEQUENCIAL, CODI_EMP_ESCRITORIO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_SEQUENCIAL asc`, `CODI_EMP_ESCRITORIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 7 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| escritorio_que_bloqueou_a_empresa | `codi_emp_escritorio` | integer(4) |  |  | Escritório que bloqueou a empresa |

**Filtros:** `sequencial` (eq/in), `escritorio_que_bloqueou_a_empresa` (eq/in)

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

### geempresa_bloqueio_historico_origem_do_historico

Confirmado: sim

> Todos os valores observados em GEEMPRESA_BLOQUEIO_HISTORICO.ORIGEM estão no comentário do banco (2026-10-18). Distribuição: S=4.389, U=72.

| Código | Significado |
|---|---|
| S | Sistema |
| U | Usuário |

### geempresa_bloqueio_historico_situacao_b_bloquead

Confirmado: sim

> Todos os valores observados em GEEMPRESA_BLOQUEIO_HISTORICO.SITUACAO estão no comentário do banco (2026-10-18). Distribuição: B=2.234, D=2.227.

| Código | Significado |
|---|---|
| B | Bloqueado |
| D | Desbloqueado |

