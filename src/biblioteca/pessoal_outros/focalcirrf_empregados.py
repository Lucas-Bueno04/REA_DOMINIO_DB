# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalcirrf_empregados (Valores da guia separados por empregado.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalcirrf_empregados"
MODULO = "pessoal_outros"
ENTIDADES = ['focalcirrf_empregados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
