# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecnae20 (CNAE 2.0) - módulo geral."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecnae20"
MODULO = "geral"
ENTIDADES = ['cnae']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
