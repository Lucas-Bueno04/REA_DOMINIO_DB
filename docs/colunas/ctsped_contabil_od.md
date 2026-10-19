# CTSPED_CONTABIL_OD — SPED Contábil - Outros Dados
2.033 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_OUTROS_DADOS | integer(4) | PK |  | Sequencial dos outros dados |
| COMPETENCIA | date(4) |  |  | Competência |
| CODI_EMP_I_SCP | integer(4) |  | S | Empresa - SCP |
| I_SCP | integer(4) |  | S | SCP |
| INDICADOR_SITUACAO_ESPECIAL | char(1) |  |  | Indicador de situação especial |
| SITUACAO_ESPECIAL | integer(4) |  | S | Situação especial |
| INDICADOR_INICIO_PERIODO | integer(4) |  | S | Indicador de início de período |
| INDICADOR_EXISTENCIA_NIRE | integer(4) |  | S | Indicador de existência de NIRE |
| FINALIDADE_ESCRITURACAO | integer(4) |  | S | Finalidade da escrituração |
| HASH_ESCRITURACAO_SUBSTITUIDA | char(128) |  | S | Hash da escrituração substituída |
| NIRE_ESCRITURACAO_SUBSTITUIDA | numeric(13) |  | S | NIRE da escrituração substituída |
| INDICADOR_EMPRESA_GRANDE_PORTE | integer(4) |  | S | Indicador de empresa de grande porte |
| DATA_ARQUIVAMENTO_ATOS_CONSTITUTIVOS | date(4) |  | S | Data do arquivamento dos atos constitutivos |
| DATA_ENCERRAMENTO_EXERCICIO_SOCIAL | date(4) |  | S | Data de encerramento do exercício social |
| INFORMAR_DATA_ARQUIVAMENTO_ATO_CONVERSAO | char(1) |  |  | Informar data de arquivamento do ato de conversão da sociedade simples em sociedade empresária |
| DATA_ARQUIVAMENTO_ATO_CONVERSAO | date(4) |  | S | Data de arquivamento do ato de conversão da sociedade simples em sociedade empresária |
| GERAR_SOMENTE_CONTAS_MOVIMENTO | char(1) |  |  | Gerar somente contas com movimento |
| GERA_LANCAMENTOS_CENTRO_CUSTO | char(1) |  |  | Gera lançamentos por centro de custo |
| NAO_GERAR_REGISTRO_I051 | char(1) |  |  | Não gerar o registro I051 com o Plano de Contas Referencial |
| PLANO_CONTAS_REFERENCIAL | integer(4) |  | S | Plano de Contas Referencial |
| GERAR_CONTAS_CONTABEIS_POR | integer(4) |  | S | Gera as contas contábeis por |
| NUMERO_LIVRO | integer(4) |  |  | Número do livro |
| POSSUI_AUDITORIA_INDEPENDENTE | char(1) |  |  | Possui auditoria independente |
| NOME_AUDITOR | char(128) |  | S | Nome do auditor |
| REGISTRO_AUDITOR_CVM | char(128) |  | S | Registro do auditor na CVM |
| GERAR_BALANCO_PATRIMONIAL | char(1) |  |  | Gerar Balanço patrimonial |
| GERAR_BALANCO_PATRIMONIAL_GRAU_MAXIMO | integer(4) |  | S | Gerar Balanço patrimonial - Grau máximo |
| GERAR_DRE | char(1) |  |  | Gerar Demonstrativo do Resultado do Exercício (DRE) |
| GERAR_DLPA | char(1) |  |  | Gerar DLPA |
| GERAR_DMPL | char(1) |  |  | Gerar DMPL |
| GERAR_DRA | char(1) |  |  | Gerar DRA |
| GERAR_DVA | char(1) |  |  | Gerar DVA |
| GERAR_DOAR | char(1) |  |  | Gerar DOAR |
| GERAR_DFC | char(1) |  |  | Gerar DFC |
| GERAR_NOTAS_EXPLICATIVAS | char(1) |  |  | Gerar Notas Explicativas |
| GERAR_ARQUIVO_EXTERNO | char(1) |  |  | Gerar Arquivo(s) Externo(s) |
| GERAR_ARQUIVO_EXTERNO_CAMINHO | char(4096) |  | S | Gerar Arquivo(s) Externo(s) - Caminho |
| GERAR_REGISTROS_ANUAIS | char(1) |  |  | Gerar os registros anuais quando houver mais de um zeramento no período de geração do arquivo |
| NAO_GERAR_CONTAS_SALDO_ZERO_BALANCO | char(1) |  |  | Não gerar as contas contábeis com saldo inicial e atual zero no Balanço Patrimonial |
| CONSIDERAR_SALDO_ANTERIOR_LANCADO_EXERCICIO | char(1) |  |  | Considerar o sado anterior lançado no próprio exercício para os demonstrativos |
| EF_GERAL_GERAR_I050_PLANO_CONTAS | char(1) |  |  | Não gerar o registro I050 com o Plano de Contas |
| EF_GERAL_NUMERO_LIVRO | integer(4) |  |  | EF - Geral - Número do Livro |
| EF_GERAL_NOME_LIVRO | varchar(80) |  |  | EF - Geral - Nome do Livro |
| EF_ESCRITURACAO_PRINCIPAL_NUMERO_LIVRO | integer(4) |  |  | EF - Escrituração principal - Número |
| EF_ESCRITURACAO_PRINCIPAL_NOME | varchar(80) |  |  | EF - Escrituração principal - Nome |
| EF_ESCRITURACAO_PRINCIPAL_TIPO | integer(4) |  |  | EF - Escrituração principal - Tipo (0-Digital (Informado no SPED) / 1-Outros) |
| FORMA_CONTA_FOI_GERADA_PERIODO_ANTERIOR | integer(4) |  |  | Forma que as contas foram geradas no período anterior |
| GERAR_COEFICIENTE_ANALISE | char(1) |  |  | Gerar Coeficiente de análise |
| GERAR_BALANCO_RTF | char(1) |  |  | Gerar balanço patrimonial em RTF |
| GERAR_DRE_RTF | char(1) |  |  | Gerar DRE em RTF |
| PM_GERAL_NAO_GERAR_I050_PLANO_CONTAS | char(1) |  |  | Não gerar o registro I050 com o Plano de Contas |
| PM_GERAL_NUMERO_LIVRO | integer(4) |  |  | PM - Geral - Número do Livro |
| PM_GERAL_NOME_LIVRO | varchar(80) |  |  | PM - Geral - Nome do Livro |
| PM_ESCRITURACAO_PRINCIPAL_NUMERO_LIVRO | integer(4) |  |  | PM - Escrituração principal - Número |
| PM_ESCRITURACAO_PRINCIPAL_NOME | varchar(80) |  |  | PM - Escrituração principal - Nome |
| PM_ESCRITURACAO_PRINCIPAL_TIPO | integer(4) |  |  | PM - Escrituração principal - Tipo (0-Digital (Informado no SPED) / 1-Outros) |
| EF_SPED_CONTABIL_CR_CP_GERAR_I050_PLANO_CONTAS | char(1) |  |  | EF - SPED Contábil - Contas a pagar e receber - Não gerar o registro I050 com Plano de Contas |
| EF_SPED_CP_CR_NUMERO_LIVRO | integer(4) |  |  | EF - SPED Contábil - Contas a pagar e receber - Número do Livro |
| EF_SPED_CP_CR_NOME_LIVRO | varchar(80) |  |  | EF - SPED Contábil - Contas a pagar e receber - Nome do Livro |
| EF_ESCRITURACAO_PRINCIPAL_SPED_CP_CR_NUMERO_LIVRO | integer(4) |  |  | EF - Escrituração principal - SPED Contábil - Contas a pagar e receber - Número do Livro |
| EF_ESCRITURACAO_PRINCIPAL_SPED_CP_CR_NOME_LIVRO | varchar(80) |  |  | EF - Escrituração principal - SPED Contábil - Contas a pagar e receber - Nome do Livro |
| EF_ESCRITURACAO_PRINCIPAL_SPED_CP_CR_TIPO | integer(4) |  |  | EF - Escrituração principal - SPED Contábil - Tipo (0-Digital (Informado no SPED) / 1-Outros) |
| CT_ESCRITURACAO_PRINCIPAL_NUMERO_LIVRO | integer(4) |  |  | CT - Escrituração principal - Número |
| CT_ESCRITURACAO_PRINCIPAL_NOME | varchar(80) |  |  | CT - Escrituração principal - Nome |
| CT_ESCRITURACAO_PRINCIPAL_TIPO | integer(4) |  |  | CT - Escrituração principal - Tipo (0-Digital (Informado no SPED) / 1-Outros) |
| GERAR_CARTA_RESPONSABILIDADE_ADMINISTRACAO_RTF | char(1) |  |  | Gerar Carta de responsabilidade de administração em RTF |
| EF_GERAL_GERAR_I550_UNIDADES_VENDIDAS | char(1) |  |  | EF - Não gerar o registro I550 referente as unidades vendidas |
| GERAR_DEMONSTRACAO_CONTABIL_TRIMESTRE_SEM_MOVIMENTO | char(1) |  |  | Gerar as demonstrações contábeis para os trimestres sem movimento quando houver zeramento trimestral |
| TERMO_VERIFICACAO_SUBSTITUICAO_ECD | varchar(4096) |  |  | Termo de verificação para substituição da ECD |
| INFORMAR_PERIODO_SALDO_ANTERIOR_DRE | char(1) |  |  | Informar período do saldo anterior para o DRE(J150) |
| PERIODO_INICIAL_SALDO_ANTERIOR_DRE | date(4) |  | S | Período inicial do saldo anterior paa o DRE(J150) |
| PERIODO_FINAL_SALDO_ANTERIOR_DRE | date(4) |  | S | Período final do saldo anterior paa o DRE(J150) |
| NAO_GERAR_REGISTRO_0020_EMPRESAS_INATIVAS | char(1) |  |  | Não gerar no registro 0020 as empresas com situação inativa |
| GERAR_DSP_RTF | char(1) |  |  | Gerar DSP em RTF |
| PERIODO_INICIAL_CONSOLIDACAO | date(4) |  | S | Periodo inicial de consolidação nas demonstrações consolidadas |
| PERIODO_FINAL_CONSOLIDACAO | date(4) |  | S | Periodo final de consolidação nas demonstrações consolidadas |
| PARECER_AUDITORES | char(1) |  |  | Parecer dos Auditores |
| PARECER_AUDITORES_CAMINHO | char(4096) |  | S | Parecer dos Auditores - Caminho |
| MOTIVO_SUBSTITUICAO | integer(4) |  | S | Motivo de substituição (1=Mudanças de saldos das contas que não podem ser realizadas por meio de lançamentos extemporâneos/2=Alteração de assinatura/3=Alteração de demonstrações contábeis/4=Alteração da forma de escrituração contábil/5=Alteração do número |
| GERAR_DMPL_RTF | char(1) |  |  | Gerar relatório DMPL em RTF |
| GERAR_DLPA_RTF | char(1) |  |  | Gerar DLPA em RTF |
| ESCRITURACAO_CENTRALIZADA | integer(4) |  |  | Escrituração centralizada |
| MUDANCA_PLANO_CONTAS | integer(4) |  |  | Mudança no plano de contas |
| GERAR_DECLARACAO_CONFORMIDADE | char(1) |  | S | Gerar Declaração Conformidade |
