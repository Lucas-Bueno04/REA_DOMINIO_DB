# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela cttabela_natureza_subconta_correlata (Natureza Subconta Correlata) - módulo contabil_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "cttabela_natureza_subconta_correlata"
MODULO = "contabil_tabela"
ENTIDADES = ['cttabela_natureza_subconta_correlata']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
