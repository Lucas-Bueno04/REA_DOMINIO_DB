# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geferiados_febraban (Feriados da FEBRABAN (Tabela Interna)) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geferiados_febraban"
MODULO = "geral_outros"
ENTIDADES = ['geferiados_febraban']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
