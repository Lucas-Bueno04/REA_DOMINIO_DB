# ctparmto — Parametros
1.441 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| masc_par | char(35) |  | S | Mascara contabil |
| lmas_par | char(1) |  | S | Informar a conta por (C=Codigo, M=Mascara) |
| mdia_par | char(1) |  | S | Permite mudar a data com diferenca DxC (S/N) |
| newp_par | char(1) |  | S | Avanca pagina na troca do grupo(balanco) (S/N) |
| mant_par | char(1) |  | S | Cursor em (D=Data, B=Deb, C=Cre, V=Valor, G=Cod.H, T=Hist.) |
| difl_par | numeric(12) |  | S | Nao usado |
| dila_par | date(4) |  | S | Data inicio dos lancamentos |
| nliv_par | integer(4) |  | S | Numero do livro |
| fpli_par | integer(4) |  | S | Folhas por livro |
| fini_par | integer(4) |  | S | Folha inicial |
| fian_par | integer(4) |  | S | Folha inicial |
| dinr_par | date(4) |  | S | Data inicial dos relatorios |
| dfir_par | date(4) |  | S | Data final dos relatorios |
| ccxa_par | integer(4) |  | S | Conta caixa |
| codi_emp | integer(4) | PK |  | Empresa |
| ctcx_par | tinyint(1) |  |  | Usar como (1=Fiscal, 2=Caixa, 3=Gerencial) |
| altl_par | char(1) |  | S | Altera lancamentos de outros sistemas |
| emat_par | char(1) |  | S | Centralizar a Contabilidade entre Matriz e Filiais (S/N) |
| codi_fil | integer(4) |  | S | Filial |
| togr_par | char(1) |  | S | Nao usado |
| masc_ger | char(35) |  | S | Mascara Gerencial |
| dini_par | date(4) |  | S | Data inicial do fechamento |
| dfin_par | date(4) |  | S | Data final do fechamento |
| lant_par | char(1) |  | S | Ação do período de trabalho (L=Livre, A=Avisar N=Não permitir) |
| codi_pad | integer(4) |  | S | Origem do Plano de Contas |
| comp_pad | char(1) |  | S | Compartilha plano de contas (S/N) |
| clasati_par | char(7) |  | S | Nao usado |
| claspas_par | char(7) |  | S | Nao usado |
| clasdes_par | char(7) |  | S | Nao usado |
| clasrec_par | char(7) |  | S | Nao usado |
| mandt_par | char(1) |  | S | Repete data(S/N) |
| mandb_par | char(1) |  | S | Mantem debito (S/N) |
| mancd_par | char(1) |  | S | Mantem credito (S/N) |
| manvl_par | char(1) |  | S | Mantem valor (S/N) |
| manch_par | char(1) |  | S | Mantem codigo historico (S/N) |
| manhi_par | char(1) |  | S | Mantem descricao do historico (S/N) |
| dre_par | char(1) |  | S | Usa DRE (S/N) |
| dlpa_par | char(1) |  | S | Usa DLPA (S/N) |
| doar_par | char(1) |  | S | Usa DOAR (S/N) |
| mostra_ger | char(1) |  | S | Mostrar tela do lancamento gerencial |
| ratf_par | char(1) |  | S | Rateio gerencial por filiais |
| rep_par | char(1) |  | S | Repetir dados no 1o lancamento |
| codi_emp_his | integer(4) |  | S | Origem dos Historicos |
| compart_his | char(1) |  | S | Compartilha historicos (S/N) |
| hist_obrig | char(1) |  | S | Digitacao obrigatoria de historicos |
| patl_par | integer(4) |  | S | Conta Patrimonio Liquido |
| zera_par | integer(4) |  | S | Conta destino |
| fili_par | char(1) |  | S | Informar o codigo da filial no lancamento (S/N) |
| faza_par | char(1) |  | S | Transferir automaticamente o resultado para o Patrimonio Liquido |
| lucr_par | integer(4) |  | S | Conta Lucro do Periodo |
| prej_par | integer(4) |  | S | Conta Prejuizo do Periodo |
| controldife_par | char(1) |  |  | Controle de Diferenca por (U=Usuario, E=Empresa |
| masc_rel | char(35) |  |  | Mascara p/ relatorios |
| infcx_par | char(1) |  |  | Informar a conta caixa no lancamento (S/N) |
| permzero_par | char(1) |  | S | Permite gravar lancamentos com valor zero (S/N) |
| ccusto_par | char(1) |  |  | Contabilidade por centro de custo (S/N) |
| ratcf_par | char(1) |  |  | Rateio de centro de custo por filial (S/N) |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| domcli_par | char(1) |  |  | Utiliza Dominio Cliente (S=Sim/N=Nao) |
| permcta_par | char(1) |  |  | Permite cadastrar contas (S=Sim/N=Nao) |
| inicta_par | integer(4) |  |  | Numero da conta inicial |
| fimcta_par | integer(4) |  |  | Numero da conta final |
| permhis_par | char(1) |  |  | Permite cadastrar historicos (S=Sim/N=Nao) |
| inihis_par | integer(4) |  |  | Numero do historico inicial |
| fimhis_par | integer(4) |  |  | Numero do historico final |
| consolidar_par | char(1) |  |  | Consolidar relatorios entre Empresas sem vinculo Matriz e Filiais (S/N) |
| posicao_data_par | char(1) |  |  | Mostrar posicao por data (S/N) |
| dmpl_par | char(1) |  |  | Usa DMPL (S/N) |
| orcamentaria_par | char(1) |  |  | Contabilidade orcamentaria (S/N) |
| sped_par | char(1) |  |  | Gera informacoes SPED (S/N) |
| dva_par | char(1) |  |  | Usa DVA (S/N) |
| masc_dva | char(35) |  |  | Mascara DVA |
| PLANO_REFERENCIAL_PAR | char(1) |  |  | Plano de contas referencial(R=Receita Federal/C=Banco Central(Cosif)) |
| repete_conta_par | char(1) |  |  | GRepetir conta a cada partida de lancamentos (S/N) |
| repete_valor_par | char(1) |  |  | Repetir valor a cada partida de lancamentos (S/N) |
| repete_codigo_historico_par | char(1) |  |  | Repetir codigo historico a cada partida de lancamentos (S/N) |
| repete_historico_par | char(1) |  |  | Repetir historico a cada partida de lancamentos (S/N) |
| DFC_PAR | char(1) |  |  | Usa DFC (S/N) |
| MOSTRA_DFC_PAR | char(1) |  |  | Mostra tela do fluxo de caixa (S/N) |
| METODO_DFC_PAR | char(1) |  |  | Metodo de calculo (D=Direto/I=Indireto) |
| MASC_CTA_OLD | char(35) |  | S | Mascara contabil antiga |
| MASC_REL_OLD | char(35) |  | S | Mascara do relatorio antiga |
| MASC_CTA_NEW | char(35) |  | S | Mascara contabil nova |
| MASC_REL_NEW | char(35) |  | S | Mascara do relatorio nova |
| I_PLANOCONTAS | integer(4) |  |  | Codigo do plano de contas (1-Antigo/2-Novo) |
| OUTROS_IDIOMAS_PAR | char(1) |  |  | Emite relatorios em outros idiomas (S/N) |
| INFORMA_LOCALIZADOR_PAR | char(1) |  |  | Informar localizador na tela de lanCamentos(S/N) |
| MANTEM_LOCALIZADOR_PAR | char(1) |  |  | Mantém o localizador(S/N) |
| FORMA_ESCRITURACAO_PAR | char(1) |  |  | Forma de escrituração contábil(G - Diário Completo/R - Diário com escrituração resumida/B - Balancetes diários e balanços) |
| NOME_LDC_PAR | char(80) |  |  | Nome (Livro diário completo) |
| NOME_LDER_PAR | char(80) |  |  | Nome (Livro diário escrituração resumida) |
| NOME_LBDB_PAR | char(80) |  |  | Nome (Livro balancetes diários e balanços) |
| GERA_FCONT_PAR | char(1) |  |  | Gera informativo FCONT (S/N) |
| DRA_PAR | char(1) |  |  | Usa DRA (S/N) |
| GERA_PROBAN_PAR | char(1) |  |  | Gera informativo PROBAN (S/N) |
| GERA_ARQUIVO_BANCO_CENTRAL_PAR | char(1) |  |  | Arquivos para o Banco Central (S/N) |
| CONSIDERAR_CONCILIADO_LANCTO_PAR | char(1) |  |  | Considerar como conciliado os lançamentos com as seguintes origens (S/N) |
| CONCILIAR_ZERAMENTO_PAR | char(1) |  |  | Considerar como conciliado zeramento (S/N) |
| CONCILIAR_TRANSFERENCIA_LP_PAR | char(1) |  |  | Considerar como conciliado transferência lucro/prejuízo (S/N) |
| CONCILIAR_PATRIMONIO_PAR | char(1) |  |  | Considerar como conciliado Patrimônio (S/N) |
| CONCILIAR_FOLHA_PAR | char(1) |  |  | Considerar como conciliado Folha da Pagamento (S/N) |
| CONCILIAR_HONORARIOS_PAR | char(1) |  |  | Considerar como conciliado Honorários (S/N) |
| CONCILIAR_DOMINIO_CLIENTE_PAR | char(1) |  |  | Considerar como conciliado Domínio Cliente (S/N) |
| CONCILIAR_ESCRITA_FISCAL_PAR | char(1) |  |  | Considerar como conciliado Escrita Fiscal (S/N) |
| CONCILIAR_EFI_ACUMULADOR_PAR | char(1) |  |  | Considerar como conciliado acumuladores Escrita Fiscal (S/N) |
| CONCILIAR_EFI_AJUSTE_PIS_COFINS_PAR | char(1) |  |  | Considerar como conciliado ajustes PIS e COFINS (S/N) |
| CONCILIAR_EFI_AJUSTE_EFI_PAR | char(1) |  |  | Considerar como conciliado ajustes Escrita Fiscal (S/N) |
| CONCILIAR_EFI_AJUSTE_ESTOQUE_PAR | char(1) |  |  | Considerar como conciliado ajustes Estoque Substituição Tributária (S/N) |
| CONCILIAR_EFI_APURACAO_PAR | char(1) |  |  | Considerar como conciliado apuração Escrita Fiscal (S/N) |
| CONCILIAR_EFI_BILHETE_PAR | char(1) |  |  | Considerar como conciliado Bilhete de Passagem (S/N) |
| CONCILIAR_EFI_BILHETE_Z_PAR | char(1) |  |  | Considerar como conciliado Bilhete de Passagem - Redução Z (S/N) |
| CONCILIAR_EFI_BILHETE_DIARIO_PAR | char(1) |  |  | Considerar como conciliado Bilhete de Passagem - Resumo de Movimentação Diária (S/N) |
| CONCILIAR_EFI_CREDITO_PIS_COFINS_IMOBILIZADO_PAR | char(1) |  |  | Considerar como conciliado crédito PIS e COFINS imobilizado (S/N) |
| CONCILIAR_EFI_CUSTO_INCORRIDO_PAR | char(1) |  |  | Considerar como conciliado custo incorrido (S/N) |
| CONCILIAR_EFI_CUSTO_ORCADO_PAR | char(1) |  |  | Considerar como conciliado custo orçado (S/N) |
| CONCILIAR_EFI_ENTRADA_PAR | char(1) |  |  | Considerar como conciliado entradas Escrita Fiscal (S/N) |
| CONCILIAR_EFI_PAGAMENTO_GUIA_PAR | char(1) |  |  | Considerar como conciliado pagamento guia Escrita Fiscal (S/N) |
| CONCILIAR_EFI_RECEBIMENTO_ECF_PAR | char(1) |  |  | Considerar como conciliado recebimentos ECF (S/N) |
| CONCILIAR_EFI_REDUCAO_Z_PAR | char(1) |  |  | Considerar como conciliado reduções Z (S/N) |
| CONCILIAR_EFI_SAIDA_PAR | char(1) |  |  | Considerar como conciliado saídas Escrita Fiscal (S/N) |
| CONCILIAR_EFI_SALDO_PIS_COFINS_PAR | char(1) |  |  | Considerar como conciliado saldo estoque PIS e COFINS (S/N) |
| CONCILIAR_EFI_SERVICO_PAR | char(1) |  |  | Considerar como conciliado serviços Escrita Fiscal (S/N) |
| CONCILIAR_EFI_VENDA_IMOBILIARIA_PAR | char(1) |  |  | Considerar como conciliado venda unidade imobiliária (S/N) |
| CONCILIAR_NOVA_ORIGEM_LANCTO_PAR | char(1) |  |  | Sempre considerar como conciliado as novas origens de lançamentos (S/N) |
| GERA_BALANCETE_ANEEL_PAR | char(1) |  |  | Gera balancete ANEEL (S/N) |
| CONCILIAR_NAO_AUTOMATICAMENTE_PAR | char(1) |  |  | Não conciliar automaticamente as contrapartidas de lançamentos (S/N) |
| CONCILIAR_EFI_DED_RESTITUICAO_PIS_COFINS_PAR | char(1) |  |  | Considerar como conciliado dedução de restituição PIS/COFINS (S/N) |
| INCORPORACAO_IMOBILIARIA_RET_PAR | char(1) |  |  | Incorporação Imobiliária optante pelo RET (S/N) |
| PERMITIR_GRAVAR_LANCAMENTO_DIFERENCA_PAR | char(1) |  |  | Permitir gravar lançamento com diferença de Débito x Crédito (S/N) |
| CONCILIAR_EFI_DEV_UNID_IMOBILIARIA_PAR | char(1) |  |  | Considerar como conciliado Devolu? Unidade Imobili?a (S/N) |
| DECLARACAO_VERACIDADE1_PAR | varchar(512) |  | S | Declaração da assinatura 1 |
| DECLARACAO_VERACIDADE2_PAR | varchar(512) |  | S | Declaração da assinatura 2 |
| DEMONSTRAR_CLASSIFICACAO_LANCAMENTO_PAR | char(1) |  |  | Demonstrar a classificação contábil na tela de lançamentos (S/N) |
| DSP_PAR | char(1) |  |  | Usa DSP (S/N) |
| CONCILIAR_EXTRATO_BANCARIO_PAR | char(1) |  |  | Considerar como conciliado extrato bancário (S/N) |
| SOCIEDADE_EM_CONTA_PARTICIPACAO_PAR | char(1) |  |  | Possui Sociedade em Conta Participação - SCP (S/N) |
| INICIO_CCU_PAR | date(4) |  | S | Contabilidade por Centro de Custo a partir de |
| I_OLE_CARTA_RESPONSABILIDADE | integer(4) |  | S | Código do modelo ole para carta de responsabilidade de administração |
| CARNE_LEAO_PAR | char(1) |  |  | Identificar rendimentos e deduções para o carnê Leão (S/N) |
| DEMONSTRAR_SALDO_TELA_LANCTO_PAR | char(1) |  |  | Demonstrar o saldo das contas na tela de lançamentos (S/N) |
| EXIBIR_DIFERENCA_LOTE_PAR | char(1) |  |  | Exibir lotes com diferença de débito e crédito (S/N) |
| BALANCETE_COFI_4010_CVM_PAR | char(1) |  |  | Balancete COFI 4010 para a CVM (S/N) |
| CONTA_CMV_PAR | integer(4) |  |  | Conta CMV |
| HISTORICO_CMV_PAR | integer(4) |  |  | Histórico CMV |
| FECHAMENTO_DATA | date(4) |  | S | Data do fechamento |
| PERIODO_TRABALHO_POR_USUARIO_PAR | char(1) |  |  | Definir permissão de lançamentos em data diferente por usuário (S/N) |
| BLOQUEAR_INTEGRACAO_PERIODO_TRABALHO_PAR | char(1) |  |  | Bloquear a integração de lançamentos dos seguintes módulos no período de trabalho (S/N) |
| BLOQUEAR_LANCTO_ESCRITA_PAR | char(1) |  |  | Bloquear o módulo Escrita Fiscal (S/N) |
| BLOQUEAR_LANCTO_FOLHA_PAR | char(1) |  |  | Bloquear o módulo Folha de Pagamento (S/N) |
| BLOQUEAR_LANCTO_PATRIMONIO_PAR | char(1) |  |  | Bloquear o módulo Patrimônio (S/N) |
| BLOQUEAR_LANCTO_HONORARIOS_PAR | char(1) |  |  | Bloquear o módulo Honorários (S/N) |
| BLOQUEAR_LANCTO_ATUALIZAR_PAR | char(1) |  |  | Bloquear o módulo Atualizar (S/N) |
| BLOQUEAR_LANCTO_CLIENTE_PAR | char(1) |  |  | Bloquear o módulo Domínio Cliente (S/N) |
| PERMITIR_CADASTRAR_MESMA_CLASSIFICACAO_PAR | char(1) |  |  | Permitir cadastrar contas analíticas com a mesma classificação (S/N) |
| DEFINIR_GRUPO_MESMA_CLASSIFICACAO_PAR | char(1) |  |  | Definir grupos de contas sintéticas que poderão ter contas analíticas cadastradas com a mesma classificação (S/N) |
| TRANSFERIR_ZER_LUCRO_PREJUIZO_PAR | char(1) |  |  | Transferir automaticamente o resultado para a conta de Lucro ou Prejuízo Acumulado (S/N) |
| CONTA_LUCRO_ACUMULADO_PAR | integer(4) |  |  | Conta Lucro Acumulado |
| CONTA_PREJUIZO_ACUMULADO_PAR | integer(4) |  |  | Conta Prejuízo Acumulado |
| EBITDA_PAR | char(1) |  |  | EBITDA/LAJIDA (S/N) |
| PERMITIR_ALTERAR_NUMERO_LOTE_LANCTO_PAR | char(1) |  |  | Permitir alterar o número do lote nos lançamentos |
| CONCILIAR_LALUR_PAR | char(1) |  |  | Considerar como conciliado Lalur (S/N) |
| GERA_SPED_ECF_PAR | char(1) |  |  | Gera SPED ECF (S/N) |
| PLANO_REFERENCIAL_SPED_ECF_PAR | integer(4) |  |  | COLUNA NÃO UTILIZADA |
| ASSINATURA_PESSOA_JURIDICA_SPED_ECF_PAR | char(1) |  |  | ASSINATURA DA PESSOA JURÍDICA (R-GERAR COM OS DADOS DO RESPONSÁVEL LEGAL/ SÓCIO / E-GERAR COM OS DADOS DA EMPRESA / C-GERAR COM OS DADOS DO CONTADOR - PROCURAÇÃO ELETRÔNICA) |
| QUALIFICACAO_ASSINANTE_SPED_ECF_PAR | integer(4) |  |  | Qualificação do assinante |
| INSCRICAO_ASSINANTE_PROCURACAO_ELETRONICA | integer(4) |  |  | Inscrição do Assinante da Procuração eletrônica |
| ARQUIVO_PRESTACAO_CONTA_PARTIDO_POLITICO | char(1) |  |  | Arquivos de prestação de contas partidos políticos |
| POSSUI_RELACIONAMENTO_PF_PJ_PARTICIPANTE_SPED_PAR | char(1) |  |  | Possui relacionamento com pessoas físicas e jurídicas consideradas participantes no SPED Contábil (S/N) |
| ARQUIVO_ESFINGE_TCE_SC | char(1) |  |  | Arquivos e-Sfinge - TCE/SC |
| DEMONSTRAR_SALDO_CONTA_TELA_CONCILIACAO | char(1) |  |  | Demonstrar o saldo da conta na tela de conciliação |
| NOME_ASSINANTE_SPED_ECF_PAR | varchar(120) |  |  | Signatários SPED ECF - Nome do assinante |
| TIPO_INSCRICAO_ASSINANTE_SPED_ECF_PAR | integer(4) |  |  | Signatários SPED ECF - Tipo de inscrição do assinante (1 - CNPJ / 2 - CPF) |
| INSCRICAO_ASSINANTE_SPED_ECF_PAR | varchar(14) |  |  | Signatários SPED ECF - Inscrição do assinante |
| QUALIFICACAO_DADO_ASSINANTE_SPED_ECF_PAR | integer(4) |  |  | Signatários SPED ECF - Qualificação do assinante |
| EMAIL_ASSINANTE_SPED_ECF_PAR | varchar(60) |  |  | Signatários SPED ECF - Email do assinante |
| TELEFONE_ASSINANTE_SPED_ECF_PAR | varchar(14) |  |  | Signatários SPED ECF - Telefone do assinante |
| PERMITIR_CONCILIAR_CONTA_SEM_CONCILIAR_LANCAMENTO | char(1) |  |  | Permitir conciliar as contas contábeis sem realizar a conciliação dos lançamentos contábeis |
| ASSINATURA_PESSOA_FISICA_SPED_CONTABIL_PAR | char(1) |  |  | Signatários SPED Contábil - Assinatura da Pessoa Física (R-Gerar com os dados do Responsável Legal / C-Gerar com os dados do Contador - Procuração) |
| QUALIFICACAO_ASSINANTE_SPED_CONTABIL_PAR | integer(4) |  |  | Signatários SPED Contábil - Qualificação do assinante |
| PLANO_REFERENCIAL_BANCO_CENTRAL_PAR | char(1) |  |  | Arquivo para o Banco Central - Tipo da Empresa |
| ARQUIVO_DIOPS_FINANCEIRO_ANS_PAR | char(1) |  |  | Arquivo DIOPS Financeiro - ANS |
| DIOPS_REGISTRO_ANS_PAR | integer(4) |  |  | DIOPS - Registro na ANS |
| DIOPS_SENHA_PAR | varchar(20) |  |  | DIOPS - Senha |
| DIOPS_MODALIDADE_PAR | varchar(5) |  |  | DIOPS - Modalidade |
| DIOPS_SEGMENTACAO_PAR | varchar(5) |  |  | DIOPS - Segmentação |
| ASSINATURA_PESSOA_JURIDICA_SPED_CONTABIL_PAR | char(1) |  |  | SIGNATÁRIOS SPED CONTÁBIL - ASSINATURA DA PESSOA JURÍDICA (E-GERAR COM OS DADOS DA EMPRESA / A-INFORMAR DADOS DO ASSINANTE / N-NÃO GERAR) |
| NOME_ASSINANTE_SPED_CONTABIL_PAR | varchar(120) |  |  | Signatários SPED Contábil - Nome da Pessoa Jurídica |
| EMAIL_ASSINANTE_SPED_CONTABIL_PAR | varchar(60) |  |  | Signatários SPED Contábil - Email da Pessoa Jurídica |
| TELEFONE_ASSINANTE_SPED_CONTABIL_PAR | varchar(14) |  |  | Signatários SPED Contábil - Telefone da Pessoa Jurídica |
| GERAR_ASSINATURA_CONTADOR_COMO_PROCURADOR_SPED_CONTABIL_PAR | char(1) |  |  | Gerar a assinatura do Contador como Procurador como responsável legal da empresa junto as bases da RFB |
| GERAR_ASSINATURA_PESSOA_JURIDICA_COMO_RESPONSAVEL_SPED_CONTABIL_PAR | char(1) |  |  | Gerar a assinatura da Pessoa Jurídica como responsável legal da empresa junto as bases da RFB |
| CNPJ_ASSINANTE_SPED_CONTABIL_PAR | varchar(14) |  |  | Signatários SPED Contábil - CNPJ da Pessoa Jurídica |
| CONTA_CPV_PAR | integer(4) |  |  | Conta CPV |
| HISTORICO_CPV_PAR | integer(4) |  |  | Hirtórico CPV |
| CONCILIAR_ONBALANCE_PAR | char(1) |  |  | Considerar como conciliado OnBalance (S/N) |
| NAO_GERAR_ASSINATURA_CONTADOR_IMUNE_ISENTA_PAR | char(1) |  |  | Não gerar assinatura do contador/empresa imune ou isenta sem obrigatoriedade de entrega da ECD |
| ESFINGE_USUARIO_PAR | varchar(20) |  |  | E-Sfinge - Usuário |
| ESFINGE_SENHA_PAR | varchar(20) |  |  | E-Sfinge - Senha |
| ESFINGE_CODIGO_UNIDADE_GESTORA_PAR | varchar(20) |  |  | E-Sfinge - Código da unidade gestora |
| DEMONSTRAR_SALDO_CONTA_TELA_CONCILIACAO_TIPO | char(1) |  |  | Demonstrar o saldo da conta na tela de conciliação tipo |
| PERMITIR_GRAVAR_LANCAMENTOS_DEBITO_CREDITO_IGUAIS | char(1) |  |  | Permitir gravar lancamentos com a mesma conta a débito e a crédito(S/N). |
| EMPRESA_CONTROLADORA_OBRIGADA_DEMONSTRACOES_CONTABEIS_BLOCO_K | char(1) |  |  | Empresa controladora obriga demonstrações contabeis bloco K. |
| LIVRO_CAIXA_PROD_RURAL | char(1) |  |  | Emitir Livro Caixa Digital do Produtor Rural - LCDPR |
| LIVRO_CAIXA_PROD_RURAL_SELEC_IMOVEL_PADRAO | char(1) |  |  | Selecionar Imóvel Rural padrão no lançamento |
| LIVRO_CAIXA_PROD_RURAL_IMOVEL_PADRAO | integer(4) |  | S | Imóvel padrão |
| LIVRO_CAIXA_PROD_RURAL_SELEC_PARTICIPANTE_PADRAO | char(1) |  |  | Selecionar Participante da Atividade Rural padrão no lançamento |
| LIVRO_CAIXA_PROD_RURAL_PARTICIPANTE_PADRAO | integer(4) |  | S | Participante padrão |
| LIVRO_CAIXA_PROD_RURAL_GERAR_ARQUIVO_RATEADO | char(1) |  |  | Emitir Livro Caixa Digital do Produtor Rural rateado |
| HOUVE_ALTERACAO_CODIGO_AGLUTINACAO_ESTRUTURA_REGISTRO_J150 | char(1) |  |  | Houve alteraÃ§Ã£o dos cÃ³digos de aglutinaÃ§Ã£o da estrutura do registro J150(S/N) |
| MANTEM_LCDPR_TP_LACNTO | char(1) |  |  | Mantém lançamento do campo "Tipo de Lançamento" |
| MANTEM_LCDPR_DOCUMENTO | char(1) |  |  | Mantém lançamento do campo "Tipo de Documento" |
| MANTEM_LCDPR_NR_DOCUMENTO | char(1) |  |  | Mantém lançamento do campo "Nº Documento" |
| MANTEM_LCDPR_PARTICIPANTE | char(1) |  |  | Mantém lançamento do campo "Participante" |
| MANTEM_LCDPR_IMOVEL_RURAL | char(1) |  |  | Mantém lançamento do grupo "Lançamentos por imóvel rural" |
| COMPENSAR_AUTOMATICAMENTE_LUCRO_PREJUIZO | char(1) |  | S | Compensar automaticamente contas de lucro/prejuízo no zeramento (S/N) |
| ICEBERG_NAO_CONTABILIZAR_AUTOMATICAMENTE | char(1) |  | S | Não contabilizar automaticamente contas ICEBERG |
| ICEBERG_CONTA_CONTABIL_PESSOA_FISICA | integer(4) |  | S | Conta contabil para transações a pessoa fisica |
| ICEBERG_CADASTRAR_AUTOMATICAMENTE_CLIENTE_FORNECEDOR | char(1) |  | S | Cadastrar automaticamente clientes e fornecedores quando não encontrado na escrita |
| ICEBERG_REALIZAR_BAIXA_AUTOMATICA_PAGAMENTOS_ESCRITA | char(1) |  | S | Realizar o pagamentos de forma automatica na escrita |
| ICEBERG_REALIZAR_BAIXA_AUTOMATICA_RECEBIMENTOS_ESCRITA | char(1) |  | S | Realizar o recebimento de forma automatica na escrita |
| ICEBERG_REALIZAR_BAIXA_AUTOMATICA_IMPOSTOS | char(1) |  | S | Realizar a baixa forma automatica de impostos na escrita fiscal, folha e lalur |
| I_OLE_CARTA_APRESENTACAO | integer(4) |  | S | Código do modelo ole para carta de apresentação |
| I_OLE_RELATORIO_ADMINISTRACAO | integer(4) |  | S | Código do modelo ole para relatório de administração |
| I_OLE_RELATORIO_AUDITORIA | integer(4) |  | S | Código do modelo ole para relatório de auditoria |
| IMPORTACAO_API_CONTAS_CONTABEIS | char(1) |  |  | Importar Contas Contábeis |
| IMPORTACAO_API_CADASTRO_HISTORICO | char(1) |  |  | Importar cadastro histórico |
| IMPORTACAO_API_SOBRESCREVER_CADASTROS | char(1) |  |  | Sobrescrever registros existentes |
| IMPORTACAO_API_NOTIFICAR_SOBRE_NOVOS_LANCAMENTOS | char(1) |  |  | Notificar sobre novos lançamentos contábeis a importar |
| IMPORTACAO_API_NOTIFICAR_POR_QUANTIDADE_LANCAMENTOS | char(1) |  |  | Notificar por quantidade de lançamentos contábeis |
| IMPORTACAO_API_NOTIFICAR_POR_PERIODO | char(1) |  |  | Notificar por período |
| IMPORTACAO_API_QUANTIDADE_LANCAMENTOS_AVISAR | integer(4) |  | S | Quantidade de novos lançamentos contabeis para avisar |
| IMPORTACAO_API_QUANTIDADE_DIAS_AVISAR | integer(4) |  | S | Quantidade de dia(s) para avisar |
| DISTRIBUICAO_LUCRO_AUTOMATICO | char(1) |  | S | N - NAO / S - SIM |
| IMPORTACAO_PLANO_CONTAS_CONTA_AZUL | char(1) |  |  | Importar Plano de Contas para Conta Azul |
| OCUPACAO_PADRAO_CARNE_LEAO | integer(4) |  | S | Ocupação |
| USUARIO_BACEN_ENVIO | varchar(50) |  | S | BACEN - Usuário |
| SENHA_BACEN_ENVIO | varchar(50) |  | S | BACEN - Senha |
| GERAR_CONTAS_CONTABEIS_POR | integer(4) |  | S | Gerar as contas contábeis por |
| PERMITIR_CONCILIACAO_FORA_PERIODO_TRABALHO | char(1) |  | S | Permitir conciliar e desconciliar os lançamentos contábeis fora do período de trabalho |
| COMPENSAR_AUTOM_LUCRO_PREJUIZO_FILIAS | char(1) |  | S | Compensar automaticamente contas de lucro/prejuízo entre Matriz e Filial no zeramento (S/N) |
| UTILIZAR_MENOR_CODIGO_CADASTRO_CONTAS | char(1) |  | S | Indica se o sistema deve utilizar o meno codigo para cadastrar a conta |
| ICEBERG_DIA_AGUARDANDO_NF | smallint(2) |  |  | Dias em que o pagamento poderá ficar como Aguardando NF |
| LOCAL_ARQUIVOS_TRASMITIDOS | varchar(256) |  |  | Armazenar os arquivos transmitidos em |
| GERA_DERE_PAR | char(1) |  |  | Gera a Declaracao de Regimes Especificos - DeRE |
