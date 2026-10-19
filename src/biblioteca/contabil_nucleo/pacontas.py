# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pacontas (Contas patrimoniais - Cadastro) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pacontas"
MODULO = "contabil_nucleo"
ENTIDADES = ['pacontas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
