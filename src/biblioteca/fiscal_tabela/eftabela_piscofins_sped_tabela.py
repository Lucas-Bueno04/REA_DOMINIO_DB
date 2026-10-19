# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_piscofins_sped_tabela (Tabela PIS/COFINS SPED) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_piscofins_sped_tabela"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_piscofins_sped_tabela']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
