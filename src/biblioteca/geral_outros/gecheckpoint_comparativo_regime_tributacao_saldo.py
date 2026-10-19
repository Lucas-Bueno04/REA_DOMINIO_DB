# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecheckpoint_comparativo_regime_tributacao_saldo (Checkpoint - Comparativo de Regime de Tributação - Informações saldos) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecheckpoint_comparativo_regime_tributacao_saldo"
MODULO = "geral_outros"
ENTIDADES = ['gecheckpoint_comparativo_regime_tributacao_saldo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
