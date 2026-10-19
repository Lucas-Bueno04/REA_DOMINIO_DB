# EFPISCOFINS_APROPRIACAO_DIRETA_CREDITO_VIGENCIA — Apropriação Direta de Créditos de PIS e COFINS - Vigência
15 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_APROPRIACAO | integer(4) | PK |  | Sequencial |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(40) |  |  | Descrição |
| RECEITA_TRIBUTADA_MERCADO_INTERNO | decimal(7) |  |  | Receita tributada no mercado interno |
| RECEITA_NAO_TRIBUTADA_MERCADO_INTERNO | decimal(7) |  |  | Receita não tributada no mercado interno |
| RECEITA_EXPORTACAO | decimal(7) |  |  | Receita de exportação |
