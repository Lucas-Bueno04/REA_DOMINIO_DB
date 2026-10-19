# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_natureza_acao (Ajustes PIS/COFINS - Natureza da ação) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_natureza_acao"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_natureza_acao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
