# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hradiantamento_aproveitamento (Adiantamentos - Aproveitamentos) - módulo financeiro_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hradiantamento_aproveitamento"
MODULO = "financeiro_outros"
ENTIDADES = ['hradiantamento_aproveitamento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
