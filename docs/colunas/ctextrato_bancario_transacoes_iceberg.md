# CTEXTRATO_BANCARIO_TRANSACOES_ICEBERG — Tipos de transações bancarias Contabilidade Digital
29 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_TRANSACAO | decimal(20) | PK |  | Código da transação |
| NOME_TRANSACAO | varchar(150) |  |  | Nome da transação |
| TIPO_VALOR | char(1) |  |  | Tipo de valor (D=Débito/C=Crédito) |
| DETALHAR | char(1) |  | S | Detalhar transação (S/N) |
| MODELO_JSON | varchar(32000) |  | S | Modelo em formato JSON |
