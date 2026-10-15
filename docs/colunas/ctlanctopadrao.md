# ctlanctopadrao — Lancamentos Padroes em Lote - Cadastro
522 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| codi_emp | integer(4) | PK |  | Empresa |
| codi_pad | integer(4) | PK |  | Codigo |
| desc_pad | char(50) |  |  | Descricao |
| cdeb_pad | integer(4) |  |  | Conta debito |
| ccre_pad | integer(4) |  |  | Conta credito |
| chis_pad | integer(4) |  |  | Codigo do historico |
| rept_pad | char(1) |  |  | Posicionar cursor no campo data |
| comp_pad | char(1) |  |  | Permite complementar historio |
| origem_reg | tinyint(1) |  |  | Origem do registro 0 - Sistema, 1 - Imp. Tabelas, 2 - Imp. Layout, 3- Imp. Tabelas Concorrentes |
| curcod_pad | char(1) |  |  | Posicionar cursor no campo codigo (S=Sim/N=Nao) |
| tipo_pad | char(1) |  |  | Tipo (D=Um debito para varios creditos/C=Um credito para varios debitos/X=Um debito para um credito/V=Varios debitos para varios creditos) |
| FCONT_RTT | char(1) |  |  | FCONT RTT (N=Nao/M=Normal (a ser expurgado)/F=Fiscal (a ser incluido)) |
| FILI_PAD | integer(4) |  |  | Filial |
