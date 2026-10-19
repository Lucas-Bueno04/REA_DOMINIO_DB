# GEATENDIMENTO_STATUS_OPCOES_BARRA_DOMINIO — No Contábil a thread responsável por habilitar/desabilitar os botões da barra da Domino, verifica os valores nesta tabela.
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODIGO | integer(4) | PK |  | Código, sempre existirá apenas uma linha |
| HABILITAR_IMPORTACAO_DOCUMENTOS_MODULO_ESCRITA_FISCAL | bit(1) |  |  | 1 - Habilitar, 2 - Desabilitar. Status do farol referente ao painel de importação de documentos no módulo Escrita Fiscal. |
| HABILITAR_IMPORTACAO_DOCUMENTOS_MODULO_FOLHA | bit(1) |  |  | 1 - Habilitar, 2 - Desabilitar. Status do farol referente ao painel de importação de documentos no módulo Folha. |
