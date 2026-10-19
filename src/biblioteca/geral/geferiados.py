# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geferiados (Feriados) - módulo geral."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geferiados"
MODULO = "geral"
ENTIDADES = ['feriado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
