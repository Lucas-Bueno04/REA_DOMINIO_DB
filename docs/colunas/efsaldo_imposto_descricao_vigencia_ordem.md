# EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_ORDEM — Tela de Apuração de Impostos - Layouts - Ordem das colunas
9.636 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Código do imposto |
| UF | char(2) | PK |  | UF |
| VIGENCIA | date(4) | PK |  | Vigência |
| MODELO | integer(4) | PK |  | Modelo |
| ORDEM | char(7) | PK |  | Ordem |
| COLUNA | varchar(255) |  |  | Coluna |
| DESCRICAO | varchar(255) |  |  | Descrição apuração |
| DESCRICAO_RELATORIO | varchar(255) |  |  | Descrição relatório |
| OPERACAO | integer(4) |  |  | Operacao |
| NIVEL | integer(4) |  |  | Nível |
| TIPO | char(1) |  |  | Tipo |
| VISUALIZACAO | integer(4) |  |  | Visualização |
| DETALHAMENTO | integer(4) |  |  | Detalhamento |
| FORMA_EXIBICAO | integer(4) |  |  | Forma Exibição |
| DEMONSTRA_RELATORIO_RESUMO | char(1) |  |  | Demonstra relatório resumo |
| COLUNA_RELATORIO_RESUMO_LANCADO | varchar(255) |  |  | Coluna relatório de resumo - modelo lançado |
| COLUNA_RELATORIO_RESUMO_CALCULADO | varchar(255) |  |  | Coluna relatório de resumo - modelo calculado |
| SOMA_NO_PAI | char(1) |  |  | Para colunas que possuem valor, indicador se vai somar no pai. |
