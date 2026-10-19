# EFTABELA_ATIVIDADE_GESTTA_PROCESSOS — Atividades
600 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_SEQUENCIAL | integer(4) | PK |  | Sequencial |
| I_MODULO | integer(4) |  |  | 1-FOLHA\2-ESCRITA FISCAL\3-CONTABILIDADE\4-PATRIMÔNIO\5-HONORÁRIOS\6-LALUR |
| I_MENU | integer(4) |  |  | 10-Movimentos\20-Processos\30-Relatórios\40-Utilitários |
| I_SUB_MENU | integer(4) |  |  | 1-Apuração\2-Parcelamento de Impostos Trimestrais\3-Pagamentos de Impostos\4-Integração Contábil\5-Integração Honorários\6-Livros\7-Informativos Federais\8-Informativos Estaduais\9-Guias Federais\10-Guias Estaduais\11-Guias Municipais |
| OPCAO | varchar(256) |  |  | Opção |
| OPCAO_DESCRICAO | varchar(256) |  |  | Descrição |
| UF | char(2) |  |  | Estado |
| ANEXO | char(1) |  |  | S-Sim\N-Não |
| ARQUIVO | char(1) |  |  | S-Sim\N-Não |
| CONFORME_IMPOSTO | char(1) |  |  | A opção representa um imposto (S/N) |
| CODI_IMP | integer(4) |  |  | Imposto |
