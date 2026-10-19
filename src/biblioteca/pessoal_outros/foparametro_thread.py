# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foparametro_thread (Informa se o sitema irá utilizar thread para processos de cálculo) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foparametro_thread"
MODULO = "pessoal_outros"
ENTIDADES = ['foparametro_thread']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
