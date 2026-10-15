"""Sobe o servidor em HTTP (streamable) numa porta local, conversa com ele por HTTP e o derruba."""
import asyncio, json, pathlib, subprocess, sys, time, urllib.request
from mcp.client import Client

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PORTA = int(sys.argv[1]) if len(sys.argv) > 1 else 8791


async def main() -> int:
    proc = subprocess.Popen([str(RAIZ / ".venv" / "Scripts" / "python.exe"), "-m", "server.mcp_server", "--transport", "streamable-http",
                             "--host", "127.0.0.1", "--port", str(PORTA)], cwd=str(RAIZ), env={**__import__("os").environ, "PYTHONPATH": str(RAIZ / "src")},
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    try:
        for _ in range(60):                       # espera abrir a porta
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{PORTA}/", timeout=1)
            except urllib.error.HTTPError:
                break                             # respondeu (404/405 são esperados): está de pé
            except Exception:
                time.sleep(0.5)
        async with Client(f"http://127.0.0.1:{PORTA}/mcp") as c:
            tools = (await c.list_tools()).tools
            r = await c.call_tool("consultar_entidade", {"entidade": "empresa", "empresa": 123, "limite": 1})
            ok = (not r.is_error) and len(tools) == 12
            nome = (r.structured_content or json.loads(r.content[0].text))["linhas"][0]["nome"][:0]
            print(f"{'OK ' if ok else 'ERRO'} HTTP: {len(tools)} ferramentas; consultar_entidade(empresa) respondeu {'com dados' if ok else 'ERRO'}")
            return 0 if ok else 1
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()


sys.exit(asyncio.run(main()))
