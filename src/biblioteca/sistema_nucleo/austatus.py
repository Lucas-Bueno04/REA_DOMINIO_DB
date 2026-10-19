# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela austatus (Status da auditoria) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "austatus"
MODULO = "sistema_nucleo"
ENTIDADES = ['austatus']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
