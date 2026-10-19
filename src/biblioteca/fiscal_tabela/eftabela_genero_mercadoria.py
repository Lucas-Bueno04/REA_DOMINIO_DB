# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_genero_mercadoria (Tabela Genero do Item de Mercadoria/Servico) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_genero_mercadoria"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_genero_mercadoria']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
