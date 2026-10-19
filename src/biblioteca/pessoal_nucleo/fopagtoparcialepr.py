# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fopagtoparcialepr (Pagamentos parciais - Empregados) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fopagtoparcialepr"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fopagtoparcialepr']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
