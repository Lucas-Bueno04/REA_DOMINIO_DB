# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gegrafico_tipo (Tipo dos gráfico) - módulo geral_grafico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gegrafico_tipo"
MODULO = "geral_grafico"
ENTIDADES = ['gegrafico_tipo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
