# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_x300_cnc (SPED ECF - Tabela de codigos CNC do registro X300) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_x300_cnc"
MODULO = "contabil_tabela"
ENTIDADES = ['cttabela_x300_cnc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
