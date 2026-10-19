# Módulo `casos_de_uso`

| Ferramenta | Tipo | Tabela | Obrigatórios | Validação |
|---|---|---|---|---|
| `visao_mensal` | caso_de_uso |  | empresa, competencia | ✔ |
| `situacao_reinf` | caso_de_uso | efd_reinf_envio_arquivos, efd_reinf_envio_arquivos_erros | empresa, competencia | ✔ |
| `informativos_da_empresa` | caso_de_uso | efoutrosdados, efoutrosdados_dados, efinformativos | empresa, de | ✔ |
| `perfil_fiscal` | caso_de_uso | efparametro_vigencia, efparametro_vigencia_impostos, geimposto, efsdoimp_simples_nacional, efsdoimp | empresa | ✔ |
| `classificacao_produto` | caso_de_uso | efprodutos_vigencia, efprodutos | empresa, produto | ✔ |
| `receita_bruta_simples` | caso_de_uso | efsaidas, efservicos, efcupom_fiscal_eletronico_impostos, efentradas, efacumulador_vigencia, efsdoimp_simples_nacional | empresa, competencia | ✔ |
| `receita_bruta_mensal` | caso_de_uso | efsaidas, efservicos, efcupom_fiscal_eletronico_impostos, efentradas, efacumulador_vigencia, efsdoimp_simples_nacional | empresa, de, ate | ✔ |
| `guias_do_mes` | caso_de_uso | efsdoimp_por_recolhimento, efpagimp, geimposto | empresa, competencia | ✔ |
| `situacao_das` | caso_de_uso | efsdoimp_simples_nacional, efdas_api_envio_arquivos, efdas_api_envio_arquivos_mensagem | empresa, competencia | ✔ |
| `historico_salarial` | caso_de_uso | foaltesal, foempregados_alteracao_contratual, focargos | empresa, empregado | ✔ |
| `resumo_folha` | caso_de_uso | fobasesserv, foliquidosfilepr | empresa, competencia | ✔ |
| `memoria_calculo_folha` | caso_de_uso | fobasesserv, focalculosbases, focadbases | empresa, empregado, competencia | ✔ |
| `situacao_esocial` | caso_de_uso | foesocial_dados_eventos, foesocial_eventos | empresa, competencia | ✔ |
| `perfil_empresa` | caso_de_uso | geempre, efparametro_vigencia, ctparmto, foparmto, foempregados, foesocial_dados_eventos | empresa | ✔ |
| `apuracao_lalur` | caso_de_uso | lrcalculo, lrcalculo_irpj_real, lrcalculo_csll_real, lrlucro_antes_csll_irpj | empresa, competencia | ✔ |

## `apuracao_lalur`

Apuração do lucro real (IRPJ e CSLL) na competência.
Apuração do IRPJ e da CSLL pelo lucro real (Lalur) da empresa numa competência, com a conferência das identidades do cálculo.
Usa o cálculo mais recente da competência (a empresa pode recalcular). Traz o IRPJ (lucro real, 15%, adicional, deduções, a recolher) e a CSLL (base, 9%, deduções,
a recolher), e `conferencia`: recalcula cada passo e diz se bate com o gravado (validado em 3.108 cálculos: lucro real, base, 15%, 9%, adicional e a recolher com piso zero).
QUANDO USAR: ver lucro antes do IR, base, IRPJ 15%, adicional, CSLL 9% e valor a recolher.
FONTES (tabelas lidas): lrcalculo, lrcalculo_irpj_real, lrcalculo_csll_real, lrlucro_antes_csll_irpj.
CONFERÊNCIA CONTRA OS DADOS: lucro real, base, 15%, 9%, adicional e valor a recolher (piso zero) fecham em 100% dos 3.108 cálculos; deduções da CSLL em 3.103.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM

## `perfil_empresa`

Perfil completo da empresa (cadastro, fiscal, contábil, folha).
Perfil completo da empresa: cadastro, perfil fiscal (regimes e impostos), parâmetros da contabilidade e da folha, e situação do eSocial.
Porta de entrada para entender uma empresa antes de consultar o resto: junta o que `perfil_fiscal` e `situacao_esocial` devolvem com o cadastro e os parâmetros
contábeis e de folha. Cada bloco que a empresa não tem vem como null, com o motivo. Contém CNPJ/CPF (dado identificável).
QUANDO USAR: ter, numa só chamada, o retrato da empresa: regime, parâmetros, empregados e envios.
FONTES (tabelas lidas): geempre, efparametro_vigencia, ctparmto, foparmto, foempregados, foesocial_dados_eventos.
CONFERÊNCIA CONTRA OS DADOS: junta funções e entidades já conferidas; blocos ausentes vêm como null com o motivo.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `data`: data AAAA-MM-DD (padrão: hoje)

## `visao_mensal`

Visão mensal consolidada da empresa.
Visão do mês da empresa numa só resposta: receita bruta, guias de impostos, folha de pagamento e o estado das obrigações (eSocial, EFD-Reinf e, no Simples, DAS/PGDAS-D).
Chama as funções já conferidas (receita_bruta_mensal, guias_do_mes, resumo_folha, situacao_esocial, situacao_reinf, situacao_das) e junta os alertas. Um bloco que não se
aplica à empresa (ex.: sem folha) vem como null com o motivo em `observacoes`. Dados financeiros da empresa.
QUANDO USAR: responder como está a empresa no mês: receita, guias, folha, eSocial, REINF, DAS e informativos.
FONTES (tabelas lidas): receita_bruta_mensal, guias_do_mes, resumo_folha, situacao_esocial, situacao_reinf, situacao_das, receita_bruta_simples, informativos_da_empresa, perfil_empresa.
CONFERÊNCIA CONTRA OS DADOS: compõe funções já conferidas; blocos que não se aplicam vêm como null com o motivo.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM

## `receita_bruta_simples`

Receita bruta do mês no Simples Nacional (recalculada × apurada).
Receita bruta do mês no Simples Nacional: recalcula a partir dos documentos e compara com a base que a Domínio apurou.
Receita = saídas não canceladas + serviços não cancelados + cupons fiscais (CF-e) vigentes, todos de acumuladores que incidem sobre
receita bruta (IREC_ACU = S, vigência em vigor na data do documento), menos as devoluções de venda lançadas em entradas com acumulador
que incide sobre devolução (IDEV_ACU = S).
Conferido contra efsdoimp_simples_nacional (imposto 44, linhas de detalhe): fecha ao centavo em 38 de 40 empresa/competências de uma
amostra aleatória (scripts/conciliar_receita_simples.py).
QUANDO USAR: conferir a receita bruta do mês de uma empresa do Simples e ver se bate com a base que a Domínio apurou (saídas + serviços + CF-e − devoluções).
FONTES (tabelas lidas): efsaidas, efservicos, efcupom_fiscal_eletronico_impostos, efentradas, efacumulador_vigencia, efsdoimp_simples_nacional.
CONFERÊNCIA CONTRA OS DADOS: 38 de 40 empresa/competências da amostra aleatória fecham ao centavo (scripts/conciliar_receita_simples.py).
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês no formato AAAA-MM

## `receita_bruta_mensal`

Receita bruta mês a mês (série).
Receita bruta mês a mês (até 36 meses): saídas + serviços + cupons fiscais (CF-e) de acumuladores que incidem sobre receita bruta, menos devoluções de venda.
Mesma regra de `receita_bruta_simples` (IREC_ACU/IDEV_ACU com a vigência do acumulador na data do documento), em série e sem exigir regime do Simples: serve para
presumido, real e Simples. Para o Simples, cada mês traz também a base que a Domínio apurou, para comparação. Regime de competência (data do documento).
QUANDO USAR: ver a evolução mensal da receita bruta de uma empresa do Simples em um intervalo.
FONTES (tabelas lidas): efsaidas, efservicos, efcupom_fiscal_eletronico_impostos, efentradas, efacumulador_vigencia, efsdoimp_simples_nacional.
CONFERÊNCIA CONTRA OS DADOS: mesma regra de receita_bruta_simples (38 de 40 competências do Simples fecham ao centavo).
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `de` (obrigatório): mês inicial AAAA-MM
- `ate` (obrigatório): mês final AAAA-MM

## `perfil_fiscal`

Perfil fiscal da empresa (regime, impostos, apuração).
Perfil fiscal da empresa numa data: regimes federal, estadual e municipal em vigor, impostos ativos e evidências do que a empresa realmente apura.
O regime federal vem de efparametro_vigencia.rfed_par, cuja legenda NÃO está no banco: aqui é deduzida do cruzamento com as apurações (5 = lucro
presumido, 4 e 2 = Simples; os demais códigos têm evidência fraca). Por isso a resposta traz `evidencias`: se há apuração do Simples (imposto 44)
e de IRPJ nos 12 meses até a data, que confirmam ou contradizem o regime.
QUANDO USAR: saber o regime tributário e quais impostos a empresa apura numa data.
FONTES (tabelas lidas): efparametro_vigencia, efparametro_vigencia_impostos, geimposto, efsdoimp_simples_nacional, efsdoimp.
CONFERÊNCIA CONTRA OS DADOS: regimes 4 (Simples), 5 (presumido) e 2 (variante do Simples) deduzidos dos dados; 1 provável real; 6, 8 e 9 não determinados.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `data`: data AAAA-MM-DD (padrão: hoje)

## `guias_do_mes`

Guias de recolhimento do mês (apurado, pago e saldo).
Guias de impostos da empresa numa competência: imposto, código de recolhimento, vencimento, saldo a recolher, valor pago e situação.
ATENÇÃO: o registro de pagamentos no sistema está praticamente parado entre 2023 e 2025, conforme a empresa (guias de 2024 em diante quase nunca têm valor pago; o último pagamento gravado é de 2025-04): `sem_pagamento_registrado`
NÃO significa guia em aberto. Onde há registro, o valor pago desta apuração fecha com a soma dos pagamentos em 98,2% das guias (2023-2024).
QUANDO USAR: listar o que a empresa tem a recolher no mês por imposto, com vencimento e pagamentos.
FONTES (tabelas lidas): efsdoimp_por_recolhimento, efpagimp, geimposto.
CONFERÊNCIA CONTRA OS DADOS: valor pago fecha com a soma dos pagamentos em 98,2% (2.044 de 2.082 guias, 2023-2024); registro de pagamentos incompleto a partir de 2024 (avisado na resposta).
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM
- `incluir_sem_saldo`: opcional: inclui apurações sem saldo a recolher

## `situacao_das`

Situação do DAS (Simples Nacional) no mês.
Situação do DAS (Simples Nacional) da empresa numa competência: apuração, declaração PGDAS-D transmitida pela API, guia DAS emitida e erros recentes.
Estado: sem_apuracao | declaracao_nao_transmitida | declarada_sem_das | declarada_e_das_emitido. A integração por API só existe a partir de 2024-04: antes disso
o estado não pode ser deduzido. Retificadora = declaração transmitida com sucesso depois da primeira na mesma competência (por evidência: 1.334 de 1.334).
QUANDO USAR: saber se o DAS do mês foi apurado, transmitido pela API, retificado ou rejeitado.
FONTES (tabelas lidas): efsdoimp_simples_nacional, efdas_api_envio_arquivos, efdas_api_envio_arquivos_mensagem.
CONFERÊNCIA CONTRA OS DADOS: legenda da situação (0-4) bate 1 para 1 com os códigos HTTP das mensagens; retificadora = a partir da 2ª transmissão com sucesso (1.334 de 1.334). Só a partir de 2024-04.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM

## `situacao_reinf`

Situação da EFD-Reinf no mês.
Situação da EFD-Reinf da empresa numa competência: fechamento da série R-2000 (R-2099 / reabertura R-2098), eventos enviados por tipo e rejeições.
Aceito = situação 1 com número de recibo (99,7% das situações 1 têm recibo); rejeitado = situação 3 (99,8% têm erro registrado); 0 = aguardando retorno.
Eventos marcados como excluídos (R-9000) ficam fora. O fechamento vale o ÚLTIMO R-2098/R-2099 aceito da competência.
QUANDO USAR: saber se a EFD-Reinf do mês foi aceita, rejeitada ou está pendente e se a competência foi fechada.
FONTES (tabelas lidas): efd_reinf_envio_arquivos, efd_reinf_envio_arquivos_erros.
CONFERÊNCIA CONTRA OS DADOS: aceito = situação 1 com recibo (99,7%); rejeitado = situação 3 (99,8% com erro); fechamento = último R-2098/R-2099 aceito.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM

## `informativos_da_empresa`

Informativos e obrigações acessórias da empresa.
Informativos (obrigações acessórias) preparados para a empresa no período: qual obrigação, competência, nº de campos informados, retificadora e número de recibo.
Vem de efoutrosdados/efoutrosdados_dados ("outros dados" de cada obrigação). Informativos anuais (DEFIS, DIRF, DMED) têm competência = 1º de janeiro do ano.
`numero_recibo` e `retificadora` só existem em alguns informativos (DCTF, DIRF, Reinf...): vazio não prova que a obrigação não foi transmitida.
QUANDO USAR: ver quais informativos (DCTF, ECD, etc.) foram gerados ou entregues num intervalo.
FONTES (tabelas lidas): efoutrosdados, efoutrosdados_dados, efinformativos.
CONFERÊNCIA CONTRA OS DADOS: todo campo tem cabeçalho (0 órfãos em 3,8 mi); recibo e retificadora só existem em alguns informativos.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `de` (obrigatório): mês inicial AAAA-MM
- `ate`: opcional: mês final AAAA-MM (padrão: igual a de)
- `informativo`: opcional: código do informativo (veja a entidade informativo)

## `classificacao_produto`

Classificação fiscal do produto na data (NCM, CST, alíquotas).
Classificação fiscal de um produto numa data: PIS/COFINS (CST, tipo de contribuição, natureza da receita, monofásico, alíquotas), ICMS, IPI e substituição tributária.
Usa a vigência de maior data até a data pedida (mesma regra de acumuladores e parâmetros). O banco NÃO traz a legenda dos CST: aparecem só os códigos (a legenda oficial vem do layout fiscal, fora do banco); o NCM vem do cadastro.
QUANDO USAR: descobrir como um produto estava classificado fiscalmente em uma data.
FONTES (tabelas lidas): efprodutos_vigencia, efprodutos.
CONFERÊNCIA CONTRA OS DADOS: vigência em uso = a mais recente até a data; todas as vigências das 5 maiores empresas têm o produto no cadastro (0 sem cadastro em 71.973).
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `produto` (obrigatório): código do produto (texto)
- `data`: data AAAA-MM-DD (padrão: hoje)

## `situacao_esocial`

Situação do eSocial no mês (eventos, aceite, fechamento).
Situação do eSocial da empresa numa competência: se a folha está fechada (S-1299), remuneração (S-1200) e pagamentos (S-1210) enviados, e pendências.
Fechamento: vale o ÚLTIMO evento S-1298 (reabertura) ou S-1299 (fechamento) da competência — a competência pode ser fechada, reaberta e fechada de novo.
Um evento está aceito quando tem número de recibo e `validado` = 1; resposta 202 é sucesso com advertência; 401/411 são rejeições. Pendências: eventos
da empresa sem recibo ou aguardando ajuste (qualquer competência).
QUANDO USAR: saber se os eventos do eSocial da competência foram enviados e aceitos e se a folha foi fechada.
FONTES (tabelas lidas): foesocial_dados_eventos, foesocial_eventos.
CONFERÊNCIA CONTRA OS DADOS: fechamento = último S-1298/S-1299 da competência (padrão fechar-reabrir-fechar visto nos dados); aceite = recibo + validado = 1 (99,99% dos registros).
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês no formato AAAA-MM

## `resumo_folha`

Resumo da folha de pagamento do mês.
Totais da folha da empresa numa competência, por tipo de folha: empregados, proventos, descontos e líquido (só agregados, sem identificar empregados).
O líquido gravado (`foliquidosfilepr`) é igual a proventos − descontos em 254 de 254 cálculos/empregados conferidos (empresa 354, 2025+). Só a linha principal do cálculo (`rateio = 0`) entra: a Domínio grava também uma linha de rateio por serviço (`rateio = 1`) que REPETE os mesmos valores, e somar as duas dobra
proventos e descontos. Nem toda base tem líquido
gravado: os tipos 60, 61 e 92 nunca têm e parte da folha mensal também não — por isso há `liquido_gravado` e `bases_sem_liquido`. Dado financeiro da empresa.
QUANDO USAR: ver totais de proventos, descontos e líquido da folha de uma empresa na competência.
FONTES (tabelas lidas): fobasesserv, foliquidosfilepr.
CONFERÊNCIA CONTRA OS DADOS: líquido gravado = proventos - descontos em 254 de 254 cálculos/empregados (empresa 354, 2025+). Dado financeiro.
PRIVACIDADE: devolve dado financeiro por pessoa identificável; use só quando a pergunta exigir.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `competencia` (obrigatório): mês AAAA-MM

## `memoria_calculo_folha`

Memória de cálculo da folha de um empregado.
Memória de cálculo da folha de um empregado numa competência: cada base de cálculo (INSS, FGTS, IRRF, férias, empréstimos...) com a base, a taxa e o valor.
Lê as bases de focalculosbases dos cálculos (I_CALCULOS) do empregado em fobasesserv; só traz bases com valor ou base diferente de zero.
Dados de remuneração por pessoa identificável: uso restrito (campo `sensivel: financeiro` no modelo).
QUANDO USAR: explicar como INSS, FGTS e IRRF de um empregado foram calculados (bases, taxas, valores).
FONTES (tabelas lidas): fobasesserv, focalculosbases, focadbases.
CONFERÊNCIA CONTRA OS DADOS: valor = base x taxa / 100 em 86,6% das bases com taxa (empresa 354, 2026); as demais são progressivas ou com dedução. Dado financeiro por pessoa: uso restrito.
PRIVACIDADE: devolve dado financeiro por pessoa identificável; use só quando a pergunta exigir.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `empregado` (obrigatório): código do empregado (int)
- `competencia` (obrigatório): mês AAAA-MM
- `tipo_folha`: opcional: código do tipo de folha (ex.: 11 = mensal)

## `historico_salarial`

Histórico salarial de um empregado.
Linha do tempo salarial de um empregado: alterações salariais (salário anterior, novo, forma e motivo) e alterações contratuais (cargo, serviço, salário), com checagem
de continuidade (o salário anterior de cada alteração deve ser o novo da anterior; fecha em 99,6% dos pares) e das contas de percentual e adição.
Dado financeiro por pessoa identificável: uso restrito. Datas de 1900-01-01 são o valor padrão (início do contrato, não uma alteração real).
QUANDO USAR: ver as alterações de salário (percentual ou aditivo) ao longo do tempo.
FONTES (tabelas lidas): foaltesal, foempregados_alteracao_contratual, focargos.
CONFERÊNCIA CONTRA OS DADOS: percentual 3.727/3.731; adição 107/107; continuidade 8.915/8.955. Dado financeiro por pessoa identificável.
PRIVACIDADE: devolve dado financeiro por pessoa identificável; use só quando a pergunta exigir.
Somente leitura. Competências no formato AAAA-MM; a resposta traz de onde vieram os números e o que conferir.

Parâmetros:

- `empresa` (obrigatório): código da empresa (int)
- `empregado` (obrigatório): código do empregado (int)
