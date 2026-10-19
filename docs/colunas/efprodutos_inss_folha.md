# EFPRODUTOS_INSS_FOLHA — Produtos - Cadastro - INSS folha
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_PDI | char(14) | PK |  | Código do produto |
| I_ATIVIDADE_INSS_FOLHA | char(8) | PK |  | Código da atividade |
| ALIQUOTA | numeric(7) |  |  | Alíquota |
| VIGENCIA_FINAL | date(4) |  | S | Vigência Final |
| VIGENCIA_INICIAL | date(4) |  | S | Vigência Inicial |
