# Modelo — Parâmetros da empresa (contabilidade e folha)

> Gerado por `src/model/gerar_docs_modelo.py` a partir de `src/model/modulos/parametros_empresa.yaml`, do catálogo e do perfil de colunas. **Não edite à mão.**

2 entidades. A coluna *Preench.* é o % de linhas com valor útil (nem nulo, nem em branco, nem zero, nem 1900-01-01; para colunas de código o zero conta como valor).

## Diagrama

```mermaid
erDiagram
```

## Entidades

| Entidade | Tabela | Linhas | Volume | Filtro obrigatório |
|---|---|---|---|---|
| [parametro_contabil](#parametro_contabil) | `ctparmto` | 1.441 | pequeno | empresa |
| [parametro_folha](#parametro_folha) | `foparmto` | 1.355 | pequeno | empresa |

## parametro_contabil

**Parâmetros da contabilidade por empresa** — tabela `ctparmto` (1.441 linhas)

Configuração contábil da empresa: máscara e origem do plano de contas, regime (fiscal/caixa/gerencial), período de trabalho, centro de custo, contas de lucro e prejuízo e transferência do resultado. 1.441 linhas, uma por empresa. Usa 39 das 249 colunas.

- **Chave:** `codi_emp`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_emp asc`

**Regras de negócio validadas:**

- Uma linha por empresa (1.441 empresas, 1.441 linhas). Regime contábil 1 (fiscal) em 1.440 e 3 (gerencial) em 1; conta informada por código (C) em 1.440 e por máscara (M) em 1.
- Plano de contas: `plano_origem_empresa` é nulo em 1.354 empresas (plano próprio) e aponta para OUTRA empresa em 87; nenhuma aponta para si mesma. 57 empresas marcam compartilha_plano = S. Para resolver as contas de uma empresa use a empresa do plano (é o `plano_empresa` do lançamento).
- Máscara do plano de contas: 9.9.9.99.999999 em 1.378 empresas; 9.9.9.99.9999 em 30; 9.9.99.999.999 em 17; 9.9.99.99.999 em 7; 9.9.9.99.99.999 em 6; 9.99.99.999999 em 2.
- Período de trabalho: 1.273 empresas têm data final (de 2020-04-30 a 2030-12-31; datas muito futuras provavelmente significam 'sem limite'); fora do período o sistema bloqueia (N) em 971 empresas e libera (L) em 470; nenhuma usa avisar (A).
- Demonstrações e fechamento: usa DRE (S) em 1.403 empresas, DLPA em 1.336, histórico obrigatório em 1.418 e transferência automática do resultado para o patrimônio líquido em 1.401; 14 empresas têm tudo isso desligado.
- Contabilidade por centro de custo (ccusto = S) em 10 empresas.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| regime_contabil | `ctcx_par` | tinyint(1) |  | regime_contabil | Usar como (1=Fiscal, 2=Caixa, 3=Gerencial) |
| mascara_plano_contas | `masc_par` | char(35) |  |  | Mascara contabil |
| mascara_gerencial | `masc_ger` | char(35) |  |  | Mascara Gerencial |
| mascara_relatorios | `masc_rel` | char(35) |  |  | Mascara p/ relatorios |
| informar_conta_por | `lmas_par` | char(1) |  | informar_conta_por | Informar a conta por (C=Codigo, M=Mascara) |
| inicio_lancamentos | `dila_par` | date(4) |  |  | Data inicio dos lancamentos |
| periodo_trabalho_inicio | `dini_par` | date(4) |  |  | Data inicial do fechamento |
| periodo_trabalho_fim | `dfin_par` | date(4) |  |  | Data final do fechamento |
| acao_fora_do_periodo | `lant_par` | char(1) |  | acao_periodo_trabalho | Ação do período de trabalho (L=Livre, A=Avisar N=Não permitir) |
| relatorios_inicio | `dinr_par` | date(4) |  |  | Data inicial dos relatorios |
| relatorios_fim | `dfir_par` | date(4) |  |  | Data final dos relatorios |
| plano_origem_empresa | `codi_pad` | integer(4) |  |  | Origem do Plano de Contas |
| compartilha_plano | `comp_pad` | char(1) |  | sim_nao_texto | Compartilha plano de contas (S/N) |
| historico_origem_empresa | `codi_emp_his` | integer(4) |  |  | Origem dos Historicos |
| compartilha_historicos | `compart_his` | char(1) |  | sim_nao_texto | Compartilha historicos (S/N) |
| centraliza_matriz_filiais | `emat_par` | char(1) |  | sim_nao_texto | Centralizar a Contabilidade entre Matriz e Filiais (S/N) |
| informa_filial_no_lancamento | `fili_par` | char(1) |  | sim_nao_texto | Informar o codigo da filial no lancamento (S/N) |
| contabilidade_por_centro_custo | `ccusto_par` | char(1) |  | sim_nao_texto | Contabilidade por centro de custo (S/N) |
| rateio_centro_custo_por_filial | `ratcf_par` | char(1) |  | sim_nao_texto | Rateio de centro de custo por filial (S/N) |
| usa_dre | `dre_par` | char(1) |  | sim_nao_texto | Usa DRE (S/N) |
| usa_dlpa | `dlpa_par` | char(1) |  | sim_nao_texto | Usa DLPA (S/N) |
| usa_doar | `doar_par` | char(1) |  | sim_nao_texto | Usa DOAR (S/N) |
| historico_obrigatorio | `hist_obrig` | char(1) |  | sim_nao_texto | Digitacao obrigatoria de historicos |
| permite_lancamento_valor_zero | `permzero_par` | char(1) |  | sim_nao_texto | Permite gravar lancamentos com valor zero (S/N) |
| permite_cadastrar_contas | `permcta_par` | char(1) |  | sim_nao_texto | Permite cadastrar contas (S=Sim/N=Nao) |
| conta_inicial | `inicta_par` | integer(4) |  |  | Numero da conta inicial |
| conta_final | `fimcta_par` | integer(4) |  |  | Numero da conta final |
| permite_cadastrar_historicos | `permhis_par` | char(1) |  | sim_nao_texto | Permite cadastrar historicos (S=Sim/N=Nao) |
| historico_inicial | `inihis_par` | integer(4) |  |  | Numero do historico inicial |
| historico_final | `fimhis_par` | integer(4) |  |  | Numero do historico final |
| conta_caixa | `ccxa_par` | integer(4) |  |  | Conta caixa |
| informa_conta_caixa | `infcx_par` | char(1) |  | sim_nao_texto | Informar a conta caixa no lancamento (S/N) |
| conta_patrimonio_liquido | `patl_par` | integer(4) |  |  | Conta Patrimonio Liquido |
| conta_destino_resultado | `zera_par` | integer(4) |  |  | Conta destino |
| conta_lucro_periodo | `lucr_par` | integer(4) |  |  | Conta Lucro do Periodo |
| conta_prejuizo_periodo | `prej_par` | integer(4) |  |  | Conta Prejuizo do Periodo |
| transfere_resultado_automaticamente | `faza_par` | char(1) |  | sim_nao_texto | Transferir automaticamente o resultado para o Patrimonio Liquido |
| altera_lancamentos_outros_sistemas | `altl_par` | char(1) |  | sim_nao_texto | Altera lancamentos de outros sistemas |
| utiliza_dominio_cliente | `domcli_par` | char(1) |  | sim_nao_texto | Utiliza Dominio Cliente (S=Sim/N=Nao) |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `empresa` → `geempre` por `codi_emp` = `codi_emp`; colunas: `empresa_nome`

**Filtros:** `plano_origem_empresa` (eq/in), `regime_contabil` (eq/in), `compartilha_plano` (eq)

## parametro_folha

**Parâmetros da folha por empresa** — tabela `foparmto` (1.355 linhas)

Configuração da folha da empresa: competência e tipo de processamento atuais, tipos de folha usados, regras de adiantamento, 13º e férias, integração contábil, rateio por serviço e dia do pagamento. 1.356 linhas, uma por empresa. Usa 39 das 599 colunas.

- **Chave:** `codi_emp`
- **Empresa:** `codi_emp`
- **Período:** `—`
- **Ordem padrão:** `codi_emp asc`

**Regras de negócio validadas:**

- Uma linha por empresa (1.356). Nenhuma empresa trabalha com folha semanal, quinzenal ou de professores (todas N).
- Competência atual (data_proces): de 2013-01 a 2026-10; 255 empresas estão em setembro/2026 ou depois, 25 entre janeiro e agosto de 2026 e 1.076 antes de 2026 (empresas sem folha ativa).
- Tipo de folha atual: 11 (mensal) em 911 empresas, 70 em 375, 41 em 65, 51 e 52 em 2 cada e 42 em 1.
- Encerramento: `mes_encerrado` tem valor em todas as 1.356 linhas, de 1900-01-01 (padrão 'não informado') a 2026-03: está desatualizado em relação à competência atual e não deve ser usado para saber se a folha está fechada (use o S-1299 do eSocial: função situacao_esocial).
- Integração contábil: gera lançamentos (cta_gera = 1) em 1.257 empresas e não em 99; só 3 usam rateio por serviço. Eventos próprios em 711 empresas e eventos de outra empresa (codi_emp_eve) em 645.
- Adiantamento: base 1 em 1.327 empresas (percentual médio 37%) e base 2 em 29 (40%). Pagamento da folha mensal: código 2 em 1.325 empresas e 1 em 31.

| Campo | Coluna | Tipo | Preench. | Domínio | Descrição (banco) |
|---|---|---|---|---|---|
| competencia_atual | `data_proces` | date(4) |  |  | Competencia atual |
| tipo_folha_atual | `tipo_proces` | integer(4) |  | tipo_folha_atual | tipo folha atual |
| mes_encerrado | `mes_encerrado` | date(4) |  |  | Data do fechamento |
| empresa_dos_eventos | `codi_emp_eve` | integer(4) |  |  | Usa eventos da empresa |
| folha_semanal | `tem_folha_semanal` | char(1) |  | sim_nao_texto | Trabalha com folha semanal |
| folha_quinzenal | `tem_folha_quinzenal` | char(1) |  | sim_nao_texto | Trabalha com folha quizenal |
| folha_professor | `tem_folha_professor` | char(1) |  | sim_nao_texto | Trabalha com folha de professores |
| adiantamento_base | `adiant_tiposal` | tinyint(1) |  | base_adiantamento | Base de cálculo |
| adiantamento_percentual | `adiant_percentual` | numeric(13) |  |  | Percentual de adiantamento |
| adiantamento_afastados | `adiant_afast` | tinyint(1) |  | sim_nao_numerico | Empregados afastados |
| adiantamento_contribuintes | `adiant_contr` | tinyint(1) |  | sim_nao_numerico | Calcular para contribuintes |
| adiantamento_dias_minimos | `adiant_afast_condic_dias` | integer(4) |  |  | Numero de dias trabalhados no mes para direito ao adiantamento |
| decimo_terceiro_percentual | `calc13_percentual` | numeric(6) |  |  | Percentual |
| decimo_terceiro_paga_medias | `calc13_pag_media` | char(1) |  | sim_nao_texto | Pagar médias horas/valor |
| decimo_terceiro_paga_adicionais | `calc13_pag_adic` | char(1) |  | sim_nao_texto | Pagar adicionais |
| decimo_terceiro_nao_calcula_diretores | `calc13_nao_calc_dir` | char(1) |  | sim_nao_texto | Não calcula para diretores |
| decimo_terceiro_mais_de_um_adiantamento | `calc13_maisde1adiant` | char(1) |  | sim_nao_texto | Permite mais de um adiantamento |
| decimo_terceiro_estagiario | `calc13_estagiario` | tinyint(1) |  | sim_nao_numerico | Pagar para estagiário |
| decimo_terceiro_desconta_faltas | `calc13_faltas` | tinyint(1) |  | sim_nao_numerico | Descontar faltas automaticamente |
| ajusta_13_em_dezembro | `ajusta_med_13` | char(1) |  | sim_nao_texto | Ajustar cálculo do 13º salário em dezembro favorável ao empregado: (N=Não/S=Sim) |
| ferias_desconta_faltas | `fer_desc_faltas` | char(1) |  | sim_nao_texto | Descontar faltas automaticamente |
| ferias_paga_adicionais | `fer_paga_adic` | char(1) |  | sim_nao_texto | Pagar adicionais |
| ferias_paga_medias | `fer_paga_med` | char(1) |  | sim_nao_texto | Pagar Medias |
| ferias_adianta_13 | `fer_decimo_1p` | char(1) |  | sim_nao_texto | Adiantar 1a. parcela do 13o. |
| ferias_estagiario | `fer_estagiario` | tinyint(1) |  | sim_nao_numerico | Pagar para estagiario |
| gera_lancamentos_contabeis | `cta_gera` | tinyint(1) |  | sim_nao_numerico | Gera lancamentos contabeis |
| lancamentos_na_empresa | `cta_codi_emp` | integer(4) |  |  | Gera os lancamentos na empresa |
| contabil_separa_rescisao | `cta_sep_rescisao` | tinyint(1) |  | sim_nao_numerico | rescisao |
| contabil_separa_ferias | `cta_sep_ferias` | tinyint(1) |  | sim_nao_numerico | Ferias |
| contabil_tipo_exportacao | `cta_tipo_exp` | tinyint(1) |  |  | Tipo de exportação contábil |
| contabil_por_centro_custo | `cta_ccus_rateio` | tinyint(1) |  | sim_nao_numerico | Contabilidade por centro de custo |
| usa_rateio_por_servico | `usa_rateio` | tinyint(1) |  | sim_nao_numerico | Usa rateio por servico (1=Sim, 0=Nao) |
| rateio_inicio | `usa_rateio_inicio` | date(4) |  |  | Inicio do rateio do calculo por servicos |
| discrimina_dsr | `separar_dsr` | tinyint(1) |  | sim_nao_numerico | Discriminar DSR |
| ordena_eventos | `ordenar_eventos` | tinyint(1) |  | sim_nao_numerico | Ordena eventos |
| movimento_ferias_na_folha_mensal | `mov_fer_mes` | char(1) |  | sim_nao_texto | movimento de ferias na folha mensal |
| data_pagamento_mensal | `data_pagto_mes` | tinyint(1) |  | data_pagamento_mes | Data de pagamento da folha mensal do empregado. 1-Último dia útil do mês de competência, 2-Quinto dia útil do mês seguinte e 3-Primeiro dia útil do mês seguinte |
| optante_simples_nacional | `simples_072007` | tinyint(1) |  | sim_nao_numerico | Opção simples nacional |
| conta_debito_gps | `gps_conta_debito` | tinyint(1) |  |  | Conta debito GPS Eletronica |

**Vínculos (LEFT JOIN, acrescentam colunas legíveis):**

- `empresa` → `geempre` por `codi_emp` = `codi_emp`; colunas: `empresa_nome`

**Filtros:** `competencia_atual` (eq/entre/gte/lte), `tipo_folha_atual` (eq/in), `gera_lancamentos_contabeis` (eq)

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

### regime_contabil

Como a contabilidade da empresa é usada (ctparmto.ctcx_par)

Confirmado: sim

| Código | Significado |
|---|---|
| 1 | Fiscal |
| 2 | Caixa |
| 3 | Gerencial |

### informar_conta_por

Confirmado: sim

| Código | Significado |
|---|---|
| C | Código |
| M | Máscara |

### acao_periodo_trabalho

O que o sistema faz com lançamentos fora do período de trabalho (ctparmto.lant_par)

Confirmado: sim

| Código | Significado |
|---|---|
| L | Livre |
| A | Avisar |
| N | Não permitir |

### tipo_folha_atual

Tipo do processamento da folha em andamento (foparmto.tipo_proces)

Confirmado: parcial

> Em uso: 11 (mensal) em 911 empresas, 70 em 375, 41 (adiantamento) em 65, 51 e 52 (13º) em 2 cada e 42 (complementar) em 1. No cadastro de folha o código 70 é 'participação nos lucros'; que 375 empresas estejam nesse tipo como processamento ATUAL não está documentado.

| Código | Significado |
|---|---|
| 11 | Mensal |
| 41 | Adiantamento |
| 42 | Complementar |
| 51 | Adiantamento de 13º salário |
| 52 | 13º salário |
| 70 | Participação nos lucros |

### base_adiantamento

Base de cálculo do adiantamento (foparmto.adiant_tiposal)

Confirmado: parcial

> O comentário só diz "Base de cálculo". Em uso 1 (1.327 empresas, percentual médio 37%) e 2 (29 empresas, 40%); a legenda não está no banco.

| Código | Significado |
|---|---|
| 1 | Base 1 (sem legenda no banco) |
| 2 | Base 2 (sem legenda no banco) |

### data_pagamento_mes

Data de pagamento da folha mensal (foparmto.data_pagto_mes)

Confirmado: parcial

> O comentário lista 1 (último dia útil do mês de competência) e 2 (quinto dia útil) e está truncado depois disso. Em uso 1 (31) e 2 (1.325).

| Código | Significado |
|---|---|
| 1 | Último dia útil do mês da competência |
| 2 | Quinto dia útil (provável) |

