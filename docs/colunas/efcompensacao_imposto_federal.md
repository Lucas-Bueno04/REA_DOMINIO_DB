# EFCOMPENSACAO_IMPOSTO_FEDERAL — Compensações de Impostos Federais
126 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| I_COMPENSACAO | integer(4) | PK |  | Sequencial da compensação |
| DATA_COMPENSACAO | date(4) |  |  | Data da compensação |
| VALOR_A_COMPENSAR | numeric(13) |  |  | Valor a compensar |
| OPERACAO | integer(4) |  |  | Operação (1/2) |
| TIPO_CREDITO | integer(4) |  | S | Tipo crédito (1/2/3/4/5/6/7/8/9/10/11) |
| FORMALIZACAO_PEDIDO | integer(4) |  |  | FORMALIZAÇÃO PEDIDO (1/2/3/4) |
| NUMERO_DCOMP_PROCESSO | varchar(24) |  |  | Número DCOMP processo |
| OBSERVACAO | varchar(250) |  |  | Observação |
| GERAR_RESSARCIMENTO_CREDITO_IPI | char(1) |  |  | Gerar Ressarcimento Crédito IPI (S/N) - (Descontinuado) |
| GERAR_RESSARCIMENTO_CREDITO_IPI_IMPOSTO | integer(4) |  | S | Gerar Ressarcimento Crédito IPI - Imposto - (Descontinuado) |
| DEMONSTRAR_VALOR_DE_COMPENSACAO | integer(4) |  |  | Demonstrar valor de compensação (1/2) |
| MEDIDA | integer(4) |  |  | Medida (0/1/2/3/4) |
| VARA | char(2) |  |  | Vara |
| UF | char(2) |  |  | UF |
| MUNICIPIO | varchar(50) |  |  | Município |
| I_SCP | integer(4) |  | S | Sequencial do SCP |
| GERAR_RESSARCIMENTO_COMPENSACAO_CREDITO | char(1) |  |  | Gerar Ressarcimento Compensação Crédito (S/N) |
| GERAR_RESSARCIMENTO_COMPENSACAO_CREDITO_IMPOSTO | integer(4) |  | S | Gerar Ressarcimento Compensação Crédito Imposto |
| I_RECOLHIMENTO_IPI | integer(4) |  | S | Sequencial do Código de Recolhimento do IPI |
| PERIODO_APURACAO | date(4) |  |  | Período para apuração |
