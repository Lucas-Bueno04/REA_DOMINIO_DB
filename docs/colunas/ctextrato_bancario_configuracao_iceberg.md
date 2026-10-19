# CTEXTRATO_BANCARIO_CONFIGURACAO_ICEBERG — Configuração para Contabilizar Extrato Bancário Contabilidade Digital
26 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_TRANSACAO | decimal(20) | PK |  | Código da transação |
| DETALHAR | char(1) |  |  | Detalhar transação (S/N) |
| CODI_CTA | integer(4) |  | S | Código da conta contábil |
| CODI_HIS | integer(4) |  | S | Código do histórico |
| HISTORICO | varchar(300) |  | S | Descrição do histórico |
| ORDENACAO | numeric(13) |  | S | Coluna para ordenar a tela de configuração |
