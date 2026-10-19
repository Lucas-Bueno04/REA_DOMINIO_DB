# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecsperguntas_solucoes (Perguntas e soluções da Central de Soluções) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecsperguntas_solucoes"
MODULO = "geral_outros"
ENTIDADES = ['gecsperguntas_solucoes']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
