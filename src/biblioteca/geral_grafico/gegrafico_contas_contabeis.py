# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gegrafico_contas_contabeis (Tabela referente as contas contabeis que devem ser emitidas no grafico.) - módulo geral_grafico."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gegrafico_contas_contabeis"
MODULO = "geral_grafico"
ENTIDADES = ['gegrafico_contas_contabeis']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
