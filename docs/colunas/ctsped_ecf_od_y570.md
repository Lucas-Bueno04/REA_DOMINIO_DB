# CTSPED_ECF_OD_Y570 — SPED ECF - Outros Dados - Registro Y570
18.290 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial Outros Dados |
| I_DEMONSTRATIVO_IR_CSLL | integer(4) | PK |  | Sequencial Interno |
| CNPJ | varchar(14) |  |  | CNPJ |
| NOME_EMPRESARIAL | varchar(150) |  |  | Nome empresarial |
| ORGAO_PUBLICO | char(1) |  |  | Órgão público |
| I_RECEITA | integer(4) |  |  | Código da receita |
| VALOR_RENDIMENTO_BRUTO_RECEITA | numeric(14) |  |  | Rendimento bruto/receita |
| VALOR_IR_RETIDO_FONTE | numeric(14) |  |  | IR retido na fonte |
| VALOR_CSLL_RETIDA_FONTE | numeric(14) |  |  | CSLL retida na fonte |
