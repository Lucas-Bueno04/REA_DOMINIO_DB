# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_diops_od_registro (DIOPs - Outros Dados - Tabela com colunas dos registros de valor) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_diops_od_registro"
MODULO = "contabil_tabela"
ENTIDADES = ['cttabela_diops_od_registro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
