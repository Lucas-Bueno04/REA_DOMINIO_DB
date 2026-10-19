# PMBEM_DOCUMENTOS_FISCAIS — Tabela de cadastro referente a documento Notas Fiscais / Conhecimento
372 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_BEM | numeric(16) | PK |  | Código do bem |
| SEQUENCIAL | integer(4) | PK |  | Número sequencial |
| NUMERO | numeric(15) |  | S | Número |
| SERIE | char(7) |  | S | Série |
| DATA_EMISSAO | date(4) |  | S | Data de emissão |
| MODELO | integer(4) |  | S | Espécie |
| CHAVE_NFE | char(44) |  | S | Chave NFe |
| CODI_FOR | integer(4) |  | S | Fornecedor |
| EMITENTE | char(1) |  | S | Emitente T - Terceiros / P - Própio |
| CODI_PDI | char(14) |  | S | Código do Produto |
| SEQUENCIAL_ITEM | integer(4) |  | S | Sequencial do Item |
| TIPO | char(1) |  | S | Documento C - Conhecimento de Transporte / N - Notas Fiscais |
| NUM_DOC_ARRECADACAO | varchar(50) |  | S | Número do documento de arrecadação |
| QUANTIDADE | numeric(13) |  | S | Quantidade |
| VALOR_ICMS | numeric(13) |  |  | Valor do ICMS |
| VALOR_ICMS_ST | numeric(13) |  |  | Valor do ICMS - Substituição Tributária |
| VALOR_ICMS_FRETE | numeric(13) |  |  | Valor do ICMS - Frete |
| VALOR_ICMS_DIFALI | numeric(13) |  |  | Valor do ICMS - Diferencial de Alíquota |
