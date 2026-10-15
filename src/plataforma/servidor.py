"""Servidor web local da plataforma de progresso do mapeamento (somente 127.0.0.1).

Executar:  executar_plataforma.cmd            (abre em http://127.0.0.1:8800)
API JSON em /api/*; a interface é um único arquivo (src/plataforma/web/index.html), sem dependências externas.
Segurança: escuta só em 127.0.0.1; recusa Host/Origin que não sejam locais (protege contra DNS rebinding e sites que tentem
chamar a API pelo navegador); o banco Domínio é acessado apenas em leitura (teste de rascunho); as únicas gravações são em
data/progresso.db, data/rascunhos/ e, na promoção, src/model/modulos/.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from plataforma import dados as dd  # noqa: E402

WEB = pathlib.Path(__file__).with_name("web") / "index.html"
MAX_CORPO = 512 * 1024
_TRAVA = threading.RLock()   # uso de uma pessoa só: a API é serializada (o catálogo SQLite compartilhado não aceita chamadas concorrentes)


class H(BaseHTTPRequestHandler):
    server_version = "PlataformaMapeamento/1.0"

    # ---- utilidades
    def _host_ok(self) -> bool:
        porta = self.server.server_address[1]
        validos = {f"127.0.0.1:{porta}", f"localhost:{porta}", f"[::1]:{porta}"}
        if (self.headers.get("Host") or "") not in validos:
            return False
        origem = self.headers.get("Origin")
        if origem and urllib.parse.urlparse(origem).netloc not in validos:
            return False
        return True

    def _json(self, obj, status=200):
        corpo = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def _erro(self, status, msg):
        self._json({"erro": msg}, status)

    def log_message(self, fmt, *args):      # silencioso (os acessos não vão para o terminal)
        pass

    # ---- GET
    def do_GET(self):
        if not self._host_ok():
            return self._erro(403, "host não permitido")
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        try:
            with _TRAVA:
                return self._get(u, q)
        except KeyError as e:
            return self._erro(404, f"não encontrado: {e}")
        except Exception as e:
            return self._erro(500, f"{type(e).__name__}: {e}")

    def _get(self, u, q):
        if True:
            if u.path in ("/", "/index.html"):
                corpo = WEB.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(corpo)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(corpo)
                return
            if u.path == "/api/resumo":
                dd.snapshot_hoje()
                return self._json({"resumo": dd.resumo(), "serie": dd.serie()})
            if u.path == "/api/tabelas":
                return self._json(dd.lista_tabelas())
            if u.path == "/api/familias":
                return self._json(dd.familias())
            if u.path == "/api/fila":
                return self._json(dd.fila(int(q.get("n", 40)), q.get("dep") or None))
            if u.path == "/api/historico":
                return self._json(dd.historico(int(q.get("n", 80))))
            if u.path == "/api/tabela":
                return self._json(dd.detalhe(q.get("nome", "")))
            if u.path == "/api/rascunho":
                return self._json(dd.rascunho_salvo(q.get("tabela", "")) or {})
            return self._erro(404, "rota inexistente")

    # ---- POST
    def do_POST(self):
        if not self._host_ok():
            return self._erro(403, "host/origem não permitidos")
        n = int(self.headers.get("Content-Length") or 0)
        if n > MAX_CORPO:
            return self._erro(413, "corpo grande demais")
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self._erro(400, "JSON inválido")
        u = urllib.parse.urlparse(self.path).path
        try:
            with _TRAVA:
                return self._post(u, body)
        except KeyError as e:
            return self._erro(404, f"não encontrado ou parâmetro ausente: {e}")
        except (ValueError, FileNotFoundError, FileExistsError) as e:
            return self._erro(400, str(e))
        except Exception as e:
            return self._erro(500, f"{type(e).__name__}: {str(e)[:300]}")

    def _post(self, u, body):
        if True:
            if u == "/api/tabela/estado":
                return self._json(dd.definir_tabela(body["tabela"], body.get("status"), body.get("prioridade"), body.get("nota")))
            if u == "/api/coluna/estado":
                return self._json(dd.definir_coluna(body["tabela"], body["coluna"], body.get("status"), body.get("nota")))
            if u == "/api/rascunho/gerar":
                return self._json(dd.gerar_rascunho(body["tabela"], body.get("modulo"), body.get("nome"), body.get("colunas")))
            if u == "/api/rascunho/salvar":
                return self._json(dd.salvar_rascunho(body["tabela"], body["yaml"]))
            if u == "/api/rascunho/validar":
                return self._json(dd.validar_rascunho(body["tabela"], body.get("yaml")))
            if u == "/api/rascunho/testar":
                return self._json(dd.testar_rascunho(body["tabela"]))
            if u == "/api/rascunho/promover":
                return self._json(dd.promover_rascunho(body["tabela"], bool(body.get("sobrescrever"))))
            return self._erro(404, "rota inexistente")


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Plataforma de progresso do mapeamento do banco Domínio")
    ap.add_argument("--port", type=int, default=8800)
    a = ap.parse_args(argv)
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), H)
    print(f"Plataforma de mapeamento em http://127.0.0.1:{a.port}  (Ctrl+C para encerrar)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
