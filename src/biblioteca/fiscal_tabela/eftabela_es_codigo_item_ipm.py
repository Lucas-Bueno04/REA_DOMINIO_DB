# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_es_codigo_item_ipm (Tabela de item para IPM - ES) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_es_codigo_item_ipm"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_es_codigo_item_ipm']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
