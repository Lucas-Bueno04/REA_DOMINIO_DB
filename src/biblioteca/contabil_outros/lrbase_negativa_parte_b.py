# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela lrbase_negativa_parte_b (Cadastro de Base Negativa e Parte B) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "lrbase_negativa_parte_b"
MODULO = "contabil_outros"
ENTIDADES = ['lrbase_negativa_parte_b']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
