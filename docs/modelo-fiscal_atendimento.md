# Modelo — Fiscal - atendimento (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_atendimento.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efatendimento_nfe_catalogo](#efatendimento_nfe_catalogo) | `EFATENDIMENTO_NFE_CATALOGO` | 67.201 | medio | empresa |
| [efatendimento_nfe_xml_v2](#efatendimento_nfe_xml_v2) | `EFATENDIMENTO_NFE_XML_V2` | 51.502 | medio | — |
| [efatendimento_nfe_empresa](#efatendimento_nfe_empresa) | `EFATENDIMENTO_NFE_EMPRESA` | 1.515 | pequeno | empresa |
| [efatendimento_nfe_catalogo_log](#efatendimento_nfe_catalogo_log) | `EFATENDIMENTO_NFE_CATALOGO_LOG` | 122 | pequeno | — |
| [efatendimento_nfe_catalogo_visualizados](#efatendimento_nfe_catalogo_visualizados) | `EFATENDIMENTO_NFE_CATALOGO_VISUALIZADOS` | 38 | pequeno | empresa |
| [efatendimento_nfe_xml](#efatendimento_nfe_xml) | `EFATENDIMENTO_NFE_XML` | 27 | pequeno | — |
| [efatendimento_nfe_controle_websocket](#efatendimento_nfe_controle_websocket) | `EFATENDIMENTO_NFE_CONTROLE_WEBSOCKET` | 1 | pequeno | — |

## efatendimento_nfe_catalogo

**Catálogo de Notas - Domínio Atendimento** — tabela `EFATENDIMENTO_NFE_CATALOGO` (67.201 linhas)

Catálogo de Notas - Domínio Atendimento. 67.201 linhas no catálogo; chave: I_CATALOGO.

- **Chave:** `I_CATALOGO`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_BAIXADO`
- **Ordem padrão:** `DATA_BAIXADO desc`, `I_CATALOGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 70.445 linhas, 530 empresa(s), DATA_BAIXADO de 2017-08-17 a 2026-10-18.
- Colunas expostas nulas em 100% das linhas (7): quantidade_de_tentativas_de_envios_ao_bo, protocolo, motivo, codigo_do_processo_criado_no_auditor_asi, url_de_download_do_xml_do_complemento, data_que_o_xml_complementar_foi_baixado, parceiro.
- tipo_da_nota_1_entrada_2_saada_3_cancela: todos os valores reais estão no comentário do banco (2=30.991, 1=26.765, 4=11.256, 3=1.433).
- baixa_do_arquivo_0_download_do_xml_ainda: todos os valores reais estão no comentário do banco (1=70.445).
- importacao_do_arquivo_0_nota_ainda_nao_i: todos os valores reais estão no comentário do banco (1=41.834, 0=28.611).
- origem_xml: todos os valores reais estão no comentário do banco (1=68.953, 4=1.492).
- exclusao_do_xml_0_nao_excluido_1_excluid: todos os valores reais estão no comentário do banco (0=54.737, 1=15.708).
- baixa_do_arquivo_complementar_0_download: todos os valores reais estão no comentário do banco (0=70.445).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_catalogo | `i_catalogo` | integer(4) |  |  | Código do catálogo |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_sequencial_do_site | `sequencial` | bigint(8) |  |  | Código sequencial do site |
| tipo_da_nota_1_entrada_2_saada_3_cancela | `tipo` | smallint(2) |  | efatendimento_nfe_catalogo_tipo_da_nota | Tipo da nota (1=Entrada/2=SaÃ­da/3=Cancelamento/4=ServiÃ§o/5=Outros) |
| data_de_emissao_da_nota | `emissao` | date(4) |  |  | Data de emissão da nota |
| baixa_do_arquivo_0_download_do_xml_ainda | `baixado` | smallint(2) |  | efatendimento_nfe_catalogo_baixa_do_arq | Baixa do arquivo (0=Download do XML ainda não realizado/1=Download do XML já realizado) |
| importacao_do_arquivo_0_nota_ainda_nao_i | `importada` | smallint(2) |  | efatendimento_nfe_catalogo_importacao_d | Importação do arquivo (0=Nota ainda não importada para a Escrita/1=Nota já importada para a Escrita) |
| chave | `chave` | varchar(256) |  |  | Chave |
| data_que_o_xml_foi_baixado | `data_baixado` | date(4) |  |  | Data que o xml foi baixado |
| origem_xml | `origem_xml` | smallint(2) |  | efatendimento_nfe_catalogo_tipo_da_nota | Tipo da nota (1=Baixado automaticamente/2=Baixado pelo utilitários/3=Baixado automaticamente pela Consulta NF-e SEFAZ RS/4=Baixado automaticamente pela Importação NF-e via Web Service Portal Federal) |
| exclusao_do_xml_0_nao_excluido_1_excluid | `xml_excluido` | smallint(2) |  | efatendimento_nfe_catalogo_exclusao_do_ | Exclusão do XML (0=Não excluído/1=Excluído) |
| tipo_nota | `tipo_nota` | integer(4) |  |  | Tipo da nota (1=NFe, 2=CTe, 3=NFCe, 4=CFe, 5=Baixa de parcela, 6=NFSe, 7=Impostos Escrita, 8=Encargos Folha, 9=Pagamentos Folha, 14=NFSe Padrão Nacional) |
| flag_que_indica_se_o_registro_vem_do_da | `origem_atendimento` | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
| c_0_registro_da_antigo_1_serviao_onvio_b | `tipo_endpoint` | tinyint(1) |  |  | 0 - Registro DA antigo, 1 - ServiÃ§o Onvio Boxe, 2 - ServiÃ§o Onvio Manifesto, 3 - ServiÃ§o Onvio API, 4 - Conta Azul |
| c_0_nota_de_saida_1_nota_de_entrada_uso | `nota_entrada` | tinyint(1) |  |  | 0 - Nota de Saída, 1 - Nota de Entrada (uso interno agente de comunicação) |
| c_0_nota_regular_1_nota_cancelada_uso_in | `nota_cancelada` | tinyint(1) |  |  | 0 - Nota regular, 1 - Nota cancelada (uso interno agente de comunicação) |
| url_de_download_do_xml_da_nota | `url_xml_nota` | varchar(1024) |  |  | URL de download do XML da nota |
| url_de_download_do_xml_do_cancelamento | `url_xml_cancelamento` | varchar(1024) |  |  | URL de download do XML do cancelamento |
| c_0_nao_1_sim | `xml_excluido_manualmente` | tinyint(1) |  |  | 0 - Não, 1 - Sim |
| nota_foi_enviada_ao_box_e | `enviou_boxe` | char(1) |  |  | Nota foi enviada ao box-e |
| quantidade_de_tentativas_de_envios_ao_bo | `quantidade_tentativas_boxe` | integer(4) |  |  | Quantidade de tentativas de envios ao box-e |
| protocolo | `protocolo_boxe` | varchar(30) |  |  | Protocolo |
| motivo | `motivo_boxe` | varchar(1024) |  |  | Motivo |
| nsu_nota | `nsu_nota` | numeric(15) |  |  | NSU Nota |
| codigo_do_processo_criado_no_auditor_asi | `codigo_processo_auditor` | integer(4) |  |  | Código do processo criado no Auditor ASIS |
| status_do_arquivo_no_auditor_asis_0_igno | `status_asis` | integer(4) |  |  | Status do arquivo no Auditor ASIS (0=Ignorar,1=Pendente,2=Enviado,3=Contrato inativo) |
| url_de_download_do_xml_do_complemento | `url_xml_complemento` | varchar(1024) |  |  | URL de download do XML do complemento |
| baixa_do_arquivo_complementar_0_download | `complemento_baixado` | smallint(2) |  | efatendimento_nfe_catalogo_baixa_do_arq | Baixa do arquivo complementar (0=Download do XML ainda nÃ£o realizado/1=Download do XML jÃ¡ realizado) |
| data_que_o_xml_complementar_foi_baixado | `complemento_data_baixado` | date(4) |  |  | Data que o xml complementar foi baixado |
| parceiro | `parceiro` | varchar(50) |  |  | Parceiro |

**Filtros:** `codigo_do_catalogo` (eq/in), `data_de_emissao_da_nota` (entre/gte/lte), `data_que_o_xml_foi_baixado` (entre/gte/lte), `data_que_o_xml_complementar_foi_baixado` (entre/gte/lte), `tipo_da_nota_1_entrada_2_saada_3_cancela` (eq/in), `chave` (contem/prefixo), `tipo_nota` (eq/in), `c_0_registro_da_antigo_1_serviao_onvio_b` (eq/in), `url_de_download_do_xml_da_nota` (contem/prefixo), `url_de_download_do_xml_do_cancelamento` (contem/prefixo), `nota_foi_enviada_ao_box_e` (eq/in), `protocolo` (contem/prefixo), `motivo` (contem/prefixo), `codigo_do_processo_criado_no_auditor_asi` (eq/in)

## efatendimento_nfe_xml_v2

**XML DAS NFES - COMPRIMIDO** — tabela `EFATENDIMENTO_NFE_XML_V2` (51.502 linhas)

XML DAS NFES - COMPRIMIDO. 51.502 linhas no catálogo; chave: I_CATALOGO.

- **Chave:** `I_CATALOGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CATALOGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 54.737 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_catalogo | `i_catalogo` | integer(4) |  |  |  |

**Filtros:** `i_catalogo` (eq/in)

## efatendimento_nfe_empresa

**Dados da empresa referente a NFe - Domínio Atendimento** — tabela `EFATENDIMENTO_NFE_EMPRESA` (1.515 linhas)

Dados da empresa referente a NFe - Domínio Atendimento. 1.515 linhas no catálogo; chave: CODI_EMP.

- **Chave:** `CODI_EMP`
- **Empresa:** `CODI_EMP`
- **Período:** `DATA_ATIVACAO`
- **Ordem padrão:** `DATA_ATIVACAO desc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.517 linhas, 1.517 empresa(s), DATA_ATIVACAO de 2024-01-17 a 2024-03-18.
- ativado_0_nao_1_sim: todos os valores reais estão no comentário do banco (0=1.515, 1=2).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| data_de_ativacao_da_empresa_no_box_e | `data_ativacao` | date(4) |  |  | Data de ativação da empresa no BOX-e |
| ativado_0_nao_1_sim | `ativado` | smallint(2) |  | efatendimento_nfe_empresa_ativado_0_n | Ativado (0=Não/1=Sim) |
| flag_que_indica_se_o_registro_vem_do_da | `origem_atendimento` | integer(4) |  |  | Flag que indica se o registro vem do DA(1) ou não (0) |
| informa_se_esta_ativo_box_e_no_onvio_par | `utiliza_boxe` | bit(1) |  |  | Informa se esta ativo Box-e no Onvio para a empresa. |
| informa_se_esta_ativo_o_manifesto_no_onv | `utiliza_manifesto` | bit(1) |  |  | Informa se esta ativo o manifesto no Onvio para a empresa. |

**Filtros:** `data_de_ativacao_da_empresa_no_box_e` (entre/gte/lte)

## efatendimento_nfe_catalogo_log

**Catalogo - Log Comunicacao DA** — tabela `EFATENDIMENTO_NFE_CATALOGO_LOG` (122 linhas)

Catalogo - Log Comunicacao DA. 122 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 122 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial_do_log | `sequencial` | integer(4) |  |  | Sequencial do log |
| sequencial_da_nota | `i_catalogo` | integer(4) |  |  | Sequencial da nota |

**Filtros:** `sequencial_do_log` (eq/in), `sequencial_da_nota` (eq/in)

## efatendimento_nfe_catalogo_visualizados

**Notas já visualizadas pelos usuários - Domínio Atendimento** — tabela `EFATENDIMENTO_NFE_CATALOGO_VISUALIZADOS` (38 linhas)

Notas já visualizadas pelos usuários - Domínio Atendimento. 38 linhas no catálogo; chave: I_CONFUSUARIO, TIPO, CODI_EMP, SEQUENCIAL.

- **Chave:** `I_CONFUSUARIO, TIPO, CODI_EMP, SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_CONFUSUARIO asc`, `TIPO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 38 linhas, 3 empresa(s).
- tipo_da_configuracao_1_usuario_2_grupo: todos os valores reais estão no comentário do banco (1=38).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 53).
- Vínculo usconfusuario (usConfUsuario): 0 de 1 linhas sem registro relacionado (empresa 53).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_configuracao_do_usuario | `i_confusuario` | integer(4) |  |  | Código da configuração do usuário |
| tipo_da_configuracao_1_usuario_2_grupo | `tipo` | smallint(2) |  | efatendimento_nfe_catalogo_visualizados_tipo_da_con | Tipo da configuração (1=Usuário/2=Grupo) |
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| codigo_do_catalogo | `sequencial` | bigint(8) |  |  | Código do catálogo |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `usconfusuario` → `usConfUsuario` por `tipo` = `tipo` e `i_confusuario` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_da_configuracao_do_usuario` (eq/in), `tipo_da_configuracao_1_usuario_2_grupo` (eq/in), `codigo_do_catalogo` (eq/in)

## efatendimento_nfe_xml

**XML DAS NFES** — tabela `EFATENDIMENTO_NFE_XML` (27 linhas)

XML DAS NFES. 27 linhas no catálogo; chave: I_CATALOGO.

- **Chave:** `I_CATALOGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CATALOGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 27 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| i_catalogo | `i_catalogo` | integer(4) |  |  |  |

**Filtros:** `i_catalogo` (eq/in)

## efatendimento_nfe_controle_websocket

**EFATENDIMENTO_NFE_CONTROLE_WEBSOCKET** — tabela `EFATENDIMENTO_NFE_CONTROLE_WEBSOCKET` (1 linhas)

EFATENDIMENTO_NFE_CONTROLE_WEBSOCKET. 1 linhas no catálogo; chave: DATA_PACOTE.

- **Chave:** `DATA_PACOTE`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `DATA_PACOTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (1): data_pacote.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| data_pacote | `data_pacote` | timestamp(8) |  |  |  |

**Filtros:** `data_pacote` (eq/in)

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

### efatendimento_nfe_catalogo_tipo_da_nota

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_CATALOGO.ORIGEM_XML estão no comentário do banco (2026-10-18). Distribuição: 1=68.953, 4=1.492.

| Código | Significado |
|---|---|
| 1 | Baixado automaticamente |
| 2 | Baixado pelo utilitários |
| 3 | Baixado automaticamente pela Consulta NF-e SEFAZ RS |
| 4 | Baixado automaticamente pela Importação NF-e via Web Service Portal Federal |

### efatendimento_nfe_catalogo_baixa_do_arq

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_CATALOGO.COMPLEMENTO_BAIXADO estão no comentário do banco (2026-10-18). Distribuição: 0=70.445.

| Código | Significado |
|---|---|
| 0 | Download do XML ainda nÃ£o realizado |
| 1 | Download do XML jÃ¡ realizado |

### efatendimento_nfe_catalogo_importacao_d

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_CATALOGO.IMPORTADA estão no comentário do banco (2026-10-18). Distribuição: 1=41.834, 0=28.611.

| Código | Significado |
|---|---|
| 0 | Nota ainda não importada para a Escrita |
| 1 | Nota já importada para a Escrita |

### efatendimento_nfe_catalogo_exclusao_do_

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_CATALOGO.XML_EXCLUIDO estão no comentário do banco (2026-10-18). Distribuição: 0=54.737, 1=15.708.

| Código | Significado |
|---|---|
| 0 | Não excluído |
| 1 | Excluído |

### efatendimento_nfe_empresa_ativado_0_n

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_EMPRESA.ATIVADO estão no comentário do banco (2026-10-18). Distribuição: 0=1.515, 1=2.

| Código | Significado |
|---|---|
| 0 | Não |
| 1 | Sim |

### efatendimento_nfe_catalogo_visualizados_tipo_da_con

Confirmado: sim

> Todos os valores observados em EFATENDIMENTO_NFE_CATALOGO_VISUALIZADOS.TIPO estão no comentário do banco (2026-10-18). Distribuição: 1=38.

| Código | Significado |
|---|---|
| 1 | Usuário |
| 2 | Grupo |

