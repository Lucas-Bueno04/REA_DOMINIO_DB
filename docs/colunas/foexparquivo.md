# foexparquivo — Configuracao Arquivo Credito em Conta
111.587 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| num_banco | integer(4) | PK |  | Numero banco |
| i_arquivos | smallint(2) | PK |  | Codigo arquivo |
| i_posicao | smallint(2) | PK |  | Posicao |
| i_sequencia | smallint(2) | PK |  | Sequencia |
| separacao | tinyint(1) |  |  | Separacao |
| seq_campo | smallint(2) |  |  | Sequencia do campo |
| conteudo | char(30) |  | S | Conteudo |
| tamanho | smallint(2) |  |  | Tamanho |
| mascara | char(30) |  |  | Mascara |
| tipo_campo | smallint(2) |  |  | Tipo campo |
| valor_fixo | char(30) |  |  | Valor fixo |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| I_BANCOS | integer(4) | PK |  | CÓDIGO DO BANCO |
