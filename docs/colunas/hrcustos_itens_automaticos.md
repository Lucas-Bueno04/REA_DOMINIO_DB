# HRCUSTOS_ITENS_AUTOMATICOS — Itens de custos automáticos pré definidos
44 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_ITEM_AUTOMATICO | integer(4) | PK |  | Codigo do item automático |
| DESCRICAO | varchar(250) |  |  | Descrição do item |
| UNIDADE | integer(4) |  | S | Unidade(1=Valor/2=Quantidade/3=Horas) |
| TIPO_EMPRESA | integer(4) |  | S | Tipo de empresa(1=Escritorio/2=Cliente) |
| MODULO | integer(4) |  | S | Modulo origem da informação |
