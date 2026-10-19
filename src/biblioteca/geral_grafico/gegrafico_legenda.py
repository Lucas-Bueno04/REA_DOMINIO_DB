# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gegrafico_legenda (Tabela referente as legendas do gráfico.) - módulo geral_grafico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gegrafico_legenda"
MODULO = "geral_grafico"
ENTIDADES = ['gegrafico_legenda']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
