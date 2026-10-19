# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_por_recolhimento_por_data (Saldo dos Impostos - Detalhamento dos Impostos por Código de Recolhimento - Por Data) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_por_recolhimento_por_data"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_por_recolhimento_por_data']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
