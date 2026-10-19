# LRCSLL_REAL_BASE_NEGATIVA — Base Negativa
2.552 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_CSLL_REAL_BASE_NEGATIVA | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| I_BASE_NEGATIVA | integer(4) |  |  | Conta Base Negativa |
| HISTORICO | varchar(50) |  |  | Histórico |
| VALOR_DEBITO | numeric(13) |  |  | Débito |
| VALOR_CREDITO | numeric(13) |  |  | Crédito |
| ORIGEM_LANCAMENTO | char(1) |  |  | Origem do lançamento (M=Manual/ S=Sistema/ C=Cisão/ I=Incorporação) |
| I_SCP | integer(4) |  | S | SCP |
| TIPO_LANCAMENTO | char(1) |  |  | Origem do lançamento (P=Prejuízo/ C=Compensação/ O=Outros/ L=Liquid. Parc. IN 1687/17/ T=Pert. Lei 13.496/17) |
| I_CSLL_REAL_ADICAO | integer(4) |  | S | Codigo do lançamento de adição |
| I_CSLL_REAL_ADICAO_ITEM | integer(4) |  | S | Codigo do lançamento de adição - Item |
| I_CSLL_REAL_EXCLUSAO | integer(4) |  | S | Codigo do lançamento de exclusão |
| I_CSLL_REAL_EXCLUSAO_ITEM | integer(4) |  | S | Codigo do lançamento de exclusão - Item |
| TIPO_ATIVIDADE | char(1) |  |  | Codigo do lançamento de exclusão - Item |
