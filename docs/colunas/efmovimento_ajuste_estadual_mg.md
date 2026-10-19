# EFMOVIMENTO_AJUSTE_ESTADUAL_MG — MG - Ajuste Impostos lançados estaduais - Geral
34 linhas

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
| SISTEMA_ORIGEM | integer(4) |  |  | Sistema de origem do movimento(Variáveis globais do sistema) |
| OPERACAO_REGIME_ESPECIAL_TRIBUTACAO | char(1) |  |  | Operação Regime Especial de Tributação - RET - Sub-Apuração |
| I_SUB_APURACAO | integer(4) |  | S | Operação Regime Especial de Tributação - RET - Sub-Apuração Código |
| CODIGO_RECEITA | varchar(6) |  | S | Código de receita |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
