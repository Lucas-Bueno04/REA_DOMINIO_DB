# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geselecao_filtro (Armazena os dados da seleção - Filtro) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geselecao_filtro"
MODULO = "geral_outros"
ENTIDADES = ['geselecao_filtro']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
