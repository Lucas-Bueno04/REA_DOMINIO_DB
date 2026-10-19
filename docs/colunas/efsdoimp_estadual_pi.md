# EFSDOIMP_ESTADUAL_PI — Saldo dos Impostos - Estadual PI
65 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| CREDITO_ATIVO_IMOBILIZADO | numeric(13) |  |  | Crédito Ativo Imobilizado |
| CREDITO_PRESUMIDO_20_TRANSPORTADORAS_ICMS | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 56, III do RICMS |
| DEBITO_FECOP_ICMS | numeric(13) |  |  | FECOP PI - Valor |
| CREDITO_ICMS_ANTECIPACAO_PARCIAL | numeric(13) |  |  | Antecipação Parcial - RICMS Art. 771 |
| PRODUTOS_FARMACEUTICOS_BASE_ENTRADAS_INTERNAS_3_ART_791 | numeric(13) |  |  | Regime especial de tributação - Base Entradas internas 3%, Art. 791-F, I, b |
| PRODUTOS_FARMACEUTICOS_BASE_ENTRADAS_INTERESTADUAIS_63_ART_791 | numeric(13) |  |  | Regime especial de tributação - Base Entradas interest. 6,3%, Art. 791-F, I, a |
| PRODUTOS_FARMACEUTICOS_BASE_ADICIONAL_EXCEDENTE_5_ART_791 | numeric(13) |  |  | Regime especial de tributação - Base Adicional excedente 5% PF, Art. 791-M |
| PRODUTOS_FARMACEUTICOS_ENTRADAS_INTERNAS_3_ART_791 | numeric(13) |  |  | Regime especial de tributação - Entradas internas 3%, Art. 791-F, I, b |
| PRODUTOS_FARMACEUTICOS_ENTRADAS_INTERESTADUAIS_63_ART_791 | numeric(13) |  |  | Regime especial de tributação - Entradas interest. 6,3%, Art. 791-F, I, a |
| PRODUTOS_FARMACEUTICOS_ADICIONAL_EXCEDENTE_5_ART_791 | numeric(13) |  |  | Regime especial de tributação - Adicional excedente 5% PF, Art. 791-M |
| PRODUTOS_FARMACEUTICOS_ESTORNO_CREDITO | numeric(13) |  |  | Estorno de crédito resultante da sistemática normal - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_ESTORNO_DEBITO | numeric(13) |  |  | Estorno de débito resultante da sistemática normal - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_A_SALDO_CREDOR_ANTERIOR | numeric(13) |  |  | A - Saldo credor do período anterior - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_B_SALDO_CREDOR_PERIODO | numeric(13) |  |  | B - Valor Saldo credor do período - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_C_ANTECIPACAO_PARCIAL | numeric(13) |  |  | C - Antecipação Parcial - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_D_VALOR_SALDO_DEVEDOR_PERIODO | numeric(13) |  |  | D - Valor Saldo devedor do período - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_RESULTANTE_DEBITO | numeric(13) |  |  | Resultante - Débito - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_RESULTANTE_CREDITO | numeric(13) |  |  | Resultante - Crédito - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_ICMS_A_RECOLHER | numeric(13) |  |  | ICMS a recolher no Regime Especial de Tributação - Produtos farmacêuticos |
| PRODUTOS_FARMACEUTICOS_ICMS_VALOR_PAGO | numeric(13) |  |  | Valor Pago de ICMS do Regime Especial de Tributação - Produtos farmacêuticos |
| JUROS_MULTA_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Juros e multa por escrituração extemporânea de documentos fiscais |
| ESTORNO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos |
| ESTORNO_ICMS_DOCUMENTOS_EXTEMPORANEOS_SEM_JUROS_MULTA | numeric(13) |  |  | Estorno de ICMS dos documentos extemporâneos (Sem juros e multa) |
| ICMS_DOCUMENTOS_EXTEMPORANEOS_RECOLHER | numeric(13) |  |  | ICMS dos documentos extemporâneos a recolher |
| VALOR_PAGO_ICMS_DOCUMENTOS_EXTEMPORANEOS | numeric(13) |  |  | Valor pago ICMS documentos extemporâneos |
| DATA_VENCIMENTO_ICMS_DOCUMENTOS_EXTEMPORANEOS | date(4) |  | S | Data vencimento ICMS documentos extemporâneos |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
