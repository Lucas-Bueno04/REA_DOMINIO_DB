# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_conjunto_dados_definicoes_dados (Definições de dados dos conjunto de dados) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_conjunto_dados_definicoes_dados"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_conjunto_dados_definicoes_dados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
