# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gelog_utilitarios (Log dos Utilitários) - módulo geral_log."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gelog_utilitarios"
MODULO = "geral_log"
ENTIDADES = ['gelog_utilitarios']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
