# LROPERACAO_RECEITA — Cadastro Operações de Receita
141 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OPERACAO_RECEITA | integer(4) | PK |  | Código |
| DESCRICAO | varchar(140) |  |  | Descrição |
| I_EMPRESA | integer(4) |  |  | Empresa/Filial |
| TIPO_RECEITA | char(1) |  |  | Tipode receita (V=Vendas/ S=Serviços/ N=Não operacional) |
| ALIQUOTA_CSLL | numeric(5) |  |  | Alíquota CSLL |
| ALIQUOTA_IRPJ | numeric(5) |  |  | Alíquota IRPJ |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
