# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geresponsavel (Responsavel - Cadastro) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geresponsavel"
MODULO = "geral_nucleo"
ENTIDADES = ['geresponsavel']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
