# CTEXTRATO_BANCARIO_LANCAMENTO_ICEBERG_LANCTO — Lançamento de extrato ICEBERG - lançamentos contábeis
10 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_EMP_LANCTO | integer(4) | PK |  | Código da empresa do lançamento |
| I_EXTRATO_BANCARIO | integer(4) | PK |  | Código extrato |
| I_ITEM | integer(4) | PK |  | Sequencial do item |
| NUME_LAN | integer(4) | PK |  | Número do lançamento contábil |
| VALOR | numeric(13) |  |  | Valor do lançamento |
| TIPO_VALOR | char(1) |  |  | Tipo de lançamento (D=Soma/ C=Subtrai) |
| CODI_CTA | integer(4) |  |  | Conta de contrapartida |
| CODI_HIS | integer(4) |  | S | Código do histórico |
| HISTORICO | varchar(300) |  | S | Histórico |
| CODI_LOTE | integer(4) | PK |  | Código do Lote |
| ORIGEM_REG | integer(4) |  |  | Origem Contabilização - 1 = Sistema (Agente Comunicação) / 2 = Usuário (Contábil) |
