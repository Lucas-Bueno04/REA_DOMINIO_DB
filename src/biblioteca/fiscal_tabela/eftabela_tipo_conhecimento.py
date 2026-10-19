# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_tipo_conhecimento (Tipo de conhecimento) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_tipo_conhecimento"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_tipo_conhecimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
