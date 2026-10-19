# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gelog_utilitarios_nota (Log dos Utilitários - Notas) - módulo geral_log."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gelog_utilitarios_nota"
MODULO = "geral_log"
ENTIDADES = ['gelog_utilitarios_nota']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
