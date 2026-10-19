# EFDESPESA_PLANO_SAUDE — Despesas com Plano de Saúde
119 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da Empresa |
| I_DESPESA | integer(4) | PK |  | Código da Despesa |
| DATA_DESPESA | date(4) |  |  | Data da Despesa |
| I_OPERADORA | integer(4) |  |  | Operadora do Plano de Saúde |
| CODI_FOR | integer(4) |  |  | Codigo do Fornecedor (Beneficiário) |
| COOPARTICIPACAO_TITULAR | numeric(13) |  | S | Valor Cooparticipação do Titular |
| COOPARTICIPACAO_DEPENDENTES | numeric(13) |  | S | Valor Cooparticipação dos Dependentes |
| GERA_COMPROVANTE_RET | char(1) |  |  | Gerar no quadro Informacoes Complementares do Comprovante Anual de Retencao |
