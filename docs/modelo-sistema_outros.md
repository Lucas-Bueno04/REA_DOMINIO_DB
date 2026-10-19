# Modelo — Sistema - outros (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/sistema_outros.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

1 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [ausituacao_inicializacao](#ausituacao_inicializacao) | `AUSITUACAO_INICIALIZACAO` | 1 | pequeno | — |

## ausituacao_inicializacao

**Tabela para sinalização da inicialização e parada da Auditoria.** — tabela `AUSITUACAO_INICIALIZACAO` (1 linhas)

Tabela para sinalização da inicialização e parada da Auditoria.. 1 linhas no catálogo; chave: SITUACAO.

- **Chave:** `SITUACAO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `SITUACAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| situacao_0_liberado_1_processando_inicia | `situacao` | smallint(2) |  |  | Situação: 0 - Liberado, 1 - Processando inicialização/parada |
| usuario_do_sistema_que_iniciou_a_auditor | `usuario` | varchar(255) |  |  | Usuario do sistema que iniciou a auditoria |
| connection_id_do_usuario_do_sistema_que | `connection_id` | integer(4) |  |  | Connection ID do usuario do sistema que iniciou a auditoria |

**Filtros:** `situacao_0_liberado_1_processando_inicia` (eq/in), `usuario_do_sistema_que_iniciou_a_auditor` (contem/prefixo)

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

