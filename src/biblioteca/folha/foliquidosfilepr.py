# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foliquidosfilepr (Líquido a pagar) - módulo folha."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foliquidosfilepr"
MODULO = "folha"
ENTIDADES = ['liquido_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
