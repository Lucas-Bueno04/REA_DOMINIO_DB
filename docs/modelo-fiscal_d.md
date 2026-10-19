# Modelo — Fiscal - d (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_d.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

14 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efd_reinf_envio_arquivos_xml](#efd_reinf_envio_arquivos_xml) | `EFD_REINF_ENVIO_ARQUIVOS_XML` | 74.952 | medio | empresa |
| [efd_reinf_retorno_arquivos_r4099_periodo](#efd_reinf_retorno_arquivos_r4099_periodo) | `EFD_REINF_RETORNO_ARQUIVOS_R4099_PERIODO` | 14.304 | medio | empresa |
| [efd_reinf_retorno_arquivos_r4099](#efd_reinf_retorno_arquivos_r4099) | `EFD_REINF_RETORNO_ARQUIVOS_R4099` | 10.057 | medio | empresa |
| [efd_reinf_retorno_arquivos_r2010](#efd_reinf_retorno_arquivos_r2010) | `EFD_REINF_RETORNO_ARQUIVOS_R2010` | 2.679 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2099_r2010](#efd_reinf_retorno_arquivos_r2099_r2010) | `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2010` | 1.516 | pequeno | empresa |
| [efd_reinf_envio_arquivos_log_erros_comunicacao](#efd_reinf_envio_arquivos_log_erros_comunicacao) | `EFD_REINF_ENVIO_ARQUIVOS_LOG_ERROS_COMUNICACAO` | 1.120 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2020](#efd_reinf_retorno_arquivos_r2020) | `EFD_REINF_RETORNO_ARQUIVOS_R2020` | 554 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2099_r2020](#efd_reinf_retorno_arquivos_r2099_r2020) | `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2020` | 299 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2060](#efd_reinf_retorno_arquivos_r2060) | `EFD_REINF_RETORNO_ARQUIVOS_R2060` | 178 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2050](#efd_reinf_retorno_arquivos_r2050) | `EFD_REINF_RETORNO_ARQUIVOS_R2050` | 147 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2099_r2050](#efd_reinf_retorno_arquivos_r2099_r2050) | `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2050` | 102 | pequeno | empresa |
| [efd_reinf_retorno_arquivos_r2099_r2060](#efd_reinf_retorno_arquivos_r2099_r2060) | `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2060` | 92 | pequeno | empresa |
| [efd_reinf_retorno_xml_evento](#efd_reinf_retorno_xml_evento) | `EFD_REINF_RETORNO_XML_EVENTO` | 17 | pequeno | empresa |
| [efd_reinf_eventos](#efd_reinf_eventos) | `EFD_REINF_EVENTOS` | 12 | pequeno | — |

## efd_reinf_envio_arquivos_xml

**EFD-Reinf - Envio dos Arquivos - XML** — tabela `EFD_REINF_ENVIO_ARQUIVOS_XML` (74.952 linhas)

EFD-Reinf - Envio dos Arquivos - XML. 74.952 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 75.273 linhas, 875 empresa(s).
- arquivo_alterado_pelo_usuario_s_sim_n_na: todos os valores reais estão no comentário do banco (N=75.232, S=41).
- Vínculo efd_reinf_envio_arquivos (EFD_REINF_ENVIO_ARQUIVOS): 0 de 41 linhas sem registro relacionado (empresa 754).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_sequencial_de_envio_dos_arquivos | `i_envio` | integer(4) |  |  | Código sequencial de envio dos arquivos |
| codigo_da_filial | `i_filial` | integer(4) |  |  | Código da filial |
| arquivo_alterado_pelo_usuario_s_sim_n_na | `alterado_pelo_usuario` | char(1) |  | efd_reinf_envio_arquivos_xml_arquivo_alterado_ | Arquivo alterado pelo Usuário (S-Sim/N-Não) |
| evento_gerado_ao_enviar_para_o_auditor_f | `gerado_pelo_auditor` | char(1) |  |  | Evento gerado ao enviar para o Auditor Fiscal(S/N) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efd_reinf_envio_arquivos` → `EFD_REINF_ENVIO_ARQUIVOS` por `codi_emp` = `codi_emp` e `i_filial` = `i_filial` e `i_envio` = `i_envio`; colunas: `efd_reinf_envio_arquivos_nome`

**Filtros:** `codigo_sequencial_de_envio_dos_arquivos` (eq/in), `codigo_da_filial` (eq/in), `arquivo_alterado_pelo_usuario_s_sim_n_na` (eq/in), `evento_gerado_ao_enviar_para_o_auditor_f` (eq/in)

## efd_reinf_retorno_arquivos_r4099_periodo

**EFD-Reinf - Retorno do Web Service - R-4099 - Periodo** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R4099_PERIODO` (14.304 linhas)

EFD-Reinf - Retorno do Web Service - R-4099 - Periodo. 14.304 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, PERIODICIDADE, PERIODO, CODIGO_RECEITA.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, PERIODICIDADE, PERIODO, CODIGO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 14.382 linhas, 567 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_de_envio | `i_envio` | integer(4) |  |  | Sequencial de envio |
| filial | `i_filial` | integer(4) |  |  | Filial |
| periodicidade | `periodicidade` | integer(4) |  |  | Periodicidade |
| periodo | `periodo` | integer(4) |  |  | Periodo |
| codigo_de_receita | `codigo_receita` | char(6) |  |  | Codigo de receita |
| valor_retido | `valor_retido` | numeric(13) |  |  | Valor retido |
| valor_nao_retido | `valor_nao_retido` | numeric(13) |  |  | Valor não retido |

**Filtros:** `sequencial_de_envio` (eq/in), `filial` (eq/in), `periodicidade` (eq/in), `periodo` (eq/in), `codigo_de_receita` (eq/in)

## efd_reinf_retorno_arquivos_r4099

**EFD-Reinf - Retorno do Web Service - R-4099** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R4099` (10.057 linhas)

EFD-Reinf - Retorno do Web Service - R-4099. 10.057 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10.112 linhas, 605 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_empresa | `i_envio` | integer(4) |  |  | Sequencial empresa |
| filial | `i_filial` | integer(4) |  |  | Filial |
| indicador_se_possui_movimentacao | `possui_movimento` | char(1) |  |  | Indicador se possui movimentacao |

**Filtros:** `sequencial_empresa` (eq/in), `filial` (eq/in), `indicador_se_possui_movimentacao` (eq/in)

## efd_reinf_retorno_arquivos_r2010

**EFD-Reinf - Retorno do Web Service - R-2010** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2010` (2.679 linhas)

EFD-Reinf - Retorno do Web Service - R-2010. 2.679 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.726 linhas, 130 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_envio` | integer(4) |  |  | Sequencial |
| filial | `i_filial` | integer(4) |  |  | Filial |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| cnpj_do_prestador 🔒 | `cnpj_prestador` | varchar(14) |  |  | CNPJ do prestador |
| base_de_calculo | `base_calculo` | numeric(14) |  |  | Base de cálculo |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |
| cno | `cno` | varchar(12) |  |  | CNO |
| valor_da_contribuicao_com_exigibilidade | `valor_contribuicao_exigibilidade_suspensa` | numeric(14) |  |  | Valor da contribuição com exigibilidade suspensa |

**Filtros:** `sequencial` (eq/in), `filial` (eq/in), `codigo_da_receita` (eq/in), `cnpj_do_prestador` (eq/in), `cno` (eq/in)

## efd_reinf_retorno_arquivos_r2099_r2010

**EFD-Reinf - Retorno do Web Service - R-2099 - R-2010** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2010` (1.516 linhas)

EFD-Reinf - Retorno do Web Service - R-2099 - R-2010. 1.516 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.516 linhas, 109 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_envio | `i_envio` | integer(4) |  |  | Sequencial envio |
| filial | `i_filial` | integer(4) |  |  | Filial |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| cnpj_do_prestador 🔒 | `cnpj_prestador` | varchar(14) |  |  | CNPJ do prestador |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| base_de_calculo | `base_calculo` | numeric(14) |  |  | Base de cálculo |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |
| cno | `cno` | varchar(12) |  |  | CNO |
| valor_da_contribuicao_com_exigibilidade | `valor_contribuicao_exigibilidade_suspensa` | numeric(14) |  |  | Valor da contribuição com exigibilidade suspensa |

**Filtros:** `sequencial_envio` (eq/in), `filial` (eq/in), `sequencial` (eq/in), `cnpj_do_prestador` (eq/in), `codigo_da_receita` (eq/in), `cno` (eq/in)

## efd_reinf_envio_arquivos_log_erros_comunicacao

**EFD-Reinf - Envio dos Arquivos - Log dos Erros na Comunicação** — tabela `EFD_REINF_ENVIO_ARQUIVOS_LOG_ERROS_COMUNICACAO` (1.120 linhas)

EFD-Reinf - Envio dos Arquivos - Log dos Erros na Comunicação. 1.120 linhas no catálogo; chave: CODI_EMP, I_FILIAL, I_ENVIO, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_FILIAL, I_ENVIO, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_FILIAL asc`, `I_ENVIO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.128 linhas, 163 empresa(s).
- Vínculo efd_reinf_envio_arquivos (EFD_REINF_ENVIO_ARQUIVOS): 0 de 3 linhas sem registro relacionado (empresa 1615).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Código da empresa |
| codigo_da_empresa_filial | `i_filial` | integer(4) |  |  | Código da empresa filial |
| codigo_sequencial_de_envio_dos_arquivos | `i_envio` | integer(4) |  |  | Código sequencial de envio dos arquivos |
| codigo_sequencial_de_erros | `i_sequencial` | integer(4) |  |  | Código sequencial de erros |
| usuario | `usuario` | varchar(128) |  |  | Usuário |
| versao_do_sistema | `versao_sistema` | varchar(40) |  |  | Versão do sistema |
| arquivo_de_atualizacao | `atualizacao` | integer(4) |  |  | Arquivo de atualização |
| versao_do_banco_de_dados | `versao_banco` | integer(4) |  |  | Versão do banco de dados |
| mensagem_do_erro | `mensagem_erro` | varchar(1024) |  |  | Mensagem do erro |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efd_reinf_envio_arquivos` → `EFD_REINF_ENVIO_ARQUIVOS` por `codi_emp` = `codi_emp` e `i_filial` = `i_filial` e `i_envio` = `i_envio`; colunas: `efd_reinf_envio_arquivos_nome`

**Filtros:** `codigo_da_empresa_filial` (eq/in), `codigo_sequencial_de_envio_dos_arquivos` (eq/in), `codigo_sequencial_de_erros` (eq/in), `usuario` (contem/prefixo), `versao_do_sistema` (contem/prefixo), `mensagem_do_erro` (contem/prefixo)

## efd_reinf_retorno_arquivos_r2020

**EFD-Reinf - Retorno do Web Service - R-2020** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2020` (554 linhas)

EFD-Reinf - Retorno do Web Service - R-2020. 554 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 554 linhas, 8 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_envio` | integer(4) |  |  | Sequencial |
| filial | `i_filial` | integer(4) |  |  | Filial |
| tipo_de_inscricao_do_tomador 🔒 | `tipo_inscricao_tomador` | integer(4) |  |  | Tipo de inscrição do tomador |
| numero_de_inscricao_do_tomador 🔒 | `numero_inscricao_tomador` | varchar(14) |  |  | Número de inscrição do tomador |
| base_de_calculo | `base_calculo` | numeric(14) |  |  | Base de cálculo |
| valor_da_retencao | `valor_retencao` | numeric(14) |  |  | Valor da retenção |
| valor_adicional_da_retencao | `valor_adicional_retencao` | numeric(14) |  |  | Valor adicional da retenção |
| deducao_retencao | `valor_deducao_retencao` | numeric(14) |  |  | Dedução retenção |

**Filtros:** `sequencial` (eq/in), `filial` (eq/in), `tipo_de_inscricao_do_tomador` (eq/in), `numero_de_inscricao_do_tomador` (eq/in)

## efd_reinf_retorno_arquivos_r2099_r2020

**EFD-Reinf - Retorno do Web Service - R-2099 - R-2020** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2020` (299 linhas)

EFD-Reinf - Retorno do Web Service - R-2099 - R-2020. 299 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 299 linhas, 7 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_envio | `i_envio` | integer(4) |  |  | Sequencial envio |
| filial | `i_filial` | integer(4) |  |  | Filial |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| tipo_de_inscricao_do_tomador 🔒 | `tipo_inscricao_tomador` | integer(4) |  |  | Tipo de inscrição do tomador |
| numero_de_inscricao_do_tomador 🔒 | `numero_inscricao_tomador` | varchar(14) |  |  | Número de inscrição do tomador |
| base_de_calculo | `base_calculo` | numeric(14) |  |  | Base de cálculo |
| valor_da_retencao | `valor_retencao` | numeric(14) |  |  | Valor da retenção |
| valor_adicional_da_retencao | `valor_adicional_retencao` | numeric(14) |  |  | Valor adicional da retenção |
| deducao_retencao | `valor_deducao_retencao` | numeric(14) |  |  | Dedução retenção |

**Filtros:** `sequencial_envio` (eq/in), `filial` (eq/in), `sequencial` (eq/in), `tipo_de_inscricao_do_tomador` (eq/in), `numero_de_inscricao_do_tomador` (eq/in)

## efd_reinf_retorno_arquivos_r2060

**EFD-Reinf - Retorno do Web Service - R-2060** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2060` (178 linhas)

EFD-Reinf - Retorno do Web Service - R-2060. 178 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 178 linhas, 4 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_envio` | integer(4) |  |  | Sequencial |
| filial | `i_filial` | integer(4) |  |  | Filial |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |

**Filtros:** `sequencial` (eq/in), `filial` (eq/in), `codigo_da_receita` (eq/in)

## efd_reinf_retorno_arquivos_r2050

**EFD-Reinf - Retorno do Web Service - R-2010** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2050` (147 linhas)

EFD-Reinf - Retorno do Web Service - R-2010. 147 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, CODIGO_RECEITA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 147 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_envio` | integer(4) |  |  | Sequencial |
| filial | `i_filial` | integer(4) |  |  | Filial |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |

**Filtros:** `sequencial` (eq/in), `filial` (eq/in), `codigo_da_receita` (eq/in)

## efd_reinf_retorno_arquivos_r2099_r2050

**EFD-Reinf - Retorno do Web Service - R-2099 - R-2050** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2050` (102 linhas)

EFD-Reinf - Retorno do Web Service - R-2099 - R-2050. 102 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 102 linhas, 1 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_envio | `i_envio` | integer(4) |  |  | Sequencial envio |
| filial | `i_filial` | integer(4) |  |  | Filial |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |

**Filtros:** `sequencial_envio` (eq/in), `filial` (eq/in), `sequencial` (eq/in), `codigo_da_receita` (eq/in)

## efd_reinf_retorno_arquivos_r2099_r2060

**EFD-Reinf - Retorno do Web Service - R-2099 - R-2060** — tabela `EFD_REINF_RETORNO_ARQUIVOS_R2099_R2060` (92 linhas)

EFD-Reinf - Retorno do Web Service - R-2099 - R-2060. 92 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL, I_SEQUENCIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 92 linhas, 4 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_envio | `i_envio` | integer(4) |  |  | Sequencial envio |
| filial | `i_filial` | integer(4) |  |  | Filial |
| sequencial | `i_sequencial` | integer(4) |  |  | Sequencial |
| codigo_da_receita | `codigo_receita` | varchar(10) |  |  | Código da receita |
| valor_da_contribuicao_previdenciaria | `valor_contribuicao_previdenciaria` | numeric(14) |  |  | Valor da contribuição previdenciária |

**Filtros:** `sequencial_envio` (eq/in), `filial` (eq/in), `sequencial` (eq/in), `codigo_da_receita` (eq/in)

## efd_reinf_retorno_xml_evento

**EFD-Reinf - Arquivos XML Enviados e de Retorno** — tabela `EFD_REINF_RETORNO_XML_EVENTO` (17 linhas)

EFD-Reinf - Arquivos XML Enviados e de Retorno. 17 linhas no catálogo; chave: CODI_EMP, I_ENVIO, I_FILIAL.

- **Chave:** `CODI_EMP, I_ENVIO, I_FILIAL`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ENVIO asc`, `I_FILIAL asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 16 linhas, 11 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial | `i_envio` | integer(4) |  |  | Sequencial |
| filial | `i_filial` | integer(4) |  |  | Filial |

**Filtros:** `sequencial` (eq/in), `filial` (eq/in)

## efd_reinf_eventos

**EFD Reinf - Eventos** — tabela `EFD_REINF_EVENTOS` (12 linhas)

EFD Reinf - Eventos. 12 linhas no catálogo; chave: I_EVENTO.

- **Chave:** `I_EVENTO`
- **Empresa:** `não se aplica (tabela global)`
- **Período:** `—`
- **Ordem padrão:** `I_EVENTO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 12 linhas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_do_evento | `i_evento` | integer(4) |  |  | Código do evento |
| descicao_do_evento | `descricao` | varchar(100) |  |  | Descição do evento |

**Filtros:** `codigo_do_evento` (eq/in), `descicao_do_evento` (contem/prefixo)

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

### efd_reinf_envio_arquivos_xml_arquivo_alterado_

Confirmado: sim

> Todos os valores observados em EFD_REINF_ENVIO_ARQUIVOS_XML.ALTERADO_PELO_USUARIO estão no comentário do banco (2026-10-18). Distribuição: N=75.232, S=41.

| Código | Significado |
|---|---|
| S | Sim |
| N | Não |

