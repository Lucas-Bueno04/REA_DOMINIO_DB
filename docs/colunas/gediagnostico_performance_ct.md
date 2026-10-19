# GEDIAGNOSTICO_PERFORMANCE_CT — Diagnóstico de Performance (retenção 90 dias)
2.464 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_LOG | bigint(8) | PK |  | Identificador único do registro |
| CODI_EMP | integer(4) |  |  | Código da empresa |
| SCP | varchar(20) |  |  | Código da SCP. Será considerado "0" para sócio ostensivo. |
| FUNCIONALIDADE | varchar(50) |  |  | Funcionalidade: SPED Contábil, SPED ECF |
| USUARIO | varchar(255) |  |  | Usuário que executou o processo |
| VERSAO_SISTEMA | varchar(80) |  |  | Versão do sistema no momento da execução |
| CODIGOS_FILIAIS | varchar(4000) |  | S | Códigos de filiais envolvidas (separadas por vírgula) |
| PERIODO_DATA_INICIAL | date(4) |  |  | Data inicial do período do relatório/processo |
| PERIODO_DATA_FINAL | date(4) |  |  | Data final do período do relatório/processo |
| TOTAL_LANCAMENTOS | integer(4) |  | S | Total de lançamentos |
| TOTAL_CONTAS_CONTABEIS | integer(4) |  | S | Total de contas |
| TOTAL_CENTROS_CUSTO | integer(4) |  | S | Total de centros de custo |
| TEMPO_GERACAO_MS | bigint(8) |  |  | Tempo de geração (CPU, ms) sem espera ociosa |
| DT_HORA_FIM | timestamp(8) |  |  | Data/hora local do término da geração |
| DOMINIO_WEB | smallint(2) |  |  | 1=Domínio Web, 0=Não |
