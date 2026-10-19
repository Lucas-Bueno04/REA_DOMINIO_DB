# EFSDOIMP_ESTADUAL_BA — Saldo dos Impostos - Estadual BA
348 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_IMP | integer(4) | PK |  | Imposto |
| DATA_SIM | date(4) | PK |  | Competencia |
| PDIC_SIM | integer(4) | PK |  | Periodicidade (1=1D, 2=2D, 3=3D, 4=1Q, 5=2Q, 6=M, 7=T, 11=1S, 12=2S, 13=3S, 14=4S, 15=5S, 51=Complementar, 52=13Sal) |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_DEVEDOR | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor |
| TRANSFERENCIA_SALDO_CREDOR | numeric(13) |  |  | Valor Transferência Saldo Credor |
| TRANSFERENCIA_SALDO_DEVEDOR | numeric(13) |  |  | Valor Transferência Saldo Devedor |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_CREDOR_ENTRADA | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor Entrada |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_DEVEDOR_ENTRADA | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor Entrada |
| TRANSFERENCIA_SALDO_CREDOR_SAIDA | numeric(13) |  |  | Valor Transferência Saldo Credor Saída |
| TRANSFERENCIA_SALDO_DEVEDOR_SAIDA | numeric(13) |  |  | Valor Transferência Saldo Devedor Saída |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_CREDOR_OUTROS | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Credor Outros |
| RECEBIMENTO_POR_TRANSFERENCIA_SALDO_DEVEDOR_OUTROS | numeric(13) |  |  | Valor Recebimento por Transferência Saldo Devedor Outros |
| TRANSFERENCIA_SALDO_CREDOR_OUTROS | numeric(13) |  |  | Valor Transferência Saldo Credor Outros |
| TRANSFERENCIA_SALDO_DEVEDOR_OUTROS | numeric(13) |  |  | Valor Transferência Saldo Devedor Outros |
| ESTORNO_DEBITOS_FUNDO_COMBATE_ERRADICACAO_POBREZA | numeric(13) |  |  | Valor Estorno Dédito FUNCEP |
| ESTORNO_CREDITO_PRESUMIDO_CONFECCAO | numeric(13) |  |  | Estorno de crédito presumido de confecção |
| CREDITO_PRESUMIDO_CONFECCAO | numeric(13) |  |  | Crédito presumido de confecção |
| CREDITO_ICMS_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Crédito de ICMS conf. alíquota do Simples Nacional - Art. 23, LC 123/06 |
| CREDITO_PRESUMIDO_AQUISICAO_INDUSTRIAS_SN_1 | numeric(13) |  |  | Créd. Presumido na aquisição de Indústrias Simples Nacional - Art. 269, X, a, 1, RICMS |
| CREDITO_PRESUMIDO_AQUISICAO_INDUSTRIAS_SN_2 | numeric(13) |  |  | Créd. Presumido na aquisição de Indústrias Simples Nacional - Art. 269, X, a, 2, RICMS |
| DEVOLUCAO_MERCADORIA_ADQUIRIDA_SN | numeric(13) |  |  | Devolução de mercadoria adquirida de Simples Nacional |
| DEVOLUCAO_MERCADORIA_CONFORME_ALIQUOTA_SN | numeric(13) |  |  | Devolução de mercadoria conf. alíquota do Simples Nacional |
| DEVOLUCAO_CREDITO_PRESUMIDO_INDUSTRIAS_SN_1 | numeric(13) |  |  | Devolução de mercadoria com crédito presumido de Indústrias Simples Nacional - Art. 269, X, a, 1, RICMS |
| DEVOLUCAO_CREDITO_PRESUMIDO_INDUSTRIAS_SN_2 | numeric(13) |  |  | Devolução de mercadoria com crédito presumido de Indústrias Simples Nacional - Art. 269, X, a, 2, RICMS |
| CREDITO_PRESUMIDO_VESTUARIO | numeric(13) |  |  | Crédito Presumido de vestuário, calçados e artefatos de tecidos - Art. 270, V |
| DEVOLUCAO_CREDITO_PRESUMIDO_VESTUARIO | numeric(13) |  |  | Devolução Crédito Presumido de vestuário, calçados e artefatos de tecidos - Art. 270, V |
| TRANSFERENCIA_CREDITOS_ACUMULADOS_TERC_ART_314 | numeric(13) |  |  | Transferência de Créditos Acumulados a terceiros - Art. 314 § 4º |
| CREDITO_PRESUMIDO_TRANSPORTE | numeric(13) |  |  | Crédito presumido de 20% para transportadoras - Art. 270, III, B, do RICMS/BA |
| CREDITO_PRESUMIDO_LEITE_DE_COCO | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI |
| CREDITO_PRESUMIDO_LEITE_DE_COCO_SAIDAS | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI - Saídas |
| CREDITO_PRESUMIDO_LEITE_DE_COCO_REDUCAO | numeric(13) |  |  | Crédito presumido aos fabricantes de leite de coco - Art. 270, VI - Redução |
| DEVOLUCAO_CREDITO_PRESUMIDO_LEITE_DE_COCO | numeric(13) |  |  | Devolução crédito presumido aos fabricantes de leite de coco - Art. 270, VI |
| ESTORNO_CREDITO_ICMS_ART_312_SAIDA | numeric(13) |  |  | Estorno de créditos - Art. 312, I do RICMS - Saída |
| ESTORNO_CREDITO_ICMS_ART_312_REDUCAO_Z | numeric(13) |  |  | Estorno de créditos - Art. 312, I do RICMS - Redução Z |
| ESTORNO_DEBITO_OPERACOES_CTE_SUBSTITUTO | numeric(13) |  |  | Estorno de débito nas operações com CT-e substituto |
| ESTORNO_CREDITO_ICMS_ART_312_SAIDA_TRANSPORTE | numeric(13) |  |  | Valor do estorno de créditos - Art. 312. I do RICMS - Transportes |
