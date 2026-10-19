# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrcalculo (Cálculos do Lalur (cabeçalho)) - módulo lalur."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrcalculo"
MODULO = "lalur"
ENTIDADES = ['calculo_lalur']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
