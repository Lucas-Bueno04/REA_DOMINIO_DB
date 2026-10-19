# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela aucolunas (Comentario das colunas auditadas) - módulo sistema_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "aucolunas"
MODULO = "sistema_nucleo"
ENTIDADES = ['aucolunas']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
