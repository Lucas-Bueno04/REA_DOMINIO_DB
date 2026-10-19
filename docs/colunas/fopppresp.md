# fopppresp — Cadastro Responsaveis PPP
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| i_filiais | integer(4) | PK |  | Código da filial |
| tipo | integer(4) | PK |  | Tipo do responsavel(1=Ambiental,2=Biologica) |
| i_pppresp | integer(4) | PK |  | Código |
| inicio_periodo | date(4) |  |  | Inicio da atividade na filial |
| nit | char(11) |  | S | NIT |
| registro | char(10) |  | S | Registro do Conselho de Classe |
| nome | char(40) |  |  | Nome do responsavel |
| CPF | char(11) |  | S | CPF |
