# Modelo — Classificação fiscal dos produtos (por vigência)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/produto_fiscal.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

1 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [produto_vigencia](#produto_vigencia) | `efprodutos_vigencia` | 261.123 | medio | empresa |

## produto_vigencia

**Classificação fiscal do produto por vigência** — tabela `efprodutos_vigencia` (261.123 linhas)

Como o produto é tributado a partir de uma data: CST e alíquotas de PIS/COFINS na entrada e na saída, tipo de contribuição, natureza da receita, CST e alíquota de ICMS e IPI, substituição tributária e monofásico. A vigência em uso numa data é a de maior `vigencia` até essa data. 261.175 linhas, 475 empresas; 190.836 produtos têm uma só vigência.

- **Chave:** `CODI_EMP, CODI_PDI, VIGENCIA_PDI`
- **Empresa:** `CODI_EMP`
- **Período:** `—`
- **Ordem padrão:** `CODI_PDI asc`, `VIGENCIA_PDI desc`

**Regras de negócio validadas:**

- Vigências: 190.836 produtos têm 1, 21.829 têm 2, 7.710 têm 3, 646 têm 4 e 167 têm 5 (até 14). A data mais antiga é 1964-06-01 (valor padrão). A vigência em uso numa data é a mais recente até essa data (mesma regra dos acumuladores).
- Tipo de contribuição: sem incidência (S) 104.403 · cumulativo (C) 82.137 · não cumulativo (N) 74.635; substituição tributária (T) não ocorre. Monofásico em apenas 46 vigências e alíquota diferenciada de saída em 984.
- CST de ICMS de saída mais frequentes: 0 (77.829), 102 (42.554), 60 (25.140), 500 (18.156), 400 (13.774), 101 (10.981), 100 (10.449) e 20 (9.768); as legendas desses CST/CSOSN vêm do layout oficial (ex.: 102 Simples sem permissão de crédito, 60 ICMS-ST cobrado anteriormente), não do banco. Nenhum produto está marcado como incluído em ST (produto_incluido_st = N em 261.175).
- Dados de PIS/COFINS conferidos (S) em 71.071 vigências e não conferidos (N) em 190.104: a apuração do PIS/COFINS usa esse indicador (com o do item) para sinalizar produtos com dados incompletos, não para excluí-los.
- Integridade (5 maiores empresas, 71.973 vigências): todas têm o produto no cadastro (efprodutos), 0 sem cadastro.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| produto_codigo | `codi_pdi` | char(14) |  |  | Produto |
| vigencia | `vigencia_pdi` | date(4) |  |  | Vigencia |
| descricao | `descricao` | char(80) |  |  | Descricao |
| pis_cofins_cst_entrada | `codigo_cst_entrada` | integer(4) |  | cst_pis_cofins | CST - Entradas |
| pis_cofins_cst_saida | `codigo_cst_saida` | integer(4) |  | cst_pis_cofins | CST - Saidas |
| tipo_contribuicao | `tipo_contribuicao` | char(1) |  | tipo_contribuicao_produto | Tipo de contribuicao (N=Nao cumulativo/ C=Cumulativo/ T=Substituicao tributaria/ S=Sem incidencia) |
| natureza_receita | `natureza_receita` | integer(4) |  |  | Natureza da receita |
| pis_cumulativo_art_6 | `pis_incidencia_cumulativa_art_6` | char(1) |  | sim_nao_texto | PIS com incidência cumulativa, conforme lei 12.693/12, Art. 6 (S/N) |
| cofins_cumulativo_art_10 | `cofins_incidencia_cumulativa_art_10` | char(1) |  | sim_nao_texto | COFINS com incidência cumulativa, conforme lei 10.833/03, Art. 10 (S/N) |
| monofasico_pis_cofins | `produto_sujeito_tributacao_monofasica_piscofins` | char(1) |  | sim_nao_texto | Produto sujeito a tributação monofásica de PIS e COFINS |
| codigo_recolhimento_pis | `codigo_recolhimento_pis` | char(6) |  |  | Codigo de recolhimento PIS |
| codigo_recolhimento_cofins | `codigo_recolhimento_cofins` | char(6) |  |  | Codigo de recolhimento COFINS |
| credito_vinculo | `vinculo_credito` | tinyint(1) |  |  | Vinculo do credito |
| credito_base | `base_credito` | integer(4) |  |  | Base do credito |
| credito_proporcional | `aproveitar_credito_proporcional` | char(1) |  | sim_nao_texto | Aproveitar credito proporcional somente a receita nao cumulativa (S/N) |
| credito_aliquota_diferenciada | `credito_aliquota_diferenciada` | char(1) |  | sim_nao_texto | Credito por aliquota diferenciada (S/N) - Entradas |
| credito_aliquota_pis | `aliquota_pis_credito` | numeric(7) |  |  | Aliquota do PIS - Entradas |
| credito_aliquota_cofins | `aliquota_cofins_credito` | numeric(7) |  |  | Aliquota do COFINS - Entradas |
| debito_aliquota_diferenciada | `debito_aliquota_diferenciada` | char(1) |  | sim_nao_texto | Debito por aliquota diferenciada (S/N) - Saidas |
| debito_aliquota_pis | `aliquota_pis_debito` | numeric(7) |  |  | Aliquota do PIS - Saidas |
| debito_aliquota_cofins | `aliquota_cofins_debito` | numeric(7) |  |  | Aliquota do COFINS - Saidas |
| dados_piscofins_ok | `dados_piscofins_ok` | char(1) |  | sim_nao_texto | Dados referente ao PIS COFINS OK (S/N) |
| icms_cst_entrada | `cst_icms_entrada` | integer(4) |  |  | CST ICMS - Entrada |
| icms_cst_saida | `cst_icms_saida` | integer(4) |  |  | CST ICMS - Saída |
| icms_aliquota | `aliquota_icms` | numeric(5) |  |  | Alíquota do ICMS |
| ipi_cst_entrada | `cst_ipi_entrada` | integer(4) |  |  | CST IPI - Entrada |
| ipi_cst_saida | `cst_ipi_saida` | integer(4) |  |  | CST IPI - Saída |
| ipi_aliquota | `aliquota_ipi` | numeric(5) |  |  | Alíquota do IPI |
| ipi_periodicidade | `periodicidade_ipi` | char(1) |  |  | PERIODICIDADE DO IPI (M / Q / D / T / S / E / N / R / V) |
| ipi_classe_enquadramento | `classe_enquadramento_ipi` | integer(4) |  |  | Classe do Enquadramento do IPI |
| st_base_calculo | `base_calculo_st` | char(1) |  |  | Base Cálculo ST (M/P) |
| st_percentual_reducao_base | `percentual_reducao_bc_st` | numeric(7) |  |  | Percentual da Redução BC ST |
| st_margem_valor_agregado | `percentual_margem_de_valor_adic_st` | numeric(5) |  |  | Percentual margem do valor adic. ST |
| st_valor_unitario | `valor_unitario_st` | numeric(13) |  |  | Valor unitário |
| st_produto_incluido | `produto_incluido_st` | char(1) |  | sim_nao_texto | Produto incluído ST (S/N) |
| st_data_inicio | `data_inicio_st` | date(4) |  |  | Data início ST |
| sped_tabela | `tabela_sped` | integer(4) |  |  | Tabela SPED |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `produto` → `efprodutos` por `CODI_EMP` = `codi_emp` e `CODI_PDI` = `codi_pdi`; colunas: `produto_descricao_cadastro`, `produto_ncm`

**Filtros:** `produto_codigo` (eq/in/prefixo), `vigencia` (eq/entre/gte/lte), `descricao` (contem/prefixo), `tipo_contribuicao` (eq/in), `pis_cofins_cst_saida` (eq/in), `icms_cst_saida` (eq/in), `monofasico_pis_cofins` (eq)

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

### tipo_contribuicao_produto

Tipo de contribuição do produto no PIS/COFINS (efprodutos_vigencia.tipo_contribuicao)

Confirmado: sim

> O comentário lista N, C, T e S; nos dados só aparecem S (104.403), C (82.137) e N (74.635), nunca T.

| Código | Significado |
|---|---|
| N | Não cumulativo |
| C | Cumulativo |
| T | Substituição tributária |
| S | Sem incidência |

### cst_pis_cofins

CST de PIS/COFINS (codigo_cst_entrada / codigo_cst_saida)

Confirmado: parcial

> O banco não traz a legenda. São os códigos da tabela oficial de CST de PIS/COFINS (01 = operação tributável com alíquota básica, 04 = monofásica com alíquota zero, 06 = alíquota zero, 07 = isenta, 08 = sem incidência, 49 = outras operações de saída, 99 = outras operações): leitura pelo layout oficial, não pelo banco. Mais frequentes na saída: 1 (105.070 vigências), 49 (45.684), 99 (34.147), 7 (20.700), 6 (15.356), nulo (13.829), 8 (13.512) e 4 (8.762).

| Código | Significado |
|---|---|
| 1 | Tributável com alíquota básica |
| 4 | Monofásica com alíquota zero |
| 6 | Alíquota zero |
| 7 | Isenta |
| 8 | Sem incidência |
| 49 | Outras operações de saída |
| 99 | Outras operações |

