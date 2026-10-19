# EFTABELA_CST_VIGENCIA — Tabela de Códigos Situação Tributária por vigência
308 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) |  |  | Código do imposto |
| VIGENCIA | date(4) |  |  | Vigência da tabela CST |
| CODIGO_CST | integer(4) |  |  | Código de Situação Tributária |
| DESCRICAO | varchar(512) |  |  | Descrição da Situação Tributária |
| TIPO_NOTA | char(1) |  |  | Tipo da nota (E=Entrada/ S=Saida/ A=Entrada e saida) |
| I_CST_VIGENCIA | integer(4) | PK |  | Código sequencial |
