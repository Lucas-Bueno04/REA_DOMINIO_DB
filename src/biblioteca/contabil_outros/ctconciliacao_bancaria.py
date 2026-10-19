# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctconciliacao_bancaria (Conciliação bancária) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctconciliacao_bancaria"
MODULO = "contabil_outros"
ENTIDADES = ['ctconciliacao_bancaria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
