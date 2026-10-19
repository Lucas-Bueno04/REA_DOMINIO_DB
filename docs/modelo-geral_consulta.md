# Modelo — Geral - consulta (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/geral_consulta.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

7 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [geconsulta_web_service_portal_federal_catalogo](#geconsulta_web_service_portal_federal_catalogo) | `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_CATALOGO` | 1.612 | pequeno | — |
| [geconsulta_web_service_portal_federal_comunicacao](#geconsulta_web_service_portal_federal_comunicacao) | `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_COMUNICACAO` | 1.000 | pequeno | — |
| [geconsulta_busca](#geconsulta_busca) | `GECONSULTA_BUSCA` | 84 | pequeno | — |
| [geconsulta_web_service_portal_federal_erros_comunicacao](#geconsulta_web_service_portal_federal_erros_comunicacao) | `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_ERROS_COMUNICACAO` | 46 | pequeno | — |
| [geconsulta_web_service_portal_federal](#geconsulta_web_service_portal_federal) | `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL` | 1 | pequeno | — |
| [geconsulta_web_service_portal_federal_versao](#geconsulta_web_service_portal_federal_versao) | `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_VERSAO` | 1 | pequeno | — |
| [geconsulta_web_service_portal_estadual_versao](#geconsulta_web_service_portal_estadual_versao) | `GECONSULTA_WEB_SERVICE_PORTAL_ESTADUAL_VERSAO` | 1 | pequeno | — |

## geconsulta_web_service_portal_federal_catalogo

**Consulta NF-e Webservice Portal Federal - Catálogo** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_CATALOGO` (1.612 linhas)

Consulta NF-e Webservice Portal Federal - Catálogo. 1.612 linhas no catálogo; chave: I_CATALOGO.

- **Chave:** `I_CATALOGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_EMISSAO`
- **Ordem padrão:** `DATA_EMISSAO desc`, `I_CATALOGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.612 linhas, DATA_EMISSAO de 2017-05-17 a 2018-08-23.
- Colunas expostas nulas em 100% das linhas (4): nsu_da_nota, quantidade_de_tentativas_de_envios_ao_bo, protocolo, motivo.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_sequencial | `i_catalogo` | integer(4) |  |  | Código sequencial |
| cnpj_emitente 🔒 | `cnpj_emitente` | varchar(14) |  |  | CNPJ emitente |
| cnpj_destinatario 🔒 | `cnpj_destinatario` | varchar(14) |  |  | CNPJ destinatário |
| data_emissao | `data_emissao` | date(4) |  |  | Data emissão |
| situacao_manifestacao | `situacao_manifestacao` | integer(4) |  |  | Situação manifestação |
| situacao_nota | `situacao_nota` | integer(4) |  |  | Situação nota |
| cstat_manifesto | `cstat_manifesto` | integer(4) |  |  | cStat manifesto |
| xmotivo_manifesto | `xmotivo_manifesto` | varchar(256) |  |  | xMotivo manifesto |
| realizar_download | `realizar_download` | char(1) |  |  | Realizar download |
| cstat_download | `cstat_download` | integer(4) |  |  | cStat download |
| xmotivo_download | `xmotivo_download` | varchar(256) |  |  | xMotivo download |
| data_download | `data_download` | date(4) |  |  | Data download |
| enviou_box_e | `enviou_boxe` | char(1) |  |  | Enviou BOX-e |
| data_envio_ao_box_e | `data_envio` | date(4) |  |  | Data envio ao BOX-e |
| quantidade_de_tentativas_da_manifestacao | `quantidade_tentativas_manifestacao` | integer(4) |  |  | Quantidade de tentativas da manifestação |
| c_1_entrada_2_saida_4_servico | `tipo_nota` | integer(4) |  |  | 1 - Entrada / 2 - Saída / 4 - Serviço |
| nsu_da_nota | `nsu_nota` | numeric(15) |  |  | NSU da nota |
| c_1_nf_e_2_ct_e_3_nfs_e | `modelo_nota` | integer(4) |  |  | 1 - NF-e / 2 - CT-e / 3 - NFS-e |
| quantidade_de_tentativas_de_envios_ao_bo | `quantidade_tentativas_boxe` | integer(4) |  |  | Quantidade de tentativas de envios ao box-e |
| protocolo | `protocolo_boxe` | varchar(30) |  |  | Protocolo |
| motivo | `motivo_boxe` | varchar(1024) |  |  | Motivo |
| chave_nota | `chave_nota` | varchar(50) |  |  | Chave nota |

**Filtros:** `codigo_sequencial` (eq/in), `data_emissao` (entre/gte/lte), `data_download` (entre/gte/lte), `data_envio_ao_box_e` (entre/gte/lte), `cnpj_emitente` (eq/in), `cnpj_destinatario` (eq/in), `situacao_manifestacao` (eq/in), `situacao_nota` (eq/in), `xmotivo_manifesto` (contem/prefixo), `realizar_download` (eq/in), `xmotivo_download` (contem/prefixo), `enviou_box_e` (eq/in), `c_1_entrada_2_saida_4_servico` (eq/in), `protocolo` (contem/prefixo)

## geconsulta_web_service_portal_federal_comunicacao

**Consulta NF-e Webservice Portal Federal - Comunicação** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_COMUNICACAO` (1.000 linhas)

Consulta NF-e Webservice Portal Federal - Comunicação. 1.000 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_SITUACAO`
- **Ordem padrão:** `DATA_SITUACAO desc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.000 linhas, DATA_SITUACAO de 2019-02-07 a 2019-02-18.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| data_da_situacao | `data_situacao` | date(4) |  |  | Data da situação |
| situacao | `situacao` | varchar(1024) |  |  | Situação |

**Filtros:** `sequencial` (eq/in), `data_da_situacao` (entre/gte/lte), `situacao` (contem/prefixo)

## geconsulta_busca

**Configuração do modo de consulta** — tabela `GECONSULTA_BUSCA` (84 linhas)

Configuração do modo de consulta. 84 linhas no catálogo; chave: I_CONFUSUARIO, TIPO_USUARIO, I_MODULO.

- **Chave:** `I_CONFUSUARIO, TIPO_USUARIO, I_MODULO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_CONFUSUARIO asc`, `TIPO_USUARIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 84 linhas.
- Vínculo usconfusuario (usConfUsuario): 0 de 84 linhas sem registro relacionado.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_usuario | `i_confusuario` | integer(4) |  |  | Código do usuário |
| tipo_do_usuario | `tipo_usuario` | smallint(2) |  |  | Tipo do usuário |
| codigo_do_modulo | `i_modulo` | integer(4) |  |  | Código do módulo |
| c_1_pelo_inicio_da_descricao_2_em_qualqu | `modo_busca` | integer(4) |  |  | 1 = Pelo início da descrição / 2 = Em qualquer posição da descrição |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `usconfusuario` → `usConfUsuario` por `tipo_usuario` = `tipo` e `i_confusuario` = `i_confusuario`; colunas: `usconfusuario_nome`

**Filtros:** `codigo_do_usuario` (eq/in), `tipo_do_usuario` (eq/in), `codigo_do_modulo` (eq/in)

## geconsulta_web_service_portal_federal_erros_comunicacao

**Consulta NF-e Webservice Portal Federal - Erros de comunicação** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_ERROS_COMUNICACAO` (46 linhas)

Consulta NF-e Webservice Portal Federal - Erros de comunicação. 46 linhas no catálogo; chave: SEQUENCIAL.

- **Chave:** `SEQUENCIAL`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `DATA_ERRO`
- **Ordem padrão:** `DATA_ERRO desc`, `SEQUENCIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 46 linhas, DATA_ERRO de 2018-06-01 a 2018-09-26.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| sequencial | `sequencial` | integer(4) |  |  | Sequencial |
| cnpj_destinatario 🔒 | `cnpj_destinatario` | varchar(14) |  |  | CNPJ destinatário |
| data_do_erro | `data_erro` | date(4) |  |  | Data do erro |
| codigo_da_situacao | `codigo_situacao` | integer(4) |  |  | Código da situação |
| situacao | `situacao` | varchar(1024) |  |  | Situação |

**Filtros:** `sequencial` (eq/in), `data_do_erro` (entre/gte/lte), `cnpj_destinatario` (eq/in), `codigo_da_situacao` (eq/in), `situacao` (contem/prefixo)

## geconsulta_web_service_portal_federal

**Consulta NF-e Webservice Portal Federal** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL` (1 linhas)

Consulta NF-e Webservice Portal Federal. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (3): e_mail_de_retorno, endereco_do_proxy, usuario_do_proxy.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `codigo` | integer(4) |  |  | Código |
| nome_da_conexao | `nome_conexao` | varchar(128) |  |  | Nome da conexão |
| horario_para_download_do_xml | `horario_download_xml` | char(1) |  |  | Horário para download do XML |
| horario_inicio_para_download_do_xml | `horario_download_xml_inicio` | time(8) |  |  | Horário início para download do XML |
| horario_fim_para_download_do_xml | `horario_download_xml_fim` | time(8) |  |  | Horário fim para download do XML |
| envio_de_notas_para_o_box_e | `envio_boxe` | char(1) |  |  | Envio de notas para o BOX-e |
| horario_inicio_para_envio_de_notas_para | `horario_envio_boxe_inicio` | time(8) |  |  | Horário início para envio de notas para o BOX-e |
| horario_fim_para_envio_de_notas_para_o_b | `horario_envio_boxe_fim` | time(8) |  |  | Horário fim para envio de notas para o BOX-e |
| e_mail_de_retorno 🔒 | `email_retorno` | varchar(128) |  |  | E-mail de retorno |
| tipo_de_inicializacao | `tipo_inicializacao` | char(1) |  |  | Tipo de inicialização |
| iniciar_parar_agora | `iniciar_parar` | integer(4) |  |  | Iniciar / Parar agora |
| configurar_proxy | `configurar_proxy` | char(1) |  |  | Configurar proxy |
| endereco_do_proxy 🔒 | `endereco_proxy` | varchar(128) |  |  | Endereço do Proxy |
| porta_do_proxy | `porta_proxy` | integer(4) |  |  | Porta do Proxy |
| usuario_do_proxy | `usuario_proxy` | varchar(128) |  |  | Usuário do Proxy |
| numero_da_porta_a_ser_utilizada_nas_cone | `numero_porta_conexoes_entrada` | integer(4) |  |  | Número da porta a ser utilizada nas conexões de entrada |
| desativar_upnp | `desativar_upnp` | char(1) |  |  | Desativar uPnP |
| codigo_identificador_gerado_em_cima_do_n | `codigo_identificador` | varchar(50) |  |  | Código identificador gerado em cima do número de série |

**Filtros:** `codigo` (eq/in), `nome_da_conexao` (contem/prefixo), `horario_para_download_do_xml` (eq/in), `envio_de_notas_para_o_box_e` (eq/in), `e_mail_de_retorno` (contem/prefixo), `tipo_de_inicializacao` (eq/in), `configurar_proxy` (eq/in), `endereco_do_proxy` (contem/prefixo), `usuario_do_proxy` (contem/prefixo), `desativar_upnp` (eq/in), `codigo_identificador_gerado_em_cima_do_n` (contem/prefixo)

## geconsulta_web_service_portal_federal_versao

**Consulta NF-e Webservice Portal Federal - Versão** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_FEDERAL_VERSAO` (1 linhas)

Consulta NF-e Webservice Portal Federal - Versão. 1 linhas no catálogo; chave: I_VERSAO.

- **Chave:** `I_VERSAO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_VERSAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (2): versao_necessaria, versao_atual_servico.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo | `i_versao` | integer(4) |  |  | Código |
| versao_necessaria | `versao_necessaria` | varchar(20) |  |  | Versão necessária |
| versao_atual | `versao_atual` | varchar(20) |  |  | Versão atual |
| indicacao_de_que_o_programa_conseguiu_se | `conectou_servidor_principal` | integer(4) |  |  | Indicação de que o programa conseguiu se conectar ao servidor principal AWS. |
| nova_versao_baixada | `nova_versao_baixada` | integer(4) |  |  |  |
| executando_atualizacao | `executando_atualizacao` | integer(4) |  |  |  |
| versao_atual_servico | `versao_atual_servico` | varchar(20) |  |  |  |

**Filtros:** `codigo` (eq/in), `versao_necessaria` (eq/in), `versao_atual` (eq/in), `versao_atual_servico` (eq/in)

## geconsulta_web_service_portal_estadual_versao

**Tabela de controle de versão do SEFAZ RS.** — tabela `GECONSULTA_WEB_SERVICE_PORTAL_ESTADUAL_VERSAO` (1 linhas)

Tabela de controle de versão do SEFAZ RS.. 1 linhas no catálogo; chave: CODIGO.

- **Chave:** `CODIGO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `CODIGO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas.
- Colunas expostas nulas em 100% das linhas (1): versao_atual_do_sefaz_rs.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| chave_primaria_para_linha_unica | `codigo` | integer(4) |  |  | Chave primária para linha única. |
| versao_atual_do_sefaz_rs | `versao_atual` | varchar(8) |  |  | Versão atual do SEFAZ RS. |
| versao_desejada_do_sefaz_rs_pelo_contabi | `versao_desejada` | varchar(8) |  |  | Versão desejada do SEFAZ RS pelo Contábil. |

**Filtros:** `chave_primaria_para_linha_unica` (eq/in), `versao_atual_do_sefaz_rs` (eq/in), `versao_desejada_do_sefaz_rs_pelo_contabi` (eq/in)

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

