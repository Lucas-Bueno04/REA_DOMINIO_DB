# EFMOVIMENTO_AJUSTE_ESTADUAL_PE — PE - Ajuste Impostos lançados estaduais - Geral
21 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| DATA_AJUSTE | date(4) |  |  | Data |
| CODI_AJU | integer(4) |  |  | Código do ajuste |
| VALOR | numeric(13) |  |  | Valor |
| OBSERVACAO | varchar(250) |  |  | Observação |
| CODIGO_UF | integer(4) |  | S | Código do estado |
| CODIGO_AJUSTE_SPED | char(8) |  | S | Código do ajuste do SPED |
| I_AJUSTE_SEF | integer(4) |  | S | Código do ajuste SEF |
| SISTEMA_ORIGEM | integer(4) |  |  | Sistema de origem do movimento(Variáveis globais do sistema) |
| OPERACAO_VINCULADA_PRODEPE | char(1) |  |  | Operação vinculada ao incentivo PRODEPE |
| I_PRODEPE_APURACAO | integer(4) |  | S | Calcular PRODEPE - Código da apuração |
