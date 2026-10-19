# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geprocessando_digial_bank (GEPROCESSANDO_DIGIAL_BANK) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geprocessando_digial_bank"
MODULO = "geral_outros"
ENTIDADES = ['geprocessando_digial_bank']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
