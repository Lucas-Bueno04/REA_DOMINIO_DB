# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela autabelas (Tabelas que serao auditadas) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "autabelas"
MODULO = "sistema_nucleo"
ENTIDADES = ['autabelas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
