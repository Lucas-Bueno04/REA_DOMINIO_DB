# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fojornadas_horarios (Horários da jornada.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fojornadas_horarios"
MODULO = "pessoal_outros"
ENTIDADES = ['fojornadas_horarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
