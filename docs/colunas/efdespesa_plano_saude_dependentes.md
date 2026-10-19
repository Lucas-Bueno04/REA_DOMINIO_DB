# EFDESPESA_PLANO_SAUDE_DEPENDENTES — Dependentes dos Beneficiários da Despesa com Plano de Saúde
45 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_DESPESA | integer(4) | PK |  | Código da Despesa |
| I_DESPESA_DEPENDENTES | integer(4) | PK |  | Sequencial dos Dependentes |
| CODI_FOR | integer(4) |  |  | Código do Fornecedor(Beneficiário) |
| I_DEPENDENTE | integer(4) |  |  | Código do Dependente |
| COOPARTICIPACAO | numeric(13) |  | S | Valor da Cooparticipação do Dependente |
