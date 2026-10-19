# EFSIMPLES_NACIONAL_INFORMACAO_ESTADUAL — Informações Estaduais do Simples Nacional
196 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_UF | integer(4) | PK |  | Código do estado |
| VIGENCIA | date(4) | PK |  | Vigência |
| DESCRICAO | varchar(40) |  |  | Descrição |
| ALIQUOTA_ICMS | char(1) |  |  | Alíquota do ICMS (G - Tabela geral/P - Tabela do próprio estado) |
| TABELA | char(1) |  |  | Tabela (G - Geral/R - Conforme regime) |
| UTILIZA_SUB_LIMITE | char(1) |  |  | Utiliza sub-limites (S/N) |
| SUB_LIMITE_ATE | numeric(13) |  |  | Sub-limite até 1.200.000,00, 1.260.000,00, 1.800.000,00 ou 2.520.000,00 |
| PERMITE_RECOLHIMENTO_VALOR_FIXO | char(1) |  |  | Permite recolhimento com valor fixo (S/N) |
| VALOR_FIXO_POR | char(1) |  |  | Valor fixo por (E - empresa/U - UF) |
| TIPO_VALOR_FIXO_POR | char(1) |  |  | Tipo do valor fixo (F - Faixa/U - Único) |
