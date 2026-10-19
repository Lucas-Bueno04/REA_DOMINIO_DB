# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcombustivel_tabela_df (Tabela de códigos de combustível do DF) - módulo fiscal_combustivel."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcombustivel_tabela_df"
MODULO = "fiscal_combustivel"
ENTIDADES = ['efcombustivel_tabela_df']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
