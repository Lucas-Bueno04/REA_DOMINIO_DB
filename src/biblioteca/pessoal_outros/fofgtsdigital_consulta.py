# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofgtsdigital_consulta (EXECUCOES DA CONSULTA DE COMPETENCIAS NO FGTS DIGITAL) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofgtsdigital_consulta"
MODULO = "pessoal_outros"
ENTIDADES = ['fofgtsdigital_consulta']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
