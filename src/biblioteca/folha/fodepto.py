# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodepto (Departamentos (folha)) - módulo folha."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodepto"
MODULO = "folha"
ENTIDADES = ['departamento_folha']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
