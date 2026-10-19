# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrreceita_bruta_item (Receita Bruta) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrreceita_bruta_item"
MODULO = "contabil_outros"
ENTIDADES = ['lrreceita_bruta_item']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
