# EFSDOIMP_SUBTRI_POR_UF_SC — Saldo dos Impostos - Substituição Tributária Por SC
122 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competência |
| PDIC_SIM | integer(4) | PK |  | Periodicidade |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| DEBITO_ICMS_SOBRE_ESTOQUE | numeric(13) |  |  | Débito ICMS Sobre Estoque |
| BASE_CALCULO_ICMS_ST_ESTOQUE_FARMACIA | numeric(13) |  |  | Base de Cálculo ICMS ST Sobre Estoque - Farmácia |
| VALOR_ICMS_ST_ESTOQUE_FARMACIA | numeric(13) |  |  | Valor ICMS ST Sobre Estoque - Farmácia |
| VALOR_ICMS_SOBRE_FRETE | numeric(13) |  |  | Valor ICMS Sobre Frete |
| BASE_CALCULO_ICMS_SOBRE_FRETE | numeric(13) |  |  | Base Cálculo ICMS Sobre Frete |
| BASE_CALCULO_ICMS_ST_SOBRE_ESTOQUE | numeric(13) |  |  | Base Cálculo ICMS ST Sobre Estoque |
| VALOR_ICMS_ST_SOBRE_ESTOQUE | numeric(13) |  |  | Valor ICMS ST Sobre Estoque |
| BASE_CALCULO_ICMS_ST_SOBRE_ESTOQUE_NAO_DEMONSTRADA | numeric(13) |  |  | Base Cálculo ICMS ST Sobre Estoque - Não Demonstrada na DIME |
| VALOR_ICMS_ST_SOBRE_ESTOQUE_NAO_DEMONSTRADA | numeric(13) |  |  | Valor ICMS ST Sobre Estoque - Não Demonstrada na DIME |
| VALOR_FUNDOSOCIAL_ST | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST |
| CREDITO_ADICIONAL_FUNDOSOCIAL_ST | numeric(13) |  |  | Crédito Adicional do FUNDOSOCIAL - ST |
| SALDO_ST_SC | numeric(13) |  |  | Saldo ST SC |
| ST_ANTECIPADA_COMBUSTIVEIS | numeric(13) |  |  | ST Antecipada Combustíveis |
| BASE_CALCULO_FUNDOSOCIAL_ST | numeric(13) |  |  | Base de Cálculo do FUNDOSOCIAL - ST |
| CREDITO_TRANSFERIDO_ESTABELECIMENTO_CONSOLIDADOR | numeric(13) |  |  | Crédito transferido ao estabelecimento consolidador |
| DEBITO_RECEBIDO_ESTABELECIMENTO_CONSOLIDADOR | numeric(13) |  |  | Débitos recebidos de estabelecimentos consolidados |
| CREDITO_RECEBIDO_ESTABELECIMENTO_CONSOLIDADOR | numeric(13) |  |  | Créditos recebidos de estabelecimentos consolidados |
| DEBITO_TRANSFERIDO_ESTABELECIMENTO_CONSOLIDADOR | numeric(13) |  |  | Débito transferido ao estabelecimento consolidador |
| RESSARCIMENTO_ICMS_ST_VENDAS_SIMPLES_NACIONAL | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para Simples Nacional |
| RESSARCIMENTO_ICMS_ST_VENDAS_OUTRAS_UF | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para outras UF |
| CREDITO_DEVOLUCAO_ST | numeric(13) |  |  | Crédito Devolução ST |
| VALOR_ICMS_SOBRE_ESTOQUE_PRODUTOS_EXCLUIDOS_SUBTRI | numeric(13) |  |  | Valor do ICMS sobre estoque - Produtos excluídos SUBTRI |
| APROPRIACAO_CREDITO_DEVOLUCAO_ST | numeric(13) |  |  | Apropriação de crédito por devolução sujeita à Subt. Trib. An. 3, art. 23 |
| ESTORNO_CREDITO_RESSARCIMENTO_ST_VENDAS_SIMPLES_NACIONAL | numeric(13) |  |  | Estorno de crédito referente ressarcimento de ICMS ST nas vendas para SN - Decreto 3.509/10 |
| DEBITO_FECOP_ICMS_ST | numeric(13) |  |  | Débito referente ao FECOP-PR - ICMS ST |
| DEVOLUCAO_FECOP_ICMS_ST | numeric(13) |  |  | Devolução referente ao FECOP-PR - ICMS ST |
| VALOR_FUNDOSOCIAL_ST_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST - Confecção Art 21 - Centralizador |
| VALOR_FUNDOSOCIAL_ST_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA | numeric(13) |  |  | Valor do FUNDOSOCIAL - ST - Confecção Art 21 - Centralizadora |
| RESSARCIMENTO_ICMS_ST_ACOBERTADO_NFE | numeric(13) |  |  | Ressarcimento de ICMS ST acobertado por NF-e |
| CREDITO_ICMS_VENDA_OUTRA_UF | numeric(13) |  |  | Crédito ICMS Próprio nas vendas para outras UFs |
| VALOR_COMPLEMENTACAO_ICMS_ST | numeric(13) |  |  | Valor de Complementação do ICMS ST |
| DATA_VENCIMENTO_COMPLEMENTACAO | date(4) |  | S | Data de Vencimento Complementação |
| VALOR_PAGO | numeric(13) |  |  | Valor pago |
| I_RECOLHIMENTO | integer(4) | PK |  | Recolhimento |
