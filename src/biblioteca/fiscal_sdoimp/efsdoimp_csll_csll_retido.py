# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_csll_csll_retido (Saldo dos Impostos - CSLL Retido) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_csll_csll_retido"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_csll_csll_retido']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
