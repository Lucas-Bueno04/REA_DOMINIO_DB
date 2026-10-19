# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctbaklanctolote (Lançamento em lote eliminados) - módulo contabil_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctbaklanctolote"
MODULO = "contabil_nucleo"
ENTIDADES = ['ctbaklanctolote']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
