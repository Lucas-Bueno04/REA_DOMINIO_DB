# LRIRPJ_REAL_PARTE_B — Lançamentos da Parte B
2.584 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_IRPJ_REAL_PARTE_B | integer(4) | PK |  | Código |
| COMPETENCIA | date(4) |  |  | Competência |
| I_PARTE_B | integer(4) |  |  | Conta Parte B |
| HISTORICO | varchar(50) |  |  | Histórico |
| MES_REFERENCIA | date(4) |  | S | Mês referência |
| VALOR_CORRIGIR | numeric(13) |  |  | Valor a corrigir |
| COEFICIENTE | numeric(13) |  |  | Coeficiente |
| VALOR_DEBITO | numeric(13) |  |  | Débito |
| VALOR_CREDITO | numeric(13) |  |  | Crédito |
| ORIGEM_LANCAMENTO | char(1) |  |  | Origem do lançamento (M=Manual/ S=Sistema/ C=Cisão/ I=Incorporação) |
| I_SCP | integer(4) |  | S | SCP |
| TIPO_LANCAMENTO | char(1) |  |  | Origem do lançamento (P=Prejuízo/ C=Compensação/ O=Outros/ L=Liquid. Parc. IN 1687/17/ T=Pert. Lei 13.496/17) |
| I_IRPJ_INCENTIVO_FISCAL | integer(4) |  | S | Código do Lançamento de Incentivo Fiscal |
| I_IRPJ_REAL_ADICAO | integer(4) |  | S | Código do Lançamento de Adição |
| I_IRPJ_REAL_ADICAO_ITEM | integer(4) |  | S | Código do Lançamento de Adição - Item |
| I_IRPJ_REAL_EXCLUSAO | integer(4) |  | S | Código do Lançamento de Exlcusão |
| I_IRPJ_REAL_EXCLUSAO_ITEM | integer(4) |  | S | Código do Lançamento de Exlcusão - Item |
| TIPO_ATIVIDADE | char(1) |  |  | Tipo de atividade (G=Atividade geral/ R=Atividade rural/ A=Ambos) |
| AJUSTE_ANUAL | integer(4) |  |  | Ajuste Anual |
