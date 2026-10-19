# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efentradas (Notas fiscais de entrada) - módulo fiscal."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efentradas"
MODULO = "fiscal"
ENTIDADES = ['nota_entrada']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
