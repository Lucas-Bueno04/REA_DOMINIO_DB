# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela eftabela_classe_consumo (Tabela de Classe de Consumo - SPED e SEF 2012) - módulo fiscal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "eftabela_classe_consumo"
MODULO = "fiscal_tabela"
ENTIDADES = ['eftabela_classe_consumo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
