# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_estadual_ba (Saldo dos Impostos - Estadual BA) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_estadual_ba"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_estadual_ba']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
