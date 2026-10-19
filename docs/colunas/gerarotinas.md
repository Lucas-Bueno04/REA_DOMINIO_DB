# GERAROTINAS — CADASTRO DE ROTINAS AUTOMÁTICAS
501 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_ROTINAS | integer(4) | PK |  | CÓDIGO DA ROTINA |
| I_SISTEMA | smallint(2) | PK |  | CÓDIGO DO SISTEMA |
| DESCRICAO | char(60) |  |  | DESCRIÇÃO DA ROTINA |
| PASTA_DESTINO_SALVA_RELATORIOS | varchar(255) |  | S | Pasta destino para salvar os relatórios em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_ACOMPANHAMENTO | varchar(255) |  | S | Pasta destino para salvar os relatórios de acompanhamentos em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_GUIA | varchar(255) |  | S | Pasta destino para salvar os relatórios de Guia em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_UTILITARIO | varchar(255) |  | S | Pasta destino para salvar os relatórios de Utilitários em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_MEI | varchar(255) |  | S | Pasta destino para salvar os relatÃ³rios da Guia MEI em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_INFORMATIVO | varchar(255) |  | S | Pasta destino para salvar os relatórios de Informativos em PDF. |
| PASTA_DESTINO_SALVA_RELATORIOS_DEMONSTRATIVO | varchar(255) |  | S | Pasta destino para salvar os relatórios de Demonstrativo em PDF. |
| TIPO_ROTINA | integer(4) |  | S | Tipo de Rotina, 0 - rotina cliente, 1 - rotina interna |
| PASTA_DESTINO_SALVA_RELATORIOS_EXCEL | varchar(255) |  | S | Pasta destino para salvar os relatórios em Excel. |
