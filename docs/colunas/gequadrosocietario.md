# gequadrosocietario — Empresa - Cadastro - Quadro Societario
1.571 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Codigo da empresa |
| data | date(4) | PK |  | Data |
| valor_quota | numeric(13) |  |  | Valor das quotas (Sem uso) |
| qdade_quota | numeric(13) |  |  | Quantidade de quotas |
| capital_social | numeric(20) |  |  | Total do Capital Social |
| total_integralizar | numeric(13) |  |  | Total do Capital a Integralizar |
| liberado | char(1) |  |  | Liberado (finalizado) pelo Modulo Registro (S=Sim/N=Nao) |
| QUOTA_INTEGRALIZADA | numeric(13) |  |  | Quotas integralizadas |
| QUOTA_A_INTEGRALIZAR | numeric(13) |  |  | Quotas a integralizar |
| CAPITAL_INTEGRALIZADO | numeric(17) |  |  | Capital integralizado |
| TOTAL_CAPITAL | numeric(17) |  |  | Total do capital |
| QUOTAS_EM_TESOURARIA | numeric(5) |  | S | Quotas em tesouraria(%) |
| CONSIDERAR_PERCENTUAL_QUOTAS_TESOURARIA_TOTAL_PARTICIPACAO_SOCIOS | char(1) |  |  | Considerar percentual de quotas da tesouraria no total de participaÃ§Ã£o dos SÃ³cios (S/N) |
