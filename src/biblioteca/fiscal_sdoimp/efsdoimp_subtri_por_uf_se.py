# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_subtri_por_uf_se (Saldo dos Impostos - Substituição Tributária Por SE) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_subtri_por_uf_se"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_subtri_por_uf_se']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
