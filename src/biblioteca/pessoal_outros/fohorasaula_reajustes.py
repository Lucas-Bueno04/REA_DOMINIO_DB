# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fohorasaula_reajustes (Tabela com reajuste de horas aula) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fohorasaula_reajustes"
MODULO = "pessoal_outros"
ENTIDADES = ['fohorasaula_reajustes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
