# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efncm (TABELA DE NCM) - módulo fiscal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efncm"
MODULO = "fiscal_nucleo"
ENTIDADES = ['efncm']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
