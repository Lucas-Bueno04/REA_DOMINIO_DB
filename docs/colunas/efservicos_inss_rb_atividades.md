# EFSERVICOS_INSS_RB_ATIVIDADES — Notas Fiscais de Serviço - INSS Receita Bruta - Receitas por Atividade
5.897 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SER | integer(4) | PK |  | Codigo |
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_ATIVIDADE | char(8) |  |  | Código da atividade |
| ALIQUOTA | numeric(7) |  |  | Aliquota |
| RECEITA_BRUTA | numeric(13) |  |  | Receita Bruta |
| RECEITA_BRUTA_TOTAL_REINF | numeric(13) |  |  | Receita Bruta REINF |
| DESCONTO_REINF | numeric(13) |  |  | Desconto REINF |
| IPI_REINF | numeric(13) |  |  | IPI REINF |
| ICMS_ST_REINF | numeric(13) |  |  | ICMS ST REINF |
| I_CNO | integer(4) |  | S | Código CNO |
| DISPENSA_CNO | char(1) |  |  | Dispensa CNO |
