# Modelo — Fiscal - cfg (rascunho em lote)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/fiscal_cfg.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

18 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [efcfg_importacao_nfe_acumuladores_entradas_item_servico](#efcfg_importacao_nfe_acumuladores_entradas_item_servico) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_ITEM_SERVICO` | 5.080 | pequeno | empresa |
| [efcfg_importacao_nfe](#efcfg_importacao_nfe) | `efcfg_importacao_nfe` | 3.104 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_entradas](#efcfg_importacao_nfe_acumuladores_entradas) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS` | 2.939 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_servicos](#efcfg_importacao_nfe_acumuladores_servicos) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS` | 1.515 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_servicos_situacao_nota](#efcfg_importacao_nfe_acumuladores_servicos_situacao_nota) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_SITUACAO_NOTA` | 1.025 | pequeno | empresa |
| [efcfg_importacao_nfe_entradas_parcelas](#efcfg_importacao_nfe_entradas_parcelas) | `EFCFG_IMPORTACAO_NFE_ENTRADAS_PARCELAS` | 558 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_entradas_situacao_nota](#efcfg_importacao_nfe_acumuladores_entradas_situacao_nota) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_SITUACAO_NOTA` | 345 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_saidas](#efcfg_importacao_nfe_acumuladores_saidas) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SAIDAS` | 45 | pequeno | empresa |
| [efcfg_importacao_nfe_servicos_parcelas](#efcfg_importacao_nfe_servicos_parcelas) | `EFCFG_IMPORTACAO_NFE_SERVICOS_PARCELAS` | 25 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_servicos_item_servico](#efcfg_importacao_nfe_acumuladores_servicos_item_servico) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_ITEM_SERVICO` | 11 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_entradas_fornecedores_sele](#efcfg_importacao_nfe_acumuladores_entradas_fornecedores_sele) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_FORNECEDORES_SELECIONADOS` | 10 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_saidas_situacao_nota](#efcfg_importacao_nfe_acumuladores_saidas_situacao_nota) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SAIDAS_SITUACAO_NOTA` | 9 | pequeno | empresa |
| [efcfg_importacao_nfe_itens_servicos](#efcfg_importacao_nfe_itens_servicos) | `EFCFG_IMPORTACAO_NFE_ITENS_SERVICOS` | 3 | pequeno | empresa |
| [efcfg_importacao_nfe_itens_selecionar_servicos](#efcfg_importacao_nfe_itens_selecionar_servicos) | `EFCFG_IMPORTACAO_NFE_ITENS_SELECIONAR_SERVICOS` | 3 | pequeno | empresa |
| [efcfg_importacao_nfe_acumuladores_servicos_clientes_selecion](#efcfg_importacao_nfe_acumuladores_servicos_clientes_selecion) | `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_CLIENTES_SELECIONADOS` | 2 | pequeno | empresa |
| [efcfg_importacao_nfe_saidas_parcelas](#efcfg_importacao_nfe_saidas_parcelas) | `EFCFG_IMPORTACAO_NFE_SAIDAS_PARCELAS` | 1 | pequeno | empresa |
| [efcfg_importacao_nfe_itens_entradas](#efcfg_importacao_nfe_itens_entradas) | `EFCFG_IMPORTACAO_NFE_ITENS_ENTRADAS` | 1 | pequeno | empresa |
| [efcfg_importacao_nfe_itens_selecionar_entradas](#efcfg_importacao_nfe_itens_selecionar_entradas) | `EFCFG_IMPORTACAO_NFE_ITENS_SELECIONAR_ENTRADAS` | 1 | pequeno | empresa |

## efcfg_importacao_nfe_acumuladores_entradas_item_servico

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Item serviço** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_ITEM_SERVICO` (5.080 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Item serviço. 5.080 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_ITEM_SERVICO.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_ITEM_SERVICO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_ITEM_SERVICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 5.080 linhas, 350 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_do_item_do_servico | `i_item_servico` | integer(4) |  |  | Sequencial do item do serviço |
| item_do_servico | `item_servico` | integer(4) |  |  | Item do serviço |

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_do_item_do_servico` (eq/in)

## efcfg_importacao_nfe

**Configuracao de importacao da Nota Fiscal Eletronica** — tabela `efcfg_importacao_nfe` (3.104 linhas)

Configuracao de importacao da Nota Fiscal Eletronica. 3.104 linhas no catálogo; chave: codi_emp, nota.

- **Chave:** `codi_emp, nota`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `nota asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3.104 linhas, 1.036 empresa(s).
- Colunas expostas nulas em 100% das linhas (10): tipo_nota_valor_do_item, tipo_nota_importar_p_conforme_padrao_do, servico_prestado_valor_do_item, servico_prestado_importar_a_conforme_inf, situacao_nota_fiscal_valor_do_item, situacao_nf_importar, objeto_isencao_valor_do_item, objeto_isencao_importar, codigo_produto_padrao, codigo_do_produto_excecao_dos_itens.
- tipo_de_nota_1_entradas_2_saidas_3_servi: todos os valores reais estão no comentário do banco (3=1.036, 1=1.034, 2=1.034).
- tipo_nota_importar_p_conforme_padrao_do: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- servico_prestado_importar_a_conforme_inf: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- situacao_nf_importar: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- objeto_isencao_importar: coluna sem nenhum valor preenchido; o domínio do comentário do banco não pôde ser verificado.
- Vínculo efacumulador (EFACUMULADOR): 3 de 3 linhas sem registro relacionado (empresa 899).
- Vínculo geempre (geempre): 0 de 3 linhas sem registro relacionado (empresa 899).
- Vínculo efespecies (efespecies): 0 de 3 linhas sem registro relacionado (empresa 899).
- Vínculo eftabelamuni_itens (eftabelamuni_itens): 1 de 3 linhas sem registro relacionado (empresa 899).
- Vínculo efprodutos (efprodutos): 3 de 3 linhas sem registro relacionado (empresa 899).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| tipo_de_nota_1_entradas_2_saidas_3_servi | `nota` | integer(4) |  | efcfg_importacao_nfe_tipo_de_not | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| codigo_da_especie | `tipo_rps` | integer(4) |  |  | Codigo da especie |
| tipo_rpsm | `tipo_rpsm` | integer(4) |  |  | Codigo da especie |
| tipo_rpsc | `tipo_rpsc` | integer(4) |  |  | Codigo da especie |
| codigo_do_acumulador | `situacao_t` | integer(4) |  |  | Codigo do acumulador |
| situacao_i | `situacao_i` | integer(4) |  |  | Codigo do acumulador |
| situacao_f | `situacao_f` | integer(4) |  |  | Codigo do acumulador |
| situacao_c | `situacao_c` | integer(4) |  |  | Codigo do acumulador |
| situacao_e | `situacao_e` | integer(4) |  |  | Codigo do acumulador |
| situacao_j | `situacao_j` | integer(4) |  |  | Codigo do acumulador |
| codigo_do_acumulador_retido | `situacao_t_retido` | integer(4) |  |  | Código do acumulador Retido |
| tipo_nota_codigo_da_tabela_municipal | `tipo_nota_i_tabela` | integer(4) |  |  | Tipo nota - Codigo da Tabela Municipal |
| tipo_nota_valor_do_item | `tipo_nota_i_item` | char(20) |  |  | Tipo nota - Valor do item |
| tipo_nota_importar_p_conforme_padrao_do | `tipo_nota_importar` | char(1) |  | efcfg_importacao_nfe_tipo_nota_i | Tipo nota - Importar (P=Conforme padrao do acumulador/ I=Informar/ N=Nao importar) |
| servico_prestado_codigo_da_tabela_munici | `servico_prestado_i_tabela` | integer(4) |  |  | Servico Prestado - Codigo da Tabela Municipal |
| servico_prestado_valor_do_item | `servico_prestado_i_item` | char(20) |  |  | Servico Prestado - Valor do item |
| servico_prestado_importar_a_conforme_inf | `servico_prestado_importar` | char(1) |  | efcfg_importacao_nfe_servico_pre | Servico Prestado - Importar (A=Conforme informacao no arquivo/ P=Conforme informacao do acumulador/ I=Informar/ N=Nao importar) |
| situacao_nota_fiscal_codigo_da_tabela_mu | `situacao_nf_i_tabela` | integer(4) |  |  | Situacao Nota Fiscal - Codigo da Tabela Municipal |
| situacao_nota_fiscal_valor_do_item | `situacao_nf_i_item` | char(20) |  |  | Situacao Nota Fiscal - Valor do item |
| situacao_nf_importar | `situacao_nf_importar` | char(1) |  | efcfg_importacao_nfe_servico_pre | Servico Prestado - Importar (A=Conforme informacao no arquivo/ P=Conforme informacao do acumulador/ I=Informar/ N=Nao importar) |
| objeto_isencao_codigo_da_tabela_municipa | `objeto_isencao_i_tabela` | integer(4) |  |  | Objeto Isencao - Codigo da Tabela Municipal |
| objeto_isencao_valor_do_item | `objeto_isencao_i_item` | char(20) |  |  | Objeto Isencao - Valor do item |
| objeto_isencao_importar | `objeto_isencao_importar` | char(1) |  | efcfg_importacao_nfe_tipo_nota_i | Tipo nota - Importar (P=Conforme padrao do acumulador/ I=Informar/ N=Nao importar) |
| codigo_da_especie_do_documento_dispensad | `especie_doc_dispensado` | integer(4) |  |  | Código da espécie do documento dispensado |
| codigo_da_especie_do_documento_autorizad | `especie_doc_autorizado` | integer(4) |  |  | Código da espécie do documento autorizado |
| codigo_da_especie_do_documento_obrigado | `especie_doc_obrigado` | integer(4) |  |  | Código da espécie do documento obrigado |
| situacao_s | `situacao_s` | integer(4) |  |  | Codigo do acumulador |
| situacao_a | `situacao_a` | integer(4) |  |  | Codigo do acumulador |
| situacao_b | `situacao_b` | integer(4) |  |  | Codigo do acumulador |
| situacao_m | `situacao_m` | integer(4) |  |  | Codigo do acumulador |
| situacao_n | `situacao_n` | integer(4) |  |  | Codigo do acumulador |
| situacao_x | `situacao_x` | integer(4) |  |  | Codigo do acumulador |
| situacao_v | `situacao_v` | integer(4) |  |  | Codigo do acumulador |
| situacao_p | `situacao_p` | integer(4) |  |  | Codigo do acumulador |
| sobrescrever_movimentos_existentes | `sobrescrever_movimentos` | char(1) |  |  | Sobrescrever movimentos existentes |
| criar_conta_contabil_para_fornecedor_cli | `criar_conta_forcli` | char(1) |  |  | Criar conta contábil para fornecedor/cliente |
| utilizar_a_mesma_conta_do_grupo_cnpj_do 🔒 | `conta_mesmo_grupo_cnpj` | char(1) |  |  | Utilizar a mesma conta do grupo CNPJ do fornecedor/cliente |
| data_do_cadastro_do_fornecedor_cliente | `data_cadastro_forcli` | char(1) |  |  | Data do cadastro do fornecedor/cliente |
| formato_de_letras_nos_cadastros | `formato_letras_cadastros` | char(1) |  |  | Formato de letras nos cadastros |
| criar_conta_contabil_cliente | `criar_conta_cliente` | char(1) |  |  | Criar conta contábil cliente |
| criar_conta_contabil_fornecedor | `criar_conta_fornecedor` | char(1) |  |  | Criar conta contábil fornecedor |
| cliente_padrao | `codi_cli_padrao` | integer(4) |  |  | Cliente padrão |
| utilizar_o_cliente_padrao | `utilizar_cliente_padrao` | char(1) |  |  | Utilizar o cliente padrão |
| importar_o_codigo_do_servico_prestado_pa | `importar_servico_prestado_na_obs` | char(1) |  |  | Importar o código do serviço prestado para o campo observação |
| gerar_lancamentos_contabeis | `gerar_lancamentos_contabeis` | char(1) |  |  | Gerar lançamentos contábeis |
| considerar_as_definicoes_do_imposto_iss | `considerar_iss_acumulador` | char(1) |  |  | Considerar as definições do imposto ISS do cadastro do acumulador |
| considerar_os_impostos_retigos_somente_s | `considerar_impostos_retidos_somente_arquivo` | char(1) |  |  | Considerar os impostos retigos somente se estiverem informados no arquivo |
| considerar_para_a_data_da_nota | `considerar_campo_data` | char(1) |  |  | Considerar para a data da nota |
| gerar_movimento_de_produtos | `gerar_movimento_produtos` | char(1) |  |  | Gerar movimento de produtos |
| codigo_produto_padrao | `codi_pdi_padrao` | char(14) |  |  | Código produto padrão |
| definir_acumulador_para_excecao | `acumulador_excecao` | char(1) |  |  | Definir acumulador para exceção |
| codigo_do_acumulador_para_excecao | `codi_acu_excecao` | integer(4) |  |  | Código do acumulador para exceção |
| gerar_parcelas_nas_notas_fiscais_de_said | `gerar_parcelas_saidas` | varchar(1) |  |  | Gerar parcelas nas notas fiscais de saída |
| gerar_parcelas_nas_notas_fiscais_de_entr | `gerar_parcelas_entradas` | varchar(1) |  |  | Gerar parcelas nas notas fiscais de entrada |
| gerar_parcelas_nas_notas_fiscais_de_serv | `gerar_parcelas_servicos` | varchar(1) |  |  | Gerar parcelas nas notas fiscais de serviço |
| se_deve_ter_produto_excecao_dos_itens | `itens_excecao_entrada` | char(1) |  |  | Se deve ter produto exceção dos Itens |
| itens_excecao_saida | `itens_excecao_saida` | char(1) |  |  | Se deve ter produto exceção dos Itens |
| itens_excecao_servico | `itens_excecao_servico` | char(1) |  |  | Se deve ter produto exceção dos Itens |
| codigo_do_produto_excecao_dos_itens | `codi_pdi_excecao_entrada` | char(14) |  |  | Código do produto exceção dos Itens |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efacumulador` → `EFACUMULADOR` por `codi_emp` = `codi_emp` e `situacao_f` = `codi_acu`; colunas: `efacumulador_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efespecies` → `efespecies` por `tipo_rps` = `codi_esp`; colunas: `efespecies_nome`
- `eftabelamuni_itens` → `eftabelamuni_itens` por `tipo_nota_i_tabela` = `i_tabela` e `tipo_nota_i_item` = `i_item`; colunas: `eftabelamuni_itens_nome`
- `efprodutos` → `efprodutos` por `codi_emp` = `codi_emp` e `codi_pdi_excecao_entrada` = `codi_pdi`; colunas: `efprodutos_nome`

**Filtros:** `tipo_de_nota_1_entradas_2_saidas_3_servi` (eq/in), `codigo_da_especie` (eq/in), `tipo_rpsm` (eq/in), `tipo_rpsc` (eq/in), `codigo_do_acumulador` (eq/in), `situacao_i` (eq/in), `situacao_f` (eq/in), `situacao_c` (eq/in), `situacao_e` (eq/in), `situacao_j` (eq/in), `codigo_do_acumulador_retido` (eq/in), `tipo_nota_codigo_da_tabela_municipal` (eq/in), `tipo_nota_valor_do_item` (eq/in), `tipo_nota_importar_p_conforme_padrao_do` (eq/in)

## efcfg_importacao_nfe_acumuladores_entradas

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS` (2.939 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores. 2.939 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR.

- **Chave:** `CODI_EMP, I_ACUMULADOR`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2.939 linhas, 892 empresa(s).
- Vínculo geempre (geempre): 0 de 2 linhas sem registro relacionado (empresa 628).
- Vínculo efacumulador (EFACUMULADOR): 0 de 2 linhas sem registro relacionado (empresa 628).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| codigo_do_acumulador | `codi_acu` | integer(4) |  |  | Código do acumulador |
| selecao_da_situacao | `selecao_situacao` | char(1) |  |  | Seleção da situação |
| selecao_do_item_do_servico | `selecao_item_servico` | char(1) |  |  | Seleção do item do serviço |
| fornecedores_do_acumulador_t_todos_s_sel | `selecao_fornecedor` | char(1) |  |  | Fornecedores do acumulador (T = Todos, S = Selecionados) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efacumulador` → `EFACUMULADOR` por `codi_emp` = `codi_emp` e `codi_acu` = `codi_acu`; colunas: `efacumulador_nome`

**Filtros:** `sequencial_do_acumulador` (eq/in), `codigo_do_acumulador` (eq/in), `selecao_da_situacao` (eq/in), `selecao_do_item_do_servico` (eq/in), `fornecedores_do_acumulador_t_todos_s_sel` (eq/in)

## efcfg_importacao_nfe_acumuladores_servicos

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS` (1.515 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores. 1.515 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR.

- **Chave:** `CODI_EMP, I_ACUMULADOR`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.515 linhas, 697 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 691).
- Vínculo efacumulador (EFACUMULADOR): 0 de 1 linhas sem registro relacionado (empresa 691).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| codigo_do_acumulador | `codi_acu` | integer(4) |  |  | Código do acumulador |
| selecao_da_situacao | `selecao_situacao` | char(1) |  |  | Seleção da situação |
| selecao_do_item_do_servico | `selecao_item_servico` | char(1) |  |  | Seleção do item do serviço |
| clientes_do_acumulador_t_todos_s_selecio | `selecao_cliente` | char(1) |  |  | Clientes do acumulador (T = Todos, S = Selecionados) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efacumulador` → `EFACUMULADOR` por `codi_emp` = `codi_emp` e `codi_acu` = `codi_acu`; colunas: `efacumulador_nome`

**Filtros:** `sequencial_do_acumulador` (eq/in), `codigo_do_acumulador` (eq/in), `selecao_da_situacao` (eq/in), `selecao_do_item_do_servico` (eq/in), `clientes_do_acumulador_t_todos_s_selecio` (eq/in)

## efcfg_importacao_nfe_acumuladores_servicos_situacao_nota

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_SITUACAO_NOTA` (1.025 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota. 1.025 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_SITUACAO_NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1.025 linhas, 212 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_da_situacao_da_nota | `i_situacao_nota` | integer(4) |  |  | Sequencial da situação da nota |
| situacao_da_nota | `situacao_nota` | char(1) |  |  | Situação da nota |

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_da_situacao_da_nota` (eq/in), `situacao_da_nota` (eq/in)

## efcfg_importacao_nfe_entradas_parcelas

**Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas** — tabela `EFCFG_IMPORTACAO_NFE_ENTRADAS_PARCELAS` (558 linhas)

Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas. 558 linhas no catálogo; chave: CODI_EMP, NOTA.

- **Chave:** `CODI_EMP, NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 558 linhas, 558 empresa(s).
- tipo_de_nota_1_entradas_2_saidas_3_servi: todos os valores reais estão no comentário do banco (1=558).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 640).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| tipo_de_nota_1_entradas_2_saidas_3_servi | `nota` | integer(4) |  | efcfg_importacao_nfe_entradas_parcelas_tipo_de_not | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| quantidade_de_parcelas | `quantidade_parcelas` | integer(4) |  |  | Quantidade de parcelas |
| vencimento_m_mesma_data_da_nota_i_inform | `vencimento` | varchar(1) |  |  | Vencimento M-Mesma data da nota/I-Informar |
| quantidade_de_dias | `quantidade_dias` | integer(4) |  |  | Quantidade de dias |
| tipo_do_titulo_d_c_p_r | `tipo_titulo` | integer(4) |  |  | Tipo do Titulo D/C/P/R |
| identificacao_s_n | `identificacao_titulo` | varchar(255) |  |  | Identificacao S/N |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `tipo_de_nota_1_entradas_2_saidas_3_servi` (eq/in), `vencimento_m_mesma_data_da_nota_i_inform` (eq/in), `tipo_do_titulo_d_c_p_r` (eq/in), `identificacao_s_n` (contem/prefixo)

## efcfg_importacao_nfe_acumuladores_entradas_situacao_nota

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_SITUACAO_NOTA` (345 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota. 345 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_SITUACAO_NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 345 linhas, 210 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_da_situacao_da_nota | `i_situacao_nota` | integer(4) |  |  | Sequencial da situação da nota |
| situacao_da_nota | `situacao_nota` | char(1) |  |  | Situação da nota |

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_da_situacao_da_nota` (eq/in), `situacao_da_nota` (eq/in)

## efcfg_importacao_nfe_acumuladores_saidas

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SAIDAS` (45 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores. 45 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR.

- **Chave:** `CODI_EMP, I_ACUMULADOR`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 45 linhas, 38 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 939).
- Vínculo efacumulador (EFACUMULADOR): 0 de 1 linhas sem registro relacionado (empresa 939).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| codigo_do_acumulador | `codi_acu` | integer(4) |  |  | Código do acumulador |
| selecao_da_situacao | `selecao_situacao` | char(1) |  |  | Seleção da situação |
| selecao_do_item_do_servico | `selecao_item_servico` | char(1) |  |  | Seleção do item do serviço |
| clientes_do_acumulador_t_todos_s_selecio | `selecao_cliente` | char(1) |  |  | Clientes do acumulador (T = Todos, S = Selecionados) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`
- `efacumulador` → `EFACUMULADOR` por `codi_emp` = `codi_emp` e `codi_acu` = `codi_acu`; colunas: `efacumulador_nome`

**Filtros:** `sequencial_do_acumulador` (eq/in), `codigo_do_acumulador` (eq/in), `selecao_da_situacao` (eq/in), `selecao_do_item_do_servico` (eq/in), `clientes_do_acumulador_t_todos_s_selecio` (eq/in)

## efcfg_importacao_nfe_servicos_parcelas

**Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas** — tabela `EFCFG_IMPORTACAO_NFE_SERVICOS_PARCELAS` (25 linhas)

Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas. 25 linhas no catálogo; chave: CODI_EMP, NOTA.

- **Chave:** `CODI_EMP, NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 25 linhas, 25 empresa(s).
- tipo_de_nota_1_entradas_2_saidas_3_servi: todos os valores reais estão no comentário do banco (3=25).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 57).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| tipo_de_nota_1_entradas_2_saidas_3_servi | `nota` | integer(4) |  | efcfg_importacao_nfe_servicos_parcelas_tipo_de_not | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| quantidade_de_parcelas | `quantidade_parcelas` | integer(4) |  |  | Quantidade de parcelas |
| vencimento_m_mesma_data_da_nota_i_inform | `vencimento` | varchar(1) |  |  | Vencimento M-Mesma data da nota/I-Informar |
| quantidade_de_dias | `quantidade_dias` | integer(4) |  |  | Quantidade de dias |
| tipo_do_titulo_d_c_p_r | `tipo_titulo` | integer(4) |  |  | Tipo do Titulo D/C/P/R |
| identificacao_s_n | `identificacao_titulo` | varchar(255) |  |  | Identificacao S/N |
| gerar_n_do_titulo_s_n | `gerar_numero_titulo` | varchar(1) |  |  | Gerar n. do titulo S/N |
| tipo_do_numero_do_titulo_n_mesmo_numero | `tipo_numero_titulo` | varchar(1) |  |  | Tipo do numero do titulo N-Mesmo número do documento/D-Mesma data de emissao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `tipo_de_nota_1_entradas_2_saidas_3_servi` (eq/in), `vencimento_m_mesma_data_da_nota_i_inform` (eq/in), `tipo_do_titulo_d_c_p_r` (eq/in), `identificacao_s_n` (contem/prefixo), `gerar_n_do_titulo_s_n` (eq/in), `tipo_do_numero_do_titulo_n_mesmo_numero` (eq/in)

## efcfg_importacao_nfe_acumuladores_servicos_item_servico

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Item serviço** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_ITEM_SERVICO` (11 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Item serviço. 11 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_ITEM_SERVICO.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_ITEM_SERVICO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_ITEM_SERVICO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 11 linhas, 6 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_do_item_do_servico | `i_item_servico` | integer(4) |  |  | Sequencial do item do serviço |
| item_do_servico | `item_servico` | integer(4) |  |  | Item do serviço |

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_do_item_do_servico` (eq/in)

## efcfg_importacao_nfe_acumuladores_entradas_fornecedores_sele

**Configuracao de importacao de NFS-e Paulistana - Acumuladores - Definição de fornecedores selecionados** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_ENTRADAS_FORNECEDORES_SELECIONADOS` (10 linhas)

Configuracao de importacao de NFS-e Paulistana - Acumuladores - Definição de fornecedores selecionados. 10 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_FORNECEDOR.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_FORNECEDOR`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_FORNECEDOR asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 10 linhas, 3 empresa(s).
- Vínculo effornece (effornece): 0 de 2 linhas sem registro relacionado (empresa 954).
- Vínculo geempre (geempre): 0 de 2 linhas sem registro relacionado (empresa 954).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_do_fornecedor | `i_fornecedor` | integer(4) |  |  | Sequencial do fornecedor |
| codigo_do_fornecedor | `codi_for` | integer(4) |  |  | Código do Fornecedor |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `effornece` → `effornece` por `codi_emp` = `codi_emp` e `codi_for` = `codi_for`; colunas: `effornece_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_do_fornecedor` (eq/in), `codigo_do_fornecedor` (eq/in)

## efcfg_importacao_nfe_acumuladores_saidas_situacao_nota

**Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SAIDAS_SITUACAO_NOTA` (9 linhas)

Configuracao de importacao da Nota Fiscal Eletronica - Acumuladores - Situação da Nota. 9 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_SITUACAO_NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_SITUACAO_NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 9 linhas, 4 empresa(s).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_da_situacao_da_nota | `i_situacao_nota` | integer(4) |  |  | Sequencial da situação da nota |
| situacao_da_nota | `situacao_nota` | char(1) |  |  | Situação da nota |

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_da_situacao_da_nota` (eq/in), `situacao_da_nota` (eq/in)

## efcfg_importacao_nfe_itens_servicos

**Importação NFS-e Paulistana - Serviço - Relacionamento de itens** — tabela `EFCFG_IMPORTACAO_NFE_ITENS_SERVICOS` (3 linhas)

Importação NFS-e Paulistana - Serviço - Relacionamento de itens. 3 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL_PDI.

- **Chave:** `CODI_EMP, SEQUENCIAL_PDI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL_PDI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 3 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1446).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_produto | `sequencial_pdi` | integer(4) |  |  | Sequencial do Produto |
| produto | `codi_pdi` | char(14) |  |  | Produto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_produto` (eq/in), `produto` (eq/in)

## efcfg_importacao_nfe_itens_selecionar_servicos

**Importação NFS-e Paulistana - Serviço - Inclusão de Item serviço** — tabela `EFCFG_IMPORTACAO_NFE_ITENS_SELECIONAR_SERVICOS` (3 linhas)

Importação NFS-e Paulistana - Serviço - Inclusão de Item serviço. 3 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL_PDI, SEQUENCIAL_INCLUSAO.

- **Chave:** `CODI_EMP, SEQUENCIAL_PDI, SEQUENCIAL_INCLUSAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL_PDI asc`, `SEQUENCIAL_INCLUSAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 3 linhas, 3 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1446).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_pai | `sequencial_pdi` | integer(4) |  |  | Sequencial do pai |
| sequencial_do_item_servico | `sequencial_inclusao` | integer(4) |  |  | Sequencial do item serviço |
| codigo_da_inclusao_de_item_servico | `codigo_inclusao` | integer(4) |  |  | Código da inclusão de item serviço |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_pai` (eq/in), `sequencial_do_item_servico` (eq/in), `codigo_da_inclusao_de_item_servico` (eq/in)

## efcfg_importacao_nfe_acumuladores_servicos_clientes_selecion

**Configuracao de importacao de NFS-e Paulistana - Acumuladores - Definição de clientes selecionados** — tabela `EFCFG_IMPORTACAO_NFE_ACUMULADORES_SERVICOS_CLIENTES_SELECIONADOS` (2 linhas)

Configuracao de importacao de NFS-e Paulistana - Acumuladores - Definição de clientes selecionados. 2 linhas no catálogo; chave: CODI_EMP, I_ACUMULADOR, I_CLIENTE.

- **Chave:** `CODI_EMP, I_ACUMULADOR, I_CLIENTE`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `I_ACUMULADOR asc`, `I_CLIENTE asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 2 linhas, 2 empresa(s).
- Vínculo efclientes (efclientes): 0 de 1 linhas sem registro relacionado (empresa 704).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 704).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| sequencial_do_acumulador | `i_acumulador` | integer(4) |  |  | Sequencial do acumulador |
| sequencial_do_cliente | `i_cliente` | integer(4) |  |  | Sequencial do cliente |
| codigo_do_cliente | `codi_cli` | integer(4) |  |  | Código do Cliente |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `efclientes` → `efclientes` por `codi_emp` = `codi_emp` e `codi_cli` = `codi_cli`; colunas: `efclientes_nome`
- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_acumulador` (eq/in), `sequencial_do_cliente` (eq/in), `codigo_do_cliente` (eq/in)

## efcfg_importacao_nfe_saidas_parcelas

**Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas** — tabela `EFCFG_IMPORTACAO_NFE_SAIDAS_PARCELAS` (1 linhas)

Configuração de importacao da Nota Fiscal Eletronica - Servicos - Geral - Gerar parcelas. 1 linhas no catálogo; chave: CODI_EMP, NOTA.

- **Chave:** `CODI_EMP, NOTA`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `NOTA asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- tipo_de_nota_1_entradas_2_saidas_3_servi: todos os valores reais estão no comentário do banco (2=1).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 928).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| codigo_da_empresa | `codi_emp` | integer(4) |  |  | Codigo da empresa |
| tipo_de_nota_1_entradas_2_saidas_3_servi | `nota` | integer(4) |  | efcfg_importacao_nfe_saidas_parcelas_tipo_de_not | Tipo de nota(1 - entradas/2 - saidas/3 - servicos) |
| quantidade_de_parcelas | `quantidade_parcelas` | integer(4) |  |  | Quantidade de parcelas |
| vencimento_m_mesma_data_da_nota_i_inform | `vencimento` | varchar(1) |  |  | Vencimento M-Mesma data da nota/I-Informar |
| quantidade_de_dias | `quantidade_dias` | integer(4) |  |  | Quantidade de dias |
| tipo_do_titulo_d_c_p_r | `tipo_titulo` | integer(4) |  |  | Tipo do Titulo D/C/P/R |
| identificacao_s_n | `identificacao_titulo` | varchar(255) |  |  | Identificacao S/N |
| gerar_n_do_titulo_s_n | `gerar_numero_titulo` | varchar(1) |  |  | Gerar n. do titulo S/N |
| tipo_do_numero_do_titulo_n_mesmo_numero | `tipo_numero_titulo` | varchar(1) |  |  | Tipo do numero do titulo N-Mesmo número do documento/D-Mesma data de emissao |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `tipo_de_nota_1_entradas_2_saidas_3_servi` (eq/in), `vencimento_m_mesma_data_da_nota_i_inform` (eq/in), `tipo_do_titulo_d_c_p_r` (eq/in), `identificacao_s_n` (contem/prefixo), `gerar_n_do_titulo_s_n` (eq/in), `tipo_do_numero_do_titulo_n_mesmo_numero` (eq/in)

## efcfg_importacao_nfe_itens_entradas

**Importação NFS-e Paulistana - Entrada - Relacionamento de itens** — tabela `EFCFG_IMPORTACAO_NFE_ITENS_ENTRADAS` (1 linhas)

Importação NFS-e Paulistana - Entrada - Relacionamento de itens. 1 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL_PDI.

- **Chave:** `CODI_EMP, SEQUENCIAL_PDI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL_PDI asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1696).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_produto | `sequencial_pdi` | integer(4) |  |  | Sequencial do Produto |
| produto | `codi_pdi` | char(14) |  |  | Produto |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_produto` (eq/in), `produto` (eq/in)

## efcfg_importacao_nfe_itens_selecionar_entradas

**Importação NFS-e Paulistana - Entrada - Inclusão de Item serviço** — tabela `EFCFG_IMPORTACAO_NFE_ITENS_SELECIONAR_ENTRADAS` (1 linhas)

Importação NFS-e Paulistana - Entrada - Inclusão de Item serviço. 1 linhas no catálogo; chave: CODI_EMP, SEQUENCIAL_PDI, SEQUENCIAL_INCLUSAO.

- **Chave:** `CODI_EMP, SEQUENCIAL_PDI, SEQUENCIAL_INCLUSAO`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `SEQUENCIAL_PDI asc`, `SEQUENCIAL_INCLUSAO asc`

**Regras de negócio validadas:**

- Medido em 2026-10-18: 1 linhas, 1 empresa(s).
- Vínculo geempre (geempre): 0 de 1 linhas sem registro relacionado (empresa 1696).

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| empresa | `codi_emp` | integer(4) |  |  | Empresa |
| sequencial_do_pai | `sequencial_pdi` | integer(4) |  |  | Sequencial do pai |
| sequencial_do_item_servico | `sequencial_inclusao` | integer(4) |  |  | Sequencial do item serviço |
| codigo_da_inclusao_de_item_servico | `codigo_inclusao` | integer(4) |  |  | Código da inclusão de item serviço |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `geempre` → `geempre` por `codi_emp` = `codi_emp`; colunas: `geempre_nome`

**Filtros:** `sequencial_do_pai` (eq/in), `sequencial_do_item_servico` (eq/in), `codigo_da_inclusao_de_item_servico` (eq/in)

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

### efcfg_importacao_nfe_tipo_de_not

Confirmado: sim

> Todos os valores observados em efcfg_importacao_nfe.nota estão no comentário do banco (2026-10-18). Distribuição: 3=1.036, 1=1.034, 2=1.034.

| Código | Significado |
|---|---|
| 1 | entradas |
| 2 | saidas |
| 3 | servicos |

### efcfg_importacao_nfe_tipo_nota_i

Confirmado: parcial

> Coluna efcfg_importacao_nfe.OBJETO_ISENCAO_IMPORTAR só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| P | Conforme padrao do acumulador |
| I | Informar |
| N | Nao importar |

### efcfg_importacao_nfe_servico_pre

Confirmado: parcial

> Coluna efcfg_importacao_nfe.SITUACAO_NF_IMPORTAR só tem valores nulos na data da medição (2026-10-18): sem evidência para confirmar o comentário do banco.

| Código | Significado |
|---|---|
| A | Conforme informacao no arquivo |
| P | Conforme informacao do acumulador |
| I | Informar |
| N | Nao importar |

### efcfg_importacao_nfe_entradas_parcelas_tipo_de_not

Confirmado: sim

> Todos os valores observados em EFCFG_IMPORTACAO_NFE_ENTRADAS_PARCELAS.NOTA estão no comentário do banco (2026-10-18). Distribuição: 1=558.

| Código | Significado |
|---|---|
| 1 | entradas |
| 2 | saidas |
| 3 | servicos |

### efcfg_importacao_nfe_servicos_parcelas_tipo_de_not

Confirmado: sim

> Todos os valores observados em EFCFG_IMPORTACAO_NFE_SERVICOS_PARCELAS.NOTA estão no comentário do banco (2026-10-18). Distribuição: 3=25.

| Código | Significado |
|---|---|
| 1 | entradas |
| 2 | saidas |
| 3 | servicos |

### efcfg_importacao_nfe_saidas_parcelas_tipo_de_not

Confirmado: sim

> Todos os valores observados em EFCFG_IMPORTACAO_NFE_SAIDAS_PARCELAS.NOTA estão no comentário do banco (2026-10-18). Distribuição: 2=1.

| Código | Significado |
|---|---|
| 1 | entradas |
| 2 | saidas |
| 3 | servicos |

