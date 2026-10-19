# EFSDOIMP_ESTADUAL_SC — Saldo dos Impostos - Estadual SC
61 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| BASE_CALCULO_DEVOLUCAO_TTD_409_410_411 | numeric(13) |  |  | Base de Calculo de ICMS Devolução TTD 409, 410 ou 411 |
| BASE_CALCULO_SAIDA_TTD_409_410_411 | numeric(13) |  |  | Base de Calculo de ICMS Saída TTD 409, 410 ou 411 |
| CREDITO_PRESUMIDO_TTD_409_410_411 | numeric(13) |  |  | Valor Crédito Presumido TTD 409, 410 ou 411 |
| DEVOLUCAO_CREDITO_PRESUMIDO_TTD_409_410_411 | numeric(13) |  |  | Valor Devolução de Crédito Presumido TTD 409, 410 ou 411 |
| ESTORNO_DEBITO_TTD_409_410_411 | numeric(13) |  |  | Valor de Estorno de Débito TTD 409, 410 ou 411 |
| DEVOLUCAO_ESTORNO_DEBITO_TTD_409_410_411 | numeric(13) |  |  | Valor de Devolução de Estorno de Débito TTD 409, 410 ou 411 |
| DEVOLUCAO_FUNDEC_TTD_409_410_411 | numeric(13) |  |  | Valor Devolução FUNDEC TTD 409, 410 ou 411 |
| DEVOLUCAO_FUNDO_EDUCACAO_TTD_409_410_411 | numeric(13) |  |  | Valor Devolução Fundo Educação TTD 409, 410 ou 411 |
| DEVOLUCAO_PRO_EMPREGO_TTD_409_410_411 | numeric(13) |  |  | Valor Devolução Pró-Emprego TTD 409, 410 ou 411 |
| CREDITO_PRESUMIDO_GADO | numeric(13) |  |  | Valor Crédito Presumido Gado |
| CREDITO_PRESUMIDO_GADO_TIPO_1_INTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 1 Operação Estadual |
| CREDITO_PRESUMIDO_GADO_TIPO_2_INTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 2 Operação Estadual |
| CREDITO_PRESUMIDO_GADO_TIPO_3_INTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 3 Operação Estadual |
| CREDITO_PRESUMIDO_GADO_TIPO_1_EXTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 1 Operação Interestadual |
| CREDITO_PRESUMIDO_GADO_TIPO_2_EXTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 2 Operação Interestadual |
| CREDITO_PRESUMIDO_GADO_TIPO_3_EXTERNO | numeric(13) |  |  | Valor Crédito Presumido Gado Tipo 3 Operação Interestadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_1_INTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 1 Operação Estadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_2_INTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 2 Operação Estadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_3_INTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 3 Operação Estadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_1_EXTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 1 Operação Interestadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_2_EXTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 2 Operação Interestadual |
| ESTORNO_CREDITO_PRESUMIDO_GADO_TIPO_3_EXTERNO | numeric(13) |  |  | Valor Estorno Crédito Presumido Gado Tipo 3 Operação Interestadual |
| CREDITO_PRESUMIDO_MADEIRA_SERRADA | numeric(13) |  |  | Valor Crédito Presumido Madeira Serrada |
| DEVOLUCAO_CREDITO_PRESUMIDO_MADEIRA_SERRADA | numeric(13) |  |  | Valor Devolução Crédito Presumido Madeira Serrada |
| CREDITO_PRO_EMPREGO | numeric(13) |  |  | Valor Crédito Pro Emprego |
| ESTORNO_CREDITO_PRO_EMPREGO | numeric(13) |  |  | Valor Estorno Crédito Pro Emprego |
| CARENCIA_PRO_EMPREGO | integer(4) |  |  | Prazo de Carencia Pro Emprego |
| CLASSE_PRO_EMPREGO | integer(4) |  |  | Classe de Vencimento Pro Emprego |
| DEVOLUCAO_FUNDO_SOCIAL_TTD_409_410_411 | numeric(13) |  |  | Valor Devolução Fundo Social - TTD 409, 410 ou 411 |
| RESSARCIMENTO_VENDA_SUBTRI_OUTRAS_UF | numeric(13) |  |  | Ressarcimento nas vendas com Subst. Tributária para outras UF - An. 3, Art. 25, RICMS |
| RESSARCIMENTO_ICMS_ST_VENDA_SIMPLES_NACIONAL | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para Simples Nacional - Decreto n° 3.509/10 |
| RESSARCIMENTO_ICMS_ST_VENDA_OUTRAS_UF | numeric(13) |  |  | Ressarcimento de ICMS ST nas vendas para outras UF - An. 3, Art. 25, RICMS |
| DEVOLUCAO_CREDITO_PRESUMIDO_MATERIAL_RECICLAVEL | numeric(13) |  |  | Valor Devolução Crédito Presumido Material Reciclado |
| CREDITO_PRESUMIDO_MATERIAL_RECICLAVEL | numeric(13) |  |  | Valor Crédito Presumido Material Reciclado |
| CREDITO_CONFECCAO_PRODUTO | numeric(13) |  |  | Crédito presumido confecção - An2, Art. 15, XXXIX |
| ESTORNO_CREDITO_CONFECCAO_PRODUTO | numeric(13) |  |  | Estorno limite do crédito presumido confecção - An2, Art. 15, XXXIX |
| DEVOLUCAO_CREDITO_CONFECCAO_PRODUTO | numeric(13) |  |  | Devolução do crédito presumido confecção - An2, Art. 15, XXXIX |
| CREDITOS_PAGAMENTOS_DEVIDOS_POR_FATO_GERADOR | numeric(13) |  |  | Créditos de pagamentos devidos por ocasião do Fato Gerador |
| CREDITO_CONFECCAO_PRODUTO_REDUCAO_Z | numeric(13) |  |  | Crédito presumido confecção - An2. Art. 15, XXXIX - Redução Z |
| CREDITO_CONFECCAO_PRODUTO_DEMAIS_SAIDAS | numeric(13) |  |  | Crédito presumido confecção - An2. Art. 15, XXXIX - Demais Saídas |
| CREDITO_PRESUMIDO_ARROZ_ENTRADAS_ESTADO | numeric(13) |  |  | Crédito presumido arroz entradas do estado |
| CREDITO_PRESUMIDO_ARROZ_TOTAL_ENTRADAS | numeric(13) |  |  | Crédito presumido arroz total das entradas |
| CREDITO_PRESUMIDO_ARROZ_PROPORCAO_ENTRADAS_ESTADO | numeric(13) |  |  | Crédito presumido arroz proporção entradas estado |
| CREDITO_PRESUMIDO_ARROZ_BASE_CALCULO_INTERESTADUAIS | numeric(13) |  |  | Base calculo crédito presumido arroz |
| CREDITO_PRESUMIDO_ARROZ_PERCENTUAL | numeric(13) |  |  | Percentual crédito presumido arroz |
| CREDITO_PRESUMIDO_ARROZ_VALOR | numeric(13) |  |  | Crédito presumido nas saídas arroz beneficiado |
| CREDITO_PRESUMIDO_ARROZ_DEVOLUCAO | numeric(13) |  |  | Devolução crédito presumido nas saídas arroz beneficiado |
| CREDITO_PRESUMIDO_BARES_RESTAURANTES | numeric(13) |  |  | Crédito Presumido Bares, Restaurantes e Similares - An2, Art. 21, IV |
| ESTORNO_CREDITO_PRESUMIDO_BARES_RESTAURANTES | numeric(13) |  |  | Estorno de ICMS dos optante do Cred. Presumido Bares, Restaurantes e Similares, An2.Art. 21 |
| DEVOLUCAO_CREDITO_PRESUMIDO_BARES_RESTAURANTES | numeric(13) |  |  | Devolução de Crédito Presumido - Bares, Restaurantes e Similares, An2, Art.21, IV |
| CREDITO_PRESUMIDO_LEITE_SAIDAS_TRIBUTADAS | numeric(13) |  |  | Crédito presumido leite Saídas Tributadas |
| CREDITO_PRESUMIDO_LEITE_TOTAL_SAIDAS | numeric(13) |  |  | Crédito presumido leite Total Saídas |
| CREDITO_PRESUMIDO_LEITE_PROPORCAO_SAIDAS_TRIBUTADAS | numeric(13) |  |  | Crédito presumido leite Proporção Saídas Tributadas |
| CREDITO_PRESUMIDO_LEITE_ENTRADAS | numeric(13) |  |  | Crédito presumido leite Entradas |
| CREDITO_PRESUMIDO_LEITE_VALOR_UTILIZADO | numeric(13) |  |  | Crédito presumido leite Valor Utilizado |
| CREDITO_PRESUMIDO_LEITE_ESTORNO | numeric(13) |  |  | Crédito presumido leite Estorno |
| ESTORNO_CREDITO_SUBTRI | numeric(13) |  |  | Estorno crédito da Substituição Tributária |
| CREDITO_ATIVO_IMOBILIZADO_ANTERIOR | numeric(13) |  |  | Crédito Ativo Imobilizado de períodos anteriores |
| DEBITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Débito ativo imobilizado - Art. 53, 7ª, I |
| CREDITO_PRESUMIDO_ERVA_MATE | numeric(13) |  |  | Crédito presumido erva-mate - An2, Art. 15, XLII |
| DEVOLUCAO_CREDITO_PRESUMIDO_ERVA_MATE | numeric(13) |  |  | Devolução do crédito presumido erva-mate - An2, Art. 15, XLII |
| CREDITO_PRESUMIDO_REDUCAO_Z_TTD_409_410_411 | numeric(13) |  |  | Valor Crédito Presumido TTD 409, 410 ou 411 com origem das Reduções Z |
| ESTORNO_DEBITO_REDUCAO_Z_TTD_409_410_411 | numeric(13) |  |  | Valor de Estorno de Débito TTD 409, 410 ou 411 com origem das Reduções Z |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_21 | numeric(13) |  |  | Estorno do ICMS nas operações de Confecção. Anexo 2, Art. 21, IX |
| ESTORNO_DEBITO_INDEVIDO_TRANSPORTE_OUTRA_UF | numeric(13) |  |  | Estorno de débito de ICMS lançado indevidamente em transporte iniciado em outra UF |
| ESTORNO_DEBITO_INDEVIDO_OUTRAS_OPERACOES | numeric(13) |  |  | Estorno de débito de ICMS lançado indevidamente em todas as operações |
| ESTORNO_DEBITO_INDEVIDO_OUTRAS_OPERACOES_AJUSTE | numeric(13) |  |  | Estorno de débito de ICMS lançado indevidamente em todas as operações - Ajuste de crédito |
| ESTORNO_DEBITO_INDEVIDO_OUTRAS_OPERACOES_ESTORNO | numeric(13) |  |  | Estorno de débito de ICMS lançado indevidamente em todas as operações - Estorno de débito |
| CREDITO_PRESUMIDO_ABATE_PROPORCAO_ENTRADAS_ESTADO | numeric(13) |  |  | Crédito presumido abate - Proporção das entradas - Internas |
| CREDITO_PRESUMIDO_ABATE_PROPORCAO_ENTRADAS_TOTAL | numeric(13) |  |  | Crédito presumido abate - Proporção das entradas - Total |
| CREDITO_PRESUMIDO_ABATE_PROPORCAO_PERCENTUAL | numeric(13) |  |  | Crédito presumido abate - Proporção das entradas - Proporção |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_ALIQUOTA | numeric(13) |  |  | Crédito presumido abate - Saídas - Alíquota |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_SUINOS | numeric(13) |  |  | Crédito presumido abate - Saídas - Suínos |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_AVES | numeric(13) |  |  | Crédito presumido abate - Saídas - Aves |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_SUINOS_DEVOLUCAO | numeric(13) |  |  | Crédito presumido abate - Saídas - Suínos - Devolução |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_AVES_DEVOLUCAO | numeric(13) |  |  | Crédito presumido abate - Saídas - Aves - Devolução |
| CREDITO_PRESUMIDO_ABATE_ENTRADAS_AVES_SUINOS | numeric(13) |  |  | Crédito presumido abate - Entradas |
| CREDITO_PRESUMIDO_ABATE_ENTRADAS_AVES_SUINOS_DEVOLUCAO | numeric(13) |  |  | Crédito presumido abate - Entradas - Devolução |
| CREDITO_PRESUMIDO_ABATE_LIMITE | numeric(13) |  |  | Crédito presumido abate - Limite de crédito |
| CREDITO_PRESUMIDO_ABATE_LIMITE_UTILIZADO | numeric(13) |  |  | Crédito presumido abate - Limite de crédito - Crédito utilizado |
| CREDITO_PRESUMIDO_ABATE_LIMITE_ESTORNO | numeric(13) |  |  | Crédito presumido abate - Limite de crédito - Estorno |
| CREDITO_PRESUMIDO_EMBARCACAO_NAUTICA | numeric(13) |  |  | Crédito presumido embarcações náuticas - An2, Art. 176 |
| DEVOLUCAO_CREDITO_PRESUMIDO_EMBARCACAO_NAUTICA | numeric(13) |  |  | Devolução do crédito presumido embarcações náuticas - An2, Art. 176 |
| ESTORNO_CREDITO_PRESUMIDO_EMBARCACAO_NAUTICA | numeric(13) |  |  | Estorno do ICMS nas operações de embarcações náuticas - An2, Art. 176 |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_SAIDA | numeric(13) |  |  | Crédito presumido confecção - Saídas |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_REDUCAO_Z | numeric(13) |  |  | Crédito presumido confecção - Redução Z |
| CREDITO_PRESUMIDO_LEITE_XXVIII | numeric(13) |  |  | Crédito Presumido Leite XXVIII |
| CREDITO_PRESUMIDO_LEITE_XXIX | numeric(13) |  |  | Crédito Presumido Leite XXIX |
| DEVOLUCAO_CREDITO_PRESUMIDO_LEITE_XXVIII | numeric(13) |  |  | Devolução Crédito Presumido Leite XXVIII |
| DEVOLUCAO_CREDITO_PRESUMIDO_LEITE_XXIX | numeric(13) |  |  | Devolução Crédito Presumido Leite XXIX |
| ESTORNO_CREDITO_PRESUMIDO_LEITE | numeric(13) |  |  | ESTORNO CRÉDITO PRESUMIDO LEITE - AN2, ART. 15, XXVIII E XXIX - ANTERIOR 04/2023 |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador |
| ANTECIPACAO_1_DECENDIO_TELECOMUNICACOES | numeric(13) |  |  | 1º parcela da antecipação do ICMS Telecomunicações sobre o ICMS do mês anterior |
| ANTECIPACAO_2_DECENDIO_TELECOMUNICACOES | numeric(13) |  |  | 2º parcela da antecipação do ICMS Telecomunicações sobre o ICMS do mês anterior |
| CREDITO_PRESUMIDO_VENDAS_INT_INTERNET | numeric(13) |  |  | Crédito Presumido nas vendas interest. a consumidor por meio da Internet - An2, Art. 15, XXX |
| DEVOLUCAO_CREDITO_PRESUMIDO_VENDAS_INT_INTERNET | numeric(13) |  |  | Devolução Crédito Presumido nas vendas interest. a consumidor por meio da Internet - An2, Art. 15, XXX |
| CREDITO_ICMS_SOBRE_ESTOQUE_EXCLUIDOS | numeric(13) |  |  | Crédito ICMS sobre estoque excluídos |
| ESTORNO_CREDITO_PRESUMIDO_LEITE_PERC | numeric(5) |  |  | Estorno Crédito Presumido Leite - Percentual |
| CREDITO_PRESUMIDO_CERVEJA_CHOPE | numeric(13) |  |  | Crédito presumido na saída de cerveja e chope artesanais - An2, Art. 15, XXXII |
| CREDITO_PRESUMIDO_CERVEJA_CHOPE_DEVOLUCAO | numeric(13) |  |  | Devolução crédito presumido na saída de cerveja e chope artesanais - An2, Art.15, XXXII |
| CREDITO_PRESUMIDO_VINHO_SAIDAS | numeric(13) |  |  | Crédito Presumido Vinho por Produto - Saídas |
| CREDITO_PRESUMIDO_VINHO_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Vinho por Produto - Redução Z |
| CREDITO_PRESUMIDO_INFORMATICA_ART146 | numeric(13) |  |  | Crédito presumido ind. Prod. Informática - Anexo 2, Art. 146 RICMS |
| CREDITO_PRESUMIDO_INFORMATICA_ART146_DEVOLUCAO | numeric(13) |  |  | Estorno de crédito presumido ind. Prod. Informática - An. 2, Art. 146 RICMS - Devolução |
| CREDITO_PRESUMIDO_INFORMATICA_SAIDAS | numeric(13) |  |  | Crédito presumido ind. Prod. Informática - Saídas |
| CREDITO_PRESUMIDO_INFORMATICA_REDUCAO_Z | numeric(13) |  |  | Crédito presumido ind. Prod. Informática - Redução Z |
| ICMS_SOBRE_ESTOQUE_CREDITO_PRESUMIDO_ART_21_ESTORNO_CREDITOS | numeric(13) |  |  | ICMS sobre estoques na opção pelo Crédito Presumido - An2, Art. 21, § 13 do RICMS |
| ICMS_SOBRE_ESTOQUE_CREDITO_PRESUMIDO_ART_21_OUTROS_CREDITOS | numeric(13) |  |  | ICMS sobre estoques no fim da opção pelo Créd. Presumido - An2, Art. 21, § 13 do RICMS |
| ICMS_SOBRE_ESTOQUE_CREDITO_PRESUMIDO_ART_23_ESTORNO_CREDITOS | numeric(13) |  |  | ICMS sobre estoques na opção pelo Crédito Presumido - An2, Art. 23 do RICMS |
| ICMS_SOBRE_ESTOQUE_CREDITO_PRESUMIDO_ART_23_OUTROS_CREDITOS | numeric(13) |  |  | ICMS sobre estoques no fim da opção pelo Créd. Presumido - An2, Art. 23 do RICMS |
| ESTORNO_ICMS_OPER_CRED_PRES_RECICLAVEL_ART21_XII | numeric(13) |  |  | Estorno do ICMS nas operações de reciclável - An2, Art. 21, XII, RICMS |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_COMPENSACAO_DEVOLUCAO_COMPRAS | numeric(13) |  |  | Compensação do ICMS devoluções de Compras - Créd. Pres. Confec. An2, Art. 21, IX |
| ESTORNO_RESSARCIMENTO_ICMS_ST | numeric(13) |  |  | Estorno de Crédito referente ressarcimento de ICMS ST nas vendas para SN - Decreto 3.509/10 |
| ADICIONAL_CREDITO_PRESUMIDO_TTD_409_410_411 | numeric(13) |  |  | Adicional do Crédito Presumido Tratamento Tributário - TTD 409, 410 ou 411 |
| ADICIONAL_ESTORNO_DEBITO_TTD_409_410_411 | numeric(13) |  |  | Adicional do Estorno de débito Tratamento Tributário - TTD 409, 410 ou 411 |
| DEVOLUCAO_ADICIONAL_CREDITO_PRESUMIDO_TTD_409_410_411 | numeric(13) |  |  | Devolução do adicional do crédito presumido TTD 409, 410 ou 411 |
| DEVOLUCAO_ADICIONAL_ESTORNO_DEBITO_TTD_409_410_411 | numeric(13) |  |  | Devolução do adicional do estorno de débito TTD 409, 410 e 411 |
| CREDITO_PRESUMIDO_SAIDA_TTD_409_410_411 | numeric(13) |  |  | Valor Crédito Presumido TTD 409, 410 ou 411 com origem das Saídas |
| ESTORNO_DEBITO_SAIDA_TTD_409_410_411 | numeric(13) |  |  | Valor de Estorno de Débito TTD 409, 410 ou 411 com origem das Saídas |
| ADICIONAL_CREDITO_PRESUMIDO_SAIDA_TTD_409_410_411 | numeric(13) |  |  | Adicional do Crédito Presumido Tratamento Tributário - TTD 409, 410 ou 411 com origem das Saídas |
| ADICIONAL_CREDITO_PRESUMIDO_REDUCAO_Z_TTD_409_410_411 | numeric(13) |  |  | Adicional do Crédito Presumido Tratamento Tributário - TTD 409, 410 ou 411 com origem das Reduções Z |
| ADICIONAL_ESTORNO_DEBITO_SAIDA_TTD_409_410_411 | numeric(13) |  |  | Adicional do Estorno de débito Tratamento Tributário - TTD 409, 410 ou 411 com origem das Saídas |
| ADICIONAL_ESTORNO_DEBITO_REDUCAO_Z_TTD_409_410_411 | numeric(13) |  |  | Adicional do Estorno de débito Tratamento Tributário - TTD 409, 410 ou 411 com origem das Reduções Z |
| CREDITO_PRESUMIDO_CERVEJA_CHOPE_SAIDAS | numeric(13) |  |  | Crédito presumido na saída de cerveja e chope artesanais - An2, Art. 15, XXXII - Saída |
| CREDITO_PRESUMIDO_CERVEJA_CHOPE_REDUCAO_Z | numeric(13) |  |  | Crédito presumido na saída de cerveja e chope artesanais - An2, Art. 15, XXXII - Redução Z |
| CREDITO_PAGAMENTO_ANTECIPADO_POR_IMPORTACAO | numeric(13) |  |  | Crédito do Pagamento Antecipado por Importação |
| SALDO_CREDOR_ANTERIOR_PAGAMENTO_ANTECIPADO_POR_IMPORTACAO | numeric(13) |  |  | Saldo credor anterior do Pagamento Antecipado por Importação |
| ESTORNO_CREDITO_TTD_409_410_411 | numeric(13) |  |  | Estorno do ICMS nas operações com TTD 409, 410 ou 411 |
| ESTORNO_SALDO_CREDOR_ANTERIOR_PAGAMENTO_ANTECIPADO_POR_IMPORTACAO | numeric(13) |  |  | Estorno do Ajuste de Saldo credor anterior do Pagamento Antecipado por Importação |
| CREDITO_PRESUMIDO_CONF_ART_15_TRANSF_CENT | numeric(13) |  |  | Crédito Presumido Confecção Art 15 Transf Centralizador |
| ESTORNO_LIM_CRED_PRES_CONF_ART_15_TRANSF_CENT | numeric(13) |  |  | Estorno Limite Crédito Presumido Confecção Art 15 Transf Centralizador |
| COMP_DEV_COMP_CRED_PRES_CONF_ART_15_TRANSF_CENT | numeric(13) |  |  | Compra ICMS Devolução Compras Crédito Presumido Confeção Art 15 Transf Centralizador |
| CREDITO_PRESUMIDO_CONF_ART_15_RECEB_CENTRALIZADA | numeric(13) |  |  | Crédito Presumido Confecção Art 15 Recebimento Centralizador |
| ESTORNO_LIM_CRED_PRES_CONF_ART_15_RECEB_CENT | numeric(13) |  |  | Estorno Limite Crédito Presumido Confecção Art 15 Recebimento Centralizador |
| COMP_DEV_COMP_CRED_PRES_CONF_ART_15_RECEB_CENT | numeric(13) |  |  | Compra ICMS Devolução Compras Crédito Presumido Confeção Art 15 Recebimento Centralizador |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR | numeric(13) |  |  | Estorno créd. presumido confecção, transferido para o estabelecimento centralizador |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA | numeric(13) |  |  | Estorno créd. presumido confecção, recebido do estabelecimento centralizado |
| PRODEC_COMPEX_CONFECCAO_ART_21 | numeric(13) |  |  | PRODEC - Confecção Art.21 |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito ativo imobilizado |
| SALDO_CREDOR_ANTERIOR_DEVOLUCAO_OPER_PREST_BENEF_CP | numeric(13) |  |  | Saldo credor anterior devolução oper. prest. beneficiadas pelo crédito presumido |
| ESTORNO_AJUSTE_DEVOLUCAO_OPER_PREST_BENEF_CP | numeric(13) |  |  | Estorno do ajuste de devolução oper. prest. beneficiadas pelo crédito presumido |
| CREDITO_PAGAMENTO_INDEVIDO_PERIODO_ANTERIOR_OPER_PREST_BENEF_CP | numeric(13) |  |  | Crédito pagamento indevido período anterior - Operações benef. crédito presumido/TTD |
| RETORNO_REMESSA_CREDITO_PRESUMIDO_TDD_409_410_411 | numeric(13) |  |  | Retorno de remessa crédito presumido TTD 409, 410 ou 411 |
| RETORNO_REMESSA_ESTORNO_DEBITO_TDD_409_410_411 | numeric(13) |  |  | Retorno de remessa estorno de débito TTD 409, 410 ou 411 |
| ESTORNO_CREDITO_PRESUMIDO_FEIJAO_ART_21_VIII | numeric(13) |  |  | Estorno do ICMS nas operações de feijão - An2, Art. 21 |
| ESTORNO_CREDITO_PRESUMIDO_TRANSPORTE_CANCELAMENTO_BILHETE_PASSAGEM | numeric(13) |  |  | Estorno Crédito Presumido Transporte - Cancelamento Bilhete Passagem |
| CREDITO_CANCELAMENTO_BILHETE_PASSAGEM | numeric(13) |  |  | Crédito por Cancelamento Bilhete de Passagem |
| CREDITOS_POR_TRANSFERENCIA_CREDITOS_ACUMULADOS | numeric(13) |  |  | Créditos por transferência de créditos acumulados |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_TTD | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - TTD |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_TRANSPORTADORA | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Transportes |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_INFORMATICA | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Informática |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_SAIDA_PEIXE | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Peixes |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_MATERIAL_RECICLADO | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Reciclado |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_BARES_RESTAURANTES_SIMILARES | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Bares |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_CONFECCAO_ART_21 | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Confecção |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_SAIDA_EMBARCACAO_NAUTICA | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Embarcação |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_SAIDAS_VINHO | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Vinho |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_SAIDA_INDUSTRIALIZACAO_LEITE | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Leite |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_SAIDAS_FEIJAO_ART_21_VIII | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Feijão |
| CREDITO_PRESUMIDO_VENDAS_INTEREST_CONS_FINAL_ART_21_XV | numeric(13) |  |  | Crédito Presumido nas vendas interest. a consumidor final não contrib. do ICMS - An2, Art.21,XV |
| ESTORNO_DEBITO_VENDAS_INTEREST_CONS_FINAL_ART_21_XV | numeric(13) |  |  | Compensação do ICMS devoluções de compras – Crédito Presumido/TTD |
| ESTORNO_CREDITO_VENDAS_INTEREST_CONS_FINAL_ART_21_XV | numeric(13) |  |  | Estorno de ICMS nas ope. de vendas interest. a consum. final não contrib. do ICMS - An2, Art.21,XV |
| DEVOLUCAO_VENDAS_INTEREST_CONS_FINAL_ART_21_XV | numeric(13) |  |  | Devolução Créd. Pres. nas vendas interest. a consum. final não contrib. do ICMS - An2, Art.21,XV |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA_SAIDA | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador Saída |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA_REDUCAO | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador Redução |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR_SAIDA | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador Saída |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR_REDUCAO | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador Redução |
| CREDITO_PRESUMIDO_CERVEJA_CHOPE_ESTORNO_EXCEDENTE | numeric(13) |  |  | Estorno crédito presumido excedente ao débito do período |
| CREDITO_PRESUMIDO_CONF_ART_15_DEVOLUCAO_VENDAS | numeric(13) |  |  | Estorno do ICMS nas operações de Confecção. Anexo 2, Art. 21, IX - Por Nota |
| CREDITO_CONFECCAO_PRODUTO_DEVOLUCAO_VENDAS | numeric(13) |  |  | Estorno do ICMS nas operações de Confecção. Anexo 2, Art. 21, IX - Por Produto |
| NCAL_ENERGIA_ELETRICA | char(1) |  |  | (N = Apurado antes da SAI 53202  / S = Apurado depois da SAI 53202) |
| VALOR_FUNDOSOCIAL_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR | numeric(13) |  |  | Valor do Fundo Social calculado no ICMS para crédito presumido Confecção Art 21 - Estabelecimento Centralizador |
| VALOR_FUNDOSOCIAL_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA | numeric(13) |  |  | Valor do Fundo Social calculado no ICMS para crédito presumido Confecção Art 21 - Estabelecimento Centralizadora |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_SAIDA_MODELO_02 | numeric(13) |  |  | Crédito presumido confecção - Saídas - Modelo 02 |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR_SAIDA_MODELO_02 | numeric(13) |  |  | Crédito Presumido An2, Art. 21. IX. transferido para o estabelecimento centralizador - Saída - Modelo 02 |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADORA_SAIDA_MODELO_02 | numeric(13) |  |  | Crédito Presumido An2, Art. 21. IX. transferido para o estabelecimento centralizadora - Saída - Modelo 02 |
| VALOR_AUC | numeric(13) |  |  | Valor de utilização de crédito |
| VALOR_CREDITO_ICMS_VENDA_OUTRA_UF | numeric(13) |  |  | Valor de crédito de ICMS nas vendas para outras UFs |
| DEBITO_CREDITO_PRESUMIDO_VENDAS_INT_CONS_FINAL_ART_21_XV_TRANSF_CENT | numeric(13) |  |  | Crédito presumido vendas interest. consumidor final valor transferido |
| DEBITO_CREDITO_PRESUMIDO_VENDAS_INT_CONS_FINAL_ART_21_XV_RECEB_CENTRALIZADA | numeric(13) |  |  | Crédito presumido vendas interest. consumidor final valor recebido |
| DEBITO_CREDITO_PRESUMIDO_VENDAS_INT_CONS_FINAL_ART_21_XV_RECEB_CENTRALIZADA_AJUSTE | numeric(13) |  |  | Crédito presumido vendas interest. consumidor final valor recebido através de ajuste |
| CREDITO_PAGAMENTO_ANTECIPADO_POR_IMPORTACAO_ICMS_NORMAL | numeric(13) |  |  | Crédito do Pagamento Antecipado por Importação |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_A_SAIDAS | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, a - Saídas |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_A_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, a - Redução Z |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_D_E_SAIDAS | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, d e e - Saídas |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_D_E_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, d e e - Redução Z |
| CREDITO_PRESUMIDO_SAIDAS_BISCOITOS_BOLACHAS_SAIDAS | numeric(13) |  |  | Crédito Presumido - Biscoitos e Bolachas - Saídas |
| CREDITO_PRESUMIDO_SAIDAS_BISCOITOS_BOLACHAS_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido - Biscoitos e Bolachas - Redução Z |
| CREDITO_PRESUMIDO_SAIDAS_BISCOITOS_BOLACHAS_DEVOLUCAO | numeric(13) |  |  | Crédito Presumido - Biscoitos e Bolachas - Devolução |
| OUTROS_DEBITOS_ICMS_COMPLEMENTAR_TTD_409_410_411 | numeric(13) |  |  | ICMS complementar - TTD 409, 410 ou 411 |
| CREDITO_PRESUMIDO_IMPOSTOS_LANCADOS_TTD_409_410_411 | numeric(13) |  |  | Crédito presumido TTD 409, 410 ou 411 com origem Impostos Lançados |
| ESTORNO_DEBITO_IMPOSTOS_LANCADOS_TTD_409_410_411 | numeric(13) |  |  | Estorno de Débito TTD 409, 410 ou 411 com origem Impostos Lançados |
| ESTORNO_CREDITO_PRESUMIDO_APURACAO_NORMAL_PARA_SUB_APURACAO | numeric(13) |  |  | Estorno de crédito presumido - Apuração normal para sub-apuração |
| ESTORNO_CREDITO_PRESUMIDO_APURACAO_NORMAL_PARA_SUB_APURACAO_SAIDAS | numeric(13) |  |  | Estorno de crédito presumido - Apuração normal para sub-apuração - Saídas |
| ESTORNO_CREDITO_PRESUMIDO_APURACAO_NORMAL_PARA_SUB_APURACAO_REDUCAO_Z | numeric(13) |  |  | Estorno de crédito presumido - Apuração normal para sub-apuração - Redução Z |
| ESTORNO_CREDITO_DEVOLUCAO_APURACAO_NORMAL_PARA_SUB_APURACAO | numeric(13) |  |  | Estorno de créditos devolução - Apuração normal para sub-apuração |
| ESTORNO_DEBITOS_APURACAO_NORMAL_PARA_SUB_APURACAO | numeric(13) |  |  | Estorno de débitos - Apuração normal para sub-apuração |
| ESTORNO_DEBITOS_APURACAO_NORMAL_PARA_SUB_APURACAO_SAIDAS | numeric(13) |  |  | Estorno de débitos - Apuração normal para sub-apuração - Saídas |
| ESTORNO_DEBITOS_APURACAO_NORMAL_PARA_SUB_APURACAO_REDUCAO_Z | numeric(13) |  |  | Estorno de débitos - Apuração normal para sub-apuração - Redução Z |
| ESTORNO_CREDITO_ENERGIA_ELETRICA_APURACAO_NORMAL_PARA_SUB_APURACAO | numeric(13) |  |  | Estorno de créditos Energia Elétrica- Apuração normal para sub-apuração |
| CREDITO_PRESUMIDO_GADO_SAIDA | numeric(13) |  |  | Crédito Presumido Gado Saída |
| CREDITO_PRESUMIDO_GADO_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Gado Saída Redução Z |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_AVES_SAIDA | numeric(13) |  |  | Crédito Presumido Abate Saídas Aves Saída |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_AVES_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Abate Saídas Aves Saída Redução Z |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_SUINOS_SAIDA | numeric(13) |  |  | Crédito Presumido Abate Saídas Suínos Saída |
| CREDITO_PRESUMIDO_ABATE_SAIDAS_SUINOS_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Abate Saídas Suínos Saída Redução Z |
| CREDITO_PRESUMIDO_TRANSPORTE_SAIDAS | numeric(13) |  |  | Crédito Presumido Transporte Saída |
| CREDITO_PRESUMIDO_TRANSPORTE_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido Transporte Redução Z |
| CREDITO_PRESUMIDO_LEITE_XXIX_SAIDA | numeric(13) |  |  | Crédito Presumido Leite XXIX - Saída |
| CREDITO_PRESUMIDO_LEITE_XXIX_REDUCAO | numeric(13) |  |  | Crédito Presumido Leite XXIX - Redução Z |
| ESTORNO_CREDITO_PRESUMIDO_APURACAO_NORMAL_PARA_SUB_APURACAO_COFECCAO_ART_21_REDUCAO_Z | numeric(13) |  |  | Estorno Crédito Presumido Sub Apuração Confeccção Redução Z |
| CREDITO_PRESUMIDO_ABATE_SUINOS_ORIGINAL_SAIDAS | numeric(13) |  |  | Crédito Presumido nas saídas de produtos resul. da matança de suínos - An2, Art 17, II |
| CREDITO_PRESUMIDO_ABATE_SUINOS_SAIDAS_PERCENTUAL | numeric(10) |  |  | Crédito Presumido nas saídas de produtos resul. da matança de suínos - An2, Art 17, II - Percentual |
| ESTORNO_CREDITO_APURACAO_NORMAL_PARA_SUB_APURACAO | numeric(13) |  |  | Estorno de crédito - Apuração normal para sub-apuração 4 |
| DEBITOS_CREDITO_PRESUMIDO_TRANSPORTE_TRANSF_CENT | numeric(13) |  |  | Crédito presumido transporte valor transferido |
| DEBITOS_CREDITO_PRESUMIDO_TRANSPORTE_RECEB_CENTRALIZADA | numeric(13) |  |  | Crédito presumido transporte valor recebido |
| DEBITOS_CREDITO_PRESUMIDO_TRANSPORTE_RECEB_CENTRALIZADA_AJUSTE | numeric(13) |  |  | Crédito presumido transporte valor recebido através de ajuste |
| ESTORNO_DEBITO_ICMS_DESTAC_INDEV_DOC_FISCAL | numeric(13) |  |  | Estorno de débito do ICMS destacado indevidamente em documento fiscal |
| ESTORNO_DEBITO_ICMS_DEVOLUCAO_SEM_APROVEITAMENTO | numeric(13) |  |  | Estorno de débito de ICMS de devolução, cuja entrada ocorreu sem o aproveitamento |
| CREDITO_SIMPLES_NACIONAL_DEVOLUCAO_VENDA | numeric(13) |  |  | Crédito de Simples Nacional pela devolução de venda |
| CREDITO_ENTRADA_MERCADORIA_IMPORTADA | numeric(13) |  |  | Crédito relativo à entrada de mercadoria importada |
| CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL | numeric(13) |  |  | Créd. pres. mat. para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 |
| CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL_SAIDAS | numeric(13) |  |  | Créd. pres. mat. para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 - Saídas |
| CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL_REDUCAO_Z | numeric(13) |  |  | Créd. pres. mat. para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 - Redução Z |
| CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL_ESTORNO | numeric(13) |  |  | Créd. pres. mat. para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 - Estorno |
| CREDITO_PRESUMIDO_MATERIAIS_USO_MEDICINAL_DEVOLUCAO | numeric(13) |  |  | Créd. pres. mat. para uso medicinal, cirúrgico, dentário ou veterinário - An2, Art. 245 - Devolução |
| ESTORNO_ICMS_COMPLEMENTAR | numeric(13) |  |  | Estorno do ICMS Complementar |
| ICMS_COMPLEMENTAR_VALOR_RECOLHER | numeric(13) |  |  | ICMS Complementar - valor a recolher |
| ICMS_COMPLEMENTAR_VALOR_PAGO | numeric(13) |  |  | ICMS Complementar - valor pago |
| ICMS_COMPLEMENTAR_DATA_VENCIMENTO | date(4) |  | S | ICMS Complementar - data de vencimento |
| ICMS_COMPLEMENTAR_CODIGO_RECOLHIMENTO | char(6) |  | S | ICMS Complementar - código de recolhimento |
| ICMS_COMPLEMENTAR_CLASSE_VENCIMENTO | integer(4) |  | S | ICMS Complementar - classe de vencimento |
| CREDITO_AQUISICAO_MERCADORIA_USO_CONSUMO_ART_29 | numeric(13) |  |  | Crédito na aquisição de mercadorias para uso e consumo - Art. 29, § 8º do RICMS |
| CREDITO_DIFALI_AQUISICAO_MERCADORIA_USO_CONSUMO_ART_29 | numeric(13) |  |  | Crédito DIFALI na aquisição de mercadorias para uso e consumo - Art. 29, § 8º do RICMS |
| CREDITO_STAT_AQUISICAO_MERCADORIA_USO_CONSUMO_ART_29 | numeric(13) |  |  | Crédito STAT na aquisição de mercadorias para uso e consumo - Art. 29, § 8º do RICMS |
| CREDITO_DEVOLUCAO_FUNDO_SOCIAL_CREDITO_PRESUMIDO_AN2_ART21 | numeric(13) |  |  | Devolução Fundo Social - Crédito presumido An2, Art. 21, XV |
| CREDITO_CONFORME_ALIQUOTA_NA_AQUISICAO_DO_SN | numeric(13) |  |  | Crédito conforme alíquota na aquisição do Simpes Nacional |
| CREDITO_ICMS_SIMPLES_NACIONAL_COMPRA_POR_PRODUTO | numeric(13) |  |  | Credito de ICMS Simples Nacional lancado por produto na compra |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_D_SAIDAS | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, "d" |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_E_SAIDAS | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, "e" |
| CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_D_REDUCAO_Z | numeric(13) |  |  | Crédito Presumido - RICMS, Anexo 2, Art. 15, XIV, "d" - reducao Z |
| CREDITO_PRESUMIDO_GADO_I | numeric(13) |  |  | Crédito presumido abatedor de gado bovino - An2, Art. 16, I |
| CREDITO_PRESUMIDO_GADO_II_5 | numeric(13) |  |  | Crédito presumido abatedor de gado bovino - An2, Art. 16, II e § 5 |
| CREDITO_PRESUMIDO_GADO_II_12 | numeric(13) |  |  | Crédito presumido abatedor de gado bovino - An2, Art. 16, II e § 12 |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV Total - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_A | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV, "a" - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_B | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV, "b" - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_C | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV, "c" - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_D | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV, "d" - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_RICMS_ANEXO_2_ART_15_XIV_E | numeric(13) |  |  | Estorno Créd. Presumido, Anexo 2, Art. 15, XIV, "e" - Devolução |
| ESTORNO_CREDITO_ENTRADA_INFORMATICA_ART144 | numeric(13) |  |  | Estorno de crédito Presumido Informática - Anexo 2, Art. 144 RICMS |
| ESTORNO_CREDITO_ENTRADA_INFORMATICA_ART145 | numeric(13) |  |  | Estorno de crédito Presumido Informática - Anexo 2, Art. 144 RICMS |
| ESTORNO_CREDITO_ENTRADA_INFORMATICA_ART146 | numeric(13) |  |  | Estorno de crédito Presumido Informática - Anexo 2, Art. 144 RICMS |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO_PERIODO_ATUAL | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto - Período atual |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO_PERIODO_ANTERIOR | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto - Período anterior |
| CREDITO_AQUISICAO_COMBUSTIVEL_INSUMO | numeric(13) |  |  | Crédito aquisição combustíveis para insumos - Conv. ICMS nº 199/22 e 15/23 |
| CREDITO_AQUISICAO_MERCADORIA_USO_CONSUMO_ART_29_ICMS_MONOFASICO | numeric(13) |  |  | Crédito na aquisição de mercadorias para uso e consumo - Art. 29, § 8º do RICMS - ICMS Monofásico |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_15_TRANSF_CENT | numeric(13) |  |  | Estorno de crédito presumido devolução - transferência para o estabelecimento centralizador |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_15_RECEB_CENT | numeric(13) |  |  | Estorno de crédito presumido devolução - recebidos do estabelecimento centralizado |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO_APUR_NORMAL_PARA_SUB_APUR | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto - Ap. normal para sub apuração 4 |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_ICMS_MONOFASICO | numeric(13) |  |  | Estorno de crédito na aquis. combustível suj. à trib. monofásica do ICMS |
| ESTORNO_CREDITO_PRESUMIDO_LEITE_XXVIII | numeric(13) |  |  | Estorno Crédito Presumido Leite - An2, Art. 15, XXVIII |
| ESTORNO_CREDITO_PRESUMIDO_LEITE_XXIX | numeric(13) |  |  | Estorno Crédito Presumido Leite - An2, Art. 15, XXIX |
| CREDITO_PRESUMIDO_SAIDAS_INTERNAS_CAFE_TORRADO_ACUCAR_SAIDAS | numeric(13) |  |  | Crédito Presumido - Café Torrado Açúcar - Saídas |
| CREDITO_PRESUMIDO_SAIDAS_INTERNAS_CAFE_TORRADO_ACUCAR_DEVOLUCAO | numeric(13) |  |  | Crédito Presumido - Café Torrado Açúcar - Devolução |
| ESTORNO_CREDITO_PRESUMIDO_PEIXES_AN2_ART21_VI_A | numeric(13) |  |  | Est. Créd. Pres. de Peixes, Crustáceos ou Moluscos - An2, Art. 21, VI, "a" |
| ESTORNO_CREDITO_PRESUMIDO_HADOQUE_BACALHAU_CONGRO_MERLUZA_AN2_ART21 | numeric(13) |  |  | Est. Créd. Pres. de Hadoque, Bacalhau, Congro, Merluza, Pirarucu, Salmão - An2, Art.21, §4º, I |
| ESTORNO_CREDITO_PRESUMIDO_PEIXES_AN2_ART21_VI_B | numeric(13) |  |  | Est. Créd. Pres. de Peixes, Crustáceos ou Moluscos - An2, Art. 21, VI, "b" |
| DEVOLUCAO_CREDITO_PRESUMIDO_HADOQUE_BACALHAU_CONGRO_MERLUZA_AN2_ART21 | numeric(13) |  |  | Devol. Créd. Pres. de Hadoque, Bacalhau, Congro, Merluza, Pirarucu, Salmão - An2, Art.21, §4º, I |
| CREDITO_PRESUMIDO_HADOQUE_BACALHAU_CONGRO_MERLUZA_AN2_ART21 | numeric(13) |  |  | Credito Presumido de Hadoque, Bacalhau, Congro, Merluza, Pirarucu, Salmão - An2, Art.21, §4º, I, "b" |
| DEBITO_CREDITO_PRESUMIDO_PEIXES_TRANSF_CENT | numeric(13) |  |  | Crédito presumido peixes valor transferido |
| DEBITO_CREDITO_PRESUMIDO_PEIXES_RECEB_CENTRALIZADA | numeric(13) |  |  | Crédito presumido peixes valor recebido |
| DEBITO_CREDITO_PRESUMIDO_PEIXES_RECEB_CENTRALIZADA_AJUSTE | numeric(13) |  |  | Crédito presumido peixes valor recebido através de ajuste |
| ESTORNO_DEBITO_INDEVIDO_OUTRAS_OPERACOES_ESTORNO_SAIDA_65 | numeric(13) |  | S | Estorno de débito de ICMS lançado indevidamente em todas as operações - Estorno de débito Saida 65 |
| CREDITO_PRESUMIDO_CONSTRUCAO_CIVIL | numeric(13) |  |  | Créd. pres. estab. fabricante de merc. para uso na construção civil - An2, Art. 249, II |
| CREDITO_PRESUMIDO_CONSTRUCAO_CIVIL_SAIDAS | numeric(13) |  |  | Créd. pres. estab. fabricante de merc. para uso na construção civil - An2, Art. 249, II - Saidas |
| CREDITO_PRESUMIDO_CONSTRUCAO_CIVIL_ESTORNO | numeric(13) |  |  | Créd. pres. estab. fabricante de merc. para uso na construção civil - An2, Art. 249, II - Estorno |
| CREDITO_PRESUMIDO_CONSTRUCAO_CIVIL_DEVOLUCAO | numeric(13) |  |  | Créd. pres. estab. fabricante de merc. para uso na construção civil - An2, Art. 249, II - Devolucao |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_CONSTRUCAO_CIVIL | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - Construtoras |
| DEBITO_SALDO_DEVEDOR_RECEBIDO_ESTABELECIMENTOS_CONSOLIDADOS | numeric(13) |  |  | Débito do saldo devedor recebido dos estabelecimentos consolidados |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO_ART_21_RECEBIDO_ESTAB_CENTRALIZADO_APUR_NORMAL_SUB_APURACAO_4 | numeric(13) |  |  | Est. créd. pres. An2, Art. 21, IX, receb. estab. cent.-Apuração normal para sub-apuração 4 |
| CREDITO_PRESUMIDO_CONFECCAO_ART21_RECEBIDO_ESTAB_CENTRALIZADO | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, recebido do estabelecimento centralizado |
| ESTORNO_DEBITO_ESTAB_CONSOLIDADOS_APURACAO_NORMAL_PARA_SUB_APURACAO_4 | numeric(13) |  |  | Estorno de débitos estabelecimentos consolidados-Apuração normal para sub-apuração 4 |
| CREDITO_PRESUMIDO_CONFECCAO_ART_21_ESTAB_CENTRALIZADOR_SAIDAS | numeric(13) |  |  | Crédito Presumido An2, Art. 21, IX, transferido para o estabelecimento centralizador Saída |
| ESTORNO_CREDITO_AQUISICAO_COMBUSTIVEL_MONOFASICO_CP_MATERIAL_RECICLAVEL_AN2_ART21_XII | numeric(13) |  |  | Estorno de crédito de combustível - Tributação Monofásica |
| DEBITO_SAIDAS_OPERACAO_INTERNA_TTD_09_AN2_ART_90_RICMS | numeric(13) |  |  | Redução da base de cálculo nas oper. internas (TTD 09) An2, Art. 90 do RICMS |
| ESTORNO_DEBITO_OPERACAO_INTERNA_TTD_09_AN2_ART_90_RICMS | numeric(13) |  |  | Est. incentivo red. base de cálc. nas oper. internas (TTD 09) An2, Art. 90 do RICMS |
| ESTORNO_DEBITO_DIFALI_DEVOLUCAO_SEM_APROVEITAMENTO | numeric(13) |  |  | Estorno de débito DIFALI de devolução, cuja entrada ocorreu sem o aproveitamento |
| CREDITO_PRESUMIDO_SAIDAS_INTERNAS_CAFE_TORRADO_ACUCAR_RETORNO_REMESSA | numeric(13) |  |  | Crédito Presumido - Café Torrado Açúcar - Retorno Remessa |
| CREDITO_PRESUMIDO_ENTRADA_OVINO_ABATE_ANE2_ART15_XLV | numeric(13) |  |  | Crédito Presumido entrada de ovino para abate- An2, Art.15, XLV, "a" |
| CREDITO_PRESUMIDO_SAIDA_PRODUTO_ABATE_OVINO_ANE2_ART15_XLV | numeric(13) |  |  | Crédito Presumido saída de produto de abate ovino - An2, Art.15, XLV "b" |
| DEVOLUCAO_CREDITO_PRESUMIDO_ENTRADA_OVINO_ABATE_ANE2_ART15_XLV | numeric(13) |  |  | Devol. Créd. Pres. na entrada de ovino para abate - An2, Art.15, XLV, "a" |
| DEBITO_CREDITO_PRESUMIDO_TTD_409_410_411_TRANSF_CENT | numeric(13) |  |  | Crédito presumido TTD 409, 410 ou 411 valor transferido |
| DEBITO_CREDITO_PRESUMIDO_TTD_409_410_411_RECEB_CENTRALIZADA | numeric(13) |  |  | Crédito presumido TTD 409, 410 ou 411 valor recebido |
| DEBITO_CREDITO_PRESUMIDO_TTD_409_410_411_RECEB_CENTRALIZADA_AJUSTE | numeric(13) |  |  | Crédito presumido TTD 409, 410 ou 411 valor recebido através de ajuste |
| ESTORNO_ICMS_OPER_ABATEDOR_GADO_ALINEA_A | numeric(13) |  |  | Estorno ICMS operações abatedor de gado bovino - An2, Art. 16, I alínea "a" |
| ESTORNO_ICMS_OPER_ABATEDOR_GADO_ALINEA_B | numeric(13) |  |  | Estorno ICMS operações abatedor de gado bovino - An2, Art. 16, I alínea "b" |
| EST_CRED_PRES_INAPROV_GADO_ALINEA_A | numeric(13) |  |  | Est. créd. pres. parc. Inaprov. - abat. gado bovino - An2, Art. 16, I alínea "a" |
| EST_CRED_PRES_INAPROV_GADO_ALINEA_B | numeric(13) |  |  | Est. créd. pres. parc. Inaprov. - abat. gado bovino - An2, Art. 16, I alínea "b" |
| EST_CRED_PRES_INAPROV_GADO_APUR_NORM_SUB_4 | numeric(13) |  |  | Est. créd. pres. parc. inaprov. - abat. bov. - An2, Art. 16 - Ap. norm. p/ sub-ap. 4 |
| ESTORNO_DEB_GADO_APUR_NORM_SUB_4 | numeric(13) |  |  | Estorno de débitos - abat. gado bov. - Apuração normal para sub-apuração 4 |
| COMPENSACAO_ICMS_DEVOLUCAO_COMPRA_CP_ABATEDOR_GADO_BOVINO | numeric(13) |  |  | Compensação do ICMS devoluções de compras - Crédito Presumido/TTD - abat. gado bovino |
