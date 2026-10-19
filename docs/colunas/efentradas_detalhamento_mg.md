# efentradas_detalhamento_mg — Notas Fiscais de Entradas - Detalhamentos - MG
4.899 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_ent | integer(4) | PK |  | Nota |
| sem_aproveitamento | numeric(13) |  |  | Imposto sem aproveitamento de credito |
| isentas | numeric(13) |  |  | Isentas |
| nao_tributadas | numeric(13) |  |  | Nao tributadas |
| base_reduzida | numeric(13) |  |  | Parcela de base de calculo reduzida |
| diferidas | numeric(13) |  |  | Diferidas |
| suspensas | numeric(13) |  |  | Suspensas |
| substituicao | numeric(13) |  |  | Substituicao tributaria |
| outras | numeric(13) |  |  | Outras |
| GERAR_NO_INFORMATIVO_DAPI | char(1) |  |  | Gerar no informativo DAPI |
| GERAR_NO_INFORMATIVO_DAPI_OPERACAO | char(1) |  |  | Gerar no informativo DAPI MG |
