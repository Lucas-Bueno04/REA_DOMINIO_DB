# EFREGERANDO_LANCTOS_CONTABEIS — Regerar Lançamentos Contábeis
30 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| USUARIO | varchar(30) | PK |  | Usuário |
| DATA_INICIAL | date(4) | PK |  | Data Inicial da competência |
| DATA_FINAL | date(4) | PK |  | Data Final da competência |
| CONNECTION_ID | integer(4) |  | S | Identificador da conexão |
| LANCAMENTOS_ENTRADAS | char(1) | PK |  | Lançamentos de entrada |
| LANCAMENTOS_SAIDAS | char(1) | PK |  | Lançamentos de saídas |
| LANCAMENTOS_SERVICOS | char(1) | PK |  | Lançamentos de serviços |
| LANCAMENTOS_REDUCAO_Z | char(1) | PK |  | Lançamentos de redução Z |
| LANCAMENTOS_REDUCAO_Z_BILHETE_PASSAGEM | char(1) | PK |  | Lançamentos de reducao Z - bilhetes de passagem |
| LANCAMENTOS_RESUMO_MOVIMENTO_DIARIO | char(1) | PK |  | Lançamentos de movimento diario |
| LANCAMENTOS_BILHETE_PASSAGEM | char(1) | PK |  | Lançamentos de bilhetes de passagem |
| PARCELAMENTO_IMPOSTOS | char(1) | PK |  | Parcelamento de impostos |
| LANCAMENTOS_AJUSTE_IMPOSTOS_CALCULADOS | char(1) | PK |  | Lançamentos de ajustes |
| LANCAMENTOS_COMPENSACAO_IMPOSTOS_FEDERAIS | char(1) | PK |  | Lançamentos de compensação de impostos |
| LANCAMENTOS_SUSPENSACAO_IMPOSTOS_FEDERAIS | char(1) | PK |  | Lançamentos de suspensão de impostos |
| BAIXAS_ENTRADAS | char(1) | PK |  | Baixas de entradas |
| BAIXAS_SAIDAS | char(1) | PK |  | Baixas de saídas |
| BAIXAS_SERVICOS | char(1) | PK |  | Baixas de serviços |
| BAIXAS_CUPONS_FISCAIS | char(1) | PK |  | Baixas de cupons fiscais |
| BAIXAS_IMPOSTOS | char(1) | PK |  | Baixas de impostos |
| PARCELAMENTO_IMPOSTO_SN | char(1) | PK |  | Parcelamento de Simples Nacional |
| LANCAMENTOS_CONTRATOS_IMOBILIARIOS | char(1) | PK |  | Lançamentos de Contratos Imobiliarios |
| BAIXAS_CONTRATOS_IMOBILIARIOS | char(1) | PK |  | Baixas de Contratos Imobiliarios |
| LANCAMENTOS_MOVIMENTO_AJUSTE_ESTADUAL | char(1) | PK |  | Lançamentos de movimento de ajuste estadual |
| LANCAMENTOS_MOVIMENTO_AJUSTE_FEDERAL | char(1) | PK |  | Lançamentos de movimento de ajuste federal |
| COMPENSACAO_SN | char(1) | PK |  | Compensação do Simples Nacional |
| LANCAMENTOS_MOVIMENTO_AJUSTE_MUNICIPAL | char(1) | PK |  | Lançamentos de movimento de ajuste municipal |
| LANCAMENTOS_CFE | char(1) | PK |  | Lançamentos Cupom fiscal eletrônico - CF-e |
| BAIXAS_CFE | char(1) | PK |  | Baixas Cupom fiscal eletrônico - CF-e |
| CONTROLE_PRODUCAO_ESTOQUE | char(1) | PK |  | Controle da produção e do estoque |
| CONTROLE_DESMONTAGEM_ESTOQUE | char(1) | PK |  | Controle da desmontagem e do estoque |
| CORRECAO_APONTAMENTO_ESTOQUE | char(1) | PK |  | Correção de Apontamento do estoque |
| LANCAMENTOS_CUPOM_MEIO_PAGAMENTO | char(1) | PK |  | Lançamentos de cupom fiscal meio pagamento |
| LANCAMENTOS_CONTRATOS_FOMENTO_MERCANTIL | char(1) | PK |  | Lançamentos de contratos fomento mercantil |
| BAIXAS_CONTRATOS_FOMENTO_MERCANTIL | char(1) | PK |  | Baixas de contratos fomento mercantil |
| LANCAMENTOS_CONTRATOS_EMPRESA_SIMPLES_CREDITO | char(1) | PK |  | Lançamentos de contratos empresa simples de crédito |
| BAIXAS_CONTRATOS_EMPRESA_SIMPLES_CREDITO | char(1) | PK |  | Baixas de contratos empresa simples de crédito |
| LOGIN_TIME | varchar(32) |  | S | Propriedade LoginTime do connection ID |
