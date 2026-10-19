# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebackup_realizado (Log de ciência de backup pré atualização do banco) - módulo geral_backup."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebackup_realizado"
MODULO = "geral_backup"
ENTIDADES = ['gebackup_realizado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
