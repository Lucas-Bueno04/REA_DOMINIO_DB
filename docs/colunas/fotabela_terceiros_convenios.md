# FOTABELA_TERCEIROS_CONVENIOS — Tabela de alíquotas dos convênios para os códigos de terceiros.
625 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_TERCEIROS | integer(4) | PK |  | Código de terceiros. |
| CODIGO_CONVENIO | smallint(2) | PK |  | Código do convênio. |
| ALIQUOTA | decimal(4) |  |  | Alíquota. |
| ALIQUOTA_MP_932_2020 | decimal(4) |  | S | Alíquota MP 932/2020 |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
