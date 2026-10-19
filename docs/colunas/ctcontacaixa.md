# ctcontacaixa — Parametros - Cadastro - Contas caixa
2.651 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_cta | integer(4) | PK |  | Conta |
| sele_cta | char(1) |  |  | Esta Selecionada(S/N) |
| TIPO_CONTA_CAIXA | integer(4) |  | S | Tipo da conta[1=Conta bancária / 2=Dinheiro/Espécie / 3=Numerários em Trânsito / 4=Não gerar no LCDPR] |
