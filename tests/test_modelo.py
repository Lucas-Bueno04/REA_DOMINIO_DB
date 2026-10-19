"""Consistência dos modelos YAML contra o catálogo — sem acesso ao banco."""
import pathlib

from model.validar_modelo import MODULOS, validar


def test_modelos_sem_erros():
    arqs = sorted(MODULOS.glob("*.yaml"))
    assert len(arqs) >= 6
    entidades, erros, avisos, _ = validar(arqs)
    assert erros == [], "\n".join(erros)
    assert len(entidades) >= 75


def test_avisos_conhecidos_apenas():
    """Os avisos aceitos hoje são relações sustentadas pelos dados mas ausentes dos JOINs dos programas da Domínio."""
    _, _, avisos, _ = validar(sorted(MODULOS.glob("*.yaml")))
    esperados = ("historico_padrao: nenhuma relação ctlancto↔cthispad", "evento_padrao: nenhuma relação fomovtoserv↔foeventosdef",
                 # alíquotas do Simples: ligação sustentada pelos dados (397 de 397 linhas cruzadas) mas sem FK declarada no banco
                 "aliquotas: nenhuma relação efsdoimp_simples_nacional↔EFSDOIMP_SIMPLES_NACIONAL_ALIQUOTAS",
                 # campos do informativo ligam ao catálogo pelo cabeçalho (efoutrosdados), 0 campos sem cabeçalho em 3,8 mi
                 "nenhuma relação efoutrosdados_dados↔efinformativos",
                 # tabelas do banco sem PK nem índice único: a chave da entidade é o conjunto de colunas expostas (gerado em lote)
                 "difere da PK [] e não há índice único igual")
    inesperados = [a for a in avisos if not any(e in a for e in esperados)]
    assert inesperados == [], inesperados


def test_dominios_nao_confirmados_estao_sinalizados():
    import yaml
    for arq in MODULOS.glob("*.yaml"):
        y = yaml.safe_load(arq.read_text(encoding="utf-8"))
        for nome, d in y.get("dominios", {}).items():
            assert "confirmado" in d, f"{arq.stem}.{nome} sem a marca 'confirmado'"
            if d["confirmado"] is False:
                assert d.get("nota"), f"{arq.stem}.{nome}: domínio não confirmado exige 'nota' explicando"


def test_nenhuma_chave_on_nos_yaml():
    """'on' vira booleano True no YAML 1.1; o modelo usa 'liga'."""
    import re
    for arq in MODULOS.glob("*.yaml"):
        assert not re.search(r"(?<![A-Za-z])on:\s*\{", arq.read_text(encoding="utf-8")), arq.name
