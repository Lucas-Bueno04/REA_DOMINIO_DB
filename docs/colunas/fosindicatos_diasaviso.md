# FOSINDICATOS_DIASAVISO — SINDICATO - CADASTRO - AVISO PREVIO
5 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | CODIGO DO SINDICATO |
| I_REGRAS | integer(4) | PK |  | NUMERO DA REGRA |
| I_REGRASEQ | integer(4) | PK |  | SEQUENCIAL DE EXPRESSOES DA REGRA |
| CAMPO | integer(4) |  |  | Codigo do campo da empressão: (1=Idade/2=Meses trabalhados/3=Sexo/4=Admissão/5=Motivo demissão/6=Salário Contratual/7=Salário Mínimo/8=Salário Base/9=Piso Salarial) |
| OPER_COMPARACAO | integer(4) |  |  | FORMA DE COMPARACAO ENTRE CAMPO E VALOR |
| OPER_LOGICO | integer(4) |  |  | OPERADOR LOGICO QUE LIGA UMA EXPRESSAO A OUTRA |
| VALOR_COMPARACAO | char(13) |  |  | Valor a ser comparado com a coluna |
| VALOR_RESULTADO | numeric(5) |  | S | RESULTADO DA REGRA |
| ORIGEM_REG | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| VALOR_COMPARACAO_FINAL | numeric(13) |  | S | Faixa salarial final |
| SOMAR_CONDICOES | smallint(2) |  |  | Somar condições. (0=Não/1=Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
