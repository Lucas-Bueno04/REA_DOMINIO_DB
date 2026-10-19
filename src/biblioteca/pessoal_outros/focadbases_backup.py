# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela focadbases_backup (FOCADBASES_BACKUP) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "focadbases_backup"
MODULO = "pessoal_outros"
ENTIDADES = ['focadbases_backup']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
