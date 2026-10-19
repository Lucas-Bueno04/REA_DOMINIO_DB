# Funções de consulta (`src/server/consultas.py`)

Gerado por `scripts/gerar_docs_funcoes.py` a partir do catálogo `FUNCOES`. Todas são **somente leitura**, recebem o `Motor` e devolvem dicionário JSON-seguro; ainda **não estão registradas como ferramentas MCP** (decisão do dono do projeto): para registrar, basta expor `FUNCOES[nome]["executar"]` em `src/server/mcp_server.py`.

15 funções.

| Função | Para quê | Parâmetros |
|---|---|---|
| `receita_bruta_simples` | Receita bruta do mês no Simples Nacional: recalcula a partir dos documentos e compara com a base que a Domínio apurou. | `empresa`, `competencia` |
| `perfil_fiscal` | Perfil fiscal da empresa numa data: regimes federal, estadual e municipal em vigor, impostos ativos e evidências do que a empresa realmente apura. | `empresa`, `data` |
| `informativos_da_empresa` | Informativos (obrigações acessórias) preparados para a empresa no período, com campos informados, retificadora e número de recibo. | `empresa`, `de`, `ate`, `informativo` |
| `apuracao_lalur` | Apuração do IRPJ e da CSLL pelo lucro real (Lalur) numa competência, com conferência das identidades do cálculo. | `empresa`, `competencia` |
| `situacao_das` | Situação do DAS (Simples Nacional) numa competência: apuração, declaração PGDAS-D transmitida pela API, guia DAS emitida e erros recentes. | `empresa`, `competencia` |
| `receita_bruta_mensal` | Receita bruta mês a mês (até 36 meses): saídas + serviços + CF-e de acumuladores que incidem sobre receita bruta, menos devoluções; para o Simples traz também a base apurada. | `empresa`, `de`, `ate` |
| `situacao_reinf` | Situação da EFD-Reinf numa competência: fechamento (R-2099/R-2098), eventos enviados, aceitos, rejeitados e aguardando, e rejeições recentes. | `empresa`, `competencia` |
| `resumo_folha` | Totais da folha numa competência por tipo de folha: empregados, proventos, descontos e líquido (agregados, sem identificar empregados). | `empresa`, `competencia` |
| `historico_salarial` | Linha do tempo salarial de um empregado (alterações salariais e contratuais) com checagem de continuidade e das contas de percentual e adição. | `empresa`, `empregado` |
| `classificacao_produto` | Classificação fiscal de um produto numa data: PIS/COFINS (CST, tipo de contribuição, monofásico, alíquotas), ICMS, IPI e substituição tributária. | `empresa`, `produto`, `data` |
| `visao_mensal` | Visão do mês da empresa numa só resposta: receita bruta, guias, folha e estado das obrigações (eSocial, EFD-Reinf e, no Simples, DAS), com alertas. | `empresa`, `competencia` |
| `perfil_empresa` | Perfil completo da empresa: cadastro, regimes e impostos, parâmetros da contabilidade e da folha, e último fechamento no eSocial. | `empresa`, `data` |
| `guias_do_mes` | Guias de impostos da empresa numa competência: imposto, código de recolhimento, vencimento, saldo a recolher, valor pago e situação. | `empresa`, `competencia`, `incluir_sem_saldo` |
| `memoria_calculo_folha` | Memória de cálculo da folha de um empregado numa competência: cada base (INSS, FGTS, IRRF, férias...) com base, taxa e valor. | `empresa`, `empregado`, `competencia`, `tipo_folha` |
| `situacao_esocial` | Situação do eSocial da empresa numa competência: se a folha está fechada (S-1299), remuneração (S-1200) e pagamentos (S-1210) enviados, e pendências. | `empresa`, `competencia` |

## `receita_bruta_simples`

Receita bruta do mês no Simples Nacional: recalcula a partir dos documentos e compara com a base que a Domínio apurou.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês no formato AAAA-MM

**Fontes:** `efsaidas`, `efservicos`, `efcupom_fiscal_eletronico_impostos`, `efentradas`, `efacumulador_vigencia`, `efsdoimp_simples_nacional`

**Validação:** 38 de 40 empresa/competências da amostra aleatória fecham ao centavo (scripts/conciliar_receita_simples.py).

## `perfil_fiscal`

Perfil fiscal da empresa numa data: regimes federal, estadual e municipal em vigor, impostos ativos e evidências do que a empresa realmente apura.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `data`: data AAAA-MM-DD (padrão: hoje)

**Fontes:** `efparametro_vigencia`, `efparametro_vigencia_impostos`, `geimposto`, `efsdoimp_simples_nacional`, `efsdoimp`

**Validação:** regimes 4 (Simples), 5 (presumido) e 2 (variante do Simples) deduzidos dos dados; 1 provável real; 6, 8 e 9 não determinados.

## `informativos_da_empresa`

Informativos (obrigações acessórias) preparados para a empresa no período, com campos informados, retificadora e número de recibo.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `de`: mês inicial AAAA-MM
- `ate`: opcional: mês final AAAA-MM (padrão: igual a de)
- `informativo`: opcional: código do informativo (veja a entidade informativo)

**Fontes:** `efoutrosdados`, `efoutrosdados_dados`, `efinformativos`

**Validação:** todo campo tem cabeçalho (0 órfãos em 3,8 mi); recibo e retificadora só existem em alguns informativos.

## `apuracao_lalur`

Apuração do IRPJ e da CSLL pelo lucro real (Lalur) numa competência, com conferência das identidades do cálculo.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM

**Fontes:** `lrcalculo`, `lrcalculo_irpj_real`, `lrcalculo_csll_real`, `lrlucro_antes_csll_irpj`

**Validação:** lucro real, base, 15%, 9%, adicional e valor a recolher (piso zero) fecham em 100% dos 3.108 cálculos; deduções da CSLL em 3.103.

## `situacao_das`

Situação do DAS (Simples Nacional) numa competência: apuração, declaração PGDAS-D transmitida pela API, guia DAS emitida e erros recentes.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM

**Fontes:** `efsdoimp_simples_nacional`, `efdas_api_envio_arquivos`, `efdas_api_envio_arquivos_mensagem`

**Validação:** legenda da situação (0-4) bate 1 para 1 com os códigos HTTP das mensagens; retificadora = a partir da 2ª transmissão com sucesso (1.334 de 1.334). Só a partir de 2024-04.

## `receita_bruta_mensal`

Receita bruta mês a mês (até 36 meses): saídas + serviços + CF-e de acumuladores que incidem sobre receita bruta, menos devoluções; para o Simples traz também a base apurada.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `de`: mês inicial AAAA-MM
- `ate`: mês final AAAA-MM

**Fontes:** `efsaidas`, `efservicos`, `efcupom_fiscal_eletronico_impostos`, `efentradas`, `efacumulador_vigencia`, `efsdoimp_simples_nacional`

**Validação:** mesma regra de receita_bruta_simples (38 de 40 competências do Simples fecham ao centavo).

## `situacao_reinf`

Situação da EFD-Reinf numa competência: fechamento (R-2099/R-2098), eventos enviados, aceitos, rejeitados e aguardando, e rejeições recentes.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM

**Fontes:** `efd_reinf_envio_arquivos`, `efd_reinf_envio_arquivos_erros`

**Validação:** aceito = situação 1 com recibo (99,7%); rejeitado = situação 3 (99,8% com erro); fechamento = último R-2098/R-2099 aceito.

## `resumo_folha`

Totais da folha numa competência por tipo de folha: empregados, proventos, descontos e líquido (agregados, sem identificar empregados).

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM

**Fontes:** `fobasesserv`, `foliquidosfilepr`

**Validação:** líquido gravado = proventos - descontos em 254 de 254 cálculos/empregados (empresa 354, 2025+). Dado financeiro.

## `historico_salarial`

Linha do tempo salarial de um empregado (alterações salariais e contratuais) com checagem de continuidade e das contas de percentual e adição.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `empregado`: código do empregado (int)

**Fontes:** `foaltesal`, `foempregados_alteracao_contratual`, `focargos`

**Validação:** percentual 3.727/3.731; adição 107/107; continuidade 8.915/8.955. Dado financeiro por pessoa identificável.

## `classificacao_produto`

Classificação fiscal de um produto numa data: PIS/COFINS (CST, tipo de contribuição, monofásico, alíquotas), ICMS, IPI e substituição tributária.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `produto`: código do produto (texto)
- `data`: data AAAA-MM-DD (padrão: hoje)

**Fontes:** `efprodutos_vigencia`, `efprodutos`

**Validação:** vigência em uso = a mais recente até a data; todas as vigências das 5 maiores empresas têm o produto no cadastro (0 sem cadastro em 71.973).

## `visao_mensal`

Visão do mês da empresa numa só resposta: receita bruta, guias, folha e estado das obrigações (eSocial, EFD-Reinf e, no Simples, DAS), com alertas.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM

**Fontes:** `receita_bruta_mensal`, `guias_do_mes`, `resumo_folha`, `situacao_esocial`, `situacao_reinf`, `situacao_das`, `receita_bruta_simples`, `informativos_da_empresa`, `perfil_empresa`

**Validação:** compõe funções já conferidas; blocos que não se aplicam vêm como null com o motivo.

## `perfil_empresa`

Perfil completo da empresa: cadastro, regimes e impostos, parâmetros da contabilidade e da folha, e último fechamento no eSocial.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `data`: data AAAA-MM-DD (padrão: hoje)

**Fontes:** `geempre`, `efparametro_vigencia`, `ctparmto`, `foparmto`, `foempregados`, `foesocial_dados_eventos`

**Validação:** junta funções e entidades já conferidas; blocos ausentes vêm como null com o motivo.

## `guias_do_mes`

Guias de impostos da empresa numa competência: imposto, código de recolhimento, vencimento, saldo a recolher, valor pago e situação.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês AAAA-MM
- `incluir_sem_saldo`: opcional: inclui apurações sem saldo a recolher

**Fontes:** `efsdoimp_por_recolhimento`, `efpagimp`, `geimposto`

**Validação:** valor pago fecha com a soma dos pagamentos em 98,2% (2.044 de 2.082 guias, 2023-2024); registro de pagamentos incompleto a partir de 2024 (avisado na resposta).

## `memoria_calculo_folha`

Memória de cálculo da folha de um empregado numa competência: cada base (INSS, FGTS, IRRF, férias...) com base, taxa e valor.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `empregado`: código do empregado (int)
- `competencia`: mês AAAA-MM
- `tipo_folha`: opcional: código do tipo de folha (ex.: 11 = mensal)

**Fontes:** `fobasesserv`, `focalculosbases`, `focadbases`

**Validação:** valor = base x taxa / 100 em 86,6% das bases com taxa (empresa 354, 2026); as demais são progressivas ou com dedução. Dado financeiro por pessoa: uso restrito.

## `situacao_esocial`

Situação do eSocial da empresa numa competência: se a folha está fechada (S-1299), remuneração (S-1200) e pagamentos (S-1210) enviados, e pendências.

**Parâmetros:**
- `empresa`: código da empresa (int)
- `competencia`: mês no formato AAAA-MM

**Fontes:** `foesocial_dados_eventos`, `foesocial_eventos`

**Validação:** fechamento = último S-1298/S-1299 da competência (padrão fechar-reabrir-fechar visto nos dados); aceite = recibo + validado = 1 (99,99% dos registros).
