# CTPLANOCONTAS — Contas Contabeis Auxiliar - Cadastro
80.098 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_CTA | integer(4) | PK |  | Codigo |
| I_PLANOCONTAS | integer(4) | PK |  | Codigo do plano de contas (1-Antigo/2-Novo) |
| NOME_CTA | char(60) |  |  | Descricao |
| CLAS_CTA | char(20) |  |  | Classificacao |
| TIPO_CTA | char(1) |  |  | Tipo (A=Analitico/S=Sintetico) |
| GRDRE_CTA | integer(4) |  | S | Grupo DRE |
| DLPA_CTA | integer(4) |  | S | Grupo DLPA |
| DOAR_CTA | integer(4) |  | S | Grupo DOAR |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes, 4 - Iceberg |
| DMPL_CTA | integer(4) |  | S | Grupo DMPL |
| DATA_CTA | date(4) |  |  | Data cadastro |
| SITUACAO_CTA | char(1) |  |  | Situacao (A-Ativa/I-Inativa) |
| DATAINATIVA_CTA | date(4) |  | S | Data da inativacao |
| DRA_CTA | integer(4) |  | S | Grupo DRA |
| DSP_CTA | integer(4) |  | S | Grupo DSP |
| DSP_ATO_CTA | char(1) |  | S | Grupo DSP - Ato (C=Cooperado/ N=Não cooperado/ A=Ambos) |
| CARNE_LEAO_CTA | tinyint(1) |  |  | Grupo Carnê Leão |
| EBITDA_CTA | integer(4) |  | S | Grupo EBITDA |
| LCDPR_CTA | integer(4) |  | S | Grupo LCDPR |
