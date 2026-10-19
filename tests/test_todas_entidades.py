"""Todas as entidades do modelo executam pelo caminho real do MCP (Motor.consultar_entidade) e serializam em JSON, contra o banco real (~1 min)."""
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
import testar_motor_entidades as t  # noqa: E402

from server.motor import Motor  # noqa: E402


def test_todas_as_entidades_executam():
    motor = Motor(auditar=False)
    res = t.executar(motor=motor)
    assert len(res) == len(motor.ents) and len(res) >= 2000
    falhas = {n: v["erro"] for n, v in res.items() if not v["ok"]}
    assert falhas == {}, list(falhas.items())[:10]
