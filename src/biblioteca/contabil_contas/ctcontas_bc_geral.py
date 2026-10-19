# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_bc_geral (Plano de contas Banco Central - Geral) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_bc_geral"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_bc_geral']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
