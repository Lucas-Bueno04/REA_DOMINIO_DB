# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geparametros_impressora (Parâmetros da impressora) - módulo geral_parametros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geparametros_impressora"
MODULO = "geral_parametros"
ENTIDADES = ['geparametros_impressora']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
