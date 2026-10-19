# geempre_informacoes — Empresa - Outras Informacoes
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| setor | tinyint(1) |  |  | Setor de Atuacao(1 - Industria/2 - Comercio Varejista/3 - Comercio Atacadista/4 - Servicos/5 - Agricola/6 - Pecuaria/7 - Outros) |
| capital_aberto | char(1) |  |  | Capital Aberto (S/N) |
| tipo | tinyint(1) |  |  | Tipo de Empresa (1 - Privada/2 - Publica/3 - Estatal/4 - Mista/5 - Autarquia/6 - Sem Fins Lucrativos/7 - Estrangeira Domiciliada no Exterior/8 - Estrangeira Domiciliada no Brasil) |
| origem_capital | tinyint(1) |  |  | Origem do Capital (1 - Nacional/2 - Estrangeiro/3 - Ambos) |
| esfera_poder | tinyint(1) |  | S | Esfera de Poder (1 - Municipal/2 - Estatual/3 - Federal/4 - Distrital) |
| tipo_imovel | tinyint(1) |  | S | Tipo do imovel (1 - Proprio Quitado/2 - Proprio Fianciado/3 - Alugado/4 - Familiar/5 - Cedido) |
| FRANQUIA | char(1) |  |  | Franquia |
| FRANQUEADORA | varchar(30) |  | S | Franqueadora |
