# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gedicasusuarios (Dicas - Controle de dicas por usuarios) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gedicasusuarios"
MODULO = "geral_nucleo"
ENTIDADES = ['gedicasusuarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
