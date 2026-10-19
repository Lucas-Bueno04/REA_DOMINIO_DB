# USCONFUSUARIO_PREFERENCIAS — Tabela para armazenar as preferências do usuário
69 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_TIPO_USUARIO | smallint(2) | PK |  | Código do tipo de usuário |
| CODI_USUARIO | integer(4) | PK |  | Código do usuário |
| RELATORIO_ABRIR_PDF_APOS_SALVAR | bit(1) |  | S | 1 = Abre o pdf depois que salva um relatório em PDF, 0 = Não abre |
| RELATORIO_ABRIR_PLANILHA_APOS_SALVAR | bit(1) |  | S | 1 = Abre o planilha depois que salva um relatório em XLS/XLSX, 0 = Não abre |
| RELATORIO_CERTIFICADO_PROPRIO_PROCURACAO | bit(1) |  | S | 0 = Próprio, 1 = Por Procuração |
