# EFEMPREENDIMENTOS_IMOBILIARIOS_CONTRATOS_VENDA_CLIENTE_ALTERACAO — Empreendimentos Imobiliários - Contratos de Venda - Alteraçõs de Clientes
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_CONTRATO | integer(4) | PK |  | Código do Contrato Imobiliário |
| I_ALTERACAO | integer(4) | PK |  | Sequencial da alteração |
| CODI_CLI_DE | integer(4) |  | S | Código do Cliente De |
| CODI_CLI_PARA | integer(4) |  | S | Código do Cliente Para |
| CAMPO | integer(4) |  |  | 1 - Cliente / 2 - Demais clientes |
| DATA_ALTERACAO | date(4) | PK |  | Data de Alteração |
