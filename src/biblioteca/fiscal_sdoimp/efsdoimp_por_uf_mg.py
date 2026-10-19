# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_por_uf_mg (Saldo dos Impostos - Por UF - MG) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_por_uf_mg"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_por_uf_mg']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
