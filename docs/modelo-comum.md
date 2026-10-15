# Modelo — Cadastros comuns

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/comum.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

1 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [empresa](#empresa) | `geempre` | 1.969 | pequeno | empresa |

## empresa

**Empresa (cadastro)** — tabela `geempre` (1.969 linhas)

Empresas atendidas pelo escritório. 62% (1.227 de 1.969) estão INATIVAS mas continuam marcadas como usuárias dos módulos (ex.: 729 inativas ainda com 'usa escrita fiscal'); para uma lista de clientes atuais filtre `status = 'A'`.

- **Chave:** `codi_emp`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_emp asc`

**Regras de negócio validadas:**

- Situação: 742 ativas (A) e 1.227 inativas (I). Nas inativas, motivo_inatividade explica: 636 'outros', 307 transferida, 282 baixada, 2 inadimplente.
- As flags usa_* NÃO indicam uso atual: 729 empresas inativas ainda têm usa_escrita_fiscal = 1 e usa_contabilidade = 1. Combine com status = 'A'.
- Das 742 empresas ativas: 680 com CNPJ de 14 dígitos, 61 com CPF (11) e 1 sem documento.
- geempre_vigencia repete o cadastro por data de vigência, mas na prática tem 1 vigência por empresa (1.967 de 1.968) e é igual a geempre em status; não foi modelada como entidade própria.
- Escritório: tipo_honorario = 'E' marca quem fatura no módulo Honorários (3 empresas); as demais (1.966) são 'C' (cliente).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codi_emp` | integer(4) | 100% |  | Codigo |
| nome | `nome_emp` | char(40) | 100% |  | Nome |
| razao_social | `razao_emp` | varchar(255) | 100% |  | Razao Social |
| nome_fantasia | `fantasia_emp` | char(50) | 30% |  | Nome fantasia |
| apelido | `apel_emp` | char(20) | 100% |  | Apelido |
| cnpj_cpf 🔒 | `cgce_emp` | char(14) | 100% |  | CNPJ |
| tipo_inscricao | `tins_emp` | integer(4) | 100% | tipo_inscricao | Tipo da inscrição(1 - CNPJ/2 - CPF/3 - CEI/6 - CAEPF) |
| inscricao_estadual | `iest_emp` | char(22) | 17% |  | Inscricao estadual |
| inscricao_municipal | `imun_emp` | char(20) | 66% |  | Inscricao municipal |
| inscricao_junta_comercial | `ijuc_emp` | char(30) | 49% |  | Inscricao na junta comercial |
| data_inicio_atividades | `dtinicio_emp` | date(4) | 100% |  | Data de inicio das atividades |
| data_cadastro | `dcad_emp` | date(4) | 92% |  | Data do cadastramento |
| status | `stat_emp` | char(1) | 100% | status_empresa | A - Ativa / I - Inativa / C - Em Constituicao / M - Ativo sem movimento / B - Em processo de baixa / E - Excluindo |
| motivo_inatividade | `tipoi_emp` | tinyint(1) | 100% | motivo_inatividade | Motivo da inatividade da empresa(1-Outros/2-Baixada/3-Transferida/4-Inadimplente)) |
| data_inativacao | `dina_emp` | date(4) | 36% |  | Data que ficou inativo |
| natureza_juridica_codigo | `njud_emp` | integer(4) | 100% |  | Natureza juridica |
| cnae | `i_cnae20` | char(15) | 81% |  | Codigo do CNAE 2.0 |
| municipio_codigo | `codigo_municipio` | integer(4) | 82% |  | Codigo do municipio |
| cidade | `cida_emp` | char(25) | 20% |  | Cidade |
| uf | `esta_emp` | char(2) | 100% |  | Estado |
| regime_federal | `rfed_emp` | integer(4) | 93% | regime_federal_empresa | Regime federal - folha |
| enquadramento_simples | `simples_emp` | char(1) | 0% |  | Enquadramento no simples - folha |
| tipo_honorario | `honorario_tipo` | char(1) | 100% | tipo_honorario_empresa | Usar o modulo honorarios como Escritorio ou Cliente (E=Escritorio/C=Cliente) |
| numero_empregados | `empreg_emp` | integer(4) | 0% |  | Nro de empregados da empresa |
| faturamento_medio 🔒 | `vlfat_emp` | numeric(13) | 0% |  | Valor Medio do Faturamento |
| valor_honorarios 🔒 | `vlhon_emp` | numeric(13) | 0% |  | Valor dos honorarios |
| responsavel_legal 🔒 | `rleg_emp` | char(60) | 80% |  | Responsavel legal |
| usa_escrita_fiscal | `uefi_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa escrita fiscal (1 - Sim/0 - Nao) |
| usa_contabilidade | `ucta_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa contabilidade (1 - Sim/0 - Nao) |
| usa_folha | `ufol_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa folha (1 - Sim/0 - Nao) |
| usa_ponto | `upto_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa ponto (1 - Sim/0 - Nao) |
| usa_honorarios | `uhon_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa honorarios (1 - Sim/0 - Nao) |
| usa_patrimonio | `upat_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa patrimonio (1 - Sim/0 - Nao) |
| usa_lalur | `ulal_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa lalur (1 - Sim/0 - Nao) |
| usa_registro | `ureg_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa registro (1 - Sim/0 - Nao) |
| usa_livro_caixa | `ucxa_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa livro caixa (1 - Sim/0 - Nao) |
| usa_protocolo | `upro_emp` | tinyint(1) | 100% | sim_nao_numerico | Usa protocolo (1 - Sim/0 - Nao) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `municipio` → `gemunicipio` por `codigo_municipio` = `codigo_municipio`; colunas: `municipio_nome`, `municipio_ibge`
- `natureza_juridica` → `genatjuridica` por `njud_emp` = `codigo`; colunas: `natureza_juridica_descricao`
- `cnae_principal` → `gecnae20` por `i_cnae20` = `i_cnae20`; colunas: `cnae_descricao`

**Filtros:** `codigo` (eq/in), `status` (eq/in), `nome` (contem/prefixo), `cnpj_cpf` (eq), `uf` (eq/in), `tipo_inscricao` (eq/in), `usa_folha` (eq), `usa_escrita_fiscal` (eq), `usa_contabilidade` (eq)

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

