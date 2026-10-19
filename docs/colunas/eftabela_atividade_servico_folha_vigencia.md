# EFTABELA_ATIVIDADE_SERVICO_FOLHA_VIGENCIA — Tabela de Atividades de Serviços da Folha - Vigência
10.076 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ATIVIDADE | char(8) | PK |  | Código da atividade |
| VIGENCIA | date(4) | PK |  | Vigência |
| DATA_FINAL | date(4) |  |  | Data final |
| ALIQUOTA | numeric(7) |  |  | Alíquota |
| CEI_INICIAL | date(4) |  | S | Obras com matrícula CEI a partir |
| CEI_FINAL | date(4) |  | S | Obras com matrícula CEI até |
| I_ATIVIDADE_REINF | char(8) |  | S | Código da atividade pra ser gerado no REINF |
