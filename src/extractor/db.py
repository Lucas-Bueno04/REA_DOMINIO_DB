"""Acesso ao banco da Domínio: SOMENTE LEITURA.

Toda consulta passa por `select()`, que recusa qualquer coisa que não seja
SELECT/WITH, roda em READ UNCOMMITTED e sempre faz rollback.
"""
import os
import re

import pyodbc

_PROIBIDO = re.compile(
    r"\b(INSERT|UPDATE|DELETE|MERGE|DROP|ALTER|CREATE|GRANT|REVOKE|TRUNCATE|CALL|EXEC|EXECUTE|SET|COMMIT|LOAD|UNLOAD)\b",
    re.IGNORECASE,
)


_RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _carregar_env(caminho: str | None = None) -> None:
    """Lê config/.env do projeto (independente do diretório de execução). Variáveis já definidas no ambiente têm prioridade."""
    caminho = caminho or os.path.join(_RAIZ, "config", ".env")
    if os.path.exists(caminho):
        for linha in open(caminho, encoding="utf-8"):
            linha = linha.strip()
            if linha and not linha.startswith("#") and "=" in linha:
                k, v = linha.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def conectar() -> pyodbc.Connection:
    _carregar_env()
    dsn = os.environ.get("DOM_DSN", "Contabil")
    uid = os.environ["DOM_UID"]
    pwd = os.environ["DOM_PWD"]
    cn = pyodbc.connect(f"DSN={dsn};UID={uid};PWD={pwd}", autocommit=False)
    # leitura sem bloqueio: não segura nem espera travas de quem está lançando dados no sistema
    cn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_READ_UNCOMMITTED)
    return cn


def validar_select(sql: str) -> None:
    if not re.match(r"^\s*(SELECT|WITH)\b", sql, re.IGNORECASE):
        raise PermissionError("Somente SELECT/WITH é permitido")
    # remove literais para não bloquear texto como 'UPDATE' dentro de string
    sem_literais = re.sub(r"'(?:[^']|'')*'", "''", sql)
    if _PROIBIDO.search(sem_literais):
        raise PermissionError("Comando não permitido na consulta")


def select(cn: pyodbc.Connection, sql: str, params: tuple = (), timeout: int | None = None) -> list[dict]:
    validar_select(sql)
    cur = cn.cursor()
    try:
        if timeout:
            try:
                cur.timeout = int(timeout)   # SQL_ATTR_QUERY_TIMEOUT; nem todo driver respeita
            except Exception:
                pass
        cur.execute("SELECT 1")  # garante sessão ativa
        cur.execute(sql, params)
        cols = [c[0].lower() for c in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
    finally:
        cn.rollback()
        cur.close()
