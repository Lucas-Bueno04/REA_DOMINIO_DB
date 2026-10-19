# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_cst_vigencia (Tabela de Códigos Situação Tributária por vigência) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_cst_vigencia"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_cst_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
