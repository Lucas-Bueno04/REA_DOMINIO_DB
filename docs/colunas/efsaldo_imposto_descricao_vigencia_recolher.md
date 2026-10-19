# EFSALDO_IMPOSTO_DESCRICAO_VIGENCIA_RECOLHER — Tela de Apuração de Impostos - Recolher
769 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_IMP | integer(4) | PK |  | Código do imposto |
| UF | char(2) | PK |  | UF |
| VIGENCIA | date(4) | PK |  | Vigência |
| MODELO | integer(4) | PK |  | Modelo |
| ORDEM | integer(4) | PK |  | Ordem |
| COLUNA | varchar(255) |  |  | Coluna |
| DESCRICAO | varchar(255) |  |  | Descrição apuração |
| DESCRICAO_RELATORIO | varchar(255) |  |  | Descrição relatório |
| VISUALIZACAO | integer(4) |  |  | Visualização |
| TIPO | integer(4) |  |  | Tipo |
| MEMORIA_CALCULO | char(1) |  |  | Botão memória de cálculo |
| NIVEL | integer(4) |  |  | Nível |
