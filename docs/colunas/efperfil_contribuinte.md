# EFPERFIL_CONTRIBUINTE — DeSTDA - Perfil do contribuinte
2 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| I_PERFIL | integer(4) | PK |  | Sequencial |
| VIGENCIA | date(4) |  |  | Período |
| EXIGIBILIDADE_REGISTRO_IMPRESSAO_DOCUMENTO_FISCAIS | char(1) |  |  | Exigibilidade do Registro de Impressão de Documentos Fiscais |
| EXIGIBILIDADE_REGISTRO_UTILIZACAO_DOCUMENTO_FISCAIS | char(1) |  |  | Exigibilidade do Registro de Utilização de Documentos Fiscais |
| EXIGIBILIDADE_LIVRO_MOVIMENTACAO_COMBUSTIVEIS | char(1) |  |  | Exigibilidade do Livro de Movimentação de Combustíveis |
| EXIGIBILIDADE_REGISTRO_VEICULOS | char(1) |  |  | Exigibilidade do Registro de Veículos |
| EXIGIBILIDADE_ANUAL_REGISTRO_INVENTARIO | char(1) |  |  | Exigibilidade anual do Registro de Inventário |
| POSSUI_OPERACAO_SUJEITA_ISS | char(1) |  |  | Possui operações sujeitas a ISS |
| POSSUI_OPERACAO_SUJEITA_RETENCAO_ISS | char(1) |  |  | Possui operações sujeitas a retenção tributária do ISS, contribuinte substituído |
| POSSUI_OPERACAO_SUJEITA_ICMS | char(1) |  |  | Possui operações sujeitas ao ICMS |
| POSSUI_OPERACAO_SUJEITA_ST_ICMS | char(1) |  |  | Possui operações sujeitas a substituição tributária do ICMS, contribuinte substituto |
| POSSUI_OPERACAO_SUJEITA_ANTECIPACAO_ICMS | char(1) |  |  | Possui operações sujeitas a antecipação tributária do ICMS, nas entradas |
| POSSUI_OPERACAO_SUJEITA_IPI | char(1) |  |  | Possui operações sujeitas ao IPI |
| APRESENTACAO_AVULSA_REGISTRO_INVENTARIO | char(1) |  |  | Apresentação avulsa do Registro de Inventário |
| EXIGIBILIDADE_ESCRITURACAO_ISS | char(1) |  |  | Exigibilidade da Escrituração do ISS |
| EXIGIBILIDADE_ESCRITURACAO_ICMS | char(1) |  |  | Exigibilidade da Escrituração do ICMS |
| INDICADOR_APRESENTACAO_ESCRITURACAO_CONTABIL | char(1) |  |  | Indicador de apresentação da escrituração contábil |
