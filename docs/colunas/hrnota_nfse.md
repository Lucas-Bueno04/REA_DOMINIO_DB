# HRNOTA_NFSE — Notas fiscais de servico eletronica emitidas
36.496 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Escritorio |
| I_NOTA_NFSE | integer(4) | PK |  | Codigo |
| I_CLIENTE | integer(4) |  |  | Cliente |
| NUMERO_RPS | numeric(17) |  |  | Numero da RPS |
| I_LOTE | integer(4) |  | S | Numero do lote |
| NUMERO_NFSE | numeric(17) |  | S | Numero da nota fiscal |
| CODIGO_VERIFICACAO | varchar(50) |  | S | Codigo de verificacao |
| EMISSAO_NFSE | date(4) |  |  | Data de emissao da nota fiscal |
| CANCELADA_NOTA_NFSE | char(1) |  |  | Nota fiscal cancelada (S/N) |
| CANCELADA_NOTA_NFSE_DATA | date(4) |  | S | Data do cancelamento da nota fiscal |
| ALIQUOTA | numeric(7) |  |  | Aliquota |
| SERIE | char(5) |  | S | Serie |
| I_CNAE20 | char(15) |  | S | CNAE |
| I_SEQUENCIAL_SERVICO_PRESTADO | integer(4) |  | S | Sequencial do Servico prestado |
| NATUREZA_OPERACAO | integer(4) |  |  | Natureza da operacao |
| DATA_HORA | timestamp(8) |  |  | Data e hora da emissao |
| USUARIO | varchar(128) |  |  | Usuario que emitiu |
| OBSERVACAO | varchar(512) |  |  | Observacao da nota fiscal |
| EMISSAO_HORA_NFSE | time(8) |  |  | Hora de emissao da nota fiscal |
| MUNICIPIO_PRESTACAO_SERVICO | integer(4) |  | S | Município de prestação do serviço |
| NUMERO_PROCESSO | varchar(30) |  | S | Número do processo |
| I_CFPS | integer(4) |  | S | CFPS |
| IDENTIFICARDOR_CNAE | integer(4) |  | S | Identificador do CNAE |
| CST | integer(4) |  | S | CST |
| VENCIMENTO_CANCELAMENTO | date(4) |  | S | Vencimento do cancelamento |
| MOTIVO_CANCELAMENTO | varchar(255) |  | S | Motivo do cancelamento |
| MENSAGEM_CANCELAMENTO | varchar(255) |  | S | Mensagem do cancelamento |
| SITUACAO_CANCELAMENTO | char(1) |  |  | Situação do cancelamento (N = Normal/ P= Em processamento/ I= Cancelamento impossibilitado/ C= Cancelada/ X= Pendente) |
| I_CFOP | integer(4) |  | S | CFOP |
| I_CFOP_VERSAO | smallint(2) |  | S | CFOP versão |
| CHAVE_ACESSO | varchar(44) |  | S | Chave de acesso |
| MENSAGEM | varchar(1024) |  | S | Mensagem |
| TIPO_CANCELAMENTO | char(1) |  |  | Tipo de cancelamento(M=Manter faturamento/E=Excluir faturamento) |
| GERAR_SOMENTE_DESCRICAO_EVENTO_CONTRATO_ARQUIVO_IMPRESSAO | char(1) |  |  | Gerar somente a descrição do evento do contrato no arquivo e impressão do RPS e NFS-e |
| NFSE_FORMA_RECOLHIMENTO_CHAR | char(1) |  |  | NFSE - Forma de recolhimento (N - Não retido / S - Retido dentro do município / F - Retido fora do município / D - Devido fora do município - não retido / I - Sem incidência do ISS) |
| IMPRIMIR_EVENTOS_VALOR_LIQUIDO_ZERO | char(1) |  |  | Imprimir eventos com valor liquido igual a zero |
| SERVICO_SIMPLES_NACIONAL | integer(4) |  | S | Serviço do Simples Nacional(Código do Serviço Prestado) |
| TIPO_ENDERECO_PRESTACAO_SERVICO | tinyint(1) |  |  | Tipo de endereço da prestação do serviço |
| ENDERECO_PRESTACAO_SERVICO | varchar(40) |  | S | Endereço da prestação do serviço |
| NUMERO_PRESTACAO_SERVICO | integer(4) |  | S | Número do endereço da prestação do serviço |
| BAIRRO_PRESTACAO_SERVICO | varchar(60) |  | S | Bairro da prestação do serviço |
| COMPLEMENTO_PRESTACAO_SERVICO | varchar(30) |  | S | Complemento da prestação do serviço |
| UF_PRESTACAO_SERVICO | char(2) |  | S | UF da prestação do serviço |
| CEP_PRESTACAO_SERVICO | char(8) |  | S | CEP da prestação do serviço |
| I_CNAE_ESPECIFICO | char(15) |  | S | CNAE Específico prefeitura. |
| GERAR_OBSERVACAO_DISCRIMINACAO_SERVICOS | char(1) |  |  | Gerar observação na discriminação dos serviços" estiver desmarcada na geração do RPS |
| CONVERTIDO_EM_NFSE_MANUALMENTE | char(1) |  |  | Convertido em NFS-e manualmente |
| GERAR_DATA_VENCIMENTO_DISCRIMINACAO_SERVICOS | char(1) |  |  | Gerar data de vencimento das parcelas na discriminação dos serviços |
| RECEITA_BRUTA_SIMPLES_NACIONAL | numeric(13) |  | S | Receita dupla simples nacional |
| I_SEQUENCIAL_RPS | integer(4) |  | S | Sequencial do Rps. |
| GERAR_HISTORICO_DESCONTO_DISCRIMINACAO_SERVICO | char(1) |  |  | Gera historico do desconto na descriminação do serviço |
| RPS_EXCLUIDO | char(1) |  | S | Coluna criada para saber se o rps fora excluído |
| RECEBIMENTO_NFSE | date(4) |  | S | Data de recebimento |
| I_SEQUENCIAL_DPS | integer(4) |  | S | Sequencial do DPS |
| CODIGO_NOTA_TECNOSPEED | varchar(50) |  | S | Código da nota retornado pela API Tecnospeed para download de PDF |
| PROTOCOLO_CANCELAMENTO_TECNOSPEED | varchar(50) |  | S | Protocolo retornado pela API Tecnospeed para o cancelamento de NFS-e |
| CODIGO_CANCELAMENTO | varchar(5) |  | S | Código de cancelamento NFS-e |
| GERAR_PARCELAS_NFSE | char(1) |  |  |  |
| GERAR_INFORMACAO_COMPETENCIA_NFSE | char(1) |  |  | Gerar informacao de competencia na NFS-e (S=Sim, N=Nao) |
| DESCRICAO_SERVICO | varchar(5000) |  | S |  |
| I_SEQUENCIAL_NBS | integer(4) |  | S |  |
| GERAR_ALIQUOTA_ISSQN_NFSE | char(1) |  |  | Gerar a aliquota do ISSQN (tag pAliq) no XML do DPS (S=Sim, N=Nao) |
