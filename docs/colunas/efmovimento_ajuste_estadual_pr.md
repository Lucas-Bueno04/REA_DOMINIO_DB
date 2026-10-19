# EFMOVIMENTO_AJUSTE_ESTADUAL_PR — PR - Ajuste Impostos lançados estaduais - Geral
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_AJUSTE | integer(4) | PK |  | Sequencial do movimento do ajuste |
| DATA_AJUSTE | date(4) |  |  | Data |
| CODI_AJU | integer(4) |  |  | Código do ajuste |
| VALOR | numeric(13) |  |  | Valor |
| OBSERVACAO | varchar(250) |  | S | Observação |
| CODIGO_UF | integer(4) |  | S | Código do estado |
| CODIGO_AJUSTE_SPED | char(8) |  | S | Código do ajuste do SPED |
| SISTEMA_ORIGEM | integer(4) |  |  | Sistema de origem do movimento(Variáveis globais do sistema) |
