# FODIRF_OUTROS_DADOS — DIRF - Outros dados
4.996 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| ANO_BASE | integer(4) | PK |  | Ano base |
| DECLARACAO_RETIFICADORA | smallint(2) |  |  | Declaração retificadora |
| CERTIFICADO_DIGITAL | smallint(2) |  | S | Certificado digital |
| NUMERO_RECIBO_DECLARACAO | char(12) |  | S | Número do recibo da delaração |
| DECLARACAO_EXTINCAO | smallint(2) |  |  | Declaração de extinção |
| DATA_EVENTO | date(4) |  | S | Data do evento |
| TIPO_EVENTO | smallint(2) |  | S | Tipo do evento |
| SOCIO_OSTENSIVO | smallint(2) |  |  | Sócio ostensivo |
| DECLARANTE_TITULAR | smallint(2) |  |  | Declarante é titular de serviços notariais e de registros |
| DECLARAR_TODOS_EMPREGADOS | smallint(2) |  |  | Declarar todos os empregados |
| GERAR_INFORMACOES_COMPLEMENTARES | smallint(2) |  |  | Gerar informações complementares para o comprovante de rendimentos |
| NATUREZA_DECLARANTE | smallint(2) |  |  | Natureza do declarante |
| COMPETENCIA_VALOR_NEGATIVO_PREVIDENCIA | char(1) |  | S | Competência com valor negativo para previdência oficial |
| COMPETENCIA_VALOR_NEGATIVO_PREVIDENCIA_OPCAO | integer(4) |  | S | Opção da competência com valor negativo para previdência oficial |
| EFETUOU_PAGTO_OLIMPIADAS | smallint(2) |  |  | Efetuou pagamentos relacionados aos Jogos Olímpicos 2016 e aos Jogos Paraolímpicos 2016 |
| EFETUOU_PAGTO_COPA | smallint(2) |  |  | Efetuou pagamentos relacionados à Copa das Confederações 2013 e a Copa do Mundo 2014 |
| LIMITAR_60_CARACTERES_DESCRICAO_OUTROS_RENDIMENTOS_ISENTOS_NAO_TRIBUTAVEIS | smallint(2) |  |  | Limitar a 60 caracteres a descrição de Outros Rendimentos Isentos e não Tributáveis. (0=Não/1=Sim) |
| DATA_OBITO | date(4) |  | S | Data do óbito. |
| CPF_INVENTARIANTE | char(11) |  | S | CPF do inventariante. |
| NOME_INVENTARIANTE | varchar(60) |  | S | Nome do Inventariante |
| GERAR_CONTRIBUINTES_AUTONOMOS_DE_CONDOMINIO_EDILICIO | smallint(2) |  |  | Gerar os contribuintes autônomos de condomínio edilício para a DIRF. (0=Não/1=Sim) |
