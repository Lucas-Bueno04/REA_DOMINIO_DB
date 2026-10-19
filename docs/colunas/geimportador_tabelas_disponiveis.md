# GEIMPORTADOR_TABELAS_DISPONIVEIS — Tabelas disponíveis para definição no importador
533 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| TABELA | char(128) | PK |  | Nome da tabela |
| DESCRICAO | varchar(256) |  |  | Descrição da tabela |
| TIPO | char(1) |  | S | Onde a tabela poder ser usada (D = Definição de dados/T = Tabela estrangeira/Q = Qualquer) |
| TABELA_PAI | char(128) |  | S | Tabela pai da tabela |
| ORDEM | integer(4) |  | S | Ordem de processamento das tabelas |
| SOBRESCREVER | varchar(5) |  | S | Sobrescrever registros (P = Padrão/N = Nota/C = Cadastro/M = Produtos/I = Imobiliário/COMB = Combustíveis/CFE = CFe/ORP = Ordem de produção/L = Lançamentos(somente para OnBalance)/PGTO = Pagamentos(somente para OnBalance)/HON = Lançamentos Honorarios/EXTRA = Saída e Entrada Extra/DIMOB = Declaracao de Informacoes sobre Atividades Imobiliarias)/CPK - Correção de Apontamento Estoque Escriturado - K280/UE - Últimas Entradas Ressarcimento/Complemento ICMS ST - IN 48/2018/ODCTB - Outros Dados Contas Contábeis/MOVOU - Outros movimentos/FUNCL - Fundos e clubes de investimentos/ORC = Lancamentos Orcados |
| ORDEM_RESUMO | varchar(128) |  | S | Ordem para o resumo da importação |
| ORDEM_GRAVACAO | integer(4) |  | S | Ordem de gravação dos dados no banco |
| OPCAO_SOBRESCREVER | char(1) |  | S | Opção considerada para sobrescrever registros (C = Cadastros/M = Movimentos) |
