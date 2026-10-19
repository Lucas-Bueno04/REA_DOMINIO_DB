# EFIMPOSTO_PADRAO — Tabela de Imposto Padrão
33 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Imposto |
| UF | char(2) | PK |  | UF |
| NOME_IMP | varchar(250) |  |  | Nome Imposto |
| SIGL_IMP | char(8) |  |  | Sigla Imposto |
| CODI_SIS | integer(4) |  | S | Codigo do Sistema |
| ATLZ_IMP | char(1) |  |  | O Atualizar atualiza este imposto (S/N) |
| NOME_RESUMIDO | varchar(250) |  |  | Nome Resumido |
