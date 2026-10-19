# Modelo — Fiscal - das (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_das.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

1 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efdas_api_envio_arquivos_json](#efdas_api_envio_arquivos_json) | `EFDAS_API_ENVIO_ARQUIVOS_JSON` | 25.498 | medio | empresa |

## efdas_api_envio_arquivos_json

**DAS Api - Envio dos Arquivos - JSON** — tabela `EFDAS_API_ENVIO_ARQUIVOS_JSON` (25.498 linhas)

DAS Api - Envio dos Arquivos - JSON. 25.498 linhas no catálogo; chave: CODI_EMP, I_ENVIO, TIPO_ARQUIVO.

- **Chave:** `CODI_EMP, I_ENVIO, TIPO_ARQUIVO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `TIPO_ARQUIVO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 25.688 linhas, 257 empresa(s).
- Vínculo efdas_api_envio_arquivos (EFDAS_API_ENVIO_ARQUIVOS): 0 de 106 linhas sem registro relacionado (empresa 1259).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_de_envio_dos_arquivos | `i_envio` | integer(4) |  |  | Código sequencial de envio dos arquivos |
| tipo_do_arquivo | `tipo_arquivo` | char(1) |  |  | Tipo do arquivo |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efdas_api_envio_arquivos` → `EFDAS_API_ENVIO_ARQUIVOS` por `codi_emp` = `codi_emp` e `i_envio` = `i_envio`; colunas: `efdas_api_envio_arquivos_nome`

**Filtros:** `codigo_sequencial_de_envio_dos_arquivos` (eq/in), `tipo_do_arquivo` (eq/in)

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

