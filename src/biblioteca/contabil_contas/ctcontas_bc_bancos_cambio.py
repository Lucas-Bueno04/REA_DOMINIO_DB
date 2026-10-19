# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctcontas_bc_bancos_cambio (Plano de contas Banco Central - Bancos de Câmbio) - módulo contabil_contas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctcontas_bc_bancos_cambio"
MODULO = "contabil_contas"
ENTIDADES = ['ctcontas_bc_bancos_cambio']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
