# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geprperguntas_respostas (Perguntas e Respostas do Checkpoint) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geprperguntas_respostas"
MODULO = "geral_outros"
ENTIDADES = ['geprperguntas_respostas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
