# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efdasn_socios (DASN - outros dados socios) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efdasn_socios"
MODULO = "fiscal_outros"
ENTIDADES = ['efdasn_socios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
