# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efbase_legal_to (Base legal do outros creditos - TO) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efbase_legal_to"
MODULO = "fiscal_outros"
ENTIDADES = ['efbase_legal_to']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
