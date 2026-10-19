# EFPARAMETRO — Paramentros - Cadastro - Escrita Fiscal
1.434 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| PERI_PAR | date(4) |  |  | Periodo atual |
| PINI_PAR | date(4) |  |  | Periodo inicial |
| DIPI_PAR | integer(4) |  | S | Gerar movimento de produtos no SINTEGRA (1 - Sim/2 - Nao) |
| ESTO_PAR | integer(4) |  | S | Faz controle de estoque (1 - Sim/2 - Nao) |
| LFOR_PAR | integer(4) |  | S | Lancamento de fornecedor por (1 - Codigo/2 - Nome/3 - CNPJ) |
| LCLI_PAR | integer(4) |  | S | Lancamento de cliente por (1 - Codigo/2 - Nome/3 - CNPJ) |
| CPOSEG_PAR | integer(4) |  | S | Campo da proxima nota segmentada (1 - Natureza/2 - Acumulador/3 - Valor Contabil) |
| DEFLAN_PAR | integer(4) |  | S | Campo default para notas com diferenca entre valor contabil e bases ICMS e IPI (1 - Sim/2 - Nao) |
| DIGECF_PAR | char(1) |  | S | Gerar informacoes para o Sintegra (S/N) |
| CHKINS_PAR | char(1) |  | S | Verifica Inscricao Estadual (S/N) |
| PFEC_PAR | date(4) |  | S | Data do fechamento, nao e permitido lancto apos esta data |
| SEQAUT_PAR | char(1) |  | S | Sequencia automatica das notas de saidas e servicos (S/N) |
| CAIXA_PAR | char(1) |  | S | Controla contas a pagar e receber (S/N) |
| PRODUTO_PAR | char(1) |  | S | Opcao para lancamento de produtos (N - Normal / B - NBM / C - NCM / I - Identificador) |
| USATM_PAR | char(1) |  | S | Usa tabelas municipais (S/N) |
| DADOSECF_PAR | char(1) |  | S | Digitar dados ECF das Notas de saidas e servicos somente no ultimo segmento (S/N) |
| PERDCOMP_PAR | char(1) |  | S | Gera PER/DCOMP (S/N) |
| INICIOEFETIVO_PAR | date(4) |  | S | Inicio efetivo das atividades da empresa |
| SPGRFCBT_PAR | char(1) |  | S | SP: Gera informacoes para o GRF-CBT |
| SPGRUPOINF_PAR | integer(4) |  | S | SP: Grupo do Informante(1-Distribuidor,2-Outros/Totalidade,3-CBT-Varejista E/S, 4-Consumidores(E) |
| DOMCLI_PAR | char(1) |  |  | Utiliza Dominio Cliente (S=Sim/N=Nao) |
| PERMPROGRU_PAR | char(1) |  |  | Modulo para cadastro de grupos e produtos(C=Contabil/L=Cliente) |
| SCANCCTB_PAR | char(1) |  |  | Gera informacoes para o Scanc-CTB (S=Sim/N=Nao) |
| ALTESP_PAR | char(1) |  | S | Especie |
| ALTSER_PAR | char(1) |  | S | Serie |
| ALTFC_PAR | char(1) |  | S | Fornecedor/Cliente |
| ALTDAT_PAR | char(1) |  | S | Data |
| ALTACU_PAR | char(1) |  | S | Acumulador |
| ALTVCO_PAR | char(1) |  | S | Valor contabil |
| ALTVIM_PAR | char(1) |  | S | Valor de impostos |
| SPED_PAR | char(1) |  | S | Gera informacoes SPED (S=Sim/N=Nao) |
| COD_MUN_FORCLI_PAR | char(1) |  | S | Digitacao no Cadastro de Clientes/Fornecedores (S=Sequencial/E=Estadual/F=Federal/I=IBGE-RAIS) |
| COD_MUN_NOTA_PAR | char(1) |  | S | Digitacao no Lancamento das notas (S=Sequencial/E=Estadual/F=Federal/I=IBGE-RAIS) |
| COD_MUN_IMP_FORCLI_PAR | char(1) |  | S | Importacao de Fornecedores/Clientes (S=Sequencial/E=Estadual/F=Federal/I=IBGE-RAIS) |
| COD_MUN_IMP_NOTA_PAR | char(1) |  | S | Importacao de Notas (S=Sequencial/E=Estadual/F=Federal/I=IBGE-RAIS) |
| CONTROLA_AIDF_PAR | char(1) |  | S | Efetuar controle no lancamento das notas de saidas conforme AIDF (S/N) |
| INFORMATIVO_NFP_PAR | char(1) |  | S | Gera informativo nota fiscal paulista(S/N) |
| ENTREGA_DOMICILIO_PAR | char(1) |  | S | Entrega a domicilio(S/N) |
| SIMPLESN_INICIO_SISTEMA_PAR | date(4) |  | S | Inicio do calculo do simples nacional no sistema (receita bruta acumulada) |
| SPED_FISCAL_PAR | char(1) |  | S | Gera SPED Fiscal (S/N) |
| SPED_PERFIL_PAR | char(1) |  | S | SPED - Perfil de apresentacao (A/B) |
| REPETE_DADOS_NOTAS_PAR | char(1) |  | S | Repetir os dados apos gravar as notas (S/N) |
| LANCAMENTO_CONHECIMENTO_PAR | integer(4) |  | S | Lancamento do remetente e destinatario por (1 - Codigo/2 - Nome/3 - CNPJ) |
| GERA_LANCAMENTOS_PAR | char(1) |  | S | Gera lancamentos contabeis(S/N) |
| COMBUSTIVEL_PAR | char(1) |  | S | Empresa distribuidora, refinaria ou revendedora de combustível(S/N) |
| IMPORTAR_NFE_PAR | char(1) |  | S | Importa a NFe do site da receita(S/N) |
| INFORMAR_NFE_TERCEIROS_PAR | char(1) |  | S | Informar a chave NFe para notas de entradas com emissão de terceiros(S/N) |
| LIMITE_REDUCAO_Z_PAR | date(4) |  |  | Data limite para o lançamento de redução Z na tela de saídas |
| ALTEROU_DATA_REDUCAO_Z | char(1) |  | S | Regerar lançamentos da redução Z quando alterar a data da redução(S/N) |
| ALTEROU_ACUMULADOR_REDUCAO_Z | char(1) |  | S | Regerar lançamentos da redução Z quando alterar o acumulador(S/N) |
| ALTEROU_VALOR_OPERACAO_REDUCAO_Z | char(1) |  | S | Regerar lançamentos da redução Z quando alterar o valor da operaçao(S/N) |
| ALTEROU_VALOR_IMPOSTO_REDUCAO_Z | char(1) |  | S | Regerar lançamentos da redução Z quando alterar o valor do imposto(S/N) |
| REPETE_CONFIGURACAO_REDUCAO_Z_PAR | char(1) |  | S | Repete a configuração da redução z anterior(S/N) |
| LANCAMENTO_CUPOM_FISCAL_PAR | integer(4) |  | S | Lançamento do cupom fiscal por (1 - Código/2 - Nome/3 - CNPJ) |
| DMED_PAR | char(1) |  |  | Gera informativo DMED (S/N) |
| DMED_TIPO_EMPRESA_PAR | tinyint(1) |  |  | DMED Tipo de empresa (1=Prestador de servico de saude/ 3=Prestador de servico de saude e Operadora de plano privado de saude) |
| DMED_REGISTRO_ANS_PAR | integer(4) |  | S | DMED Registro ANS |
| DMED_CNES_PAR | integer(4) |  | S | DMED CNES |
| VAREJISTA_COMBUSTIVEL_PAR | char(1) |  |  | Empresa do ramo varejista de combustíveis(Postos de combustíveis) (S/N) |
| EFETUA_VENDA_CARTAO_PAR | char(1) |  |  | Efetua vendas com cartões de débito/crédito(S/N) |
| SPED_PISCOFINS_PAR | char(1) |  |  | Gera Informativo SPED PIS/COFINS (S/N) |
| CFEM_PAR | char(1) |  |  | Gera Informativo CFEM (S/N) |
| ALTEROU_DATA_REDUCAO_Z_BILHETE | char(1) |  |  | Regerar lançamentos da redução Z - bilhetes de passagem quando alterar a data da redução |
| ALTEROU_ACUMULADOR_REDUCAO_Z_BILHETE | char(1) |  |  | Regerar lançamentos da redução Z - bilhetes de passagem quando alterar o acumulador |
| ALTEROU_VALOR_CONTABIL_REDUCAO_Z_BILHETE | char(1) |  |  | Regerar lançamentos da redução Z - bilhetes de passagem quando alterar o valor contábil |
| ALTEROU_VALOR_IMPOSTO_REDUCAO_Z_BILHETE | char(1) |  |  | Regerar lançamentos da redução Z - bilhetes de passagem quando alterar o valor do imposto |
| ALTEROU_ESPECIE_REDUCAO_Z_BILHETE | char(1) |  |  | Regerar lançamentos da redução Z - bilhetes de passagem quando alterar a espécie |
| EMITE_BILHETE_PASSAGEM_PAR | char(1) |  |  | Emite bilhetes de passagem |
| REPETE_CONFIGURACAO_REDUCAO_Z_BILHETE_PAR | char(1) |  |  | Repete a configuração da redução z - bilhetes de passagem anterior(S/N) |
| INFORMA_DADOS_FRETE_NOTA_PAR | char(1) |  |  | Informa dados do frete para notas fiscais modelo 1 e 1A (S/N) |
| SIMP_PAR | char(1) |  |  | Gera informativo I-SIMP |
| SIMP_CODIGO_AGENTE_REGULADO | varchar(10) |  |  | Código Agente Regulado |
| SIMP_CODIGO_INSTALACAO | varchar(7) |  |  | Código Instalação |
| SIMP_NUMERO_CERTIFICADO_QUALIDADE | varchar(10) |  |  | Número Certificado/Boletim Qualidade |
| NOTIFICAR_NFE_A_IMPORTAR | char(1) |  | S | Notificar sobre novas NF-e a importar |
| NOTIFICAR_NFE_A_IMPORTAR_POR_QUANTIDADE | char(1) |  | S | Notificar sobre novas NF-e a importar por quantidade |
| NOTIFICAR_NFE_A_IMPORTAR_QUANTIDADE_NFE | integer(4) |  | S | Quantidade de NF-e para notificar sobre novas NF-e a importar |
| NOTIFICAR_NFE_A_IMPORTAR_POR_PERIODO | char(1) |  | S | Notificar sobre novas NF-e a importar por período |
| NOTIFICAR_NFE_A_IMPORTAR_DIAS | integer(4) |  | S | Número de dias para notificar sobre novas NF-e a importar |
| GERAR_CONTRIBUICAO_INSS_BLOCO_P | char(1) |  |  | Gerar as Contribuições do INSS sobre a Receita Bruta - Bloco P (S/N) |
| VAREJISTA_MEDICAMENTO_PAR | char(1) |  |  | Empresa do ramo varejista de medicamentos |
| IMPORTAR_CTE_SITE_PAR | char(1) |  | S | Importar do portal CTe as informações dos Conhecimentos de Transporte eletrônico nos lançamentos de notas |
| GERAR_CONVENIO_ICMS | char(1) |  |  | Gera o arquivo do Convênio ICMS 115/03 (S/N) |
| PE_GERAR_SEF_2 | char(1) |  |  | Gerar o informativo SEF 2012 |
| IMPORTAR_CADASTROS_SITE_RFB | char(1) |  |  | Importar do portal da RFB os dados no cadastro de clientes, fornecedores e remetentes/destinatários |
| PA_GERA_INFORMATIVO_NOTA_PARA | char(1) |  |  | PA - Gera o informativo Nota Pará do programa Nota Fiscal Cidadã |
| GERAR_REINTEGRA | char(1) |  |  | Gerar informações do REINTEGRA |
| AM_GERAR_DIA | char(1) |  |  | AM - Gera a Declaração de Ingresso no Amazonas - DIA (S/N) |
| AM_EMPRESA_ZONA_FRANCA_MANAUS | char(1) |  |  | AM - Empresa situada na Zona Franca de Manaus (S/N) |
| SP_GERA_E_CREDRURAL | char(1) |  |  | Gera o arquivo digital e-CredRural |
| CONSIDERAR_ZERO_A_ESQUERDA_PRODUTO | char(1) |  |  | Considerar zeros à esquerda no código dos produtos |
| EFETUA_CONTROLE_PRODUCAO_ACUCAR_E_ALCOOL | char(1) |  |  | Efetua controle da produção de açúcar e álcool - Usinas (S/N) |
| RJ_GERA_DUB_ICMS | char(1) |  |  | RJ - Gera o Documento de Utilização de Benefício - DUB-ICMS (S/N) |
| DF_PROGRAMA_CONCESSAO_CREDITOS_NOTA_LEGAL | char(1) |  |  | DF - Empresa enquadrada no programa de concessão de créditos - Nota Legal (S/N) |
| RS_GERA_LIVRO_OPER_COMPRA_E_VENDA_AGROTOXICOS | char(1) |  |  | RS - Gera o livro de registro das operações de compra e venda de agrotóxicos fitossanitários |
| RS_NUMERO_REGISTRO_NA_SEAPA | char(9) |  |  | RS - Número do registro da SEAPA |
| PRODUTO_DEFINIR_DADOS_IMPOSTO_CONFORME_NCM | char(1) |  |  | Definir os dados de impostos no cadastro de produtos conforme NCM |
| EXISTEM_OUTRAS_EMPRESAS_COM_MESMO_CNPJ | char(1) |  |  | Existem outras empresas com mesmo CNPJ |
| GERAR_SPED_CONTABIL_INVENTARIO | char(1) |  |  | Gera o SPED Contábil - Inventário |
| ALTEROU_DATA_CFE | char(1) |  |  | Regerar lançamentos do CF-e quando alterar a data |
| ALTEROU_CLIENTE_CFE | char(1) |  |  | Regerar lançamentos do CF-e quando alterar o cliente |
| ALTEROU_ACUMULADOR_CFE | char(1) |  |  | Regerar lançamentos do CF-e quando alterar o acumulador |
| ALTEROU_VALOR_OPERACAO_CFE | char(1) |  |  | Regerar lançamentos do CF-e quando alterar o valor da operação |
| ALTEROU_VALOR_IMPOSTO_CFE | char(1) |  |  | Regerar lançamentos do CF-e quando alterar o valor de impostos |
| EMITE_CF_E_PAR | char(1) |  |  | Emite cupom fiscal eletrônico |
| LANCAMENTO_CFE_CLI_PAR | integer(4) |  | S | Lançamento do CFE - Cliente por (1 - Código/2 - Nome/3 - CNPJ) |
| DF_EMPRESA_ST_USUARIA_SIAFI_SIGGO | char(1) |  |  | DF - Empresa substituta tributária usuária dos sistemas SIAFI e SIGGO - Portaria 210/2006, Art. 10-A |
| PERMITE_GERAR_PARCELA_SO_ULTIMO_SEG | char(1) |  |  | Permitir gerar parcela somente no último segmento (S/N) |
| GERAR_SPED_CONTABIL_CONTAS_PAGAR_RECEBER | char(1) |  |  | Gera o SPED Contábil - Contas a pagar e receber |
| GERAR_DIMOB_PAR | char(1) |  |  | Gera o informativo DIMOB (S/N) |
| EFD_REINF_PAR | char(1) |  |  | Gera EFD-Reinf |
| EFD_REINF_TIPO_AMBIENTE_PAR | char(1) |  |  | Ambiente |
| EFD_REINF_DADOS_CERTIFICADO_PAR | integer(4) |  |  | Certificado digital |
| LOCAL_ARQUIVOS_TRASMITIDOS | varchar(256) |  | S | Armazenar os arquivos transmitidos em |
| CONTROLAR_NOTAS_CONFERIDAS_TIPO | char(1) |  |  | Controlar notas conferidas (N-Não permite alterar / P-Permite alterar / A-Avisar) |
| SP_CREDITO_OUTORGADO_INICIO_PAR | date(4) |  | S | SP - Competência de adesão do crédito outorgado |
| EFD_REINF_RECEBIMENTO_RECURSOS | char(1) |  |  | Recebimento de recursos |
| EFD_REINF_REPASSE_RECURSOS | char(1) |  |  | Repasse de recursos |
| EFD_REINF_RECEITA_ESPETACULO_DESPORTIVO | char(1) |  |  | Receita de Espetáculo Desportivo |
| CONTROLAR_INTERVALO_NOTAS_PERIODO | char(1) |  |  | Controlar o intervalo de notas no período |
| DIF_PAPEL_IMUNE_PAR | char(1) |  |  | Gera o informativo DIF - Papel Imune |
| CONSIDERAR_DADOS_CADASTRAIS_EMPRESA_TRANSMISSORA_RELATORIOS | char(1) |  |  | Considerar dados cadastrais de empresa transmissora em relatórios |
| COMPANY_ID | uniqueidentifier(16) |  |  | Onvio company global unique identifier |
| RS_CREDITO_PRESUMIDO_E_COMMERCE_INICIO_PAR | date(4) |  | S | RS - Competência de início do crédito presumido "e-commerce" |
| LISTAR_NFCE_TODOS_CLIENTES_NAS_DEVOLUCOES_VENDAS | char(1) |  |  | Listar as NFC-e de todos os clientes nas notas de devolução de vendas |
| GERA_CORRELACAO_CODIGO_ITENS_COMERCIALIZADOS | char(1) |  |  | Gerar correlação entre códigos de itens comercializados - Registro 0221 do SPED Fiscal |
| GERAR_DAS_API_CONTADOR | char(1) |  |  | Gerar guia DAS pela API Integra Contador com certificado digital do contador |
| GERAR_DARF_DCTFWEB_API_CONTADOR | char(1) |  |  | Gerar guia DARF DCTF Web pela API Integra Contador com certificado digital do contador |
| GERAR_DEFIS_API_CONTADOR | char(1) |  |  | Gerar guia DEFIS pela API Integra Contador com certificado digital do contador |
| EFETUAR_CALCULO_FUNRURAL_CONFORME_EFD_REINF | char(1) |  |  | Efetuar o cálculo do FUNRURAL conforme a EFD-Reinf |
| GERAR_MIT_API_CONTADOR | char(1) |  |  | Gerar guia MIT pela API Integra Contador com certificado digital do contador |
| TIPO_AMBIENTE_EVENTOS_NFE | integer(4) |  |  | Tipo Ambiente NF-e - (1 - Homologação / 2 - Produção) |
| GERAR_DECLARACAO_DERE | char(1) |  |  | Gera a Declaracao de Regimes Especificos - DeRE |
| LOCAL_ARQUIVOS_DERE | varchar(256) |  | S | Armazenar os arquivos da DeRE em |
