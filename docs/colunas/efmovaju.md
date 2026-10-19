# efmovaju — Outros Movimentos - Impostos Lancados
3 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_aju | integer(4) | PK |  | Ajuste |
| data_maj | date(4) | PK |  | Data |
| vlor_maj | numeric(13) |  |  | Valor |
| crec_maj | char(6) |  | S | Codigo da receita |
| obse_maj | varchar(250) |  | S | Observacao |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| classe_maj | integer(4) |  | S | Classe de vencimento |
| vcto_maj | date(4) |  | S | Data de vencimento |
| descdeb_maj | tinyint(1) |  | S | Descricao dos debitos (DIME - SC) |
| desc_livro_maj | char(1) |  |  | Descricao no livro (N - Nome do ajuste/O - Observacao do movimento) |
| cod_especie_maj | tinyint(1) |  | S | Codigo da especie |
| numero_maj | double(8) |  | S | DAE ou IDA |
| descricao_ce_maj | varchar(100) |  | S | Descricao de outro credito |
| processo_maj | char(15) |  | S | Numero do processo (DIME - SC) |
| codigo_uf | integer(4) |  | S | Codigo do estado |
| valor_pago_maj | numeric(13) |  | S | Valor pago do debito |
| acordo_maj | numeric(15) |  | S | Numero do acordo (DIME - SC) |
| dacon_origem_maj | char(1) |  | S | Origem do credito(I-interno/E-externo) |
| fomentar_operacao_maj | char(1) |  | S | Fomentar - Operação Fiscal(N - Nao incentivada/I - Incentivada/F - Não financiada) |
| PROTEGE_MAJ | char(1) |  | S | Incide PROTEGE/GO (S/N) |
| PROTEGE_DISPOSITIVO_MAJ | integer(4) |  | S | Dispositivo - PROTEGE/GO |
| PROTEGE_TARE_MAJ | char(20) |  | S | Numero do TARE - PROTEGE/GO |
| DETALHAMENTO_MAJ | integer(4) |  | S | Detalhamento do movimento de ajuste(RS) |
| CODIGO_AJUSTE_SPED_MAJ | char(8) |  | S | Codigo da tabela de ajustes sped |
| NUMERO_GUIA_DAR_MAJ | numeric(14) |  | S | Numero guia DAR |
| NUMERO_PARCELA_MAJ | integer(4) |  | S | Numero de parcelas |
| BA_OPERACAO_PROJETO_DESENVOLVE | char(1) |  |  | Operação não vinculada ao Projeto DESENVOLVE |
| I_RECOLHIMENTO | integer(4) |  | S | Sequencial do código de recolhimento |
| I_AJUSTE_SEF | integer(4) |  | S | Código sequencial do Ajuste do SEF 2012 |
| DESCRICAO_CREDITO | integer(4) |  | S | Descrição do crédito |
| SE_OPERACAO_VINCULADA_PSDI | char(1) |  |  | Operação não vinculada ao PSDI - Programa Sergipano de Desenvolvimento Industrial |
| MS_OPER_VINCULADA_BENEFICIO_PROGRAMA_FOMENTO | char(1) |  |  | MS - Operação vinculada ao benefício do Programa de Fomento à Industrialização - Lei Comp. nº 93/2001 |
| DF_AJUSTE_REFERENTE_LEI_5005 | char(1) |  |  | DF - Ajuste referente a Lei 5.005/2012 |
| REGISTRO_CONVERTIDO | char(1) |  |  | Registro convertido para a nova tela de lançamento de ajuste |
| SISTEMA_ORIGEM | integer(4) |  |  | Sistema de origem do movimento(Variáveis globais do sistema) |
