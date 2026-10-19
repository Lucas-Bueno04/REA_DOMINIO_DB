# FODIFERENCA_ALTERACAO_RETROATIVA_PISO_SALARIAL — Diferenças referentes a alteração retroativa de piso salarial.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SINDICATOS | integer(4) | PK |  | Código do sindicato. |
| I_SINDPISO | integer(4) | PK |  | Código do piso salarial. |
| COMPETENCIA_ALTERACAO | date(4) | PK |  | Competência da alteração. |
| COMPETENCIA_RETROATIVA | date(4) |  |  | Competência retroativa. |
| FORMA_AJUSTE | smallint(2) |  |  | Forma de ajuste. (1=Complementar mês a mês/2=Folha mensal do mês do aumento/3=Folha complementar do mês do aumento) |
| ORIGEM_REGISTRO | smallint(2) |  |  | Origem do registro. (0=Sistema/1=Importação de tabelas/2=Importação de layout) |
| CONSIDERAR_ALTERACAO_PAGAMENTO_DIFERENCA_GARANTIA_MINIMA | smallint(2) |  |  | Considerar a alteração para pagamento de diferenças de Garantia Mínima. (0=Não/1=Sim) |
| CALC_DIFERENCA_REFERENTE_PISO_SAL_CONVENCAO_COLETIVA_TRABALHO | integer(4) |  | S | Calcular Diferença referente a Piso Salarial como Convenção Coletiva de Trabalho (0-Não/1-Sim) |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
