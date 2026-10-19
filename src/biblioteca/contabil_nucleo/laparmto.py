# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela laparmto (Parametros - Lalur) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "laparmto"
MODULO = "contabil_nucleo"
ENTIDADES = ['laparmto']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
