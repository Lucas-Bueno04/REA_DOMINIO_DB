# CTPARMTO_CONTAS_ICEBERG — Parâmetrização de contas Contabilidade Digital
4 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CODI_CTA | integer(4) |  |  | Código da conta contábil |
| CODI_FIL | integer(4) | PK |  | Código da filial |
| I_BANCO | integer(4) | PK |  | Codigo de identificacão do banco |
| DATA_INICIO_INTEGRACAO | date(4) |  | S | DATA INICIAL PARA BUSCA DE DADOS DE EXTRATO BANCÁRIO. |
| SALDO_INICIAL | decimal(13) |  | S | Saldo Inicial |
