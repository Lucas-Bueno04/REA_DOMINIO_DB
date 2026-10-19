# EFLUCROS_DIVIDENDOS_TRIBUTAVEIS_DISTRIBUICAO_CONTAS_PARAM — Distribuição de lucros e dividendos tributáveis - Contas parâmetros
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_LANC_LUCROS_DIVIDENDOS_TRIBUTAVEIS | integer(4) | PK |  | Código de Lancamento de Lucros e Dividendos Tributáveis |
| I_SEQUENCIAL_DISTRIBUICAO | integer(4) | PK |  | Sequencial Distribuição |
| PERIODO_INICIAL | date(4) |  |  | Período inicial |
| PERIODO_FINAL | date(4) |  |  | Período final |
| FORMA_IMPORTAR_SALDO | integer(4) |  |  | Determinar a forma de importar o saldo das contas contábeis |
