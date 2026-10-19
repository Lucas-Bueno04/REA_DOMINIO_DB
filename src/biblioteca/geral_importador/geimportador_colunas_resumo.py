# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_colunas_resumo (Colunas exibidas no resumo do importador) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_colunas_resumo"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_colunas_resumo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
