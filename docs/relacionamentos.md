# Relacionamentos (Fase 2)

Gerado por `src/model/exportar_grafo.py` a partir de `data/catalog/dominio_catalog.db`.

## Fontes e confiança

| Origem | Descrição | Confiança |
|---|---|---|
| declarada | FK criada no banco | 1,0 |
| observada | igualdade `A.col = B.col` minerada dos executáveis/.pbd da Domínio, validada contra o catálogo | 0,5 a 0,9 (pelo nº de usos) |
| inferida | filha contém toda a chave do pai **e** o nome começa com o do pai (`EFMVSPRO_*` → `efmvspro`); precisão medida contra as FKs declaradas: ~72% (sem a regra de nome: 17%) | 0,6 |

Tipos: `fk` (chave completa), `vigencia` (ligação por período, tabelas `*_vigencia`), `ligacao` (colunas em comum sem chave completa de nenhum lado), `temporaria` (`eftmp_*`, fora do grafo).

## Resumo

| Origens | Tipo | Relações | Confiança média |
|---|---|---|---|
| declarada,observada | fk | 4130 | 1.0 |
| observada | ligacao | 2721 | 0.68 |
| observada | fk | 2397 | 0.72 |
| declarada | fk | 2168 | 1.0 |
| observada | vigencia | 1383 | 0.72 |
| observada | temporaria | 796 | 0.72 |
| inferida | fk | 522 | 0.6 |
| declarada,observada | vigencia | 304 | 1.0 |
| declarada | vigencia | 167 | 1.0 |
| declarada | temporaria | 1 | 1.0 |

## Cobertura por departamento (tabelas base legíveis)

| Departamento | Tabelas | Com relação | % |
|---|---|---|---|
| Fiscal | 2716 | 2637 | 97% |
| Pessoal | 787 | 728 | 93% |
| Contábil | 604 | 575 | 95% |
| Geral | 404 | 247 | 61% |
| Financeiro do escritório | 185 | 169 | 91% |
| Processos | 39 | 35 | 90% |
| Societário | 35 | 33 | 94% |
| Outros | 24 | 12 | 50% |
| Sistema | 23 | 8 | 35% |

## Tabelas mais referenciadas (como pai)

| Tabela | Filhas | Descrição |
|---|---|---|
| geempre | 1390 | Empresa - Cadastro |
| efprodutos | 276 | Produtos - Cadastro |
| efsaidas | 227 | Notas Fiscais de Saida |
| efsdoimp | 215 | Saldo dos Impostos |
| ctlancto | 208 | Lancamentos Contabeis |
| efnatureza | 197 | Naturezas - Cadastro |
| foempregados | 195 | Empregados - Cadastro |
| efentradas | 186 | Notas Fiscais de Entrada |
| EFACUMULADOR | 154 | Acumuladores - Cadastro |
| ctcontas | 149 | Contas Contabeis - Cadastro |
| EFPARAMETRO_VIGENCIA | 126 | Paramentros - Cadastro - Escrita Fiscal |
| GEIMPOSTO_VIGENCIA | 120 | Impostos |
| geimposto | 106 | Impostos |
| EFTABELA_CST_VIGENCIA | 103 | Tabela de Códigos Situação Tributária por vigência |
| efservicos | 91 | Notas Fiscais de Servico |
| gemunicipio | 85 | Cadastro de municipios |
| foparmto | 82 | Tabela de parâmetros |
| efespecies | 80 | Especies - Cadastro |
| GEIMPOSTO_VIGENCIA_RECOLHIMENTO | 77 | Impostos - Cadastro - Codigo de Recolhimento |
| efmvepro | 74 | Notas Fiscais de Entrada - Produtos |
| efmvspro | 74 | Notas Fiscais de Saida - Produtos |
| FOESOCIAL_DADOS_EVENTOS | 71 | Dados dos eventos para envio ao eSocial. |
| GESCP | 66 | Sociedade em Conta de Participação - SCP |
| effornece | 65 | Fornecedores - Cadastro |
| EFECF_REDUCAO_Z | 62 | ECF - Dados da redução Z |
| efclientes | 59 | Clientes - Cadastro |
| foservicos | 56 | Servico - Cadastro |
| ctparmto | 53 | Parametros |
| geestado | 51 | Cadastro de estados |
| CTSPED_ECF_OD | 50 | SPED ECF - Outros Dados |

## Relações usadas pela Domínio e NÃO declaradas como FK (mais frequentes)

| Filha | Pai | Colunas (filha → pai) | Usos | Programas | Tipo |
|---|---|---|---|---|---|
| GEIMPOSTO_VIGENCIA | ctcontas | ctrc_imp→codi_cta, ctvd_imp→codi_cta, ctrp_imp→codi_cta, ctcp_imp→codi_cta | 24808 | 1 | vigencia |
| GEIMPOSTO_VIGENCIA | cthispad | chip_imp→codi_his, chir_imp→codi_his, chdevcompra_imp→codi_his, chadicfsoc_imp→codi_his | 21048 | 1 | vigencia |
| EFACUMULADOR_VIGENCIA | efsaidas | codi_emp→codi_emp, codi_acu→codi_acu | 10383 | 179 | vigencia |
| EFACUMULADOR_VIGENCIA | efentradas | codi_emp→codi_emp, codi_acu→codi_acu | 9879 | 183 | vigencia |
| efsdoimp | geempre | codi_emp→codi_emp | 5287 | 95 | fk |
| EFACUMULADOR_VIGENCIA_IMPOSTOS | GEIMPOSTO_VIGENCIA | codi_emp→codi_emp, codi_imp→codi_imp | 5169 | 57 | vigencia |
| EFPARAMETRO_VIGENCIA | efsaidas | codi_emp→codi_emp | 5095 | 162 | vigencia |
| EFACUMULADOR_VIGENCIA_IMPOSTOS | efsaidas | codi_emp→codi_emp, codi_acu→codi_acu | 4657 | 86 | vigencia |
| ctlancto | ctcontas | codi_emp_plano→codi_emp, cdeb_lan→codi_cta, ccre_lan→codi_cta, codi_emp→codi_emp | 4632 | 95 | fk |
| fomovtoserv | fobasesserv | i_calculos→i_calculos, codi_emp→codi_emp, i_empregados→i_empregados, data→competencia | 3856 | 34 | fk |
| LRPARAMETRO_VIGENCIA | ctcontas | conta_lucro_operacional_geral→codi_cta, conta_prejuizo_operacional_geral→codi_cta, conta_lucro_nao_operacional_geral→codi_cta, conta_prejuizo_nao_operacional_geral→codi_cta | 3452 | 1 | vigencia |
| EFACUMULADOR_VIGENCIA | ctcontas | ccre_acu→codi_cta, cdeb_acu→codi_cta, ctcp_acu→codi_cta, ctjr_acu→codi_cta | 3389 | 3 | vigencia |
| EFACUMULADOR_VIGENCIA_IMPOSTOS | efservicos | codi_emp→codi_emp, codi_acu→codi_acu | 3378 | 48 | vigencia |
| EFPRODUTOS_VIGENCIA | GEIMPOSTO_VIGENCIA_RECOLHIMENTO | codi_emp→codi_emp, i_recolhimento_ipi→i_recolhimento, i_recolhimento_pis_entrada→i_recolhimento, i_recolhimento_cofins_entrada→i_recolhimento | 3346 | 3 | vigencia |
| EFACUMULADOR_VIGENCIA | efservicos | codi_emp→codi_emp, codi_acu→codi_acu | 3085 | 68 | vigencia |
| EFACUMULADOR_VIGENCIA | cthispad | chis_acu→codi_his, chcp_acu→codi_his, chjr_acu→codi_his, chmt_acu→codi_his | 2856 | 1 | vigencia |
| EFPARAMETRO_VIGENCIA | efservicos | codi_emp→codi_emp | 2693 | 61 | vigencia |
| efentradas | EFPARAMETRO_VIGENCIA | codi_emp→codi_emp | 2664 | 121 | vigencia |
| efsaidaspag | EFVSAIDASPAG | codi_emp→codi_emp, codi_sai→codi_sai, pgto_saip→pgto_saip, parc_saip→parc_saip | 2097 | 8 | ligacao |
| EFCONFIGURACAO_PRODUTO_POR_NCM_VIGENCIA_ITENS_PRO | GEIMPOSTO_VIGENCIA_RECOLHIMENTO | codi_emp→codi_emp, i_recolhimento_icmsa→i_recolhimento, codigo_recolhimento_icmsa→codigo_recolhimento, i_recolhimento_recali→i_recolhimento | 2015 | 3 | vigencia |
| efmvepro | efprodutos | codi_emp→codi_emp, codi_pdi→codi_pdi | 1990 | 116 | fk |
| efmvspro | efprodutos | codi_emp→codi_emp, codi_pdi→codi_pdi | 1968 | 117 | fk |
| geempre | gemunicipio | codigo_municipio→codigo_municipio | 1910 | 124 | fk |
| EFACUMULADOR_VIGENCIA_IMPOSTOS | efentradas | codi_emp→codi_emp, codi_acu→codi_acu | 1878 | 65 | vigencia |
| EFECF_REDUCAO_Z_SITUACAO_TRIBUTARIA_DETALHAMENTO | EFECF_REDUCAO_Z | codi_emp→codi_emp, i_reducao→i_reducao | 1841 | 76 | fk |
| efsdoimp | geimposto | codi_emp→codi_emp, codi_imp→codi_imp | 1794 | 21 | fk |
| HRPARAMETRO_VIGENCIA | ctcontas | receber_conta_multa→codi_cta, receber_conta_juros→codi_cta, receber_conta_desconto→codi_cta, receber_conta_adiantamento→codi_cta | 1691 | 1 | vigencia |
| LRPARAMETRO_VIGENCIA | cthispad | imposto_csll_recolher_historico→codi_his, imposto_csll_recuperar_historico→codi_his, imposto_irpj_recolher_historico→codi_his, imposto_irpj_recuperar_historico→codi_his | 1621 | 1 | vigencia |
| EFACUMULADOR_VIGENCIA | EFECF_REDUCAO_Z_SITUACAO_TRIBUTARIA_DETALHAMENTO | codi_emp→codi_emp, codi_acu→codi_acu | 1618 | 74 | vigencia |
| HRPARAMETRO_VIGENCIA | cthispad | receber_historico_multa→codi_his, receber_historico_juros→codi_his, receber_historico_desconto→codi_his, receber_historico_adiantamento→codi_his | 1594 | 1 | vigencia |
| ctlancto | ctparmto | codi_emp→codi_emp | 1579 | 24 | fk |
| EFOUTROSDADOS_EFD_CONTAS_CST | EFOUTROSDADOS_EFD_CONTAS_NATUREZA | codi_emp→codi_emp, competencia→competencia, i_informativos→i_informativos, registro→registro | 1489 | 1 | ligacao |
| efmvepro | EFPRODUTOS_VIGENCIA | codi_emp→codi_emp, codi_pdi→codi_pdi | 1485 | 65 | vigencia |
| eftabecfm | efsaidas | codi_emp→codi_emp, codi_ecm→codi_sai | 1475 | 62 | fk |
| efmvspro | EFPRODUTOS_VIGENCIA | codi_emp→codi_emp, codi_pdi→codi_pdi | 1467 | 58 | vigencia |
| efsdoimp | GEIMPOSTO_VIGENCIA | codi_emp→codi_emp, codi_imp→codi_imp | 1466 | 42 | vigencia |
| efservicospag | EFVSERVICOSPAG | codi_emp→codi_emp, codi_ser→codi_ser, pgto_serp→pgto_serp, parc_serp→parc_serp | 1461 | 8 | ligacao |
| efsaidaspag | efsaidas | codi_emp→codi_emp, codi_sai→codi_sai | 1412 | 35 | fk |
| efservicospag | efservicos | codi_emp→codi_emp, codi_ser→codi_ser | 1404 | 32 | fk |
| EFPARAMETRO_VIGENCIA | efprodutos | codi_emp→codi_emp | 1235 | 13 | vigencia |

## Tabelas base sem nenhuma relação

373 tabelas (lista completa em `exports/tabelas_sem_relacao.txt`).
