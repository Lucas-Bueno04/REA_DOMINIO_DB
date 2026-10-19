# ctbalancosocial — Balanco Social - Estrutura
108 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | codi_emp |
| codi_soc | integer(4) | PK |  | Codigo do item |
| sequ_soc | integer(4) |  |  | Sequencial |
| desc_soc | varchar(120) |  | S | Descricao |
| tipo_soc | char(1) |  | S | Tipo da descricao(C=Conta/V=Variavel/I=Informar/T=Total/D=Titulo) |
| ccta_soc | varchar(1000) |  | S | Codigo das contas |
| base_soc | char(3) |  | S | Base para percentual |
| vari_soc | integer(4) |  | S | Codigo da variavel |
| indi_soc | tinyint(1) |  | S | Indicador |
