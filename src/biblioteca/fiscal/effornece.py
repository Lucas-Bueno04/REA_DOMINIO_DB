# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela effornece (Fornecedores) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "effornece"
MODULO = "fiscal"
ENTIDADES = ['fornecedor']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
