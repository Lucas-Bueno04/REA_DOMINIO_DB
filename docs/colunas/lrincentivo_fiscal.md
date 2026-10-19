# LRINCENTIVO_FISCAL — Cadastro de Incentivos Fiscais
17 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_INCENTIVO_FISCAL | integer(4) | PK |  | Código |
| DESCRICAO | varchar(140) |  |  | Descrição |
| PAT | char(1) |  |  | PAT (S/N) |
| INFORMAR_POR | char(1) |  |  | Informar por (N=Número de refeições/ V=Valor) |
| ALIQUOTA | tinyint(1) |  |  | Alíquota |
| LIMITE_APROVEITAMENTO | tinyint(1) |  |  | LIMITE DE APROVEITAMENTO (1=1%/ 2=2% 3=3%/ 4=4% / 100=100%) |
| APROVEITAR_PERIODO_SUBSEQUENTE | char(1) |  |  | Aproveitar o valor excedido nos períodos subsequentes (S/N) |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| TIPO | integer(4) |  | S | Tipo |
