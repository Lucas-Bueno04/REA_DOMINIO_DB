# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geselecao (Armazena os dados da seleção) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geselecao"
MODULO = "geral_nucleo"
ENTIDADES = ['geselecao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
