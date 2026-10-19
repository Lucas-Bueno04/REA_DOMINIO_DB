# CTGRUPOSDFC_DIRETO — Estrutura DFC - Metodo Direto
2.323 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_DIRETO | integer(4) | PK |  | Codigo |
| ORDEM | integer(4) |  |  | Ordem |
| ATIVIDADE | integer(4) |  |  | Atividade (1=Operacionais/2=Investimento/3=Financiamento) |
| DESCRICAO | varchar(128) |  |  | Descricao |
| NATUREZA | char(1) |  |  | Natureza (A=Analitica/S=Sub-Total/V=Atividade) |
