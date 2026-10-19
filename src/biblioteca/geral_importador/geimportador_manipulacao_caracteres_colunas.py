# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_manipulacao_caracteres_colunas (Colunas da manipulação de caracteres) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_manipulacao_caracteres_colunas"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_manipulacao_caracteres_colunas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
