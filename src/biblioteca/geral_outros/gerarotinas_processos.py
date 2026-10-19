# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gerarotinas_processos (PROCESSOS DAS ROTINAS AUTOMÁTICAS) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gerarotinas_processos"
MODULO = "geral_outros"
ENTIDADES = ['gerarotinas_processos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
