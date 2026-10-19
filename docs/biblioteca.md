# Biblioteca de tools MCP do banco Domínio

Objetivo: cada tabela mapeada vira **ferramentas (tools) no formato do protocolo MCP**, com a descrição que o modelo de IA precisa para se orientar (o que é a tabela,
filtros obrigatórios, legendas de códigos, regras de negócio, privacidade, exemplos), validação de entrada e um caso de uso por ferramenta. **Somente leitura**: toda
ferramenta chama o `Motor` (`SELECT`/`WITH`, valores sempre como parâmetros, credenciais nunca saem, limites de linhas e de colunas).

## Estrutura (padrão de biblioteca)

```
src/biblioteca/
  base.py          Ferramenta, Param, como_funcao (assinatura tipada -> JSON Schema da tool), validar_argumentos
  contexto.py      modelo + catálogo (sem tocar o banco)
  entidades.py     constrói as tools de uma entidade: *_consultar, *_obter, *_totais
  registro.py      descobre todos os arquivos e monta o índice (por tabela / módulo)
  servidor.py      liga a biblioteca ao servidor MCP (perfis compacto e completo; gateway)
  validacao.py     bateria de validação contra o banco
  estado.py        acompanhamento (SQLite data/biblioteca_estado.db) e status derivado por tabela
  <modulo>/        uma pasta por módulo do modelo (137): fiscal_saidas/, pessoal_nucleo/, contabil_bem/, ...
    <tabela>.py    UMA TABELA POR ARQUIVO: TABELA, MODULO, ENTIDADES, TOOLS
  casos_de_uso/    ferramentas que cruzam tabelas e carregam regra de negócio conferida (receita do Simples, folha, Lalur...)
```

Os arquivos de tabela são **gerados** por `scripts/gerar_biblioteca.py` (cabeçalho `# GERADO`). Para curar um arquivo à mão (acrescentar uma ferramenta específica,
por exemplo), troque a primeira linha por `# CURADO`: o gerador nunca o sobrescreve. As descrições são montadas do modelo YAML na carga, então acompanham as regras de negócio
sem reescrever arquivos.

## Ferramentas por tabela

| Tipo | Nome | Para quê |
|---|---|---|
| consultar | `<entidade>_consultar` | listar/filtrar com todos os filtros do modelo, ordenação, colunas, `contar`, `decodificar` e paginação (`proximo_offset`) |
| obter | `<entidade>_obter` | um registro pela chave (quando toda a chave tem filtro de igualdade) |
| totais | `<entidade>_totais` | contagem e soma/média/mín/máx por grupo (`agrupar_por: ["data:mes", "uf"]`), com total geral; para tabelas com campo numérico somável |
| caso_de_uso | nome da função | regra de negócio entre várias tabelas (ver `docs/funcoes.md`) |

Regras sempre ativas: filtro de **empresa** obrigatório quando a tabela depende dela; tabelas grandes exigem filtro protetor (`exige_algum`); limite máximo de 500 linhas;
colunas sensíveis marcadas na descrição; credenciais nunca saem.

## Perfis do servidor

`python -m server.mcp_server [--perfil compacto|completo] [--modulos m1,m2]`

- **compacto** (padrão): 3 tools de *gateway* (`buscar_ferramentas`, `descrever_ferramenta`, `executar_ferramenta`) + os casos de uso direto na lista. Os clientes MCP carregam a lista
  de tools inteira no contexto; as ~4.900 tools de tabela ocupariam ~14 MB de schema, então o modelo acha a ferramenta pelo gateway.
- **completo**: todas as tools registradas individualmente (use `--modulos` para um servidor dedicado a um módulo, ex.: `--modulos estoque,cfe`).

## Validação (bateria contra o banco)

`python scripts/validar_biblioteca.py [--modulo M] [--entidade E] [--refazer] [--so-falhas] [--threads 4]` (retoma de onde parou):

1. **esquema** a tool MCP é montada; 2. **descrição** tem tamanho útil e cita a tabela; 3. **entrada** recusa obrigatórios ausentes e parâmetro desconhecido com mensagem acionável;
4. **execução** com amostra real (empresa mediana e um filtro obrigatório) devolve JSON; 5. **campos** só os declarados; 6. **credenciais** nenhuma coluna de credencial sai;
7. **filtro** filtrar por um valor lido da própria linha devolve essa linha; 8. **paginação** a 2ª página existe e não repete a 1ª; 9. **obter** a chave da linha recupera a linha;
10. **totais** o total geral é igual à contagem da consulta e à soma dos grupos.

O que a bateria prova é que **a ferramenta funciona e faz o que diz**. Ela não prova que a regra de negócio está certa: isso é o que separa *curada* (modelo conciliado com os dados à mão)
de *gerada* (fatos medidos). A bateria já achou defeitos reais do motor que afetavam todas as entidades: `CHAR(n)` com brancos no fim/início (`NCM = '0101'` não achava `'0101    '`),
filtro chamado `periodo` tratado como o período da tabela e comparação de texto vazio.

## Status por tabela (derivado, aba “Biblioteca de tools” da plataforma)

`sem_ferramenta` → `gerada` → `validada` (bateria) → `curada` (modelo conciliado à mão) / `revisada` (um agente independente, sem contexto, aprovou depois de testar as ferramentas).
`falhou` = alguma checagem falhou. Revisão por agente: `scripts/revisar_biblioteca_cli.py` (amostra estratificada, `descrever`, `executar`, `veredito`).

## Como acrescentar

- **Tabela nova**: crie a entidade no modelo (plataforma ou `scripts/mapear_lote.py`), rode `scripts/gerar_biblioteca.py`, depois `scripts/validar_biblioteca.py`.
- **Caso de uso**: escreva a função em `src/server/consultas.py` (SQL parametrizado, somente leitura), registre em `FUNCOES` e declare a ferramenta em `src/biblioteca/casos_de_uso/<tema>.py`
  com `de_funcao(...)`, incluindo o `exemplo` e, se precisar descobrir argumentos no banco, o `teste=descobrir(SQL, ...)`.
- Documentação: `scripts/gerar_docs_biblioteca.py` gera `docs/biblioteca/` (índice e um arquivo por módulo).
