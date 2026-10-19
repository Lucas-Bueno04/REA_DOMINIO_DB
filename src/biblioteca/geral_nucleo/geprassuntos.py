# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geprassuntos (Assuntos do Perguntas e Respostas do Checkpoint) - módulo geral_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geprassuntos"
MODULO = "geral_nucleo"
ENTIDADES = ['geprassuntos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
