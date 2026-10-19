# CTTABELA_SPED_ECF_OD_REGISTRO — SPED ECF - Outros Dados - Tabela com colunas dos registros de valor
10.776 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| REGISTRO | varchar(4) | PK |  | Registro |
| CODIGO | numeric(10) | PK |  | Código do registro |
| VIGENCIA | date(4) | PK |  | Vigência do registro |
| DESCRICAO | varchar(512) |  |  | Descrição |
| TIPO | integer(4) |  |  | TIPO (1=TÍTULO / 2=VALOR / 3=CALCULADO / 4=VALOR DE OUTRO REGISTRO / 5=FÓRMULA CONDICIONAL COM VALOR DE OUTRO REGISTRO / 6=VALOR CONTA DESABILITADA / 7=FÓRMULA CONDICIONAL COM VALOR DE OUTRO REGISTRO HABILITADO) |
| FORMULA | varchar(1024) |  |  | Fórmula |
| TIPO_LANCAMENTO_LALUR | char(1) |  |  | Tipo do Lançamento (R=Rótulo / L=Lucro / A=Adição / E=Exclusão / P=Compensação de prejuízo) |
| MASCARA_CAMPO | varchar(10) |  | S | Mascara para o campo. |
