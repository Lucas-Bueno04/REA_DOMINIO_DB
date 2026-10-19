# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabela_terceiros (Tabela de códigos de terceiros.) - módulo pessoal_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabela_terceiros"
MODULO = "pessoal_tabela"
ENTIDADES = ['fotabela_terceiros']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
