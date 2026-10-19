# Servidor MCP `dominio-db` — guia de uso

Servidor **somente leitura** do banco do Sistema Domínio (SQL Anywhere 17). Código em `src/server/` (`motor.py` = consultas, `mcp_server.py` = ferramentas MCP, `sqlbuilder.py` = geração de SQL).

## Registrar no Claude Code
```powershell
claude mcp add dominio-db --scope user -- "C:\Users\Administrator\Desktop\REA_DOMINIO_DB\executar_servidor.cmd"
```
(O servidor antigo `dominio`, em `https://mcp.intra.venegas/dominio/mcp`, continua independente.) As credenciais vêm de `config\.env`; nada precisa ser passado na linha de comando.

Rede interna (HTTP): `executar_servidor.cmd --transport streamable-http --host 127.0.0.1 --port 8765` e conectar em `http://127.0.0.1:8765/mcp`.
**Atenção:** o modo HTTP **não tem autenticação**; não exponha a porta fora de `127.0.0.1` antes de implementar token/papéis (versões futuras).

## Ferramentas (13)
| Camada | Ferramenta | Para quê |
|---|---|---|
| Descoberta | `listar_modulos`, `buscar_entidades`, `listar_entidades`, `descrever_entidade`, `dominio` | **achar a entidade certa entre as 2.117** (use `buscar_entidades`), ver regras de negócio e significado dos códigos |
| | `buscar_tabelas`, `descrever_tabela`, `relacionamentos`, `caminho_entre` | achar qualquer tabela, colunas/índices, JOINs (com confiança) |
| Consulta | `consultar_entidade` | **2.117 entidades de negócio**: 107 curadas à mão (regras conciliadas com totais da Domínio) e 2.010 geradas em lote (regras = fatos medidos; `buscar_entidades` mostra a `origem`). Preferir sempre a entidade à tabela |
| | `consultar_tabela` | qualquer das ~4.700 tabelas legíveis |
| Prontas | `balancete`, `contas_a_receber` | consultas agregadas validadas |

### Entidades curadas x geradas em lote
Toda tabela útil do banco tem entidade. As **curadas** têm nomes legíveis, descrições e regras de negócio conferidas contra um total que a Domínio calcula (ex.: `nota_saida`, `saldo_produto`, `cupom_fiscal_eletronico`). As **geradas em lote** (módulos `fiscal_*`, `pessoal_*`, `contabil_*`, `geral_*`, `financeiro_*`, `processos_*`, `societario_*`, `sistema_*`, `outros_*`) usam o nome da tabela e as regras são fatos estruturais medidos (volume, período, colunas vazias, domínios, linhas sem pai). Leia `descrever_entidade` antes de confiar numa coluna.

### Formato dos filtros
`filtros` = `{nome: valor | [lista] | {"entre": [a, b]} | {"gte": v} | {"lte": v} | {"contem": "x"} | {"prefixo": "x"} | {"in": [...]}}`.
Período: `"periodo": {"de": "2025-01-01", "ate": "2025-01-31"}`. Datas `AAAA-MM-DD`. Paginação: `limite` (máx. 500) e `offset`; a resposta traz `proximo_offset`. `contar=true` devolve o total.

### Exemplos
```
consultar_entidade(entidade="nota_saida", empresa=879, filtros={"periodo":{"de":"2025-01-01","ate":"2025-01-31"}}, ordem=["data_saida desc"], limite=20, contar=true)
consultar_entidade(entidade="base_folha", empresa=245, filtros={"periodo":{"de":"2025-01-01","ate":"2025-12-31"}, "tipo_folha":11}, colunas=["empregado_codigo","competencia","proventos","descontos","liquido"])
consultar_entidade(entidade="lancamento", empresa=1430, filtros={"conta":{"in":[1234]}, "periodo":{"de":"2025-01-01","ate":"2025-03-31"}})   # razão da conta: débito OU crédito
balancete(empresa=1430, data_inicial="2025-01-01", data_final="2025-12-31")
contas_a_receber(escritorio=930, situacao="aberta", contar=true)
buscar_tabelas(termo="cupom fiscal")  →  consultar_tabela(tabela="EFCUPOM_FISCAL_ELETRONICO", empresa=1010, filtros={...}, colunas=[...])
```

## Salvaguardas sempre ativas (`config/seguranca.yaml`)
- **Somente leitura em três camadas:** o servidor só executa `SELECT`/`WITH`; valores sempre como parâmetros e identificadores validados contra o catálogo; e o usuário do banco (`EXTERNOII`) não tem permissão de escrita (testado).
- **Credenciais nunca saem:** o banco guarda senhas, tokens e segredos em texto em 79 tabelas. Colunas com esses nomes são omitidas (e recusadas se pedidas) e tabelas que são cofres de credenciais ficam bloqueadas. As entidades curadas já não as expõem.
- **Limites:** até 500 linhas por chamada; tabelas com mais de 200 mil linhas exigem filtro por coluna indexada ou por empresa; consultas genéricas devolvem até 40 colunas por padrão (há tabelas com 400).
- **Auditoria:** cada chamada é registrada em `logs/auditoria.jsonl` (ferramenta, argumentos, linhas, tempo, erro).
- **Dados em claro:** nesta versão **não há mascaramento** de dado pessoal ou financeiro (decisão do dono do projeto). Os campos já marcados `sensivel` nos modelos (67) servirão de base para as cópias futuras com papéis e restrições.

## Testes
```powershell
.\.venv\Scripts\python.exe -m pytest -q                    # 61 testes: segurança do SQL, modelos, integração com o banco
.\.venv\Scripts\python.exe scripts\testar_mcp_stdio.py     # ponta a ponta pelo protocolo MCP (processo real, stdio)
.\.venv\Scripts\python.exe scripts\testar_mcp_http.py      # idem pelo transporte HTTP
.\.venv\Scripts\python.exe scripts\testar_entidades.py     # as 75 entidades contra o banco real
```

## Atualização do catálogo
Quando a Domínio atualizar a versão do banco, regenere na ordem (ver `STATUS.md`): `catalogo.py` → `indices.py` → `joins_sql.py` → `relacoes.py` → `perfil_colunas.py`; rode `validar_modelo.py` e `pytest`.


## Biblioteca de tools por tabela (gateway)

Além das 13 ferramentas acima, o servidor expõe a biblioteca (`docs/biblioteca.md`): cada tabela mapeada tem `*_consultar`, `*_obter` e `*_totais`, e os casos de uso (`receita_bruta_simples`, `resumo_folha`, ...) aparecem direto na lista.
Por padrão (`--perfil compacto`) o cliente vê 3 ferramentas de gateway: `buscar_ferramentas(termo)` -> `descrever_ferramenta(nome)` -> `executar_ferramenta(nome, argumentos)`.
`--perfil completo` registra todas (≈ 4.900; use `--modulos estoque,cfe` para um servidor dedicado a poucos módulos).
