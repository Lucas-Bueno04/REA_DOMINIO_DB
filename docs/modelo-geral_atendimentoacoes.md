# Modelo — Geral - atendimentoacoes (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_atendimentoacoes.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

4 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geatendimentoacoes_onvio](#geatendimentoacoes_onvio) | `GEATENDIMENTOACOES_ONVIO` | 1.081.410 | grande | empresa; um de: sequencial_autoincremento |
| [geatendimentoacoes_onvio_avisos](#geatendimentoacoes_onvio_avisos) | `GEATENDIMENTOACOES_ONVIO_AVISOS` | 13.713 | medio | empresa |
| [geatendimentoacoes_erro](#geatendimentoacoes_erro) | `GEATENDIMENTOACOES_ERRO` | 1.402 | pequeno | empresa |
| [geatendimentoacoes_avisos](#geatendimentoacoes_avisos) | `GEATENDIMENTOACOES_AVISOS` | 337 | pequeno | empresa |

## geatendimentoacoes_onvio

**Ações à serem enviadas para o Onvio.** — tabela `GEATENDIMENTOACOES_ONVIO` (1.081.410 linhas)

Ações à serem enviadas para o Onvio.. 1.081.410 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—` · exige um de: `sequencial_autoincremento`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.082.429 linhas, 1.864 empresa(s).
- Vínculo geatendimentotabelastran (GEATENDIMENTOTABELASTRANSFERIR): 0 de 29 linhas sem registro relacionado (empresa 1347).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_autoincremento | `codigo` | integer(4) |  |  | Sequencial autoincremento |
| codigo_da_tabela | `codigo_tabela` | integer(4) |  |  | Código da tabela |
| acao | `acao` | tinyint(1) |  |  | 1 - Inclusão, 2 - Exclusão, 3 - Desativação, 4 - Carga Inicial, 5 - Consulta chaves Onvio |
| clausula_com_argumentos_para_geracao_de | `clausula` | varchar(512) |  |  | Cláusula com argumentos para geração de carga inicial e para versões anteriores de geração |
| tipos_de_status_3_ignorado_2_aguardando | `status` | smallint(2) |  |  | Tipos de Status (-3=Ignorado\-2=Aguardando prioridades\-1=Erro\0=Pendente\1=Concluído\2=Aviso\3=Consulta pendente\10=Ação concluida via .SQL\11=Ação concluida via contabilidade |
| endpoint_referencial_do_registro_no_onvi | `endpoint_exclusao` | varchar(512) |  |  | EndPoint referencial do registro no Onvio |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| ordem_da_tabela_no_envio | `ordem` | integer(4) |  |  | Ordem da tabela no envio |
| c_0_aplicacao_1_carga_inicial_2_reenvio | `origem_acao` | tinyint(1) |  |  | 0 - Aplicação, 1 - Carga Inicial, 2 - Reenvio de ação pai |
| coluna_que_indica_o_codigo_referente_a_f | `i_filial` | integer(4) |  |  | Coluna que indica o código referente a filial |
| coluna_que_indica_a_quantidade_de_vezes | `numero_tentativas` | integer(4) |  |  | Coluna que indica a quantidade de vezes que foi tentado enviar esta ação |
| empresa_usa_o_da_quando_a_acao_foi_proce | `empresa_usa_da` | bit(1) |  |  | Empresa usa o DA quando a ação foi processada. (0=Não usa/1=Usa) |
| codigo_do_usuario_utilizado_para_realiza | `i_confusuario` | integer(4) |  |  | Código do usuário utilizado para realizar o login específico ao enviar a ação. |
| indica_que_ocorreu_conflito_no_envio_do | `registro_conflitado` | bit(1) |  |  | Indica que ocorreu conflito no envio do registro |
| endpoint_para_consulta_de_envio_assincro | `operation_location` | varchar(512) |  |  | endpoint para consulta de envio Assíncrono |
| indica_que_a_acao_foi_enviada_com_metodo | `atualizar_registro` | bit(1) |  |  | Indica que a ação foi enviada com metodo PUT para o onvio |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geatendimentotabelastran` → `GEATENDIMENTOTABELASTRANSFERIR` por `codigo_tabela` = `codigo`; colunas: `geatendimentotabelastran_nome`

**Filtros:** `sequencial_autoincremento` (eq/in), `codigo_da_tabela` (eq/in), `clausula_com_argumentos_para_geracao_de` (contem/prefixo), `endpoint_referencial_do_registro_no_onvi` (contem/prefixo), `coluna_que_indica_o_codigo_referente_a_f` (eq/in), `codigo_do_usuario_utilizado_para_realiza` (eq/in), `endpoint_para_consulta_de_envio_assincro` (contem/prefixo)

## geatendimentoacoes_onvio_avisos

**Avisos gerados pelas ações enviadas ao Onvio.** — tabela `GEATENDIMENTOACOES_ONVIO_AVISOS` (13.713 linhas)

Avisos gerados pelas ações enviadas ao Onvio.. 13.713 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 13.713 linhas, 793 empresa(s).
- Vínculo geatendimentogrupoexecuc (GEATENDIMENTOGRUPOEXECUCAO): 0 de 9 linhas sem registro relacionado (empresa 421).
- Vínculo geatendimentotabelastran (GEATENDIMENTOTABELASTRANSFERIR): 0 de 9 linhas sem registro relacionado (empresa 421).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_autoincremento | `codigo` | integer(4) |  |  | Sequencial autoincremento |
| codigo_do_grupo | `codigo_grupo` | integer(4) |  |  | Código do grupo |
| codigo_da_tabela | `codigo_tabela` | integer(4) |  |  | Código da tabela |
| codigo_da_acao | `codigo_acao` | integer(4) |  |  | Código da ação |
| c_1_documento_ja_existe_2_documento_ja_v | `tipo_aviso` | tinyint(1) |  |  | 1 - Documento já existe, 2 - Documento já visualizado, 3 - Aviso gerado de erro, 4 - Aviso WarningCode, 5 - Avisos Gestta Processos, 6 - Proxy |
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| indica_se_o_aviso_deve_ser_mostrado | `mostrar_aviso` | bit(1) |  |  | Indica se o aviso deve ser mostrado |
| mensagem_do_aviso | `mensagem_erro` | varchar(512) |  |  | Mensagem do aviso |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geatendimentogrupoexecuc` → `GEATENDIMENTOGRUPOEXECUCAO` por `codigo_grupo` = `codigo`; colunas: `geatendimentogrupoexecuc_nome`
- `geatendimentotabelastran` → `GEATENDIMENTOTABELASTRANSFERIR` por `codigo_tabela` = `codigo`; colunas: `geatendimentotabelastran_nome`

**Filtros:** `sequencial_autoincremento` (eq/in), `codigo_do_grupo` (eq/in), `codigo_da_tabela` (eq/in), `codigo_da_acao` (eq/in), `c_1_documento_ja_existe_2_documento_ja_v` (eq/in), `mensagem_do_aviso` (contem/prefixo)

## geatendimentoacoes_erro

**Erros gerados ao tentar enviar alguma ação ao Onvio ou ao Domínio Atendimento** — tabela `GEATENDIMENTOACOES_ERRO` (1.402 linhas)

Erros gerados ao tentar enviar alguma ação ao Onvio ou ao Domínio Atendimento. 1.402 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.400 linhas, 156 empresa(s).
- Vínculo geatendimentogrupoexecuc (GEATENDIMENTOGRUPOEXECUCAO): 0 de 2 linhas sem registro relacionado (empresa 229).
- Vínculo geatendimentotabelastran (GEATENDIMENTOTABELASTRANSFERIR): 0 de 2 linhas sem registro relacionado (empresa 229).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  |  |
| codigo_grupo | `codigo_grupo` | integer(4) |  |  |  |
| codigo_tabela | `codigo_tabela` | integer(4) |  |  |  |
| codigo_acao | `codigo_acao` | integer(4) |  |  |  |
| codi_emp | `codi_emp` | integer(4) |  |  |  |
| mensagem | `mensagem` | varchar(5000) |  |  |  |
| versao_agente | `versao_agente` | varchar(20) |  |  |  |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geatendimentogrupoexecuc` → `GEATENDIMENTOGRUPOEXECUCAO` por `codigo_grupo` = `codigo`; colunas: `geatendimentogrupoexecuc_nome`
- `geatendimentotabelastran` → `GEATENDIMENTOTABELASTRANSFERIR` por `codigo_tabela` = `codigo`; colunas: `geatendimentotabelastran_nome`

**Filtros:** `codigo` (eq/in), `codigo_grupo` (eq/in), `codigo_tabela` (eq/in), `codigo_acao` (eq/in), `mensagem` (contem/prefixo), `versao_agente` (eq/in)

## geatendimentoacoes_avisos

**Avisos gerados pelas ações enviadas ao Domínio Atendimento** — tabela `GEATENDIMENTOACOES_AVISOS` (337 linhas)

Avisos gerados pelas ações enviadas ao Domínio Atendimento. 337 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 337 linhas, 145 empresa(s).
- Vínculo geatendimentogrupoexecuc (GEATENDIMENTOGRUPOEXECUCAO): 0 de 1 linhas sem registro relacionado (empresa 1021).
- Vínculo geatendimentotabelastran (GEATENDIMENTOTABELASTRANSFERIR): 0 de 1 linhas sem registro relacionado (empresa 1021).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  |  |
| codigo_grupo | `codigo_grupo` | integer(4) |  |  |  |
| codigo_tabela | `codigo_tabela` | integer(4) |  |  |  |
| codigo_acao | `codigo_acao` | integer(4) |  |  |  |
| tipo_aviso | `tipo_aviso` | integer(4) |  |  |  |
| codi_emp | `codi_emp` | integer(4) |  |  |  |
| mostrar_aviso | `mostrar_aviso` | integer(4) |  |  |  |
| mensagem_do_aviso_quando_vindo_de_erro | `mensagem_erro` | varchar(500) |  |  | Mensagem do aviso quando vindo de erro |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geatendimentogrupoexecuc` → `GEATENDIMENTOGRUPOEXECUCAO` por `codigo_grupo` = `codigo`; colunas: `geatendimentogrupoexecuc_nome`
- `geatendimentotabelastran` → `GEATENDIMENTOTABELASTRANSFERIR` por `codigo_tabela` = `codigo`; colunas: `geatendimentotabelastran_nome`

**Filtros:** `codigo` (eq/in), `codigo_grupo` (eq/in), `codigo_tabela` (eq/in), `codigo_acao` (eq/in), `tipo_aviso` (eq/in), `mensagem_do_aviso_quando_vindo_de_erro` (contem/prefixo)

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

