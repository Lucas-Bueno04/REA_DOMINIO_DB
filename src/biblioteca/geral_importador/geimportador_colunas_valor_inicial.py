# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geimportador_colunas_valor_inicial (Valor inicial das colunas) - módulo geral_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geimportador_colunas_valor_inicial"
MODULO = "geral_importador"
ENTIDADES = ['geimportador_colunas_valor_inicial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
