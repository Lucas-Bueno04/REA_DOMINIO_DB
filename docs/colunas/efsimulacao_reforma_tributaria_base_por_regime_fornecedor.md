# EFSIMULACAO_REFORMA_TRIBUTARIA_BASE_POR_REGIME_FORNECEDOR — Simulador Reforma Tributaria - Base por Regime de Fornecedor/Cliente
111 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERIODO | date(4) | PK |  | Periodo - Competencia |
| FILIAL | integer(4) | PK |  | Filial |
| CLI_FOR | char(1) | PK |  | Cliente ou Fornecedor |
| TIPO_REGIME | char(1) | PK |  | Regime Fornecedor |
| TIPO_MOVIMENTO | char(2) | PK |  | Tipo Movimento (CE - Credito Entrada / DS - Debito Saida) |
| VALOR_CONTABIL | numeric(13) |  |  | Valor contabil |
| PERCENTUAL | numeric(5) |  |  | Percentual representacao |
