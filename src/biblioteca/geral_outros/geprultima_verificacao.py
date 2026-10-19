# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geprultima_verificacao (Verificação das perguntas e respostas do Checkpoint) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geprultima_verificacao"
MODULO = "geral_outros"
ENTIDADES = ['geprultima_verificacao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
