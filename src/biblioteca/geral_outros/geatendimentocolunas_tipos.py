# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimentocolunas_tipos (Tipo de colunas para envio de dados) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimentocolunas_tipos"
MODULO = "geral_outros"
ENTIDADES = ['geatendimentocolunas_tipos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
