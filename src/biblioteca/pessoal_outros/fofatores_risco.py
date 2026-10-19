# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofatores_risco (Fatores de risco.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofatores_risco"
MODULO = "pessoal_outros"
ENTIDADES = ['fofatores_risco']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
