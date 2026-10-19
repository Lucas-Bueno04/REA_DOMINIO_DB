# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_ans (Plano de contas ANS) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_ans"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_ans']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
