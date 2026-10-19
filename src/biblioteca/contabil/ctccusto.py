# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctccusto (Centros de custo) - módulo contabil."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctccusto"
MODULO = "contabil"
ENTIDADES = ['centro_custo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
