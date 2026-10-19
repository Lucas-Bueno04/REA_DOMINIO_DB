# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lacsaliquotas (Aliquotas para CS) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lacsaliquotas"
MODULO = "contabil_nucleo"
ENTIDADES = ['lacsaliquotas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
