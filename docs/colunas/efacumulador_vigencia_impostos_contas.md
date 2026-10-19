# EFACUMULADOR_VIGENCIA_IMPOSTOS_CONTAS — Acumuladores - Cadastro - Impostos - Contas
453.490 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| CODI_IMP | integer(4) | PK |  | Imposto |
| CTRC_IAC | integer(4) |  | S | Conta contabil do imposto a recolher |
| CHIP_IAC | integer(4) |  | S | Historico padrao do imposto a recolher |
| CTRP_IAC | integer(4) |  | S | Conta contabil do imposto a recuperar |
| CHIR_IAC | integer(4) |  | S | Historico padrao do imposto a recuperar |
| CTVD_IAC | integer(4) |  | S | Conta contabil para o imposto sobre vendas |
| CTCP_IAC | integer(4) |  | S | Conta contabil para o imposto sobre compras |
| CTDV_IAC | integer(4) |  | S | Conta de devolucao de vendas |
| CTDEVCOMPRA_IAC | integer(4) |  | S | Conta devolucao de compras |
| CHDEVCOMPRA_IAC | integer(4) |  | S | Historico devolucao de compras |
| GERA_LAN_CTB_IAC | char(1) |  | S | Gera lancamentos contabeis(S/N) |
| CHESTORNO_DEBITO_IAC | integer(4) |  | S | Estorno de débito - Histórico |
| CHOUTROS_CREDITOS_VENDA_FORA_ESTABELECIMENTO_IAC | integer(4) |  | S | Histórico crédito venda fora do estabelecimento |
