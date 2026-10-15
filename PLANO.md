# REA_DOMINIO_DB — Plano do projeto

**Objetivo:** disponibilizar um servidor MCP (Model Context Protocol) que exponha o máximo possível das tabelas do banco do Sistema Domínio (SQL Anywhere 17, banco `Contabil`, owner `bethadba`), com consulta, filtro e paginação por tipo de informação, a partir de um modelo relacional reconstruído por engenharia reversa.

**Regras inegociáveis**
1. **Somente leitura.** Nenhuma etapa executa INSERT/UPDATE/DELETE/DDL. Todo acesso passa por `scripts/consulta_readonly.ps1` ou pela camada `src/server` com validador de SELECT, transação `READ UNCOMMITTED` e rollback.
2. **Credenciais fora do repositório.** Usuário/senha só em `config/.env` (ignorado pelo git) ou variáveis de ambiente. Nunca em código, docs ou CSV.
3. **Dados de clientes não vão para o catálogo.** O catálogo guarda estrutura (nomes, tipos, FKs, contagens). Amostras de dados ficam em `data/samples/` (ignorado pelo git) e são mínimas.
4. **O banco é a fonte da verdade; o REA é a fonte do "como a Domínio usa".**

---

## 1. Ponto de partida (já feito)

| Item | Resultado |
|---|---|
| Aplicação analisada | `C:\Contabil\Utilitários\geradrel.exe` (PowerBuilder 12.5, x86) |
| Conexão | DSN ODBC `Contabil` → SQL Anywhere 17.0.11; usuário `EXTERNOII` (grupo `_somenteconsulta`) |
| Dicionário usado pelo gerador | views `DSDBA.SYSTABLE`, `SYSCOLUNAS`, `SYSFOREIGNKEYS`, `SYSUSERPERMS` (o EXTERNOII **não** lê as `DSDBA.*`; usar `SYS.*`) |
| Consulta original das "fontes de dados" | `sql/gerador_lista_tabelas.original.sql` |
| Inventário | 4.844 fontes (99 views); 4.787 legíveis pelo EXTERNOII — `data/raw/inventario_fontes_gerador.csv` |
| FKs declaradas | 6.770 |
| Tabelas centrais com PK/FK levantadas | ~30 (ver `docs/descobertas-rea.md`) |
| Ghidra | **Não necessário** (PowerBuilder compila para p-code nos `.pbd`; os SQLs são extraídos por strings) |

---

## 2. Arquitetura alvo

```
 SQL Anywhere 17 (Contabil)            REA / .pbd (como a Domínio usa)
        │  ODBC (SYS.* + SELECT)               │  SQL dos relatórios (DEFSELECT/COLSSELECT)
        ▼                                      ▼
 ┌──────────────┐   ┌───────────────────────────────────┐
 │ 1 Extractor  │──▶│ 2 Catálogo (SQLite: data/catalog) │
 └──────────────┘   │  tabelas, colunas, PK, FK, módulo,│
                    │  permissão, joins "de fato"       │
                    └───────────────┬───────────────────┘
                                    ▼
                    ┌───────────────────────────────┐
                    │ 3 Modelo relacional (src/model)│  entidades de negócio, grafo de joins,
                    └───────────────┬───────────────┘  YAML curado por módulo
                                    ▼
                    ┌───────────────────────────────┐
                    │ 4 Gerador de ferramentas       │  consultas parametrizadas + filtro + paginação
                    └───────────────┬───────────────┘
                                    ▼
                    ┌───────────────────────────────┐
                    │ 5 Servidor MCP (src/server)    │  stdio e/ou HTTP, somente leitura
                    └───────────────────────────────┘
```

**Stack proposta:** Python 3.14 já instalado + `pyodbc` + SDK MCP oficial (`mcp`/FastMCP) + SQLite para o catálogo + driver ODBC **SQL Anywhere 17 64-bit** (já presente). Alternativa: reutilizar a stack do MCP `dominio` interno (`https://mcp.intra.venegas/dominio/mcp`) — decidir na Fase 0.

---

## 3. Fases

### Fase 0 — Preparação (0,5 dia)
- [ ] Decidir stack e hospedagem: servidor novo independente vs. estender o MCP `dominio` existente (em `mcp.intra.venegas`).
- [ ] Criar venv, instalar `pyodbc`, `mcp`, `pydantic`, `pyyaml`, `pytest`.
- [ ] Criar `config/.env` a partir de `config/.env.example` (usuário dedicado de leitura; **trocar a senha do EXTERNOII**, que já foi exposta em conversa).
- [ ] Teste de conexão com o driver 64-bit e confirmação de somente leitura (tentativa de escrita deve falhar).
- **Entrega:** `scripts/testar_conexao.py` verde.

### Fase 1 — Descoberta: tabelas e colunas (1 dia) — ✅ concluída em 2026-10-15
- [ ] Extrair de `SYS.SYSTAB`, `SYSTABCOL`, `SYSIDX/SYSIDXCOL`, `SYSDOMAIN`: tabelas, views, colunas (tipo, tamanho, escala, nulo, default, PK, comentário), índices únicos.
- [ ] Extrair comentários de tabelas/colunas (`remarks`) — são os rótulos usados no gerador.
- [ ] Extrair permissões do usuário de leitura (`SYSTABLEPERM`/grupo `_somenteconsulta`) e marcar o que é legível.
- [ ] Contagem de linhas (`SYSTAB.count`) e data de última atualização quando disponível.
- [ ] Gravar tudo em `data/catalog/dominio_catalog.db` (SQLite).
- [ ] Classificar cada tabela por módulo/departamento (prefixo) e subcluster (segundo termo do nome).
- **Entrega:** catálogo com ~4.800 tabelas e todas as colunas; relatório de cobertura (`docs/cobertura.md`).

### Fase 2 — Relacionamentos (1–2 dias) — ✅ concluída em 2026-10-15 (ver `STATUS.md` e `docs/relacionamentos.md`)
- [ ] Importar as 6.770 FKs (`SYSFOREIGNKEYS`) com tabela pai/filha, colunas e papel (role).
- [ ] **Inferência de relações não declaradas:** colunas com o mesmo nome e tipo que a PK de outra tabela (ex.: `codi_emp`, `codi_cli`, `codi_sai`); pontuar por nome, tipo, cardinalidade e contenção de valores (amostra limitada, só contagens `COUNT(DISTINCT)`).
- [ ] **Fonte "como a Domínio usa":** ler `bethadba.DEFSELECT`, `COLSSELECT`, `SELSSELECT`, `ORDSELECT`, `RELATORIOS` e extrair os JOINs dos relatórios padrão (parser de SQL → pares de tabela/colunas). Marcar relações confirmadas por relatório.
- [ ] Montar o grafo de tabelas (nós = tabelas, arestas = FK declarada | inferida | usada em relatório) com grau de confiança.
- [ ] Identificar a chave multiempresa (`codi_emp`) e as tabelas "globais" (sem `codi_emp`).
- **Entrega:** tabela `relacoes` no catálogo; `docs/relacionamentos.md`; grafo exportado (`exports/grafo.json`).

### Fase 3 — Engenharia reversa do modelo (2–3 dias) — ✅ núcleo concluído em 2026-10-15 (Fiscal, Contábil, Folha, Honorários, Geral: 75 entidades); lacunas por volume e módulos menores opcionais (ver `STATUS.md`)
- [ ] REA nos `.pbd` (`geradsql`, `geraddvr`, `geradgrc`, `funcaogl`, `objglob`) e nas `.pbd` dos módulos (`esc*`, `esr*`, `esm*`, `esf*`, `ctr*`, `hrc*`, `focad*`) para extrair os SQLs embutidos → `data/raw/sql_por_modulo/`.
- [ ] Mapear o significado de colunas de código (situação, tipo, modelo, espécie, CFOP etc.) lendo domínios (`SYSDOMAIN`), tabelas de apoio (`EFTABELA_*`, `GE*`) e checando valores distintos (sempre com `LIMIT`).
- [ ] Reconstruir **entidades de negócio** por módulo (ex.: *Nota de Saída* = `efsaidas` + `efmvspro` + `efimpsai` + `efclientes` + `efacumulador`).
- [ ] Documentar em YAML curado por módulo (`src/model/modulos/*.yaml`): entidade, tabela raiz, joins, colunas expostas, filtros permitidos, ordenação padrão.
- [ ] Ordem de prioridade: **Geral (GE) → Fiscal (EF) → Contábil (CT) → Folha (FO) → Honorários (HR) → Lalur/Patrimônio → demais**.
- **Entrega:** YAMLs dos módulos prioritários + `docs/modelo-<modulo>.md` com diagrama.

### Fase 4 — Camada de consulta (2–3 dias) — ✅ concluída em 2026-10-15 (ver `STATUS.md`)
- [ ] Construtor de SQL seguro: apenas SELECT, identificadores validados contra o catálogo (nunca interpolados do usuário), valores sempre como parâmetros.
- [ ] Filtros declarativos: igualdade, intervalo, `IN`, `LIKE` (prefixo), datas, competência; mapeados por entidade.
- [ ] Paginação: `limite` (padrão 50, máx. 500) + `offset` com `ORDER BY` determinístico (PK); resposta com `total` opcional (COUNT só sob demanda) e `proxima_pagina`.
- [ ] Timeout de consulta, limite de linhas, escolha de colunas, mascaramento opcional de campos sensíveis (CPF/CNPJ de pessoas físicas, salários — decisão de política na Fase 0).
- [ ] Log de auditoria das chamadas (quem, o quê, quando, linhas).
- **Entrega:** biblioteca `src/server/query.py` + testes unitários.

### Fase 5 — Servidor MCP (2 dias) — ✅ concluída em 2026-10-15 (12 ferramentas; falta registrar no Claude Code)
Ferramentas em três níveis, para evitar centenas de ferramentas soltas:
1. **Descoberta (genéricas):** `listar_modulos`, `buscar_tabelas(termo)`, `descrever_tabela(nome)`, `relacionamentos(tabela)`, `caminho_entre(tabelaA, tabelaB)`.
2. **Consulta genérica segura:** `consultar_tabela(tabela, colunas, filtros, ordem, limite, offset)` sobre qualquer tabela legível do catálogo.
3. **Entidades de negócio (curadas):** uma ferramenta por informação relevante, ex.: `notas_saida`, `notas_entrada`, `notas_servico`, `itens_nota`, `impostos_nota`, `lancamentos_contabeis`, `plano_contas`, `empregados`, `eventos_folha`, `calculos_folha`, `faturamento_honorarios`, `bens_patrimonio`, `empresas`, `socios`…
- [ ] Resources MCP: catálogo e dicionário por módulo (`dominio://modulo/EF`, `dominio://tabela/efsaidas`).
- [ ] Transporte: stdio (local) e HTTP streamable (rede interna), com autenticação por token.
- [ ] Compatibilidade com o MCP `dominio` atual (manter nomes existentes onde já houver ferramenta equivalente).
- **Entrega:** servidor rodando e registrado no Claude Code (`claude mcp add`).

### Fase 6 — Qualidade e segurança (1–2 dias)
- [ ] Testes: unitários (construtor de SQL, paginação), contrato (schemas MCP), integração contra o banco (somente leitura) com empresa de teste.
- [ ] Teste de injeção (identificadores, `LIKE`, `ORDER BY`) e de tentativa de escrita (deve ser recusada).
- [ ] Desempenho: tabelas grandes (`ctlancto` 13,7 mi, `audados` 31 mi, `EFCUPOM_*` 12 mi) exigem filtro obrigatório por `codi_emp` + período; bloquear varredura sem filtro.
- [ ] Revisão de privacidade (dados pessoais da folha) e política de acesso por perfil.
- **Entrega:** relatório de testes e checklist de segurança.

### Fase 7 — Operação (1 dia)
- [ ] Serviço Windows (NSSM) ou tarefa agendada; logs rotativos; variáveis em arquivo protegido.
- [ ] Regeneração do catálogo a cada atualização da Domínio (script `scripts/atualizar_catalogo.py`) com diff de tabelas/colunas novas.
- [ ] Documentação de uso (`docs/uso-mcp.md`) e exemplos de prompts.

---

## 4. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Atualização da Domínio altera tabelas | Catálogo versionado + diff automático; ferramentas curadas validam colunas na inicialização |
| Consultas pesadas travam o banco | Filtro obrigatório em tabelas grandes, timeout, limite de linhas, `READ UNCOMMITTED` |
| Exposição de dados sensíveis (folha, CPF) | Política de mascaramento, tokens por perfil, auditoria |
| Relações inferidas erradas | Grau de confiança + confirmação pelos JOINs dos relatórios da Domínio; marcar "inferida" na resposta |
| ~4.800 tabelas é demais para curar | Camada genérica cobre todas; curadoria só para as entidades de maior valor |
| Senha exposta em conversa | Trocar a senha do EXTERNOII e criar usuário dedicado de leitura |
| Licenciamento/termos da Domínio | Confirmar que o acesso ODBC somente leitura com esse usuário é permitido para este uso |

## 5. Critérios de aceite
- Catálogo cobre ≥ 99% das 4.787 tabelas legíveis, com colunas e PK.
- Relacionamentos: 100% das FKs declaradas + relações dos relatórios padrão para os módulos prioritários.
- `consultar_tabela` funciona para qualquer tabela legível com filtro e paginação.
- Pelo menos 15 entidades de negócio curadas (GE, EF, CT, FO, HR) com testes.
- Nenhuma operação de escrita possível (comprovado por teste).

## 6. Estimativa
~10–14 dias úteis de trabalho efetivo, sendo as Fases 1–2 (catálogo + relacionamentos) as mais rápidas e de maior retorno; a curadoria da Fase 3 é a que mais pode crescer conforme a cobertura desejada.

## 7. Próximo passo imediato
Executar a **Fase 0** (stack, venv, `.env`, teste de conexão) e em seguida a **Fase 1** (catálogo completo), que já destrava a camada genérica `consultar_tabela`.
