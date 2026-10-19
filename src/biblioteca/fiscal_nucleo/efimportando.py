# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportando (Usuários importando) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportando"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efimportando']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
