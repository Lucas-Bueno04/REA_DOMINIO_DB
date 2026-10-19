# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrservico_prestado (Codigo do servico prestado) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrservico_prestado"
MODULO = "financeiro_outros"
ENTIDADES = ['hrservico_prestado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
