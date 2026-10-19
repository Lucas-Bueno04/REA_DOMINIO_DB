# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fohorafolha_backup (Horario - Cadastro) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fohorafolha_backup"
MODULO = "pessoal_outros"
ENTIDADES = ['fohorafolha_backup']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
