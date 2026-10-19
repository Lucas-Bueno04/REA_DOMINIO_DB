# CTGRUPOSDSP — Estrutura DSP
21.120 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODIGO | integer(4) | PK |  | Código |
| SEQUENCIA | integer(4) |  |  | Sequencia |
| DESCRICAO | varchar(60) |  |  | Descrição |
| OPERACAO | char(1) |  |  | OPERAÇÃO (C=CONTAS/ T=TOTAL / I=CONTAS - INVERTER NATUREZA DO SALDO) |
| CONFIGURACAO | char(1) |  | S | Configuração (I=Inicia Sub Total/ F=Fecha Sub Total) |
| SOMA_ABAIXO | char(1) |  |  | Soma grupos abaixo (S/N) |
| SOMA_ABAIXO_QUANTIDADE | integer(4) |  |  | Soma grupos abaixo - Quantidade |
