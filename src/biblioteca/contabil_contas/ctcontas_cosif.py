# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_cosif (Plano de contas COSIF) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_cosif"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_cosif']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
