# EFOUTROS_DADOS_PLANEJAMENTO_TRIBUTARIO_IVA — Outros Dados - Planejamento Tributário - IVA
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| COMPETENCIA | date(4) | PK |  | Competencia |
| I_INFORMATIVOS | integer(4) | PK |  | Informativo |
| ALIQUOTA_CBS | numeric(5) |  | S | Aliquota CBS |
| ALIQUOTA_IBS | numeric(5) |  | S | Alíquota IBS |
| BASE_CALCULO_IVA | integer(4) |  | S | Base de Calculo IVA |
| ATIVIDADE_COM_REDUCAO_ALIQUOTA | char(1) |  | S | Atividade com redução de aliquota |
| CALCULAR_CBS_IBS_PELO_REGIME_REGULAR_SIMPLES_NACIONAL | char(1) |  | S | Calcular a CBS e o IBS pelo regime regular no planejamento tributário para o Simples Nacional (N=Não/S=Sim) |
| CONSIDERAR_SALDO_CONTAS | char(1) |  | S | Considerar saldo das contas contabeis |
| FORMA_IMPORTACAO | char(1) |  | S | Forma de importação do saldo das contas |
| FORMA_CALCULO | char(1) |  | S | Forma de Calculo |
