# rgalteracao_contratual — Alteracao Contratual
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| i_alteracao | integer(4) | PK |  | Codigo |
| data | date(4) |  |  | Data |
| i_tipoalteracao | integer(4) |  |  | Tipo da alteracao |
| filial | integer(4) |  | S | Codigo da filial |
| i_advogado | integer(4) |  | S | Advogado |
| i_testemunha1 | integer(4) |  | S | Testemunha |
| i_testemunha2 | integer(4) |  | S | Testemunha |
| i_ato | integer(4) |  | S | Ato |
| i_evento1 | integer(4) |  | S | Evento 1 |
| i_evento2 | integer(4) |  | S | Evento 2 |
| i_evento3 | integer(4) |  | S | Evento 3 |
| outra_uf_matriz | char(1) |  |  | Transferencia de UF da matriz |
| outra_uf_filial | char(1) |  |  | Transferencia de UF da filial |
| i_ole | integer(4) |  | S | Codigo ole |
| dataprotocolo | date(4) |  | S | Data do Protocolo |
| nroprotocolo | char(15) |  | S | Numero do Protocolo |
| avisar | char(1) |  |  | Avisar (S/N) |
| nrodias | integer(4) |  | S | Numero de dias para conclusao |
| dataaviso | date(4) |  | S | Data de aviso do processo |
| finalizado | char(1) |  |  | Alteracao finalizada (S/N) |
| nire | char(11) |  | S | Numero do NIRE |
| datafinalizado | date(4) |  | S | Data da finalizacao |
| INUTILIZAR_CAMPO_NAO_PREENCHIDO | char(1) |  |  | Inutilizar campos não preenchidos (S/N) |
| ALTERACAO_TRANSFORMACAO | char(1) |  |  | Alteração de transformação (S/N) |
| SITUACAO_NATUREZA_JURIDICA | char(1) |  |  | Situação da natureza jurídica (E=Empresário individual/ S=Sociedade LTDA/ R=EIRELI) |
| INFORMAR_VALOR_CAPITAL_SOCIAL | char(1) |  |  | Informar valor do capital social |
| VALOR_CAPITAL_SOCIAL | numeric(13) |  |  | Capital social |
| HABILITA_MODELO | char(1) |  |  | Habilita grupo de modelo de relatório. |
| HABILITA_DOCUMENTO_VINCULADO | char(1) |  |  | Habilita grupo de documento vinculado. |
