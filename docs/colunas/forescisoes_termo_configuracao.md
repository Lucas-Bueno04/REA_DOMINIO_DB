# FORESCISOES_TERMO_CONFIGURACAO — Recibo de Rescisão - Configuração
378 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| TIPO_DEMONSTRACAO | smallint(2) |  |  | Tipo de demonstração: (1=Todos/2=Nenhum/3=Seleção) |
| TIPO_CODIGO_CAMPO_27 | smallint(2) |  |  | Tipo do código do campo 27: (0=Todos/1=Código afastamento homolognet/2=Código do saque FGTS) |
| IMPRIMIR_IDENTIFICACAO | smallint(2) |  |  | Imprimir a identificação do empregador/trabalhador a partir da segunda página: 0=Não/1=Sim |
| IMPRIMIR_DEDUCOES_SEQUENCIA | smallint(2) |  |  | Imprimir as deduções na sequência das verbas rescisórias: 0=Não/1=Sim |
| MODELO | smallint(2) | PK |  | Modelo: (1=TRCT Portaria MTE 1621/2010 - Anexo I/2=TRCT Portaria MTE 1621/2010 - Alterado) |
| CONFIGURACAO_CAMPO_23 | smallint(2) |  |  | Configuração para emissão do campo 2 do recibo de rescisão (1=De acordo com a configuração das rubricas/2=Salário contratual e adicionais/3=Zerado) |
| DEMONSTRAR_BRANCO_CAMPOS_SEM_VALOR | smallint(2) |  |  | Demonstrar em branco os campos sem valor. (0=Não/1=Sim) |
| DEMONSTRAR_QUANTIDADE_DIAS_FERIAS_GOZADOS_MES_RESCISAO_CAMPO_50 | smallint(2) |  |  | Demonstrar no campo 50 a quantidade de dias de férias que o empregado gozou no mês da rescisão. (0=Não/1=Sim) |
| CONSIDERAR_FOLHA_COMPLEMENTAR_CAMPO_23 | smallint(2) |  |  | Considerar para o campo 23-Remuneração Mes Ant. as folhas complementares calculadas. (0=Não/1=Sim) |
| DEMONSTRAR_CODIGO_ENTIDADE_SINDICAL_CAMPO_31_TRABALHADOR_RURAL | smallint(2) |  |  | Demonstrar código da entidade sindical no campo 31 quando trabalhador rural. (0=Não/1=Sim) |
| DEMONSTRAR_VALOR_INFORMADO_OUTROS_DESCONTOS | smallint(2) |  |  | Demonstrar nos outros descontos o valor informado da rubrica. (0=Não/1=Sim) |
| EMITIR_DADOS_CONTA_BANCARIA_COLABORADOR | smallint(2) |  |  | Imprimir dados da conta bancaria do colaborador no relatorio "TRCT Portaria MTE 1621/2010 - Alterado": 0=Não/1=Sim |
