# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela laparmto_anos (Parametros - Lalur - Anos) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "laparmto_anos"
MODULO = "contabil_outros"
ENTIDADES = ['laparmto_anos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
