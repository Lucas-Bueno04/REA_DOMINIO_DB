# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_planilha_stda (SP - Tabela da Planilha do STDA) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_planilha_stda"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_planilha_stda']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
