# EFPARAMETRO_VIGENCIA_INSCRICOES_SUBTRI — Paramentros - Inscricoes de Substituicao Tributaria
16 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| SIGL_EST | char(2) | PK |  | Sigla do estado (UF) |
| VIGENCIA_PAR | date(4) | PK |  | Vigencia |
| IEST_INF | char(22) |  |  | Inscricao Estadual |
| PMPF_INF | char(1) |  |  | Preco Medio Ponderado Fiscal |
| ORIGEM_REG | integer(4) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
