# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrparametro_vigencia (Parâmetros Lalur - Vigência) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrparametro_vigencia"
MODULO = "contabil_outros"
ENTIDADES = ['lrparametro_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
