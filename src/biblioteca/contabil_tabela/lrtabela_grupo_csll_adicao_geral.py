# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrtabela_grupo_csll_adicao_geral (Tabela grupos de Adições da CSLL - Geral) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrtabela_grupo_csll_adicao_geral"
MODULO = "contabil_tabela"
ENTIDADES = ['lrtabela_grupo_csll_adicao_geral']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
