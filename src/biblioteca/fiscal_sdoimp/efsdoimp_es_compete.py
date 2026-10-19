# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efsdoimp_es_compete (Saldo dos Impostos - COMPETE - ES) - módulo fiscal_sdoimp."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efsdoimp_es_compete"
MODULO = "fiscal_sdoimp"
ENTIDADES = ['efsdoimp_es_compete']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
