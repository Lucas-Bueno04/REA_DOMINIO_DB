# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focalcmedias_mem (Memoria de calculo) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focalcmedias_mem"
MODULO = "pessoal_outros"
ENTIDADES = ['focalcmedias_mem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
