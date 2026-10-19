# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_dcip (Tabela - Códigos DCIP) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_dcip"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_dcip']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
