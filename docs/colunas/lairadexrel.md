# lairadexrel — Adicoes e Exclusoes do IR - Cadastro - Relacionamento
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empsa |
| codi_aei | integer(4) | PK |  | Codigo Adicao ou Exclusao |
| codi_rae | integer(4) | PK |  | Codigo Relacionamento |
| desc_rae | char(140) |  | S | Descricao |
| orig_rae | char(1) |  | S | Origem (L=Lancado, C=Contabilidade, B=Parte B) |
| codi_cta | integer(4) |  | S | Conta da Contabilidade |
| codi_pab | integer(4) |  | S | Codigo da contab parte B |
