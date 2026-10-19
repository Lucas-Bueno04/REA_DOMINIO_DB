# GEPERFIL_EMPRESA_MODULO — Perfis de Empresas - Módulos
119 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| I_PERFIL_EMPRESA | integer(4) | PK |  | Sequencial do perfil |
| I_MODULO | integer(4) | PK |  | Sequencial do módulo |
| CONFIGURAR | char(1) |  |  | Configurar (S/N) |
| CODI_EMP | integer(4) |  | S | Empresa |
| EF_PARAMETRO | char(1) |  |  | EF - Parâmetros |
| EF_HISTORICO_PADRAO | char(1) |  |  | EF - Históricos padrões |
| EF_PLANO_CONTA | char(1) |  |  | EF - Plano de contas |
| EF_IMPOSTO_AJUSTE | char(1) |  |  | EF - Impostos e ajustes |
| EF_ACUMULADOR | char(1) |  |  | EF - Acumuladores |
| EF_FORNECEDOR | char(1) |  |  | EF - Fornecedores |
| EF_CLIENTE | char(1) |  |  | EF - Clientes |
| EF_REMETENTE_DESTINATARIO | char(1) |  |  | EF - Remetentes/Destinatários |
| EF_GRUPO_PRODUTO | char(1) |  |  | EF - Grupos de produtos |
| EF_PRODUTO | char(1) |  |  | EF - Produtos |
| EF_OBSERVACAO | char(1) |  |  | EF - Observações |
| EF_CONFIGURACAO_REDUCAO_Z | char(1) |  |  | EF - Configuração de Reduções Z |
| EF_CONFIGURACAO_IMPORTACAO_NFE_PORTAL | char(1) |  |  | EF - Configuração de Importação de NF-e do Portal |
| EF_CONFIGURACAO_IMPORTACAO_NFE_ARQUIVO_XML | char(1) |  |  | EF - Configuração de Importação de NF-e Arquivo XML |
| EF_CONFIGURACAO_IMPORTACAO_NFCE_ARQUIVO_XML | char(1) |  |  | EF - Configuração de Importação de NFC-e Arquivo XML |
| EF_CONFIGURACAO_IMPORTACAO_CTE_PORTAL | char(1) |  |  | EF - Configuração de Importação de CT-e do Portal |
| EF_CONFIGURACAO_IMPORTACAO_CTE_ARQUIVO_XML | char(1) |  |  | EF - Configuração de Importação de CT-e Arquivo XML |
| EF_CONFIGURACAO_IMPORTACAO_SPED_FISCAL | char(1) |  |  | EF - Configuração de Importação do SPED Fiscal |
| EF_CONFIGURACAO_IMPORTACAO_ATO_COTEPE | char(1) |  |  | EF - Configuração de Importação do Ato Cotepe 17/04 - CAT 52 |
| FO_PARAMETRO | char(1) |  |  | FO - Parâmetros |
| FO_CARGO | char(1) |  |  | FO - Cargos |
| FO_DEPARTAMENTO | char(1) |  |  | FO - Departamentos |
| FO_CENTRO_CUSTO | char(1) |  |  | FO - Centros de custos |
| FO_HORARIO | char(1) |  |  | FO - Horários |
| FO_JORNADA | char(1) |  |  | FO - Jornadas |
| CT_PARAMETRO | char(1) |  |  | CT - Parâmetros |
| CT_HISTORICO | char(1) |  |  | CT - Históricos |
| CT_CONTA_CONTABIL | char(1) |  |  | CT - Contas Contábeis |
| CT_NATUREZA_CONTA | char(1) |  |  | CT - Natureza das contas |
| CT_ZERAMENTO | char(1) |  |  | CT - Zeramento |
| CT_LIVRO_CAIXA | char(1) |  |  | CT - Livro Caixa |
| CT_ESTRUTURA_DRE | char(1) |  |  | CT - Estrutura do DRE |
| CT_ESTRUTURA_DRA | char(1) |  |  | CT - Estrutura do DRA |
| CT_ESTRUTURA_DVA | char(1) |  |  | CT - Estrutura do DVA |
| CT_ESTRUTURA_DLPA | char(1) |  |  | CT - Estrutura do DLPA |
| CT_ESTRUTURA_DOAR | char(1) |  |  | CT - Estrutura do DOAR |
| CT_ESTRUTURA_DMPL | char(1) |  |  | CT - Estrutura do DMPL |
| CT_ESTRUTURA_DFC | char(1) |  |  | CT - Estrutura do DFC |
| CT_ESTRUTURA_DSP | char(1) |  |  | CT - Estrutura do DSP |
| CT_ESTRUTURA_EBITDA_LAJIDA | char(1) |  |  | CT - Estrutura do EBITDA/LAJIDA |
| CT_PLANO_REFERENCIAL_SPED | char(1) |  |  | CT - Plano Referencial SPED |
| CT_PLANO_REFERENCIAL_SPED_ECF | char(1) |  |  | CT - Plano Referencial SPED ECF |
| CT_PLANO_REFERENCIAL_ANEEL | char(1) |  |  | CT - Plano Referencial ANEEL |
| CT_PLANO_REFERENCIAL_COFI | char(1) |  |  | CT - Plano Referencial COFI |
| CT_PLANO_OUTRO_IDIOMA | char(1) |  |  | CT - Outros Idiomas |
| CT_CONTA_GERENCIAL | char(1) |  |  | CT - Contas Gerenciais |
| CT_RATEIO_GERENCIAL | char(1) |  |  | CT - Rateio Gerencial |
| CT_DEPARTAMENTO | char(1) |  |  | CT - Departamento |
| CT_CENTRO_CUSTO | char(1) |  |  | CT - Centros de Custos |
| CT_RATEIO_CENTRO_CUSTO | char(1) |  |  | CT - Rateio Centro de Custo |
| PM_GRUPO_CONTABIL | char(1) |  |  | PM - Grupos contábeis |
| PM_CONTA_PATRIMONIAL | char(1) |  |  | PM - Contas patrimoniais |
| PM_DEPARTAMENTO | char(1) |  |  | PM - Departamentos |
| PM_CENTRO_CUSTO | char(1) |  |  | PM - Centros de custos |
| HR_CLIENTE | char(1) |  |  | HR - Clientes |
| HR_FORNECEDOR | char(1) |  |  | HR - Fornecedores |
| HR_IMPOSTO | char(1) |  |  | HR - Impostos |
| HR_TIPO_CONTRATO | char(1) |  |  | HR - Tipo de contrato |
| HR_HISTORICO | char(1) |  |  | HR - Históricos |
| HR_COMPLEMENTO_HISTORICO_CONTABIL | char(1) |  |  | HR - Complemento de históricos contábeis |
| HR_CATEGORIA_PAGAR | char(1) |  |  | HR - Categorias de contas a pagar |
| HR_CATEGORIA_RECEBER | char(1) |  |  | HR - Categorias de contas a receber |
| HR_EVENTO | char(1) |  |  | HR - Eventos |
| AT_IMPOSTO_AJUSTE | char(1) |  |  | AT - Impostos e Ajustes |
| LR_ADICAO | char(1) |  |  | LR - Adições |
| LR_EXCLUSAO | char(1) |  |  | LR - Exclusões |
| LR_OPERACAO_RECEITA | char(1) |  |  | LR - Operações de receita |
| LR_GANHO | char(1) |  |  | LR - Ganhos |
| EF_CONFIGURACAO_IMPORTACAO_NFSE_ARQUIVO_XML_ABRASF | char(1) |  |  | EF - Configuração de Importação de NFS-e Arquivo XML - ABRASF |
| EF_CONFIGURACAO_IMPORTACAO_CFE_ARQUIVO_XML | char(1) |  |  | EF - Configuração de Importação de CF-e Arquivo XML |
| CT_GRUPO_CONTA_SUCONTA | char(1) |  |  | CT - Grupos de Contas-Subcontas |
| CT_SUBCONTA_CORRELATA | char(1) |  |  | CT - Subcontas correlatas |
| CT_PLANO_REFERENCIAL_BANCO_CENTRAL | char(1) |  |  | CT - Plano Referencial Banco Central |
| CT_PLANO_REFERENCIAL_ANS | char(1) |  |  | CT - Plano Referencial ANS |
| CT_CONTA_REFERENCIAL_DIOPS | char(1) |  |  | CT - Contas Referenciais DIOPs |
| EF_CONFIGURACAO_IMPORTACAO_SINTEGRA | char(1) |  |  | EF - Configuração de Importação do Sintegra |
| EF_CONFIGURACAO_IMPORTACAO_ONBALANCE | char(1) |  |  | EF - Configuração de Importação do OnBalance |
| CT_PLANO_REFERENCIAL_SUSEP | char(1) |  |  | CT - Plano Referencial SUSEP |
