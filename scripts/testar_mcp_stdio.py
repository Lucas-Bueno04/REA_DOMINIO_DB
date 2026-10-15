"""Teste de ponta a ponta pelo PROTOCOLO MCP: sobe o servidor como processo (stdio) e conversa como o Claude Code faria."""
import asyncio, json, pathlib, sys
from mcp.client import Client
from mcp.client.stdio import StdioServerParameters

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PARAMS = StdioServerParameters(command=str(RAIZ / ".venv" / "Scripts" / "python.exe"), args=["-m", "server.mcp_server"],
                               env={"PYTHONPATH": str(RAIZ / "src")}, cwd=str(RAIZ))


def dados(res):
    if res.is_error:
        return {"ERRO": " ".join(getattr(c, "text", "") for c in res.content)}
    if getattr(res, "structured_content", None):
        return res.structured_content
    return json.loads(res.content[0].text)


async def main() -> int:
    falhas = 0
    async with Client(PARAMS) as c:
        tools = (await c.list_tools()).tools
        print(f"servidor: {c.server_info.name} | {len(tools)} ferramentas")
        print("instruções do servidor:", (c.instructions or "")[:90].replace("\n", " "), "...")

        async def chamar(_ferramenta, esperado_erro=False, contem=None, **args):
            """esperado_erro=True: a chamada DEVE ser recusada E a mensagem deve chegar ao cliente (contendo `contem`)."""
            nonlocal falhas
            r = dados(await c.call_tool(_ferramenta, args))
            erro = "ERRO" in r
            ok = erro if esperado_erro else not erro
            if esperado_erro and ok:
                msg = r["ERRO"]
                ok = bool(msg) and msg.strip() != f"Error executing tool {_ferramenta}" and (contem is None or contem.lower() in msg.lower())
            falhas += not ok
            return r, ok

        r, ok = await chamar("listar_modulos"); print("OK " if ok else "ERRO", "listar_modulos:", {k: v["entidades"] for k, v in r["modulos_modelados"].items()} if ok else r)
        r, ok = await chamar("descrever_entidade", entidade="nota_saida"); print("OK " if ok else "ERRO", f"descrever_entidade: {len(r['campos'])} campos, {len(r['regras'])} regras" if ok else r)
        r, ok = await chamar("consultar_entidade", entidade="nota_saida", empresa=879, filtros={"periodo": {"de": "2025-01-01", "ate": "2025-01-31"}}, limite=3, contar=True, decodificar=True)
        print("OK " if ok else "ERRO", f"consultar_entidade nota_saida: {r.get('retornadas')} linhas, total {r.get('total')}" if ok else r)
        r, ok = await chamar("consultar_entidade", esperado_erro=True, contem="empresa", entidade="nota_saida", limite=3)
        print("OK " if ok else "ERRO", "sem 'empresa' é recusado:", r.get("ERRO", "")[:100])
        r, ok = await chamar("consultar_entidade", esperado_erro=True, contem="nota_saida", entidade="nota_saidaa", empresa=879)
        print("OK " if ok else "ERRO", "entidade inexistente sugere:", r.get("ERRO", "")[:110])
        r, ok = await chamar("buscar_tabelas", termo="cupom fiscal", limite=3); print("OK " if ok else "ERRO", "buscar_tabelas:", [t["tabela"] for t in r["tabelas"]] if ok else r)
        r, ok = await chamar("descrever_tabela", tabela="efsaidas"); print("OK " if ok else "ERRO", f"descrever_tabela efsaidas: {len(r['colunas'])} colunas, PK {r['chave_primaria']}" if ok else r)
        r, ok = await chamar("relacionamentos", tabela="efsaidas", limite=3); print("OK " if ok else "ERRO", "relacionamentos:", [(x['papel'], x['tabela_relacionada']) for x in r["relacoes"]] if ok else r)
        r, ok = await chamar("caminho_entre", origem="efmvspro", destino="efclientes")
        print("OK " if ok else "ERRO", "caminho efmvspro→efclientes:", " → ".join([r["passos"][0]["de"]] + [p["para"] for p in r["passos"]]) if ok and r["encontrado"] else r)
        r, ok = await chamar("consultar_tabela", tabela="efprodutos", empresa=997, limite=2); print("OK " if ok else "ERRO", f"consultar_tabela efprodutos: {r.get('retornadas')} linhas, {len(r.get('colunas', []))} colunas" if ok else r)
        r, ok = await chamar("consultar_tabela", tabela="EFPARAMETRO_VIGENCIA", empresa=941, limite=1)
        print("OK " if ok and any("SENHA" in a.upper() for a in r.get("avisos", [])) and not any("senha" in k for k in r["linhas"][0]) else "ERRO",
              "credencial omitida:", r.get("avisos"))
        falhas += not (ok and not any("senha" in k for k in (r["linhas"][0] if r.get("linhas") else {})))
        r, ok = await chamar("consultar_tabela", esperado_erro=True, contem="bloqueada", tabela="GECERTIFICADOSDIGITAIS", limite=1); print("OK " if ok else "ERRO", "tabela de credenciais bloqueada:", r.get("ERRO", "")[:90])
        r, ok = await chamar("consultar_tabela", esperado_erro=True, contem="indexada", tabela="ctlancto", limite=1); print("OK " if ok else "ERRO", "tabela grande sem filtro indexado é recusada:", r.get("ERRO", "")[:110])
        r, ok = await chamar("balancete", empresa=1430, data_inicial="2025-01-01", data_final="2025-12-31")
        t = r.get("totais", {}); fecha = ok and abs(t["debitos"] - t["creditos"]) < 0.01 and abs(t["saldo_final"]) < 0.01
        falhas += not fecha; print("OK " if fecha else "ERRO", f"balancete: {r.get('contas')} contas, débitos {t.get('debitos')} = créditos {t.get('creditos')}, saldo final {t.get('saldo_final')}")
        r, ok = await chamar("contas_a_receber", escritorio=930, situacao="aberta", limite=2, contar=True); print("OK " if ok else "ERRO", f"contas_a_receber 930 abertas: total {r.get('total')}" if ok else r)
        r, ok = await chamar("dominio", nome="situacao_documento"); print("OK " if ok else "ERRO", "dominio situacao_documento: confirmado =", r.get("confirmado") if ok else r)
    print(f"\n{falhas} falhas")
    return 1 if falhas else 0


sys.exit(asyncio.run(main()))
