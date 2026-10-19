# efrsgmb_anexo5 — GMB - Tabela de Codigos Fiscais
554 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| i_cfop | integer(4) | PK |  | CFOP |
| competencia | date(4) | PK |  | Competencia |
| valor_contabil | tinyint(1) |  |  | Permite valor contabil (1=Sim/0=Nao) |
| base_calculo | tinyint(1) |  |  | Permite base calculo (1=Sim/0=Nao) |
| isentas | tinyint(1) |  |  | Permite isentas (1=Sim/0=Nao) |
| outras | tinyint(1) |  |  | Permite outras (1=Sim/0=Nao) |
| excluidas | tinyint(1) |  |  | Permite excluidas (1=Sim/0=Nao) |
| FORMA_GERACAO_EXCLUIDAS | integer(4) |  |  | Forma de geração das excluídas(1-Valor Contábil/2-Base de cálculo+isentas+outras) |
