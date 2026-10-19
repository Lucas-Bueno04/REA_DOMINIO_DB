# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foportal_empregado (Dados gerais referente ao portal do empregado) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foportal_empregado"
MODULO = "pessoal_outros"
ENTIDADES = ['foportal_empregado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
