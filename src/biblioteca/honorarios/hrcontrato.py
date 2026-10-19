# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrcontrato (Contratos de honorários) - módulo honorarios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrcontrato"
MODULO = "honorarios"
ENTIDADES = ['contrato']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
