# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctlivro_caixa_produtor_rural_leiaute (Leiautes produtor rural) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctlivro_caixa_produtor_rural_leiaute"
MODULO = "contabil_outros"
ENTIDADES = ['ctlivro_caixa_produtor_rural_leiaute']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
