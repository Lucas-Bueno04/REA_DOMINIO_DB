# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcprocesso_atividade (Processos - Atividades) - módulo processos_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcprocesso_atividade"
MODULO = "processos_outros"
ENTIDADES = ['pcprocesso_atividade']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
