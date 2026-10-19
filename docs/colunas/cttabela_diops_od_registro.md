# CTTABELA_DIOPS_OD_REGISTRO — DIOPs - Outros Dados - Tabela com colunas dos registros de valor
121 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| REGISTRO | varchar(50) | PK |  | Registro |
| CODIGO | numeric(8) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| DESCRICAO | varchar(512) |  |  | Descrição |
| TIPO | integer(4) |  |  | Tipo (1=Título / 2=Valor / 3=Calculado / 4=Valor de outro registro / 5=Fórmula condicional com valor de outro registro / 6=Valor conta desabilitada / 7=Fórmula condicional com valor de outro registro habilitado) |
| FORMULA | varchar(512) |  |  | Fórmula |
