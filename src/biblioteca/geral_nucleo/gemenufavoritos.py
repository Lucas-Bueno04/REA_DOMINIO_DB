# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gemenufavoritos (Itens do menu favoritos) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gemenufavoritos"
MODULO = "geral_nucleo"
ENTIDADES = ['gemenufavoritos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
