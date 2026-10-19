# ctgruposdmpl — Estrutura do DMPL
23.905 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_grupo | integer(4) | PK |  | Codigo grupo |
| sequencial | integer(4) |  |  | Sequencial |
| descricao | char(30) |  |  | Descricao |
| tipo | char(1) |  |  | Tipo (G=Grupo/S=SubGrupo) |
| possui_subgrupo | char(1) |  |  | Possui subgrupo (S/N) |
