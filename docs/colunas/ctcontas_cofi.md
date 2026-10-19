# CTCONTAS_COFI — Plano de contas COFI
492 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO_CTA_COFI | integer(4) | PK |  | Código |
| CLASSIFICACAO_COFI | varchar(20) |  |  | Classificação |
| DESCRICAO_COFI | varchar(100) |  |  | Descrição |
| DATA_INICIO_COFI | date(4) |  |  | Data início |
| DATA_FIM_COFI | date(4) |  | S | Data fim |
| PERMITE_RELACIONAMENTO_COFI | char(1) |  |  | Permite relacionamento (S/N) |
| NORMAL_RETIFICADORA_COFI | varchar(2) |  |  | Normal ou retificadora (N=Normal/ R=Retificadora/ NR=Normal e Retificadora) |
| CONTA_SUPERIOR_COFI | varchar(20) |  |  | Conta superior |
| CLASSIFICACAO_COFI_AUXILIAR | varchar(20) |  |  | Classificação auxiliar |
