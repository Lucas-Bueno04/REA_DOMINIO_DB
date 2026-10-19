# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcombustivel_bico_vigencia (Combustível - Bicos - Vigência) - módulo fiscal_combustivel."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcombustivel_bico_vigencia"
MODULO = "fiscal_combustivel"
ENTIDADES = ['efcombustivel_bico_vigencia']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
