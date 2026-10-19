# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_rn_tributacao (RN - Tabela Tributação) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_rn_tributacao"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_rn_tributacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
