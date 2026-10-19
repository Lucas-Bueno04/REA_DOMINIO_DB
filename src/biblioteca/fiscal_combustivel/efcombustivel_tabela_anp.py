# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efcombustivel_tabela_anp (Tabela de códigos de combustível da ANP) - módulo fiscal_combustivel."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efcombustivel_tabela_anp"
MODULO = "fiscal_combustivel"
ENTIDADES = ['efcombustivel_tabela_anp']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
