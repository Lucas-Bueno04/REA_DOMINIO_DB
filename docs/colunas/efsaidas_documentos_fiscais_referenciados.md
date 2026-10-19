# EFSAIDAS_DOCUMENTOS_FISCAIS_REFERENCIADOS — Notas Fiscais de Saída - Documentos fiscais referenciados
618 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_SAI | integer(4) | PK |  | Código |
| DOCUMENTO_DFSAI | integer(4) | PK |  | Sequencial |
| OPERACAO_DFSAI | char(1) |  |  | Operação (0 - Entrada/1 - Saída) |
| EMITENTE_DFSAI | char(1) |  |  | Emitente (0 - Emissão própria/1 - Terceiros) |
| PARTICIPANTE_DFSAI | integer(4) |  | S | Participante |
| ESPECIE_DFSAI | integer(4) |  |  | Modelo da espécie |
| SERIE_DFSAI | char(4) |  |  | Série |
| SUBSERIE_DFSAI | integer(4) |  |  | Sub-série |
| NUMERO_DFSAI | integer(4) |  |  | Número do documento |
| EMISSAO_DFSAI | date(4) |  |  | Data de emissão |
| SAIDA_DFSAI | date(4) |  | S | Saída |
| VALOR_NOTA_DFSAI | numeric(13) |  |  | Valor da nota |
| SITUACAO_DFSAI | integer(4) |  |  | Situação |
| VALOR_ISS_DFSAI | numeric(13) |  |  | Valor do ISS |
| VALOR_ISS_RETIDO_DFSAI | numeric(13) |  |  | Valor do ISS Retido |
| VALOR_ICMS_DFSAI | numeric(13) |  |  | Valor do ICMS |
| VALOR_ICMS_ST_DFSAI | numeric(13) |  |  | Valor do ICMS ST |
| VALOR_IPI_DFSAI | numeric(13) |  |  | Valor do IPI |
| CHAVE_NFE_CTE | varchar(44) |  | S | Chave NFe ou CTe |
