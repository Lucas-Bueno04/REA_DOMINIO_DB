# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fostatus (INDICA A SITUACAO DO SISTEMA PARA DETERMINADOS PROCESSOS) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fostatus"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fostatus']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
