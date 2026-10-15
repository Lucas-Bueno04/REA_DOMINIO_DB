# Descobertas da engenharia reversa (REA)

Data: 2026-10-15 · Alvo: `C:\Contabil\Utilitários\geradrel.exe` (SHA-256 `117742f3…a5b1e` ) e `.pbd` associados.

## Natureza do alvo
- Executável PE32 (x86) PowerBuilder 12.5 (`pbvm125.dll`); lógica nos `.pbd` (`geradsql`, `geraddvr`, `geradgrc`, `geradobj`, `geradope`, `geradexe`, `conexao gerador`, `funcaogl`, `objglob`).
- O REA/Ghidra não decompila p-code PowerBuilder; os SQL embutidos foram extraídos por strings (`scripts/extrair_strings_pbd.ps1`) e a cadeia de blocos `DAT*` foi remontada (`scripts/remontar_bloco_pbd.ps1`) quando uma string atravessa blocos de 512 bytes.
- **Ghidra não é necessário** para este projeto.

## Conexão
- DSN ODBC `Contabil` (usuário, 32/64 bits) → driver **SQL Anywhere 17**; banco `Contabil`, servidor 17.0.11.7312.
- Owner de todas as tabelas de negócio: **`bethadba`** (≈5.140 objetos).
- Dicionário de dados do gerador: views do owner **`DSDBA`** (`SYSTABLE`, `SYSCOLUNAS`, `SYSFOREIGNKEYS`, `SYSUSERPERMS`, `SYSGROUPS`, `SYSPROCEDURE`, `SYSTRIGGERS`, `DUMMY`, `ROWGENERATOR`…).
- O usuário de leitura `EXTERNOII` (grupo `_somenteconsulta`) **não lê `DSDBA.*`**, mas lê `SYS.*` (catálogo nativo). Equivalências usadas:
  - `DSDBA.SYSTABLE` → `SYS.SYSTAB` / `SYS.SYSTABLE`
  - `DSDBA.SYSCOLUNAS` → `SYS.SYSTABCOL` / `SYS.SYSCOLUMN`
  - `DSDBA.SYSFOREIGNKEYS` → `SYS.SYSFOREIGNKEYS`
  - Permissões: `SYS.SYSTABLEPERM` (grantee `_somenteconsulta`, `PUBLIC`).

## Como o gerador decide quais tabelas oferecer
Consulta em `sql/gerador_lista_tabelas.original.sql`: tabelas e views do owner `bethadba`, exceto prefixos `AUDIT_`/`PBCAT` e ~130 tabelas internas (config, backup, licença, telas, temporárias e as tabelas do próprio gerador).

## Tabelas do próprio gerador de relatórios (fonte de JOINs "de fato")
`RELATORIOS`, `CLASSIFICACOES_RELATORIOS`, `ARGUM_RELS`, `DEFARGUM`, `BANDAS_RELS`, `OBJETOS_RELS`, `OBJETOS_RELS_IMAGENS`, `DEFSELECT`, `COLSSELECT`, `SELSSELECT`, `ORDSELECT`, `CPTSSELECT`, `LAYOUT_ARQS`, `RELATORIOS_ATUALIZACAO`.

## Inventário
- 4.844 fontes (99 views); 4.787 legíveis pelo EXTERNOII.
- 6.770 FKs declaradas (owner `bethadba`).
- Arquivo: `data/raw/inventario_fontes_gerador.csv` (colunas: TABLE_ID, TABLE_NAME, TABLE_TYPE, COUNT_ROWS, COMENT, pref, ok).

## Módulos (prefixo → área)
| Prefixo | Área | Tabelas | Observação |
|---|---|---|---|
| EF | Escrita Fiscal | 2.723 | CF-e é o maior volume |
| FO | Folha | 793 | eSocial: `FOESOCIAL_*` |
| GE | Geral | 390 | `geempre` é a raiz multiempresa |
| CT | Contabilidade | 379 | `ctlancto` 13,7 mi linhas |
| HR | Honorários (atual) | 149 | substitui HO/HN |
| LR / LA | Lalur (novo / antigo) | 129 / 23 | |
| PM / PA | Patrimônio (novo / antigo) | 52 / 11 | |
| PO, RG, PC, PR, AU | Ponto, Registro, Processos, Protocolos, Auditoria | 37, 35, 28, 9, 17 | |
| HN, HO | Honorários antigo | 26, 11 | HO vazio |
| SU, MO, SY, TE, TM… | suporte / sistema / temporárias | – | |

## Tabelas centrais já levantadas (PK)
| Tabela | PK | Colunas | Linhas |
|---|---|---|---|
| geempre | codi_emp | 142 | 1.967 |
| gesocios | i_socio | 77 | 2.316 |
| GEIMPOSTO_VIGENCIA | CODI_EMP, CODI_IMP, VIGENCIA_IMP | 367 | 316.644 |
| ctcontas | codi_emp, codi_cta | 23 | 1.574.170 |
| ctlancto | codi_emp, nume_lan | 30 | 13.710.657 |
| ctlanctolote | codi_emp, codi_lote | 8 | 12.641.512 |
| cthispad | codi_emp, codi_his | 4 | 266.424 |
| ctccusto | codi_emp, codi_ccu | 6 | 1.383 |
| efentradas | codi_emp, codi_ent | 144 | 511.920 |
| efmvepro | codi_emp, codi_ent, nume_mep | 127 | 620.262 |
| efimpent | codi_ent, codi_imp, codi_emp, sequ_ien | 44 | 806.916 |
| efsaidas | codi_emp, codi_sai | 169 | 512.487 |
| efmvspro | codi_emp, codi_sai, nume_msp | 142 | 1.338.671 |
| efimpsai | codi_sai, codi_imp, codi_emp, sequ_isa | 39 | 636.483 |
| efservicos | codi_emp, codi_ser | 50 | 585.763 |
| efimpser | codi_ser, codi_imp, codi_emp, sequ_ise | 25 | 1.155.595 |
| efclientes | codi_emp, codi_cli | 54 | 689.034 |
| effornece | codi_emp, codi_for | 63 | 61.982 |
| efprodutos | codi_pdi, codi_emp | 216 | 221.151 |
| efsdopro | codi_emp, codi_pdi, data_pro | 19 | 8.446.958 |
| EFPARAMETRO_VIGENCIA | CODI_EMP, VIGENCIA_PAR | 657 | 6.450 |
| foempregados | codi_emp, i_empregados | 416 | 10.973 |
| foeventos | codi_emp, i_eventos | 163 | 1.306.923 |
| fomovtoserv | codi_emp, i_empregados, data, tipo_proces, i_eventos, rateio, i_servicos, I_CALCULOS | 22 | 2.927.129 |
| fobasesserv | codi_emp, i_empregados, competencia, tipo_process, i_servicos, rateio, I_CALCULOS | 146 | 415.218 |
| focargos / fodepto | codi_emp + i_cargos / i_depto | 30 / 24 | 6.042 / 1.403 |
| HRCLIENTE | CODI_EMP, I_CLIENTE | 131 | 2.916 |
| PMBEM | CODI_EMP, I_BEM | 112 | 4.353 |

**Observações:** `EFACUMULADORES` (83 col.) e `geusuarios` estão vazias; os acumuladores reais estão em `EFACUMULADOR`. Quase toda tabela é multiempresa via `codi_emp`.

## Relacionamentos principais confirmados (FK declarada)
- `efentradas` → `effornece (codi_emp,codi_for)`, `EFACUMULADOR`, `efespecies`, `efnatureza (codi_nat,versao_nat)`, `geempre`
- `efsaidas` → `efclientes (codi_emp,codi_cli)`, `EFACUMULADOR`, `efnatureza`, `efespecies`, `geempre`
- `efservicos` → `efclientes`, `EFACUMULADOR`, `efespecies`, `geempre`
- `efmvepro` → `efentradas (codi_emp,codi_ent)`; `efmvspro` → `efsaidas (codi_emp,codi_sai)`
- `efimpent` → `efentradas`; `efimpsai` → `efsaidas`; `efimpser` → `efservicos`
- `ctlancto` → `ctlanctolote (codi_emp,codi_lote)`, `ctlanctopadrao`, `geempre`
- `foempregados` → `focargos`, `fodepto`, `foservicos`, `fosindicatos`, `fofiliais`, `foccustos`, `gemunicipio`, `gepais`…
- `fomovtoserv` → `foempregados`, `foservicos`, `focalculos`
- `HRCLIENTE` → `geempre`, `efprodutos`, `efnatureza`, `HRCLASSIFICACAO`, `HRCONTA_FINANCEIRA`
- `PMBEM` → `PMCONTA_PATRIMONIAL`, `ctccusto`, `effornece`, `efprodutos`, `GESCP`, `geempre`

## Permissões (EXTERNOII)
Grupo `_somenteconsulta` com SELECT em 5.598 tabelas; também `PUBLIC`. Outros grupos do banco: escrita, honorarios, folha, contabilidade, patrimonio, Lalur, protocolos, ponto, administrar, registro, auditoria, PROCESSOS, atualizar.
