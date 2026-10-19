# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_inss_rb_por_recolhimento (Saldo dos Impostos - INSS Receita Bruta - Por Recolhimento) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_inss_rb_por_recolhimento"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_inss_rb_por_recolhimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
