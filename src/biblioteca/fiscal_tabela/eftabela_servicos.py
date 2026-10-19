# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_servicos (Tabela Lista de Servicos) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_servicos"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_servicos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
