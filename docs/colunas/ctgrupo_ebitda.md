# CTGRUPO_EBITDA — Estrutura EBITDA
14.390 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_EBITDA | integer(4) | PK |  | Código |
| SEQUENCIA | integer(4) |  |  | Sequencia |
| DESCRICAO | varchar(60) |  |  | Descrição |
| OPERACAO | char(1) |  |  | Operaçãio (C=Contas/ I=Contas - Inverter natureza do saldo/ T=Total) |
| CONFIGURACAO | char(1) |  | S | Configuração (I=Inicia Sub Total/ F=Fecha Sub Total) |
| SOMA_GRUPO | char(1) |  |  | Soma grupos abaixo (S/N) |
| SOMA_GRUPO_ABAIXO | integer(4) |  |  | Soma grupos abaixo - Quantos |
