# ctlanctolote — Lancamento em lote
12.642.297 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_lote | integer(4) | PK |  | Codigo |
| tipo | char(1) |  |  | Tipo (D=Um debito para varios creditos/C=Um credito para varios debitos/X=Um debito para um credito/V=Varios debitos para varios creditos) |
| codi_pad | integer(4) |  | S | Lancamento padrao |
| LOCALIZADOR | char(15) |  | S | Localizador |
| FCONT_RTT | char(1) |  |  | FCONT RTT (N=Nao/ M=Normal (a ser expurgado) / F=Fiscal (a ser incluido) / E=Encerramento Fiscal) |
| ATUALIZANDO_LANCTO_OUTROS_DADOS | char(1) |  |  | Flag que controla se o lançamento está sendo atualizado através da janela de lançamento |
| GUID_LOTE | uniqueidentifier(16) |  | S | Identificador do lote importado via API |
