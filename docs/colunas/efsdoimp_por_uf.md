# EFSDOIMP_POR_UF — Saldo dos Impostos - Por UF
6.997 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| SIGLA_UF | char(2) | PK |  | Sigla da UF |
| SALDO_DEVEDOR | numeric(15) |  |  | Saldo Devedor |
| VALOR_DEBITO_SAIDAS | numeric(15) |  |  | Débitos Saídas |
| VALOR_PAGO | numeric(15) |  |  | Valor Pago |
| VENCIMENTO | date(4) |  |  | Vencimento |
| SALDO_CREDOR | numeric(15) |  |  | Saldo Credor |
| SALDO_CREDOR_ANTERIOR | numeric(15) |  |  | Saldo Credor Anterior |
| OUTROS_DEBITOS | numeric(15) |  |  | Outros Débitos |
| OUTROS_CREDITOS | numeric(15) |  |  | Outros Créditos |
| ESTORNO_DEBITOS | numeric(15) |  |  | Estorno Débitos |
| ESTORNO_CREDITOS | numeric(15) |  |  | Estorno Créditos |
| OUTRAS_DEDUCOES | numeric(15) |  |  | Outras Deduções |
| CREDITO_DEVOLUCAO | numeric(15) |  |  | Créditos pelas devoluções de vendas ICMS diferencial alíq. UF destino |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino |
| CREDITO_ANULACAO_SERVICOS_TRANSPORTE_ORIGEM | numeric(13) |  |  | Créditos pelas anulações de serviços de transp. iniciados em outra UF - ICMS dif. de alíq. |
| CREDITO_ANULACAO_SERVICOS_TRANSPORTE_DESTINO | numeric(13) |  |  | Créditos pelas anulações de serviços de transp. iniciados em outra UF - ICMS dif. de alíq. |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente) |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA_IGUAL | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente igual empresa) |
| DEBITO_SERVICOS_TRANSPORTE_ORIGEM_UF_EMPRESA_DIFERENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF origem (UF da empresa ativa nota com UF do cliente diferente empresa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE_IGUAL | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente igual empresa) |
| DEBITO_SERVICOS_TRANSPORTE_DESTINO_UF_CLIENTE_DIFERENTE | numeric(13) |  |  | Débitos serviços de transp. - ICMS dif. de alíq. UF destino (UF do cliente com UF do cliente diferente empresa) |
| UF_ENVOLVIDA_OPERACAO_TRANSPORTE | char(1) |  |  | UF envolvida na operação de transporte |
| TRANSFERENCIA_SALDO_CREDOR_ICMS_DIFAL_UF | numeric(13) |  |  | Transf. saldo credor ICMS DIFAL UF origem/destino para apuração no ICMS próprio |
| TRANSFERENCIA_SALDO_DEVEDOR_ICMS_DIFAL_UF | numeric(13) |  |  | Transf. saldo devedor ICMS DIFAL UF origem/destino para apuração no ICMS próprio |
| VALOR_DEBITOS_ENTRADAS | numeric(13) |  |  | Débitos Entradas |
| ESTORNO_CONFORME_BENEFICIO_ART_530_LRI_RICMS | numeric(13) |  |  | Estorno Conforme Benefício Art. 530-LRI RICMS |
| ESTORNO_CONFORME_BENEFICIO_ART_530_LRI_RICMS_DEVOLUCAO | numeric(13) |  |  | Estorno Conforme Benefício Art. 530-LRI RICMS - Devolução |
| ESTORNO_DEBITO_RECOLHIMENTO_JUNTO_ICMS_ST | numeric(13) |  |  | Estorno de débitos recolhimento junto ao ICMS ST |
| ESTORNO_CREDITO_DEVOLUCOES_RECOLHIMENTO_JUNTO_ICMS_ST | numeric(13) |  |  | Estorno credito devolucoes recolhimento junto ICMS ST |
| OUTROS_CREDITOS_LANCADO | numeric(15) |  |  | Outros CrÃ©ditos - LanÃ§ados |
| OUTROS_DEBITOS_LANCADO | numeric(15) |  |  | Outros Débitos - Lançados |
| VALOR_RECOLHER_CREDITO_DEVOLUCOES | numeric(13) |  |  | Soma dos valores (a recolher e crédito pelas devoluções de vendas) para geração de relatório |
