# FOEVENTOS_ALTERACAO_DADOS_CADASTRAIS — Alteração de dados cadastrais do histórico do cadastro de rubricas
1.310.502 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa do evento. |
| I_EVENTOS | integer(4) | PK |  | Código da rubrica. |
| VIGENCIA | date(4) | PK |  | Vigência da alteração. |
| TAXA | numeric(7) |  |  | Taxa da rubrica. |
| SOMA_ADICIONAL_AVISO_PREVIO | smallint(2) |  |  | Soma adicional aviso prévio. |
| COMP_13FER | char(1) |  |  | Computa 13/Ferias. |
| SOMA_MEDIA_AVISO_PREVIO | smallint(2) |  |  | Soma média aviso prévio. |
| SOMA_MED_13 | char(1) |  |  | Soma média 13° |
| SOMA_MED_FER | char(1) |  |  | Soma média férias. |
| BASE_RDSR | char(1) |  | S | Reflexo DSR. |
| DESCONTA_DSR | smallint(2) |  |  | Desconta no DSR. |
| SOMA_MEDIA_LICENCA_PREMIO | smallint(2) |  |  | Soma média licença prêmio. |
| SOMA_ADICIONAL_LICENCA_PREMIO | smallint(2) |  |  | Soma adicional licença prêmio. |
| TIPO_VALOR_CONSIDERAR_CALCULO_MEDIAS | smallint(2) |  | S | Tipo de valor pra considerar no cálculo de médias. |
| DETALHAR_LANCAMENTO_POR_SERVICO | smallint(2) |  |  | Detalhar lançamento por serviço. |
| ORIGEM_ALTERACAO | smallint(2) |  | S | Origem do registro ( 1=Sistema/2=Alteração de Faseamento do eSocial). |
| UTILIZA_PARA_ESOCIAL_DOMESTICO | smallint(2) |  |  | Utiliza para o eSocial Doméstico |
| CODIGO_ESOCIAL_DOMESTICO | varchar(15) |  | S | Código eSocial Doméstico |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
