# EFPLANEJAMENTO_TRIBUTARIO — Planejamento Tributário
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| REGIME | char(1) | PK |  | Regime de Planejamento (P  - Presumido, R - Real, S - Simples) |
| ANO | integer(4) |  |  | Ano Planejamento |
| PERIODO_CONSIDERADO_INICIO | date(4) |  |  | Periodo Inicial considerado para calculo |
| PERIODO_CONSIDERADO_FIM | date(4) |  |  | Periodo Final considerado para calculo |
| PERIODO_ESTOURO_LIMITE_ESTADUAL | date(4) |  |  | Periodo com estouro do limite estadual |
| PERIODO_ESTOURO_LIMITE_FEDERAL | date(4) |  |  | Periodo com estouro do limite federal |
| EMPRESA_ESTOUROU_LIMITE_FEDERAL_ANO_ANTERIOR | char(1) |  |  | Empresa estourou limite federal ano anterior |
| EMPRESA_ESTOUROU_LIMITE_ESTADUAL_ANO_ANTERIOR | char(1) |  |  | Empresa estourou limite estadual ano anterior |
| POSSUI_SOCIO_EM_OUTRA_EMPRESA | char(1) |  |  | Possui socio em outra empresa |
| POSSUI_NCM_COM_MULTIPLO_CCLASSTRIB | char(1) |  | S | Possui Ncm múltiplos cclasstrib |
| JSON_DADOS_DIAGNOSTICO_IA | long binary(32767) |  | S | Arquivo JSON com dados do diagnóstico gerados por IA para o planejamento tributário |
| FORMA_CALCULO | tinyint(1) |  | S | Forma de cálculo (1-Movimentações da empresa,2-Manualmente) |
