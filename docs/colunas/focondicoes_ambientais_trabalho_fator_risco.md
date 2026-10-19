# FOCONDICOES_AMBIENTAIS_TRABALHO_FATOR_RISCO — Fatores de riscos do ambiente de trabalho.
62 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa. |
| I_EMPREGADOS | integer(4) | PK |  | Código do empregado. |
| DATA_INICIO | date(4) | PK |  | Data início da condição. |
| I_FATOR_RISCO | integer(4) | PK |  | Fator de risco. |
| TIPO_AVALIACAO | smallint(2) |  |  | Tipo de avaliação (0=Não Aplicável, 1=Quantitativo, 2=Qualitativo) |
| GRAU_EXPOSICAO | numeric(10) |  | S | Grau de exposição |
| LIMITE_TOLERANCIA | numeric(10) |  | S | Limite de tolerância |
| I_UNIDADE_MEDIDA | integer(4) |  | S | Unidade de medida. |
| TECNICA_MEDICAO | varchar(40) |  | S | Técnica de medição |
| INSALUBRIDADE | smallint(2) |  |  | Insalubridade (0=Não/1=Sim). |
| PERICULOSIDADE | smallint(2) |  |  | Periculosidade (0=Não/1=Sim). |
| APOSENTADORIA_ESPECIAL | smallint(2) |  |  | Aposentadoria especial (0=Não/1=Sim). |
| UTILIZA_PROTECAO_COLETIVA | smallint(2) |  |  | Utiliza proteção coletiva (1=Não se aplica/2=Não implementa/3=Implementa). |
| EPC_EFICAZ | smallint(2) |  |  | EPC eficaz (0=Não/1=Sim). |
| UTILIZA_PROTECAO_INDIVIDUAL | smallint(2) |  |  | Utiliza proteção individual (1=Não se aplica/2=Não utilizado/3=Utilizado). |
| SEQUENCIAL | integer(4) | PK |  | Sequencial |
| EFICAZ_NEUTRALIZACAO_RISCO_TRABALHADOR | smallint(2) |  |  | Eficaz na neutralização do fator de risco ao trabalhador (0=Não/1=Sim). |
| TENTATIVA_IMPLEMENTACAO_MEDIDAS_PROTECAO_COLETIVA | smallint(2) |  |  | Houve tentativa de implementação de medidas de proteção coletiva (0=Não/1=Sim). |
| OBSERVADO_CONDICOES_FUNCIONAMENTO | smallint(2) |  |  | Observado condicões de funcionamento do equipamento(0=Não/1=Sim). |
| OBSERVADO_USO_ININTERRUPTO | smallint(2) |  |  | Observado o uso ininterrupto do equipamento(0=Não/1=Sim). |
| OBSERVADO_PRAZO_VALIDADE_CERTIFICADO_APROVACAO | smallint(2) |  |  | Observado o prazo de validade do certificado de aprovação (0=Não/1=Sim). |
| OBSERVADO_PERIODICIDADE_MANUTENCAO | smallint(2) |  |  | Observado periodicidade da manutenção do equipamento (0=Não/1=Sim). |
| OBSERVADO_HIGIENIZACAO_CONFORME_ORIENTACAO | smallint(2) |  |  | Observado higienização conforme a orientação (0=Não/1=Sim). |
| DESCRICAO_AGENTE_NOCIVO | varchar(200) |  | S | Descrição do agente nocivo. |
| NUMERO_PROCESSO | varchar(21) |  | S | Número do Processo Agentes Nocivos |
