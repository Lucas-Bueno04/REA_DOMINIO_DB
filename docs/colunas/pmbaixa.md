# PMBAIXA — Baixas - Parcial e total
240 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_BAIXA | integer(4) | PK |  | Código |
| I_BEM | numeric(16) |  |  | Bem |
| DATA_BAIXA | date(4) |  |  | Data da baixa |
| BAIXA | char(1) |  |  | Baixa (P=Parcial/ T=Total) |
| VALOR_VENDA | numeric(13) |  |  | Valor da venda |
| VALOR_BAIXA | numeric(13) |  |  | Valor da baixa fiscal |
| VALOR_BAIXA_ICMS | numeric(13) |  |  | Valor da baixa ICMS |
| VALOR_SALDO_ATUAL | numeric(13) |  |  | Saldo Fiscal atual |
| VALOR_ICMS_CREDITADO | numeric(13) |  |  | ICMS a ser creditado |
| VALOR_DEPRECIACAO_FISCAL_ACUMULADA_BEM | numeric(13) |  |  | Depreciação acumulada fiscal - Posição do bem |
| VALOR_DEPRECIACAO_FISCAL_ACUMULADA_BAIXA | numeric(13) |  |  | Depreciação acumulada fiscal - Dados da baixa |
| VALOR_DEPRECIACAO_SOCIETARIA_ACUMULADA_BEM | numeric(13) |  |  | Depreciação acumulada societária - Posição do bem |
| VALOR_DEPRECIACAO_SOCIETARIA_ACUMULADA_BAIXA | numeric(13) |  |  | Depreciação acumulada societária - Dados da baixa |
| VALOR_GANHO_PERDA_CAPITAL | numeric(13) |  |  | Ganho/perda capital |
| TIPO_BAIXA | char(2) |  |  | Tipo da baixa (OT=OT - Outras Saídas Imobilizado/ AT=AT - Alienação ou Transferência/ PE=PE - Perecimento Extravio ou Deterioração) |
| I_HISTORICO | integer(4) |  | S | Código do histórico |
| HISTORICO | varchar(512) |  |  | Histórico |
| CONTA_CONTABIL | integer(4) |  |  | Conta contábil da baixa |
| FISCAL_NUMERO | numeric(15) |  | S | Documento fiscal - Número |
| FISCAL_SERIE | char(7) |  | S | Documento fiscal - Série |
| FISCAL_DATA_EMISSAO | date(4) |  | S | Documento fiscal - Data de emissão |
| FISCAL_MODELO | integer(4) |  | S | Documento fiscal - Espécie |
| FISCAL_CHAVE_NFE | char(44) |  | S | Documento fiscal - Chave NFe |
| FISCAL_CODI_CLI | integer(4) |  | S | Documento fiscal - Cliente |
| FISCAL_EMITENTE | char(1) |  | S | Documento fiscal - Emitente (T=Terceiros/ P=Próprio) |
| FISCAL_CODI_PDI | char(14) |  | S | Documento fiscal - Produto |
| FISCAL_SEQUENCIAL_ITEM | integer(4) |  | S | Documento fiscal - Sequencial do ítem |
| VALOR_SALDO_SOCIETARIO_ATUAL | numeric(13) |  |  | Saldo Societário atual |
| VALOR_ORIGINAL_AVALIADO | numeric(13) |  |  | Valor original/avaliado |
| VALOR_BAIXA_SOCIETARIO | numeric(13) |  |  | Valor da baixa societária |
| BAIXA_POR | char(1) |  |  | Baixa por(V=Valor/Q=Quantidade) |
| QUANTIDADE_ATUAL | numeric(12) |  |  | Quantidade atual |
| QUANTIDADE_BAIXA | numeric(12) |  |  | Quantidade a ser baixada |
| VALOR_BAIXA_ICMS_CREDITADO | numeric(12) |  |  | Valor da baixa ICMS creditado |
| VALOR_BAIXA_ICMS_TOTAL | numeric(12) |  |  | Valor total da baixa ICMS |
| VALOR_TOTAL_CREDITO_ICMS | numeric(12) |  |  | Total do crédito de ICMS |
| BEM_VINCULADO_AVALIACAO_VALOR_JUSTO | char(1) |  |  | Bem vinculado à avaliação do valor justo |
| BAIXA_AGRUPADA | char(1) |  |  | Baixa agrupada (S/N) |
| FISCAL_QUANTIDADE | numeric(13) |  | S | Gerar quantidade de documento fiscal |
