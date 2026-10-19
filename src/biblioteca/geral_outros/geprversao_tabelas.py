# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geprversao_tabelas (Versão das tabelas do perguntas e respostas do Checkpoint) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geprversao_tabelas"
MODULO = "geral_outros"
ENTIDADES = ['geprversao_tabelas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
