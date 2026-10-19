# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcomplemento_cfop_cat_17_99 (COMPLEMENTO DA CFOP - PORTARIA CAT Nº 17/99) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcomplemento_cfop_cat_17_99"
MODULO = "fiscal_outros"
ENTIDADES = ['efcomplemento_cfop_cat_17_99']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
