# EFIMPORTADOR_FIXO_SPED_FISCAL_BILHETE_PASSAGEM — Configuração do leiaute SPED Fiscal do Importador Fixo - Bilhete de Passagem
1.178 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Código da empresa |
| CONSIDERAR_ICMS_ACUMULADOR | char(1) |  |  | Considerar as definições do imposto ICMS no acumulador |
| GERAR_LANCAMENTOS_CONTABEIS | char(1) |  |  |  |
| SAI_DADOS_EXCECAO | char(1) |  |  | Definir dados para exceção das saídas |
| SAI_CODI_ACU_EXCECAO | integer(4) |  | S | Código do acumulador para exceção das saídas |
| DEDUZIR_VALOR_ICMS_BASE_CALCULO_PISCOFINS | varchar(1) |  |  | Deduzir o valor do ICMS da base de cálculo do PIS e COFINS |
| DATA_CANCELADA | char(1) |  |  | Data das notas canceladas |
| CODI_ACU_CANCELADA | integer(4) |  | S | Código do acumulador para nota cancelada |
| CFOP_CANCELADA | integer(4) |  | S | CFOP das notas canceladas |
| VERSAO_CFOP_CANCELADA | smallint(2) |  | S | Versão do CFOP das notas canceladas |
| DEDUZIR_ISS_DA_BASE_CALCULO_PIS_COFINS | char(1) |  | S | Deduzir o valor do ISS da base de cÃ¡lculo do PIS e COFINS. |
