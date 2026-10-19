# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gelog_geral (Tabela de logs gerais do contÃ¡bil.) - módulo geral_log."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gelog_geral"
MODULO = "geral_log"
ENTIDADES = ['gelog_geral']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
