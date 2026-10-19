# FOAVISOSVENCIMENTOS — GUARDA OS AVISOS DE VENCIMENTOS PARA CONSULTA
48.139 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | CÓDIGO DA EMPRESA |
| I_EMPREGADOS | integer(4) | PK |  | CÓDIGO DO EMPREGADO |
| I_AVISOSVENCIMENTOS | integer(4) | PK |  | CÓDIGO SEQUENCIAL PARA CHAVE PRIMÁRIA |
| TIPO | integer(4) |  |  | 5=CONTRATO DE EXPERIÊNCIA,6=AVISO DE RESCISÃO,7=PROGRAMAÇÃO DE FÉRIAS,8=CARTEIRA VACINAÇÃO DEPENDENTE,9=ATESTADO DE FREQUENCIA,10=CARTEIRA DE MOTORISTA,11=ATESTADOS OCUPACIONAIS,12=CONSELHOS REGIONAIS |
| VENCIMENTO | date(4) |  | S | DATA VENCIMENTO |
| DESCRICAO_ESPECIAL | char(50) |  | S | DESCRIÇÃO ESPECIAL |
| I_FILHOS | integer(4) |  | S | CÓDIGO DO FILHO DO EMPREGADO |
| I_FERIAS_PROGRAMACAO | integer(4) |  | S | CÓDIGO DA PROGRAMAÇÃO DE FÉRIAS |
| I_ATESTADO_OCUPACIONAL | integer(4) |  | S | CÓDIGO DO ATESTADO OCUPACIONAL |
| I_CONSELHO_REGIONAL | integer(4) |  | S | CÓDIGO DO CONSELHO REGIONAL |
| I_AFASTAMENTOS | integer(4) |  | S | Código do afastamento. |
| DATA_REAL_DN | numeric(10) |  | S | DATA_REAL_DN do afastamento |
| I_EPI | integer(4) |  | S | Código do EPI |
| DATA_ENTREGA_EPI | date(4) |  | S | Código do EPI |
| I_FERIAS_AQUISITIVOS | integer(4) |  | S | Código do período aquisitivo |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| I_MONITORAMENTO_SAUDE | integer(4) |  | S | Código do monitoramento de saúde |
