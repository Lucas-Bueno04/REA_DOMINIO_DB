# rgtipo_alteracao_contratual — Tipo de Alteracao Contratual
6 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_tipoalteracao | integer(4) | PK |  | Codigo |
| descricao | char(50) |  |  | Descricao |
| cadastral | char(1) |  |  | Alteracao cadastral(S/N) |
| quadrosocietario | char(1) |  |  | Alteracao do quadro societario(S/N) |
| filial | char(1) |  |  | Alteracao de dados da filial(S/N) |
| tipofilial | char(1) |  | S | Tipo da alteracao da filial(I-Inclusao/E-Exclusao/A-Alteracao Cadastral) |
| outros | char(1) |  |  | Outros tipos de alteracao(S/N) |
| NATUREZA_JURIDICA | char(1) |  |  | Natureza Jur?ca (S/N) |
| CAPITAL_SOCIAL | char(1) |  |  | Capital Social (S/N) |
