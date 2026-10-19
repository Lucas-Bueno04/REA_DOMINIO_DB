# EFACUMULADOR_VIGENCIA_IMPOSTOS_SIMPLESN — Acumuladores - Cadastro - Impostos - Simples Nacional
1 linhas

| Coluna | Tipo | PK | Nulo | Comentário |
|---|---|---|---|---|
| CODI_EMP | integer(4) | PK |  | Empresa |
| CODI_ACU | integer(4) | PK |  | Acumulador |
| VIGENCIA_ACU | date(4) | PK |  | Vigencia |
| CODI_IMP | integer(4) | PK |  | Imposto |
| IMPOSTO | integer(4) | PK |  | Imposto com exigibilidade suspensa(1 - ICMS/2 -IPI/3 - ISS/4 - PIS/5 - COFINS/6 - CSLL/7 - IRPJ/8 - INSS) |
| MOTIVO | char(1) |  |  | Motivo(1 - Liminar em Mandado de Seguranca/2 - Deposito Judicial/3 - Antecipacao de Tutela/4 - Liminar em Medida Cautelar/5 - Deposito Administrativo/6 - Outros) |
| PROCESSO | char(20) |  | S | Numero do processo |
| VARA | integer(4) |  | S | Vara |
| CODIGO_MUNICIPIO | integer(4) |  | S | Municipio |
| UF | char(2) |  | S | UF |
| DEPOSITO | char(1) |  | S | Com deposito(S/N) |
