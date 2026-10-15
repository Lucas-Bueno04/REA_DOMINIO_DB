# CTLANCTO_SALDO — Tabela Saldos Contábeis
0 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| ID_SALDO | bigint(8) | PK |  | Identificador único do saldo contábil |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| CODI_EMP_PLANO | integer(4) |  |  | Código da empresa do plano de contas |
| FILI_LAN | integer(4) |  |  | Filial do lançamento |
| CODI_CTA | integer(4) |  |  | Código da conta contábil |
| DATA_LAN | date(4) |  |  | Data do lançamento contábil |
| VLOR_DEB | decimal(15) |  | S | Valor do lançamento a débito |
| VLOR_CRE | decimal(15) |  | S | Valor do lançamento a crédito |
| CODI_CCU | integer(4) |  |  | Código do centro de custo |
| CODI_EMP_SCP | integer(4) |  |  | Código da empresa dona do SCP |
| I_SCP | integer(4) |  |  | Código SCP do lançamento |
| ORIG_LAN | tinyint(1) |  |  | Origem do lançamento |
| CODI_EMP_CONSOLIDADA | integer(4) |  |  | Código da empresa consolidada |
| CODI_EMP_CONTROLADORA | integer(4) |  |  | Código da empresa controladora |
