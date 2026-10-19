# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_nao_cumulativos (Saldo do Impostos - Detalhamento dos Nao Cumulativos) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_nao_cumulativos"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_nao_cumulativos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
